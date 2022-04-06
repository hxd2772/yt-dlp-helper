from zipfile import ZipFile
import wget
import shutil
import os
ytdlpbin = "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe"
ffmpegzip = "https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
print("Downloading latest yt-dlp")
wget.download(ytdlpbin)
print("Downloaded yt-dlp")
print("Downloading latest ffmpeg build")
wget.download(ffmpegzip)
print("Downloaded ffmpeg")

file_name = "ffmpeg-master-latest-win64-gpl.zip"

with ZipFile(file_name, "r") as zip:

    print("Extracting ffmpeg")
    zip.extractall()
    print("ffmpeg extracted")


print("building folder")
os.mkdir("yt-dlp")
shutil.move("ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe", "yt-dlp/ffmpeg.exe")
shutil.move("ffmpeg-master-latest-win64-gpl/bin/ffprobe.exe", "yt-dlp/ffprobe.exe")
shutil.move("yt-dlp.exe", "yt-dlp/yt-dlp.exe")
os.remove("ffmpeg-master-latest-win64-gpl.zip")
shutil.rmtree(r"ffmpeg-master-latest-win64-gpl")
print("installation completed! Copy the generated yt-dlp folder to a location of choice then while you are in the yt-dlp folder enter cmd on the address bar to start the app")
os.system(pause)
