#!/bin/bash

# Optional environment variables:
#   HYPERFLASK_PROJECT_NAME: name of the project
#   HYPERFLASK_AGENT: coding agent to install (claude, codex, opencode, none)
# When both are provided, the project is created without prompting.

json_escape() {
    local s=${1//\\/\\\\}
    printf '%s' "${s//\"/\\\"}"
}

# wrap in main to prevent partial execution if failed download
main() {
    local extra_context=()
    [ -n "$HYPERFLASK_PROJECT_NAME" ] && extra_context+=("\"project_name\": \"$(json_escape "$HYPERFLASK_PROJECT_NAME")\"")
    [ -n "$HYPERFLASK_AGENT" ] && extra_context+=("\"agent\": \"$(json_escape "$HYPERFLASK_AGENT")\"")
    local IFS=,
    local cruft_extra_context="{${extra_context[*]}}"
    unset IFS

    local cruft_args=""
    local docker_args=(-it)
    local stdin=/dev/tty # interactively ask for missing values
    if [ ${#extra_context[@]} -eq 2 ]; then
        cruft_args="--no-input"
        docker_args=()
        stdin=/dev/null
    fi

    # use the same image as the dev container to prevent downloading one-time use images
    docker pull nikolaik/python-nodejs:python3.14-nodejs24 && \
    docker run --rm "${docker_args[@]}" \
           -v "$(pwd)":/workspace \
           --user $(id -u):$(id -g) \
           -e CRUFT_EXTRA_CONTEXT="$cruft_extra_context" \
           -e CRUFT_ARGS="$cruft_args" \
           nikolaik/python-nodejs:python3.14-nodejs24 \
           bash -c 'cd /workspace && uv tool run cruft create $CRUFT_ARGS --extra-context "$CRUFT_EXTRA_CONTEXT" https://github.com/hyperflask/hyperflask-start' \
           < $stdin
}

main
