import requests

BASE_URL = "http://localhost:8080/api/locations"


def get_locations():
    response = requests.get(BASE_URL)
    print(f"GET /locations status: {response.status_code}")
    locations = response.json()
    for location in locations:
        if "Balaton" not in location["name"]:
            print(location["name"])


def create_location(name, coords):
    payload = {"name": name, "coords": coords}
    response = requests.post(BASE_URL, json=payload)
    print(f"POST /locations status: {response.status_code}")
    print(response.json())


def main():
    print("--- GET all locations ---")
    get_locations()

    print("\n--- Create location (Balaton) ---")
    create_location("Balaton", "46.0,18.0")

    print("\n--- Create location with empty name ---")
    create_location("", "46.0,18.0")


if __name__ == "__main__":
    main()
