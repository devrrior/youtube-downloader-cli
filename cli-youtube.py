#!/usr/bin/env python3
import argparse
import ffmpeg
import os
from pytube import YouTube


class YoutubeDownload:
    DOWNLOAD_FOLDER = os.path.expanduser("~")+"/Downloads/"

    def __init__(self, url):
        self.__url = url

    # Functions

    def download_audio(self):
        try:
            url = YouTube(self.__url)
            title_video = YoutubeDownload.normalize_video_title(url.title)
            audio = url.streams.filter(only_audio=True, file_extension="mp4")
            audio[0].download(YoutubeDownload.DOWNLOAD_FOLDER)
            os.rename(YoutubeDownload.DOWNLOAD_FOLDER + title_video + r".mp4",
                      YoutubeDownload.DOWNLOAD_FOLDER + title_video + r".mp3")
            print("Successfuly download!")
            return 0
        except Exception as e:
            print(e)
            # print("Url invalid!. Type one url valid please.")
            return 1

    def download_video(self, quality):
        try:
            url = YouTube(self.__url)
        except Exception as e:
            print("Url invalid!. Type one url valid please.")
            return 1

        title_video = YoutubeDownload.normalize_video_title(url.title)
        print(title_video)
        quality = f"{quality}p"
        try:
            YoutubeDownload.download_video_and_audio(url, quality)
        except Exception as e:
            print("Invalid quality, the valid qualities are the following:")
            qualities_of_video = url.streams.filter(
                adaptive=True, file_extension="mp4", only_video=True)

            qualities = ""
            last_resolution = ""
            last_fps = 0
            for quality in qualities_of_video:

                if last_resolution == quality.resolution:
                    if last_fps == quality.fps:
                        pass
                    else:
                        qualities += f"{quality.resolution}    "
                        last_resolution = quality.resolution
                        last_fps = quality.fps
                else:
                    qualities += f"{quality.resolution}    "
                    last_resolution = quality.resolution
                    last_fps = quality.fps
            print(qualities)
            return 1

        YoutubeDownload.merge_video_and_audio(title_video)
        YoutubeDownload.delete_cache()
        print("Download successful!")

    @classmethod
    def normalize_video_title(cls, title):
        # Change /
        normalized_title = title.replace("/", ":")
        # Delete dot "."
        normalized_title = normalized_title.replace(".", "")

        return normalized_title

    @classmethod
    def download_video_and_audio(cls, url, quality):
        video = url.streams.filter(file_extension="mp4", res=quality).first()
        video.download(filename="video", output_path=".cache/")
        audio = url.streams.filter(
            only_audio=True, file_extension="mp4").first()
        audio.download(filename="audio", output_path=".cache/")

    @classmethod
    def merge_video_and_audio(cls, title_video):
        video = ffmpeg.input(f".cache/video.mp4")
        audio = ffmpeg.input(f".cache/audio.mp4")

        out = ffmpeg.output(
            video, audio, f"{YoutubeDownload.DOWNLOAD_FOLDER}{title_video}.mp4", vcodec="copy", acodec="aac", strict="experimental")
        out.run()

    @classmethod
    def delete_cache(cls):
        os.remove(".cache/video.mp4")
        os.remove(".cache/audio.mp4")


def cli():
    parser = argparse.ArgumentParser(
        prog="Youtube Downloader",
        description="Youtube Downloader will help you to download video or audio of videos from youtube"
    )
    parser.add_argument(
        "--audio", "-a",
        action="store_true",
        help="Download audio of url"
    )
    parser.add_argument(
        "--video", "-v",
        action="store_true",
        help="Download video of url"
    )
    parser.add_argument(
        "url",
        type=str,
        help="Url of video, you must type it beetween quotation marks"
    )
    parser.add_argument(
        "--quality", "-q",
        type=int,
        help="Quality of video")

    return parser.parse_args()


def main():
    args = cli()

    if args.video is False and args.audio is False:
        print("Select one option for to download (--audio or --video)")
        return 1

    if args.video and args.quality is None:
        print("Please type the quality")
        return 1

    if args.video and args.quality:
        video = YoutubeDownload((args.url).replace("'", ""))
        video.download_video(args.quality)

    if args.audio:
        audio = YoutubeDownload((args.url).replace("'", ""))
        audio.download_audio()


if __name__ == "__main__":
    main()