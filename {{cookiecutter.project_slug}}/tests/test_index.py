
def test_index(client):
    assert client.get("/", follow_redirects=True).status_code == 200
