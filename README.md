# Gebedstijden + Streak (MVP)

Minimalistische MVP webapp in Python + Flask.

Functies:

- Voer locatie in als stad[,land] of als coördinaten `lat,lon`.
- Backend haalt gebedstijden op via AlAdhan API.
- Checkbox per gebed (Fajr, Dhuhr, Asr, Maghrib, Isha) om af te vinken.
- Streak van opeenvolgende dagen wordt opgeslagen in `localStorage` (browser).
- Geen accounts, geen database.

## Snel starten

1. (Optioneel) Maak en activeer een virtuele omgeving.
2. Installeer dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start de app:
   ```bash
   python app.py
   ```
4. Open in de browser: `http://127.0.0.1:5000/`.

## Gebruik

- Locatie input accepteert:
  - Stad of `stad,land` (bijv. `Eindhoven` of `Eindhoven, Netherlands`).
  - Coördinaten `lat,lon` (bijv. `51.44,5.47`).
- Klik op "Ophalen" om de gebedstijden te laden.
- Vink alle 5 gebeden af om de streak voor vandaag te verhogen.
- MVP-gedrag: unchecken verlaagt de streak niet automatisch.

## Structuur

- `app.py`: Flask app met één UI-route `/` en één API-route `/api/prayer-times`.
- `templates/index.html`: simpele UI met input, tabel en checkboxes.
- `static/style.css`: minimalistische styling.
- `requirements.txt`: Flask + requests.

## Notities

- De app gebruikt `requests` om de AlAdhan API aan te roepen.
- Berekeningen en opslag van voortgang/streak zitten in de frontend (`localStorage`).

