from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "dbd_api online"}


def test_read_chapter():
    response = client.get("/chapter")
    assert response.status_code == 200


def test_read_map():
    response = client.get("/map")
    assert response.status_code == 200


def test_read_survivor():
    response = client.get("/survivor")
    assert response.status_code == 200


def test_read_killer():
    response = client.get("/killer")
    assert response.status_code == 200


# def test_read_perks_survivor_set():
#     response = client.get("/perk/survivor/set")
#     assert response.status_code == 200


# def test_read_perks_killer_set():
#     response = client.get("/perk/killer/set")
#     assert response.status_code == 200


# def test_read_perk_survivor_single():
#     response = client.get("/perk/survivor/single")
#     assert response.status_code == 200


# def test_read_perk_killer_single():
#     response = client.get("/perk/killer/single")
#     assert response.status_code == 200
