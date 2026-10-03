# 🔐 Password Guessing Game

A modern, full-stack word-guessing game built with **FastAPI** (backend) and a **React-style frontend** featuring tactile design, real-time hints, and scoring mechanics.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 🎮 Features

### Backend (Python + FastAPI)
- **Object-Oriented Architecture** — Clean class-based game logic
- **RESTful API** — Complete game lifecycle endpoints
- **Three Difficulty Levels** — Easy (10 attempts), Medium (7), Hard (5)
- **Smart Scoring System** — Based on difficulty multiplier and speed
- **Enhanced Hints** — Position-based + letter-count feedback
- **Input Validation** — Case-insensitive, rejects empty/invalid guesses
- **In-Memory Game Sessions** — UUID-based game tracking

### Frontend (HTML/CSS/JavaScript)
- **Tactile 3D Tile Design** — Physical keycap effects with shadows
- **Elegant Typography** — Instrument Serif headings + Plus Jakarta Sans UI
- **Light/Dark Themes** — Warm off-white (#FBF9F5) / Matte charcoal (#121316)
- **Emerald/Amber/Slate Feedback** — Color-coded hints
- **Smooth Micro-Interactions** — Spring animations, shake on errors
- **Fully Responsive** — Desktop to mobile (480px+)
- **Real-Time Game State** — Live attempt tracking and hints

---

## 📁 Project Structure

```
Password Guessing Game/
├── Password_Guess.py       # Core game logic + CLI wrapper
├── main.py                 # FastAPI application
├── models.py               # Pydantic request/response schemas
├── requirements.txt        # Python dependencies
└── frontend/
    └── password-game.html  # Single-page web application
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- Modern web browser

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Password-Guessing-Game.git
cd Password-Guessing-Game
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Backend
```bash
uvicorn main:app --reload
```
The API will run at `http://localhost:8000`

You can explore the auto-generated API docs at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 4. Open the Frontend
Simply open `frontend/password-game.html` in your browser.

The game will automatically connect to your running backend.

---

## 🎯 How to Play

1. **Select Difficulty** — Choose Easy, Medium, or Hard
2. **Start Guessing** — Enter your guess and hit Submit
3. **Use the Hints** — 
   - 🔡 Position hints show correct letters in the right place
   - ✅ Letter count shows how many correct letters exist in the word
4. **Win!** — Guess correctly within the attempt limit to earn points

### Scoring Formula
```
Base Points = 100
Speed Bonus = (Max Attempts - Used Attempts) × 10
Final Score = (Base + Speed Bonus) × Difficulty Multiplier

Difficulty Multipliers:
- Easy: 1x
- Medium: 2x
- Hard: 3x
```

---

## 🛠️ API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/game/start` | Start a new game (returns `game_id`) |
| `POST` | `/game/{game_id}/guess` | Submit a guess |
| `GET` | `/game/{game_id}/status` | Get current game state |
| `DELETE` | `/game/{game_id}` | Delete a game |
| `GET` | `/stats` | View active games |

### Example API Usage

**Start a game:**
```bash
curl -X POST http://localhost:8000/game/start \
  -H "Content-Type: application/json" \
  -d '{"difficulty": "medium"}'
```

**Submit a guess:**
```bash
curl -X POST http://localhost:8000/game/{game_id}/guess \
  -H "Content-Type: application/json" \
  -d '{"guess": "python"}'
```

---

## 🎨 Design System

### Color Palette
- **Light Mode Background:** Warm Off-White (#FBF9F5)
- **Dark Mode Background:** Matte Charcoal (#121316)
- **Correct Feedback:** Emerald Green (#059669)
- **Present Feedback:** Amber/Gold (#D97706)
- **Incorrect Feedback:** Slate (#64748B)

### Typography
- **Headings:** Instrument Serif (Google Fonts)
- **UI/Body:** Plus Jakarta Sans (Google Fonts)

---

## 🧪 Terminal CLI Version

You can also play the game in your terminal:

```bash
python Password_Guess.py
```

This runs the original CLI version with the same game logic.

---

## 📦 Dependencies

### Backend
- **FastAPI** — Modern web framework
- **Uvicorn** — ASGI server
- **Pydantic** — Data validation

### Frontend
- **Axios** — HTTP client (loaded via CDN)
- Pure HTML/CSS/JavaScript (no build tools required)

---

## 🚢 Deployment (Optional)

### Deploy Backend to Render/Railway

**Render:**
1. Create a new Web Service
2. Connect your GitHub repo
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**Railway:**
1. Create a new project from GitHub
2. Railway auto-detects Python and runs the app

### Deploy Frontend to GitHub Pages

1. Create a new branch `gh-pages`
2. Push `frontend/password-game.html` as `index.html`
3. Enable GitHub Pages in repo settings
4. Update API endpoint in the HTML to your deployed backend URL

---

## 🛡️ Security Note

This project stores game sessions **in-memory** only. For production use with persistent data, consider:
- Adding Redis for session storage
- Implementing user authentication
- Using a proper database (PostgreSQL, MongoDB)

---

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Kush Jain**

- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)
- Project built to demonstrate full-stack Python development skills

---

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Object-Oriented Programming in Python
- ✅ RESTful API design with FastAPI
- ✅ Frontend-backend integration
- ✅ Modern UI/UX design principles
- ✅ Responsive web design
- ✅ Game logic implementation
- ✅ Error handling and validation

---

## 📸 Screenshots

> Add screenshots of your game here to showcase on your GitHub profile!

---

**Made with ❤️ and Python**
