# {{cookiecutter.project_name}}

This is an [Hyperflask](https://hyperflask.dev) project.

## Development environment

Using Visual Studio Code:

1. Open your project folder in vscode
2. Use the Dev Containers: Reopen in Container command from the Command Palette
3. Launch your app from a VS Code terminal: `uv run hyperflask dev`

Using other editors:

1. [Install devcontainers-cli](https://github.com/devcontainers/cli#npm-install)
2. Start dev container: `devcontainer up --workspace-folder .`
3. Launch your app: `devcontainer exec uv run hyperflask dev`
3. Go to http://localhost:5000
{%- if cookiecutter.agent != "none" %}
{%- set agent_name = {"claude": "Claude Code", "codex": "Codex", "opencode": "OpenCode"}[cookiecutter.agent] %}
{%- set agent_url = {"claude": "https://code.claude.com/docs", "codex": "https://developers.openai.com/codex/cli", "opencode": "https://opencode.ai/docs"}[cookiecutter.agent] %}
{%- set agent_cmd = {"claude": "claude", "codex": "codex", "opencode": "opencode"}[cookiecutter.agent] %}
{%- set agent_dirs = {"claude": "`~/.claude` and `~/.claude.json`", "codex": "`~/.codex`", "opencode": "`~/.config/opencode` and `~/.local/share/opencode`"}[cookiecutter.agent] %}

## Coding agent

[{{ agent_name }}]({{ agent_url }}) is installed in the dev container. Run it from a terminal inside the container: `{{ agent_cmd }}`

Your credentials and settings are shared with the host: {{ agent_dirs }} are mounted in the container.
{%- if cookiecutter.agent == "claude" %}
On macOS, Claude Code stores credentials in the Keychain, so you will need to log in once inside the container.
{%- endif %}
{%- endif %}

## Updating from the template

This project was generated from [hyperflask-start](https://github.com/hyperflask/hyperflask-start) using [cruft](https://cruft.github.io/cruft/). The template version it is based on is tracked in `.cruft.json`.

To pull the latest template improvements into this project, commit or stash your changes first, then run (from inside the dev container or anywhere [uv](https://docs.astral.sh/uv/) is installed):

    uvx cruft check   # check if the project is up to date with the template
    uvx cruft diff    # show the differences between the project and the template
    uvx cruft update  # apply the latest template changes

`cruft update` shows you the changes before applying them. Changes that conflict with your own modifications are left as conflict markers or `.rej` files that you need to resolve manually. Review the result with `git diff` and commit it.
