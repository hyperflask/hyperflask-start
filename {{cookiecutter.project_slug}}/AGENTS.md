This web application is built using Hyperflask.

Hyperflask is a batteries-included Flask-based framework optimized for containerized, component-driven, HTMX-based web apps with SQLORM, Tailwind, DaisyUI, asset bundling, static generation, background tasks, SSE, forms, and user management.

Use the hyperflask skill as needed. Its references contain the full Hyperflask documentation.

# Directory overview

- `app/`
  - `assets/` – JS/CSS to bundle (esbuild, Tailwind).
  - `components/` – UI components (HTML/JPY/JS/TS/JSX/TSX).
  - `pages/` – file-based routes (Jinjapy or content).
  - `layouts/` – page layouts, `default.html` overrides built-in.
  - `templates/` – traditional Jinja templates for function routes.
  - `models.py` or `models/` – SQLORM models.
  - `routes.py` – function-based endpoints (like Flask).
  - `tasks.py` – Dramatiq background jobs.
  - `cron.py` – scheduled jobs.
  - `cli.py` – custom CLI commands.
- `public/` – public static files (no fingerprinting).
- `tests/` – pytest.
- `config.yml` (+ `config.<env>.yml`) – app config.
- `.env` (+ `.env.<env>`) – env vars (auto-loaded).
- `Dockerfile`, `pyproject.toml`, `package.json`.

# Useful commands

- Launch dev server: `uv run hyperflask dev` (starts a server available at <https://localhost:5000>)
- Run database migrations: `uv run hyperflask db migrate`
- Install a new python package: `uv add <package-name>`
- Use npm to install new javascript packages: `npm install <package-name>`

# Code style

Follow standard PEP 8 style when modifying Python code.
Use `uv run ruff format` to format python files.

# Testing

To validate your work, use `uv run hyperflask test-request /path` which will return the full HTTP response. DO NOT USE the dev server for your own testing.
Cookies can be preserved in between requests using `--cookie-file cookies.txt`. Use `--help` for more information if needed.

If you need to read the session data, use `uv run hyperflask decode-session-cookie --cookie-file cookies.txt`.

To build assets use:
- Development mode: `uv run hyperflask assets dev --build-only`
- Production mode: `uv run hyperflask assets build`

If the request you are testing requires assets, remember to build them before calling `test-request`.

You can query the database and get CSV formatted results using `echo "SELECT * FROM ..." | uv run hyperflask db query`

## Testing in a browser with Playwright

Playwright (Python) and Chromium are installed. Use it when `test-request` is not enough: checking the visual result, JavaScript behavior (htmx, Alpine.js, components), or multi-step user flows.

1. Build the assets (see above). Without them, pages render unstyled and without JS.
2. Start a dedicated server in the background on port 5001 (port 5000 is reserved for the user's dev server):
   `uv run hyperflask serve --no-gunicorn --port 5001 > /tmp/server.log 2>&1 & echo $! > /tmp/server.pid`
   Wait until `curl -s -o /dev/null http://127.0.0.1:5001/` succeeds. Restart it after modifying Python code.
3. Take a screenshot and look at it: `uv run playwright screenshot --full-page http://127.0.0.1:5001/path /tmp/screenshot.png`
   Use `--viewport-size "390,844"` to check the mobile layout.
4. For interactions, write a throwaway script in `/tmp` and run it with `uv run python /tmp/check.py`:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.on("console", lambda msg: print(f"console.{msg.type}: {msg.text}"))  # surface JS errors
    page.goto("http://127.0.0.1:5001/")
    page.get_by_role("link", name="Sign up").click()
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_role("button", name="Submit").click()
    page.wait_for_load_state("networkidle")  # let htmx requests settle
    print(page.get_by_role("alert").inner_text())
    page.screenshot(path="/tmp/screenshot.png", full_page=True)
    browser.close()
```

5. Stop the server when done: `kill $(cat /tmp/server.pid)`

Do not save screenshots or scripts in the project directory.

## Writing tests

Once you are satisfied that things are working properly, write unit tests for features that could suffer from regressions.
Tests should use pytest and be located in `tests/`. A `client` fixture provided a Flask test client is available.
Run tests using `uv run pytest tests`

Only write browser tests for features that depend on JavaScript or client-side behavior; prefer `client` tests otherwise.
Browser tests use pytest-playwright: request the `page` fixture and use relative URLs. The app is served automatically by the `live_server_url` fixture (see `tests/test_browser.py`):

```python
from playwright.sync_api import Page, expect

def test_signup(page: Page):
    page.goto("/signup")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_role("alert")).to_contain_text("Welcome")
```

Use `uv run pytest tests --tracing retain-on-failure` to keep a trace of failing browser tests in `test-results/`.

# Best practices

- Focus on implementing business logic of the app. Do not try to re-create features provided by the framework.
- Hyperflask aims to create component-driven apps. Do not hesitate to create as many custom components as needed. Pages should be an assembly of components.
- Use built-in UI components as much as possible. Custom components should be used for custom interfaces and custom logic. Custom components should use built-in UI components for their interfaces
- When the apps requires realtime updates because it has some collaboration features use server push. If you need to update different part of the apps as part of a single AJAX request (performed via htmx), use HTMX Out-of-band (OOB). Read the interactive apps and server push references of the hyperflask skill to learn more.
- Don't forget to include {% raw %}`{% use_layout %}`{% endraw %} on pages (unless no layout is needed)
- Don't forget to use imports in the python code of components.
- Only define a `get()` function in components if the component needs to be fetched using htmx. If the component is meant to be rendered as part of the template and only needs to react to POST request, defining a `post()` function is enough.
- Past the initial creation phase, always use migrations when modifying the database schema.
- Never use Flask blueprints. Prefer adding new routes as "pages" in `app/pages`.
