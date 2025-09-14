# Hyperflask-Start

Starter kit for [Hyperflask](https://hyperflask.dev) projects.

Features:

 - Hyperflask app based on recommended best practices
 - Dev environment based on [Development Containers](https://containers.dev/)
 - Useful dotfiles to start with
 - Optimized for VScode with breakpoint debugging for frontend and backend
 - [Mailpit](https://github.com/axllent/mailpit) for email testing
 - Production Dockerfile using [Litestream](https://litestream.io/) for realtime replication of SQLite

## Usage

Ensure that Docker is available on your machine.

The easiest way is to use the provided script:

    $ curl -L https://raw.githubusercontent.com/hyperflask/hyperflask-start/main/start.sh | bash

The longer way is to [install cookiecutter](https://cookiecutter.readthedocs.io/en/stable/README.html#installation) yourself and create a project using `gh:hyperflask/hyperflask-start`.

If you want to update your template at a later date, it is recommended to use [cruft](https://pypi.org/project/cruft/) instead of cookiecutter.

Once a project is created see the project's README.