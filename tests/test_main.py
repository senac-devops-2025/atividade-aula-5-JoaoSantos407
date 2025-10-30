# tests/test_main.py

from app.main import greet

def test_greet_basic():
    # Altere o valor esperado aqui:
    assert greet("DevOps") == "Olá, DevOps! Bem-vindo à Aula 05."
