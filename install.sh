#!/bin/sh

# Welcome
echo "Cloning files..."
echo "Cloning repository..."
git clone https://github.com/devrrior/youtube-downloader-cli/
echo "Installing required modules..."
pip install -r youtube-downloader-cli/requirements.txt
echo "Copy script..."
cp youtube-downloader-cli/downtube /usr/local/bin
echo "Delete files..."
rm -rf youtube-downloader-cli/
echo "That's done!"
