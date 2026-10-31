# Hyperflask-Start

Starter kit for [Hyperflask](https://hyperflask.dev) projects.

Features:

 - Hyperflask app based on recommended best practices
 - Dev environment based on [Development Containers](https://containers.dev/)
 - Coding agent of your choice (Claude Code, Codex or OpenCode) installed in the dev container, using your existing credentials
 - Useful dotfiles to start with
 - Optimized for VScode with breakpoint debugging for frontend and backend
 - [Mailpit](https://github.com/axllent/mailpit) for email testing
 - Production Dockerfile using [Litestream](https://litestream.io/) for realtime replication of SQLite

## Usage

Ensure that Docker is available on your machine.

The easiest way is to use the provided script:

    $ curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

The longer way is to use [cruft](https://cruft.github.io/cruft/) yourself (recommended, as it allows updating your project later):

    $ uvx cruft create https://github.com/hyperflask/hyperflask-start

You can also use [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html#installation) directly with `gh:hyperflask/hyperflask-start`.

Once a project is created see the project's README.

## Updating your project

Projects created with cruft (including through `start.sh`) keep track of the template version they were generated from in a `.cruft.json` file. This lets you pull improvements made to this template into your existing project.

From your project directory (a git repository with no uncommitted changes):

    $ uvx cruft check   # check if your project is up to date with the template
    $ uvx cruft diff    # show the differences between your project and the template
    $ uvx cruft update  # apply the latest template changes to your project

`cruft update` shows you the changes before applying them. Changes that conflict with your own modifications are left as conflict markers or `.rej` files that you need to resolve manually. Review the result with `git diff` and commit it.

If your project was created with cookiecutter, you can link it to the template first:

    $ uvx cruft link https://github.com/hyperflask/hyperflask-start
