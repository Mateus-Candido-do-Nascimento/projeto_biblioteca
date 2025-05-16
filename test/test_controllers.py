def test_authors_list(client):
    resp = client.get('/authors/')
    assert resp.status_code == 200
    assert b'Autor' in resp.data or b'autor' in resp.data


def test_create_client(client):
    resp = client.post('/clients/create', data={
        'name': 'Teste',
        'email': 'teste@email.com',
        'phone': '1234'
    }, follow_redirects=True)
    assert resp.status_code == 200
    assert b'Teste' in resp.data


def test_books_list(client):
    resp = client.get('/books/')
    assert resp.status_code == 200
    assert b'Livro' in resp.data or b'livro' in resp.data 