<div align="center">

# 🤖 Gemini Realtime AI API ⚡

### 🚀 Ultra Fast • Realtime • Developer Friendly

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=00F7FF&center=true&vCenter=true&width=700&lines=Unofficial+Gemini+Realtime+AI+API;Fast+%7C+Simple+%7C+Powerful;Built+For+Developers+%F0%9F%92%99" />

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![API](https://img.shields.io/badge/API-Online-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v1.0-purple?style=for-the-badge)

</div>

---

# 🌟 About Project

Gemini Realtime AI API is a fast and lightweight unofficial Google Gemini API built using Flask.  
It provides instant realtime AI responses in clean JSON format for developers, bots, tools and AI applications.

---

# ✨ Features

```diff
+ ⚡ Ultra Fast Realtime Responses
+ 🤖 Smart Gemini AI Integration
+ 🌐 Clean JSON Output
+ 🚀 Lightweight Flask Backend
+ 🔓 Easy API Integration
+ 🆓 Free To Use
+ 💻 Perfect For Bots & Apps
+ 📡 Stable API Structure
```

---

# 🌍 Live API

```bash
https://mkworld.eu.org/api/ask?prompt=Hello,%20how%20are%20you
```

---

# ⚡ API Endpoint

```http
GET /api/ask
```

---

# 🔮 Parameters

| Parameter | Type | Required | Description |
|-----------|------|-----------|-------------|
| `prompt` | string | ✅ Yes | Your message or question |

---

# 💠 Example Request

```bash
https://mkworld.eu.org/api/ask?prompt=Tell%20me%20a%20joke
```

---

# 📦 Example Response

```json
{
  "success": true,
  "response": "Why don't programmers like nature? Because it has too many bugs! 😂",
  "metadata": {
    "response_time": "2.31s",
    "timestamp": "2026-05-02T12:00:00Z",
    "model": "gemini"
  }
}
```

---

# 🚀 Quick Deploy

## 🟣 Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/)

---

## 🔵 Render

- Build Command:

```bash
pip install -r requirements.txt
```

- Start Command:

```bash
gunicorn app:app
```

---

## ⚫ Vercel

Supports instant deployment using `vercel.json`

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/gemini-realtime-api.git
cd gemini-realtime-api
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run Server

```bash
python app.py
```

---

# 🌐 Localhost Example

```bash
http://127.0.0.1:5000/api/ask?prompt=Hello
```

---

# 📁 Project Structure

```bash
gemini-realtime-api/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── vercel.json
└── README.md
```

---

# 🛠 Technologies Used

| Technology | Usage |
|------------|------|
| Python | Backend |
| Flask | API Framework |
| Requests | HTTP Requests |
| BeautifulSoup4 | Parsing |

---

# 📌 Available Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/` | GET | API Information |
| `/api/ask` | GET | Ask Gemini AI |

---

# ⚠️ Disclaimer

This project is made for educational & research purposes only.  
This is an unofficial implementation and is not affiliated with Google.

---

# 👨‍💻 Credits

<div align="center">

<a href="https://t.me/apift">
  <img src="https://img.shields.io/badge/Telegram-@apift-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
</a>
<a href="https://t.me/bizft">
  <img src="https://img.shields.io/badge/Telegram-@bizft-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/>
</a>
<br>
### 💙 Developed With Love By @bizft

</div>
