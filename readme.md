# CS551P Flask Football App

This project is a Flask-based web application for the CS551P course.
It uses an open data source (football.db) to display tournaments, matches, and goal scorers.

## Features
- SQLite database with three related tables: Tournament, Match, GoalScorer
- List and detail views for tournaments and matches
- Search functionality for matches
- Basic HTML table "charts" for top 10 matches
- Custom 404 and 500 error pages

## Installation
```bash
pip install -r requirements.txt
python app.py
```

## Running Tests
```bash
pytest
```

## Deployment
This app can be deployed on Render using the provided render.yaml.

