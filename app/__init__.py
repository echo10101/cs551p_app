import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    db_path = os.path.join(os.path.dirname(__file__), '..', 'football.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath(db_path)}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from app.main.routes import main_bp
    from app.tournaments.routes import tournaments_bp
    from app.matches.routes import matches_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(tournaments_bp, url_prefix='/tournaments')
    app.register_blueprint(matches_bp, url_prefix='/matches')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500

    return app
