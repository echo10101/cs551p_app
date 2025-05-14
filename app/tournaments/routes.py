from flask import Blueprint, render_template, abort
from app.models import Tournament, Match

tournaments_bp = Blueprint('tournaments', __name__)

@tournaments_bp.route('/')
def list_tournaments():
    tournaments = Tournament.query.all()
    return render_template('tournaments/list.html', tournaments=tournaments)

@tournaments_bp.route('/<int:id>')
def tournament_detail(id):
    tournament = Tournament.query.get(id)
    if tournament is None:
        abort(404)
    matches = Match.query.filter_by(tournament_id=id).all()
    return render_template('tournaments/detail.html', tournament=tournament, matches=matches)
