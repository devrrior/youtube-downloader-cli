#!/usr/bin/env python
from youtube import YoutubeDownload
import argparse


def cli():
    parser = argparse.ArgumentParser(
        prog='Youtube Downloader',
        description='Youtube Downloader will help you to download video or audio of videos from youtube'
    )
    parser.add_argument(
        '--audio', '-a',
        action='store_true',
        help='Download audio of url'
    )
    parser.add_argument(
        '--video', '-v',
        action='store_true',
        help='Download video of url'
    )
    parser.add_argument(
        'url',
        type=str,
        help='Url of video, you must type it beetween quotation marks'
    )
    parser.add_argument(
        '--quality', '-q',
        type=int,
        help='Quality of video')

    return parser.parse_args()


def main():
    args = cli()

    # print(args)
    if args.video is False and args.audio is False:
        print('Select one option for to download (--audio or --video)')
        return 1

    if args.video and args.quality is None:
        print('Please type the quality')
        return 1

    if args.audio:
        audio = YoutubeDownload((args.url).replace("'", ""))
        audio.download_audio()

    if args.video and args.quality:
        video = YoutubeDownload((args.url).replace("'", ""))
        video.download_video(args.quality)


if __name__ == "__main__":
    main()
