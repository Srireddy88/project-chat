#!/bin/bash

# Update system packages
sudo apt update

# Install system dependencies
sudo apt install python3-pip python3-venv python3-dev build-essential -y

# Set up the virtual environment
python3 -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Confirm installation
pip list
