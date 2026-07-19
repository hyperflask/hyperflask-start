import random
import os


def generate_secret_key():
    secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    with open(".env", "w") as f:
        f.write(f"FLASK_SECRET_KEY={secret_key}")


def download_agent_skills():
    import re
    import textwrap
    import urllib.parse
    import urllib.request

    llms_url = "https://hyperflask.dev/llms.txt"
    skills_dir = ".agents/skills"

    os.makedirs(skills_dir, exist_ok=True)

    try:
        with urllib.request.urlopen(llms_url) as response:
            llms_txt = response.read().decode()
    except Exception as e:
        print(f"Failed to download agent skills: {e}")
        return

    def parse_llms_links(llms_txt):
        sections = {}
        current_section = None
        link_re = re.compile(r"^- \[([^\]]+)\]\(([^)]+)\)")

        for line in llms_txt.splitlines():
            if line.startswith("## "):
                current_section = line[3:].strip()
                sections.setdefault(current_section, [])
                continue

            if current_section is None:
                continue

            match = link_re.match(line.strip())
            if match:
                sections[current_section].append({
                    "title": match.group(1).strip(),
                    "url": match.group(2).strip(),
                })

        return sections

    def slug_from_url(url):
        path_parts = [
            part
            for part in urllib.parse.urlparse(url).path.split("/")
            if part and part != "index.md"
        ]
        if not path_parts:
            return None
        return path_parts[-1]

    def download_text(url):
        with urllib.request.urlopen(url) as response:
            return response.read().decode()

    def write_skill(skill_name, title, description, content):
        skill_path = os.path.join(skills_dir, skill_name, "SKILL.md")
        os.makedirs(os.path.dirname(skill_path), exist_ok=True)

        skill_content = textwrap.dedent(f"""\
            # {title}

            {description}

            ## Reference

            {content.rstrip()}
        """)

        with open(skill_path, "w") as f:
            f.write(skill_content)
            f.write("\n")

    sections = parse_llms_links(llms_txt)

    for guide in sections.get("Guides", []):
        slug = slug_from_url(guide["url"])
        if not slug:
            continue

        skill_name = f"hyperflask-{slug}"
        try:
            content = download_text(guide["url"])
            write_skill(
                skill_name=skill_name,
                title=f"Hyperflask {guide['title']}",
                description=f"Use this skill when working with Hyperflask {guide['title'].lower()} features.",
                content=content,
            )
        except Exception as e:
            print(f"Failed to download skill {skill_name}: {e}")

    component_sections = []
    for component in sections.get("Components", []):
        try:
            content = download_text(component["url"]).rstrip()
            component_sections.append(f"# {component['title']}\n\nSource: {component['url']}\n\n{content}")
        except Exception as e:
            print(f"Failed to download built-in component guide {component['title']}: {e}")

    if component_sections:
        try:
            write_skill(
                skill_name="hyperflask-builtin-components",
                title="Hyperflask built-in components",
                description="Use this skill when working with Hyperflask built-in UI components.",
                content="\n\n---\n\n".join(component_sections),
            )
        except Exception as e:
            print(f"Failed to write skill hyperflask-builtin-components: {e}")


if __name__ == "__main__":
    generate_secret_key()
    download_agent_skills()
