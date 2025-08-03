# 📱 Higher-Lower: Instagram Followers Game

A simple terminal-based game built with Python where you guess which Instagram profile has **more followers**. Inspired by the classic "Higher-Lower" game format.

---

## 🎮 Features

- 100 popular Instagram accounts
- Random profile matchups
- Accurate follower comparison logic
- Score tracking system
- Replay functionality
- Clean CLI interface
- Easy to extend or customize

---

## 📷 Example Gameplay

```
Who has more Instagram followers?
A: Cristiano Ronaldo
B: Kylie Jenner
Your answer (A/B): A

✅ Correct! Cristiano Ronaldo has 630,000,000 followers.
🏆 Score: 1
```

---

## 🧠 How It Works

- Two random Instagram accounts are shown.
- You guess which one has more followers.
- If you're right, your score increases.
- If you're wrong, the game ends.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ayovz/HigherLower.git
cd HigherLower
```

### 2. Run the game
```
python main.py
```
⚠️ Requires Python 3.6 or higher.

## 📁 Project Structure
```
higher-lower-instagram-game/
│
├── main.py          # Main game logic
├── data.py          # Instagram accounts & ASCII art
└── README.md        # Documentation
```

✍️ Customize

Want to add more profiles?
Open data.py and add to the data list:
```
data = [
    {"name": "Cristiano Ronaldo", "followers": 630_000_000},
    {"name": "Your New Influencer", "followers": 123_000_000},
    ...
]
```

---

## ✅ To-Do Ideas

- Add difficulty levels
- Track high scores
- Add GUI using Tkinter or PyGame
- Turn into a web app (Flask or React)

## 📄 License

MIT License. Feel free to modify and share.
