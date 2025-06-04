import pytest 
from wsgi import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_dice(client):
    response = client.get('/dice')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data["roll"], int)
    assert data["roll"] > 0
    assert data["roll"] <= 6