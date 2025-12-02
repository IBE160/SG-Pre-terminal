# Use a multi-stage build to keep the final image clean
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Install Node.js, Python, and uv
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends curl python3 python3-pip \
    && curl -sL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get -y install nodejs \
    && pip3 install uv

# Set the working directory
WORKDIR /workspace

# Copy setup scripts
COPY on-create.sh start.sh /tmp/
RUN chmod +x /tmp/on-create.sh /tmp/start.sh

USER vscode
