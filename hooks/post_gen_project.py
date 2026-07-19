import random
import os
import json


def generate_secret_key():
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    with open(".env", "w") as f:
        f.write(f"FLASK_SECRET_KEY={secret_key}")


def download_agent_skills():
    import urllib.request

    manifest_url = "https://hyperflask.dev/agent-skills/skills.json"
    skills_dir = ".agents/skills"

    os.makedirs(skills_dir, exist_ok=True)

    try:
        with urllib.request.urlopen(manifest_url) as response:
            manifest = json.loads(response.read().decode())
    except Exception as e:
        print(f"Failed to download agent skills: {e}")
        return

    for skill in manifest:
        if skill['name'] == "hyperflask":
            continue
        skill_url = f"{skill['url']}SKILL.md"
        skill_path = os.path.join(skills_dir, skill['name'], "SKILL.md")
        os.makedirs(os.path.dirname(skill_path), exist_ok=True)
        try:
            with urllib.request.urlopen(skill_url) as response:
                with open(skill_path, "wb") as f:
                    f.write(response.read())
        except Exception as e:
            print(f"Failed to download skill {skill['name']}: {e}")


if __name__ == "__main__":
    generate_secret_key()
    download_agent_skills()
