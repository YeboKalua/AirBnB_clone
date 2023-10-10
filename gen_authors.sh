#!/usr/bin/env bash

set -e

# Set the path to the Git repository
REPO_PATH="/AirBnB_clone"

# Set the path to the AUTHORS file
AUTHORS_FILE="AUTHORS"

# Generate unique authors and emails from Git commit history
git -C "$REPO_PATH" log '--format=%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf > "$AUTHORS_FILE"
