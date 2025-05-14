from flask import Blueprint, render_template
from app.models import Tournament

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    tournaments = Tournament.query.all()
    return render_template('index.html', tournaments=tournaments)
