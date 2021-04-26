# <img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v4/icons/youtube.svg" /> YouTube Downloader CLI

If you wanna a terminal too for download video or audio from YouTube, this project will help you.

> _NOTE:_ _This script **only** works on unix systems_

## Installation

Follow the next steps:

1.  Git clone this repository: `git clone https://github.com/devrrior/youtube-downloader-cli.git`
1.  Install the requirements: `pip install -r requirements.txt`
1.  That's done!

> **NOTE**: If your downloads folder **isn't called Downloads**, just edit the file **youtube.py** and in the variable **DOWNLOAD_FOLDER**, change **Downloads** to the name of your folder.

## Usage

### Arguments

- `url`: This argument is required, you must type the link of the video in quotes.

### Optional arguments

- `--help -h`: This verbose will return information about CLI.
- `--video -v`: This verbose will help you to download any video, but you also need `--quality`.
- `--audio -a`: Type this option if you wanna download one audio.
- `--quality -q`: In this argument you should type the quality that need you.

## Examples

- If you need to download some video, you must type the following:</br>
  <img width="632" alt="image" src="https://user-images.githubusercontent.com/69869135/116021195-583b5080-a60d-11eb-9d05-b4a45b24f95d.png"></br>
  In this example we call the verbose `--video`, `--quality` and type the argument url in quotes. It's important mention that the verbose `--quality` is required if you will use the verbose `--video`.

- If you need to download some audio, you must type the following:</br>
  <img width="577" alt="image" src="https://user-images.githubusercontent.com/69869135/116021713-5625c180-a60e-11eb-8f51-6a97944654f8.png"></br>
  In this example I call the verbose `--audio` and type the argument url in quotes.

## TODO

- **Make a script for integrate this script in the bash.**
- **Hide the log of ffmpeg.**
- **Make this script work on windows.**
