import random


def generate_secret_key():
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    with open(".env", "w") as f:
        f.write(f"FLASK_SECRET_KEY={secret_key}")


if __name__ == "__main__":
    generate_secret_key()