# 🎵 AI Playlist Generator

A web application that generates music playlists based on your mood. Describe how you feel in natural language — get a playlist back.

Built as a collaborative project: Python/Flask backend ([@DusiEkler](https://github.com/DusiEkler)) + React frontend ([@OreeestDev](https://github.com/OreeestDev)).

---

## 🖥️ How It Works

1. User enters a mood or description in the frontend (e.g. *"rainy evening, something calm"*)
2. The backend processes the prompt and queries the Deezer API for matching tracks
3. Results are parsed and returned to the React frontend as a structured playlist

---

## 🏗️ Architecture

```
AI-Playlist-Generator/
├── backend/
│   ├── main.py          # Flask app, API routes
│   ├── prompts.py       # Prompt construction logic
│   ├── deezer.py        # Deezer API integration
│   ├── parsing.py       # Response parsing and structuring
│   ├── data/            # Sample responses for development
│   └── requirements.txt
│
├── frontend/
│   ├── src/             # React components
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## 🚀 Getting Started

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` folder:
```
DEEZER_API_KEY=your_key_here
```

Run the server:
```bash
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

Frontend runs at `http://localhost:3000`, backend at `http://localhost:5000`.

---

## 🛠️ Tech Stack

| Part | Stack |
|---|---|
| Backend | Python, Flask, Deezer API |
| Frontend | React, JavaScript, CSS |
| Config | python-dotenv |

---

## 👥 Authors

| Role | GitHub |
|---|---|
| Backend | [@DusiEkler](https://github.com/DusiEkler) |
| Frontend | [@OreeestDev](https://github.com/OreeestDev) |
