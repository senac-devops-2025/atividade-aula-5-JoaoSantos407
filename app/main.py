import os

def greet(name: str):
    # Altere esta linha:
    return f"Olá, {name}! Bem-vindo à Aula 05."

if __name__ == "__main__":
    user = os.getenv("APP_USER", "Mundo")
    print(greet(user))
