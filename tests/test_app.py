import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Football' in res.data

def test_tournaments_list(client):
    res = client.get('/tournaments/')
    assert res.status_code == 200

def test_tournaments_detail(client):
    res = client.get('/tournaments/1')
    assert res.status_code in (200, 404)

def test_matches_list(client):
    res = client.get('/matches/')
    assert res.status_code == 200

def test_matches_search(client):
    res = client.get('/matches/?q=United')
    assert res.status_code == 200

def test_match_detail(client):
    res = client.get('/matches/1')
    assert res.status_code in (200, 404)

def test_404_page(client):
    res = client.get('/nonexistent')
    assert res.status_code == 404
