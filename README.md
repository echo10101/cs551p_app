```markdown
 CS551P Flask Football App

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-3.1.1-lightgrey)](https://flask.palletsprojects.com/)  
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A Flask-based web application for the **CS551P Advanced Programming** course.  
It uses an open data source (`football.db`) to display tournaments, matches, and goal scorers.  

---

 Table of Contents

 [Features](#features)  
 [Architecture](#architecture)  
 [Data Source](#data-source)  
 [Installation](#installation)  
 [Configuration](#configuration)  
 [Usage](#usage)  
 [Testing](#testing)  
 [Deployment](#deployment)  
 [Project Structure](#project-structure)  
 [Maintenance & Contributing](#maintenance--contributing)  
 [License](#license)  

---

 Features

- **Database**: SQLite with three related tables (`Tournament`, `Match`, `GoalScorer`)  
- **Blueprints**: Modular routes for main, tournaments, matches  
- **Search & Filters**: Search by team, year, country  
- **Charts**: Top-10 matches “chart” via HTML tables  
- **Error Handling**: Custom `404` and `500` pages  
- **Testing**: `pytest` coverage for routes, search, error pages  
- **Responsive UI**: Bootstrap 5 with custom styles  

---

 Architecture

```

app.py          # Application factory and entry point
wsgi.py         # WSGI entrypoint for production servers
app/            # Flask package
├── **init**.py # create\_app()
├── models.py   # SQLAlchemy models
├── main/       # Homepage routes
├── tournaments/# Tournament routes & templates
└── matches/    # Match routes, search & filters
static/         # CSS, JS (Bootstrap) assets
templates/      # Jinja2 templates hierarchy
tests/          # pytest test suite
render.yaml     # Render.com deployment config
football.db     # SQLite open data source (7k+ records)

````

---

Data Source

 Name**: `football.db`  
 Records: ~3,700 matches, ~9,000 goal events  
Schema:  
   `tournaments(id, name)`  
   `matches(id, home_team, away_team, home_score, away_score, date, match_city, match_country, tournament_id)`  
   `goal_scorers(id, team_scored, scorer, minute, match_id)`  

---

 Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/echo10101/cs551p_app.git
   cd cs551p_app
````

2. Create a virtual environment (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3.Install dependencies

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4.Ensure database file

   Place `football.db` in the project root
   Or update `SQLALCHEMY_DATABASE_URI` in `app/__init__.py`



 Configuration

Environment Variables (optional)

  ```bash
  export FLASK_ENV=development
  export SECRET_KEY='your-secret-key'
  ```

Render.com will read `render.yaml` automatically.

---

 Usage

Run locally

  ```bash
  python3 app.py
  ```

  Access at: `http://localhost:3000/`

Gunicorn (production)

  ```bash
  gunicorn wsgi:app
  ```

---

Testing

Run the test suite with pytest:

```bash
pytest --maxfail=1 --disable-warnings -q
```

You should see all tests pass for routes, search, and error handlers.

---

Deployment

This project can be deployed on Render.com with zero-config:

1. Connect your GitHub repo in the Render Dashboard.
2. Ensure `render.yaml` is at the repo root:

   ```yaml
   services:
     - type: web
       name: cs551p-flask-app
       rootDirectory: .
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn wsgi:app
   ```
3. Push to `main` branch → Render will automatically build and deploy.

Live Demo: [https://cs551p-app.onrender.com](https://cs551p-app.onrender.com)

---


---

Maintenance & Contributing

 Add new features**: follow Blueprint pattern in `app/`
 Update data**: replace `football.db` and run migrations (optional)
 Style changes**: edit `static/css/style.css`
 Testing**: add tests under `tests/` and ensure 100% route coverage
 Issues & PR**: welcome on GitHub

---

License

This project is licensed under the MIT License** – see the [LICENSE](LICENSE) file for details.



Last updated: May 2025*

```
```

