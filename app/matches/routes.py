from flask import Blueprint, render_template, request, abort
from app.models import Match

matches_bp = Blueprint('matches', __name__)

@matches_bp.route('/')
def list_matches():
    
    team_q   = request.args.get('q', type=str)
    year_q   = request.args.get('year', type=str)
    country_q= request.args.get('country', type=str)

    
    query = Match.query

   
    if team_q:
        query = query.filter(
            (Match.home_team.contains(team_q)) |
            (Match.away_team.contains(team_q))
        )

    # filter by year (assuming date stored as 'YYYY-MM-DD' or contains YYYY)
    if year_q:
        query = query.filter(Match.date.contains(year_q))

    # filter by country
    if country_q:
        query = query.filter(Match.match_country.contains(country_q))

    matches = query.all()

    # pass back the current search values for the form
    return render_template(
        'matches/list.html',
        matches=matches,
        q=team_q,
        year=year_q,
        country=country_q
    )

@matches_bp.route('/<int:id>')
def match_detail(id):
    match = Match.query.get(id)
    if match is None:
        abort(404)
    return render_template('matches/detail.html', match=match, goals=match.goals)
