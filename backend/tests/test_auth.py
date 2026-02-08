import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_signup_and_login_success(client):
    signup_data = {
        "username": "testuser_auth_success",
        "password": "testpassword",
        "confirm_password": "testpassword"
    }

    signup_response = client.post(
        "/auth/signup",
        json=signup_data
    )
    assert signup_response.status_code == 201

    login_data = {
        "username": "testuser_auth_success",
        "password": "testpassword"
    }

    login_response = client.post(
        "/auth/login",
        json=login_data
    )
    assert login_response.status_code == 200

    response_json = login_response.get_json()
    assert "access_token" in response_json
    assert "refresh_token" in response_json


def test_signup_existing_user_fails(client):
    user_data = {
        "username": "testauth_user_duplicate",
        "password": "password123",
        "confirm_password": "password123"
    }

    first_response = client.post(
        "/auth/signup",
        json=user_data
    )
    assert first_response.status_code == 201

    second_response = client.post(
        "/auth/signup",
        json=user_data
    )
    assert second_response.status_code == 409
