import random
import subprocess


def generate_secret_key():
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    with open(".env", "w") as f:
        f.write(f"FLASK_SECRET_KEY={secret_key}")


def install_skill(source, skill):
    try:
        subprocess.run(
            ["npx", "-y", "skills", "add", source, "--skill", skill, "-y"],
            check=True,
        )
    except Exception as e:
        print(f"Failed to install {skill} skill: {e}")


if __name__ == "__main__":
    generate_secret_key()
    install_skill("https://hyperflask.dev", "hyperflask")
    install_skill("anthropics/skills", "frontend-design")
    install_skill("https://specification.website", "specification-website")
