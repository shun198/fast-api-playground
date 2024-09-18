from fastapi import status


def test_user_list(client):
    response = client.get("/api/users")
    assert response.status_code == status.HTTP_200_OK
