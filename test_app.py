import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_health_check(client):
    rv = client.get('/health')
    json_data = rv.get_json()
    assert json_data['status'] == "UP"
