#!/bin/bash

main() {
    VENV=/tmp/cookiecutter-venv
    python -m venv $VENV && \
    $VENV/bin/pip install cruft && \
    $VENV/bin/cruft create https://github.com/hyperflask/hyperflask-start && \
    rm -r $VENV
}

main