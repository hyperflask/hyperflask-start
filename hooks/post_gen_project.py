import random


def generate_secret_key():
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    with open(".env", "r") as f:
        content = f.read()
    with open(".env", "w") as f:
        content = content.replace("FLASK_SECRET_KEY=changeme", f"FLASK_SECRET_KEY='{secret_key}'")
        f.write(content)


if __name__ == "__main__":
    generate_secret_key()