# 🚀 AI-Powered Website SEO Audit Platform

# 🚀 AI-Powered Website SEO Audit Platform

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![React](https://img.shields.io/badge/React-19-61DAFB?logo=react)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-4-38BDF8?logo=tailwindcss)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-purple)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

An AI-powered SEO auditing platform that crawls websites, performs comprehensive SEO analysis, generates AI-based optimization recommendations using OpenRouter LLMs, and exports professional PDF reports.

---

## 📸 Screenshots

| Dashboard | Audit Details |
|-----------|---------------|
| ![](images/dashboard.png) | ![](images/audit-details.png) |

| AI Recommendations | PDF Report |
|-------------------|------------|
| ![](images/recommendations.png) | ![](images/pdf-report.png) |

---

# ✨ Features

### 🌐 Website Crawling

- Crawl websites up to a configurable number of pages
- Extract internal links
- Ignore duplicate pages
- Respect crawl limits

---

### 📊 Technical SEO Analysis

Checks include:

- Title tag
- Meta description
- Heading structure
- Canonical tag
- Language attribute
- Internal links
- External links
- Image ALT attributes
- Word count
- SEO score calculation

---

### 🤖 AI Recommendations

Powered by **OpenRouter LLMs**

Generates recommendations for:

- Meta title
- Meta description
- Heading structure
- Image ALT improvements
- Internal linking
- Page speed
- Mobile optimization
- Crawl optimization

Only failed checks receive recommendations.

---

### 📄 PDF Report Generation

Generate downloadable reports containing:

- Website details
- SEO score
- SEO metrics
- Passed checks
- Failed checks
- AI recommendations

---

### 📈 Dashboard

- Audit history
- SEO score visualization
- Detailed metrics
- AI recommendation viewer

---

# 🏗️ Project Architecture

```
                React Frontend
                      │
                      ▼
               FastAPI Backend
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Website Crawler  SEO Analyzer   OpenRouter
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 SQLite Database
                      │
                      ▼
                 PDF Report Generator
```

---

# 🛠 Tech Stack

## Backend

- FastAPI
- SQLAlchemy ORM
- Pydantic
- ReportLab
- Requests
- BeautifulSoup
- OpenRouter API

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- Recharts

## Database

- SQLite

## AI

- OpenRouter
- DeepSeek Chat

---

# 📁 Folder Structure

```
seo-audit-platform/

│
├── app/
│   ├── api/
│   ├── core/
│   ├── crawler/
│   ├── database/
│   ├── models/
│   ├── repositories/
│   ├── reports/
│   ├── response_schemas/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.jsx
│
├── pyproject.toml
├── docker-compose.yml
└── README.md
```

---

# 🚀 Installation

## Clone

```bash
git clone https://github.com/yourusername/seo-audit-platform.git

cd seo-audit-platform
```

---

## Backend

```bash
uv sync

uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# ⚙️ Environment Variables

Backend `.env`

```env
OPENROUTER_API_KEY=your_api_key

OPENROUTER_MODEL=deepseek/deepseek-chat-v3

DATABASE_URL=sqlite:///seo_audit.db

MAX_AI_RECOMMENDATIONS=1
```

---

# 📊 SEO Metrics

The platform evaluates:

- Title Length
- Meta Description Length
- Word Count
- H1 Count
- H2 Count
- Total Images
- Images without ALT
- Internal Links
- External Links
- Canonical Tag
- Language
- SEO Score

---

# 🤖 AI Recommendation Engine

The AI analyzes SEO issues and generates actionable recommendations.

Example:

```
Meta Description

Add a meta description between 120–160 characters to improve CTR.
```

---

# 📄 PDF Report

Each audit generates a professional PDF containing:

- Website Information
- SEO Score
- Metrics Table
- Passed Checks
- Failed Checks
- AI Recommendations

---

# 🎯 Future Improvements

- User Authentication
- PostgreSQL
- Celery Background Tasks
- Scheduled SEO Audits
- Email Reports
- Historical Comparison
- SEO Trend Charts
- Multi-user Dashboard

---

# 👨‍💻 Author

**Harkirat Singh**

Backend Developer | Python | FastAPI | AI Applications

GitHub:https://github.com/harkirat-singh2

LinkedIn:https://www.linkedin.com/in/harkiratsingh11/
---

# ⭐ If you like this project

Give it a ⭐ on GitHub!
