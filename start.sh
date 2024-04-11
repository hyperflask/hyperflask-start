#!/bin/bash

# wrap in main to prevent partial execution if failed download
main() {
    # use the same image as the dev container to prevent downloading one-time use images
    docker pull nikolaik/python-nodejs:python3.11-nodejs22 && \
    docker run --rm -it \
           -v $(pwd):/workspace \
           nikolaik/python-nodejs:python3.11-nodejs22 \
           bash -c "cd /workspace && pip install cruft && cruft create https://github.com/hyperflask/hyperflask-start"
}

main