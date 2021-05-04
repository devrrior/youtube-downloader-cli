# <img height="32" width="32" src="https://cdn.jsdelivr.net/npm/simple-icons@v4/icons/youtube.svg" /> Downtube CLI

If you wanna a terminal too for download video or audio from YouTube, this project will help you.

> _NOTE:_ _This script **only** works on unix systems_

## Installation

Install In One Command!

```
bash <(curl -s https://raw.githubusercontent.com/devrrior/youtube-downloader-cli/master/install)
```

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

  ```
  downtube -vq 720 'https://www.youtube.com/watch?v=PGJ43zaam_0'
  ```

  In this example we call the verbose `--video`, `--quality` and type the argument url in quotes. It's important mention that the verbose `--quality` is required if you will use the verbose `--video`.

- If you need to download some audio, you must type the following:</br>

  In this example we call the verbose `--video`, `--quality` and type the argument url in quotes. It's important mention that the verbose `--quality` is required if you will use the verbose `--video`.

  ```
  downtube -a 'https://www.youtube.com/watch?v=PGJ43zaam_0'
  ```

  In this example I call the verbose `--audio` and type the argument url in quotes.

## Uninstall

- For uninstall Downtube, just run this command:
  ```
  bash <(curl -s https://raw.githubusercontent.com/devrrior/youtube-downloader-cli/master/uninstall)
  ```

## TODO

- **Hide the log of ffmpeg.**
- **Make this script work on windows.**
