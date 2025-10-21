Gebedstijden Tracker (MVP)
webapplicatie met streak-tracking gebouwd met Python (Flask) +HTlm.
________________________________________
Overzicht
Deze MVP webapp toont dagelijkse gebedstijden op basis van de locatie van de gebruiker en houdt een dagelijkse streak bij voor motivatie en discipline. De app is bewust lichtgewicht gebouwd zonder accounts of database, zodat de focus ligt op functionele logica en webtechniek.
________________________________________
 Kernfunctionaliteiten
•	 Gebedstijden ophalen via AlAdhan API
•	 Locatie invoer: stad, land of coördinaten (lat, lon)
•	 Checkbox per gebed: Fajr, Dhuhr, Asr, Maghrib, Isha
•	 Streaksysteem: telt opeenvolgende dagen met volledige gebeden
•	 Opslag in localStorage (geen database nodig)
•	 Simpel, overzichtelijk ontwerp (Flask + HTML/CSS + JS)
________________________________________
 Tech Stack
Onderdeel	Technologie
Backend	Python + Flask
Frontend	HTML, CSS, JavaScript
Data	localStorage (browser opslaan)
API	AlAdhan Prayer Times API
Architectuur	MVP – minimal viable product
________________________________________
 Installatie
1. Dependencies installeren
pip install -r requirements.txt.
2. Start de server
python app.py
Open nu in je browser:
http://127.0.0.1:5000/
________________________________________
 Gebruik
1.	Vul een locatie in (bijvoorbeeld: Eindhoven of 51.44,5.47).
2.	Klik op Ophalen om gebedstijden te laden.
3.	Vink gebeden af zodra ze zijn verricht.
4.	De app slaat voortgang lokaal op en telt je streak automatisch bij.
Let op: dit is een MVP. Unchecken verlaagt de streak niet.
________________________________________
 Projectstructuur
project/
│ app.py                # Flask backend + API proxy
│ requirements.txt       # Dependencies
│
├── templates/
│     └── index.html     # UI layout
│
└── static/
      └── style.css      # Styling
________________________________________
MVP Scope
Dit project is bewust klein gehouden om de kernlogica te ontwikkelen:
✔ Werkende API-integratie
✔ Streaklogica in frontend
✔ Geen database
✔ Geen notificaties
✔ Geen user accounts
________________________________________
Toekomstige uitbreidingen (Roadmap)
•	Countdown tot volgende gebed
•	Gebedstijden cache offline
•	Keuze voor method / madhab
•	Progress opslaan per account
•	Cloud deployment + CI/CD
•	PWA / mobiel icoon + offline mode
________________________________________ Bronnen
•	AlAdhan API – https://aladhan.com/prayer-times-api
•	Flask Documentation – https://flask.palletsprojects.com
•	MDN Web Docs – https://developer.mozilla.org

