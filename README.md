# 📒 Notebook Notes

A simple full-stack notes app with a notebook-style UI.  
Built for fast prototyping and hackathons.

---

## 🚀 Live Demo
- **Frontend:** https://end-to-end-notes.vercel.app  
- **Backend API Docs:** https://end-to-end-notes.onrender.com/docs

---

## 🧠 What it does
- Add notes
- Persist notes in a database
- View saved notes after refresh

---

## 🏗️ Architecture

```

Client (HTML + CSS + JS)
↓
FastAPI REST API (Render)
↓
MongoDB Atlas (Cloud Database)

```

---

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS (Notebook-style UI)
- Vanilla JavaScript
- Deployed on **Vercel**

**Backend**
- Python
- FastAPI
- Deployed on **Render**

**Database**
- MongoDB Atlas (Free Tier)

---

## 📂 Project Structure

```

.
├── backend
│   ├── main.py
│   └── requirements.txt
│
└── frontend
└── index.html

````

---

## ⚙️ API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/` | Health check |
| POST | `/add` | Add a note |
| GET | `/all` | Fetch all notes |

---

## 🧪 Local Setup (Optional)

### Backend
```bash
pip install -r requirements.txt
uvicorn main:app --reload
````

Set environment variable:

```
MONGO_URL=mongodb+srv://<user>:<password>@cluster...
```

### Frontend

Open `frontend/index.html` in browser or deploy via Vercel.

---

## 🎯 Why this project

* Demonstrates full-stack integration
* Clean REST API design
* Cloud database usage
* Real deployment (not just local)

---

## 🔒 Notes

* CORS enabled for hackathon/demo purposes
* Uses free tiers (may have cold start delay)

---

## 👤 Author

Built by **Team Vanaras** for hackathon submission.

````

---

## ✅ What to do now
```bash
git add README.md
git commit -m "add README"
git push
````
