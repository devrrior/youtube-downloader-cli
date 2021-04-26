from pytube import YouTube
import ffmpeg
import os


class YoutubeDownload:
    DOWNLOAD_FOLDER = os.path.expanduser("~")+"/Downloads/"

    def __init__(self, url):
        self.__url = url

    # Functions

    def download_audio(self):
        try:
            url = YouTube(self.__url)
            audio = url.streams.filter(only_audio=True, file_extension="mp4")
            audio[0].download(YoutubeDownload.DOWNLOAD_FOLDER)
            os.rename(YoutubeDownload.DOWNLOAD_FOLDER + url.title + r'.mp4',
                      YoutubeDownload.DOWNLOAD_FOLDER + url.title + r'.mp3')
            print('Successfuly download!')
            return 0
        except Exception as e:
            print(e)
            # print('Url invalid!. Type one url valid please.')
            return 1

    def download_video(self, quality):
        try:
            url = YouTube(self.__url)
        except Exception as e:
            print('Url invalid!. Type one url valid please.')
            return 1

        name = (url.title).replace("/", "-")
        quality = f'{quality}p'
        try:
            YoutubeDownload.download_video_and_audio(url, quality)
        except Exception as e:
            print('Invalid quality, the valid qualities are the following:')
            qualities_of_video = url.streams.filter(
                adaptive=True, file_extension="mp4", only_video=True)

            qualities = ''
            last_resolution = ""
            last_fps = 0
            for quality in qualities_of_video:

                if last_resolution == quality.resolution:
                    if last_fps == quality.fps:
                        pass
                    else:
                        qualities += f'{quality.resolution}    '
                        last_resolution = quality.resolution
                        last_fps = quality.fps
                else:
                    qualities += f'{quality.resolution}    '
                    last_resolution = quality.resolution
                    last_fps = quality.fps
            print(qualities)
            return 1

        YoutubeDownload.merge_video_and_audio(name)
        YoutubeDownload.delete_cache()

    @classmethod
    def download_video_and_audio(cls, url, quality):
        video = url.streams.filter(file_extension="mp4", res=quality).first()
        video.download(filename="video", output_path=".cache/")
        audio = url.streams.filter(
            only_audio=True, file_extension="mp4").first()
        audio.download(filename="audio", output_path=".cache/")

    @classmethod
    def merge_video_and_audio(cls, name):
        video = ffmpeg.input(f".cache/video.mp4")
        audio = ffmpeg.input(f".cache/audio.mp4")

        out = ffmpeg.output(
            video, audio, f"{YoutubeDownload.DOWNLOAD_FOLDER}{name}.mp4", vcodec="copy", acodec="aac", strict="experimental")
        out.run()

    @classmethod
    def delete_cache(cls):
        os.remove(".cache/video.mp4")
        os.remove(".cache/audio.mp4")
