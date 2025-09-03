import requests

URL = "http://localhost:8080/api/locations"


def delete_all():
    requests.delete(URL)


def create(name: str = "Balaton", coords: str = "46.0,18.0") -> None:
    """
    Create a new location.

    This function sends a POST request to the API to create a new location with the given name and coordinates.
    """
    payload = {"name": name, "coords": coords}
    response = requests.post(URL, json=payload)
    assert response.status_code == 201
    json = response.json()
    assert json["name"] == name
