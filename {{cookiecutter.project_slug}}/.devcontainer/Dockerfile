FROM nikolaik/python-nodejs:python3.14-nodejs24

# Configure apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get -y install --no-install-recommends apt-utils 2>&1

# Install git, process tools, lsb-release (common in install instructions for CLIs)
RUN apt-get -y install git procps lsb-release nano

# Install any missing dependencies for enhanced language service
RUN apt-get install -y libicu[0-9][0-9]

# Install system dependencies required by Playwright browsers (browsers are installed in postCreateCommand)
RUN npx -y playwright install-deps chromium

RUN mkdir /workspace
WORKDIR /workspace
RUN pip install -U setuptools wheel pip
{%- if cookiecutter.agent == "opencode" %}

# Create the parents of the agent credentials mounts so docker does not create them as root
RUN mkdir -p /home/pn/.config /home/pn/.local/share && chown -R pn:pn /home/pn/.config /home/pn/.local
{%- endif %}

# Set the default shell to bash rather than sh
ENV SHELL /bin/bash
ENV DEBIAN_FRONTEND=
