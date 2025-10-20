from flask import Flask, render_template, request, jsonify
import requests
import re


app = Flask(__name__)


@app.route("/")
def index():
    """
    Render the single-page interface. The frontend uses fetch() to call
    the backend API and localStorage to store daily progress and streak.
    """
    return render_template("index.html")


def _parse_location(loc: str):
    """
    Try to parse the provided location string as either:
      - coordinates: "lat,lon" (floats)
      - city[,country]: city name with optional country (defaults to Netherlands)

    Returns a tuple (mode, params) where mode is either "coords" or "city".
    """
    if not loc or not isinstance(loc, str):
        raise ValueError("Location must be a non-empty string")

    s = loc.strip()

    # Detect coordinates like: 51.4416, 5.4697 (lat, lon)
    coord_match = re.match(r"^\s*([+-]?\d+(?:\.\d+)?)\s*,\s*([+-]?\d+(?:\.\d+)?)\s*$", s)
    if coord_match:
        lat = float(coord_match.group(1))
        lon = float(coord_match.group(2))
        return "coords", {"latitude": lat, "longitude": lon}

    # Otherwise, treat as city[,country]
    parts = [p.strip() for p in s.split(",") if p.strip()]
    if len(parts) == 1:
        city = parts[0]
        country = "Netherlands"  # default fallback for convenience
    elif len(parts) >= 2:
        city = parts[0]
        country = parts[1]
    else:
        raise ValueError("Invalid location format")

    if not city:
        raise ValueError("City cannot be empty")

    return "city", {"city": city, "country": country}


@app.route("/api/prayer-times")
def api_prayer_times():
    """
    Proxy to AlAdhan API. Accepts a query parameter "location" which can be:
      - coordinates: "lat,lon" (e.g., "51.44,5.47")
      - city or city,country: (e.g., "Eindhoven" or "Eindhoven, Netherlands")

    Optional params (with sensible defaults):
      - method (int): calculation method (default 2 = Muslim World League)
      - school (int): Asr juristic method (default 0 = Shafi, Maliki, Hanbali)

    Returns a simplified JSON with timings and date.
    """
    location = request.args.get("location", "").strip()
    method = request.args.get("method", "2")  # MWL default
    school = request.args.get("school", "0")  # Shafi default

    if not location:
        return jsonify({"error": "Missing 'location' query parameter"}), 400

    try:
        mode, params = _parse_location(location)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    try:
        if mode == "coords":
            # https://aladhan.com/prayer-times-api#GetTimings 
            url = "https://api.aladhan.com/v1/timings"
            resp = requests.get(url, params={
                "latitude": params["latitude"],
                "longitude": params["longitude"],
                "method": method,
                "school": school,
            }, timeout=10)
        else:
            # https://aladhan.com/prayer-times-api#GetTimingsByCity
            url = "https://api.aladhan.com/v1/timingsByCity"
            resp = requests.get(url, params={
                "city": params["city"],
                "country": params["country"],
                "method": method,
                "school": school,
            }, timeout=10)

        resp.raise_for_status()
        payload = resp.json()
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to reach AlAdhan API: {e}"}), 502
    except ValueError:
        return jsonify({"error": "Unexpected response from AlAdhan API"}), 502

    if not isinstance(payload, dict) or payload.get("code") != 200:
        return jsonify({"error": "AlAdhan API returned an error", "raw": payload}), 502

    data = payload.get("data", {})
    timings = data.get("timings", {})
    date_info = data.get("date", {})

    # Keep only the five obligatory prayers for the UI.
    minimal_timings = {
        "Fajr": timings.get("Fajr"),
        "Dhuhr": timings.get("Dhuhr"),
        "Asr": timings.get("Asr"),
        "Maghrib": timings.get("Maghrib"),
        "Isha": timings.get("Isha"),
    }

    return jsonify({
        "date": {
            "readable": date_info.get("readable"),
            "gregorian": date_info.get("gregorian", {}).get("date"),
            "hijri": date_info.get("hijri", {}).get("date"),
        },
        "timings": minimal_timings,
        "source": "AlAdhan",
    })


if __name__ == "__main__":
    # Run the development server. In production, use a WSGI server.
    app.run(debug=True)

