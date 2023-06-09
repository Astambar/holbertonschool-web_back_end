#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    Envoie une requête POST pour enregistrer un nouvel utilisateur
    en utilisant les paramètres email et password
    """
    url = 'http://localhost:5000/users'
    payload = {'email': email, 'password': password}
    response = requests.post(url, data=payload)

    # Vérifie que la réponse est 200 OK et contient le message attendu
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Envoie une requête POST pour se connecter
    en utilisant un mot de passe incorrect
    """
    url = 'http://localhost:5000/sessions'
    payload = {'email': email, 'password': password}
    response = requests.post(url, data=payload)

    # Vérifie que la réponse est un échec d'authentification
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Envoie une requête POST pour se connecter
    en utilisant les paramètres email et password
    """
    url = 'http://localhost:5000/sessions'
    payload = {'email': email, 'password': password}
    response = requests.post(url, data=payload)

    # Vérifie que la réponse est 200 OK et contient le message attendu
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}

    # Retourne l'identifiant de session
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """
    Envoie une requête GET pour récupérer
    le profil d'un utilisateur non connecté
    """
    url = 'http://localhost:5000/profile'
    response = requests.get(url)

    # Vérifie que la réponse est un échec d'authentification
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """
    Envoie une requête GET pour récupérer
    le profil d'un utilisateur connecté en utilisant l'identifiant de session
    """
    url = 'http://localhost:5000/profile'
    headers = {"session_id": session_id}
    response = requests.get(url, cookies=headers)

    # Vérifie que la réponse est 200 OK
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """
    Envoie une requête DELETE pour se déconnecter
    en utilisant l'identifiant de session
    """
    url = 'http://localhost:5000/sessions'
    cookies = {'session_id': session_id}
    response = requests.delete(url, cookies=cookies)

    # Vérifie que la réponse est 200 OK et contient le message attendu
    assert response.status_code == 200
    assert response.json() == {'message': 'Bienvenue'}


def reset_password_token(email: str) -> str:
    """
    Demande un token de réinitialisation de mot de passe
    pour l'utilisateur donné
    """
    url = 'http://localhost:5000/reset_password'
    data = {'email': email}
    response = requests.post(url, json=data)
    assert response.status_code == 200
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Met à jour le mot de passe de l'utilisateur donné
    en utilisant un token de réinitialisation
    """
    url = 'http://localhost:5000/reset_password'
    data = {'email': email,
            'reset_token': reset_token,
            'new_password': new_password}
    response = requests.put(url, json=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'Password updated'}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
