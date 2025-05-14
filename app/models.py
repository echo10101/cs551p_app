from app import db

class Tournament(db.Model):
    __tablename__ = 'tournaments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    matches = db.relationship('Match', back_populates='tournament', lazy=True)

class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    home_team = db.Column(db.String, nullable=False)
    away_team = db.Column(db.String, nullable=False)
    home_score = db.Column(db.Integer)
    away_score = db.Column(db.Integer)
    date = db.Column(db.String)
    match_city = db.Column(db.String)
    match_country = db.Column(db.String)
    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
    tournament = db.relationship('Tournament', back_populates='matches')
    goals = db.relationship('GoalScorer', back_populates='match', lazy=True)

class GoalScorer(db.Model):
    __tablename__ = 'goal_scorers'
    id = db.Column(db.Integer, primary_key=True)
    team_scored = db.Column(db.String)
    scorer = db.Column(db.String)
    minute = db.Column(db.Integer)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'))
    match = db.relationship('Match', back_populates='goals')
