#!/bin/bash

# wrap in main to prevent partial execution if failed download
main() {
    # use the same image as the dev container to prevent downloading one-time use images
    docker pull nikolaik/python-nodejs:python3.13-nodejs24 && \
    docker run --rm -it \
           -v $(pwd):/workspace \
           --user $(id -u):$(id -g) \
           nikolaik/python-nodejs:python3.13-nodejs24 \
           bash -c "cd /workspace && uv tool run cruft create https://github.com/hyperflask/hyperflask-start" \
           < /dev/tty # interactively ask for project name
}

main