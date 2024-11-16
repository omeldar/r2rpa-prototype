#!/usr/bin/env bash

# Check if DISPLAY variable is set
if [ -z "$DISPLAY" ]; then
  echo "DISPLAY variable is not set. Setting it to :0"
  export DISPLAY=:0
fi

# Allow local Docker containers to access the X11 server
echo "Granting X11 access to Docker..."
xhost +local:docker

# Run docker-compose up
echo "Starting Docker Compose..."
docker-compose up

# Revoke X11 access to Docker after docker-compose stops
echo "Revoking X11 access for Docker..."
xhost -local:docker

