<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00f7ff,100:7b2ff7&height=200&section=header&text=Gemini%20Realtime%20AI%20API&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=Ultra%20Fast%20%E2%80%A2%20Realtime%20%E2%80%A2%20Developer%20Friendly&descAlignY=58&descSize=16&animation=fadeIn" />

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=00F7FF&center=true&vCenter=true&width=750&lines=Unofficial+Gemini+Realtime+AI+API+%E2%9A%A1;No+API+Key+Required+%F0%9F%94%93;Built+For+Developers+%7C+Bots+%7C+Tools+%F0%9F%92%99;Fast+%7C+Simple+%7C+Powerful+%F0%9F%9A%80" alt="Typing SVG" />

<br><br>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/API-Online%20%E2%9C%85-00C853?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-FF6F00?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-v1.0-7B2FF7?style=for-the-badge)
![Dev](https://img.shields.io/badge/Dev-%40bizft-00f7ff?style=for-the-badge)

<br>

> **🔥 The fastest unofficial Google Gemini API — no keys, no limits, just results.**

</div>

---

<div align="center">

## 🌟 About Project

</div>

**Gemini Realtime AI API** is a fast, lightweight unofficial Google Gemini wrapper built on **Flask**.  
It reverse-engineers Gemini's web interface to deliver real-time AI responses in clean JSON — **zero API key required.**

Perfect for Telegram bots, automation tools, Discord bots, web apps, and anything that needs AI responses instantly.

---

<div align="center">

## ✨ Features

</div>

```diff
+ ⚡ Ultra Fast Realtime AI Responses
+ 🔓 No API Key Required — Works Out of The Box
+ 🤖 Smart Gemini AI Integration via Web Scraping
+ 🌐 Clean & Structured JSON Output
+ 🚀 Lightweight Flask Backend — Low Resource Usage
+ 📊 Rich Metadata — Response Time, Word Count, Timestamp
+ 💻 Perfect For Bots, Apps & Automation Tools
+ 🔄 Auto Session + Token Extraction Per Request
+ 🛡️ Built-in Error Handling & Clean Error Responses
+ 🆓 Completely Free To Use
```

---

<div align="center">

## 🌍 Live API

</div>

<div align="center">

```
https://mkworld.eu.org/api/ask?prompt=Hello,%20how%20are%20you
```

</div>

---

<div align="center">

## ⚡ API Reference

</div>

### Base URL
```
https://mkworld.eu.org
```

### Endpoint
```http
GET /api/ask
```

### Parameters

| Parameter | Type | Required | Description |
|:---------:|:----:|:--------:|:------------|
| `prompt` | `string` | ✅ Yes | Your message or question for Gemini |

---

<div align="center">

## 💠 Example Request

</div>

```bash
curl "https://mkworld.eu.org/api/ask?prompt=Tell%20me%20a%20joke"
```

Or simply open in browser:
```
https://mkworld.eu.org/api/ask?prompt=Tell me a joke
```

---

<div align="center">

## 📦 Example Response

</div>

```json
{
  "success": true,
  "prompt": "Tell me a joke",
  "response": "Why don't programmers like nature? Because it has too many bugs! 😂",
  "metadata": {
    "response_time": "2.31s",
    "timestamp": "2026-05-02T12:00:00Z",
    "model": "gemini",
    "character_count": 68,
    "word_count": 14
  },
  "api_dev": "@bizft"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Missing required parameter: prompt",
  "api_dev": "@bizft"
}
```

---

<div align="center">

## 🚀 Quick Deploy

</div>

### 🟣 Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/)

---

### 🔵 Render
| | |
|---|---|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |

---

### ⚫ Vercel
Add a `vercel.json` in root — supports instant serverless deployment.

```json
{
  "builds": [{ "src": "app.py", "use": "@vercel/python" }],
  "routes": [{ "src": "/(.*)", "dest": "app.py" }]
}
```

---

<div align="center">

## ⚙️ Self Host

</div>

**1. Clone**
```bash
git clone https://github.com/mkhossainx/gemini-realtime-api.git
cd gemini-realtime-api
```

**2. Install**
```bash
pip install -r requirements.txt
```

**3. Run**
```bash
python app.py
```

**4. Test**
```bash
http://127.0.0.1:5000/api/ask?prompt=Hello
```

---

<div align="center">

## 📁 Project Structure

</div>

```
gemini-realtime-api/
│
├── 🐍 app.py               ← Main Flask application
├── 📦 requirements.txt     ← Python dependencies
├── ⚙️  Procfile             ← For Railway / Heroku
├── 🏃 runtime.txt          ← Python version
├── ▲  vercel.json          ← Vercel config
└── 📄 README.md            ← Documentation
```

---

<div align="center">

## 🛠 Tech Stack

</div>

| Technology | Role |
|:----------:|:----:|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Backend Logic |
| ![Flask](https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask) | API Framework |
| ![Requests](https://img.shields.io/badge/-Requests-FF6F00?style=flat-square) | HTTP Client |
| ![BeautifulSoup](https://img.shields.io/badge/-BeautifulSoup4-4CAF50?style=flat-square) | HTML Parsing |

---

<div align="center">

## 📌 All Endpoints

</div>

| Endpoint | Method | Description |
|:--------:|:------:|:-----------:|
| `/` | `GET` | API info & usage |
| `/api/ask` | `GET` | Ask Gemini AI |

---

<div align="center">

## ⚠️ Disclaimer

</div>

> This project is built for **educational & research purposes only.**  
> This is an **unofficial implementation** and is not affiliated with, endorsed by, or connected to Google in any way.  
> Use responsibly and at your own risk.

---

<div align="center">

## 👨‍💻 Credits

<br>

<img src="https://capsule-render.vercel.app/api?type=rect&color=0:7b2ff7,100:00f7ff&height=2&width=600" />

<br>

### 💙 Developed By

[![bizft](https://img.shields.io/badge/%40bizft-Developer-00f7ff?style=for-the-badge&logo=telegram)](https://github.com/mkhossainx)

### 🚀 Powered By

[![apift](https://img.shields.io/badge/%40apift-API%20Partner-7b2ff7?style=for-the-badge&logo=telegram)](https://t.me/apift)

<br>

---

## ⭐ Support The Project

**If this helped you:**

[![Star](https://img.shields.io/badge/⭐%20Star-This%20Repo-FFD700?style=for-the-badge)](https://github.com/mkhossainx)
[![Fork](https://img.shields.io/badge/🍴%20Fork-This%20Project-00C853?style=for-the-badge)](https://github.com/mkhossainx)
[![Share](https://img.shields.io/badge/📢%20Share-With%20Friends-FF6F00?style=for-the-badge)](https://github.com/mkhossainx)

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7b2ff7,100:00f7ff&height=120&section=footer&text=Made%20with%20%F0%9F%92%99%20%26%20Python&fontSize=20&fontColor=ffffff&fontAlignY=65&animation=fadeIn" />

</div>
