import json
from app import app

def test_create_comment():
    client = app.test_client()
    response = client.post("/accounts/1/tasks/10/comments",
                            json={"text": "Automated test comment"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["text"] == "Automated test comment"

def test_get_comments():
    client = app.test_client()
    response = client.get("/accounts/1/tasks/10/comments")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_comment():
    client = app.test_client()
    response = client.put("/accounts/1/tasks/10/comments/1",
                           json={"text": "Updated by test"})
    assert response.status_code == 200
    assert response.get_json()["text"] == "Updated by test"

def test_delete_comment():
    client = app.test_client()
    response = client.delete("/accounts/1/tasks/10/comments/1")
    assert response.status_code == 200
