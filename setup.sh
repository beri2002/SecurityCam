#!/bin/bash

# Update package manager
sudo apt update

# Install essential packages
sudo apt install -y python3-dev python3-pip

# Install OpenCV and contrib modules
pip3 install numpy opencv-python opencv-contrib-python

# Additional dependencies or setup steps can be added here as needed

echo "Setup complete."

