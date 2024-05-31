
A python GUI application built on top of Tkinter, FFmpeg <br>
_(Only for Educational purpose, don't use the code to download videos without permission from the owner, I don't take any responsibility of Your actions)_
## Introduction to FFmpeg

FFmpeg is a powerful multimedia framework that allows users to decode, encode, transcode, mux, demux, stream, filter, and play almost any type of audio and video files. It's a command-line tool with a vast array of capabilities, making it a popular choice for multimedia processing tasks.

## Features

- **Codec Support:** FFmpeg supports a wide range of audio and video codecs, including popular formats like H.264, AAC, MP3, and more.
- **Cross-Platform:** It's available on various operating systems, including Linux, Windows, and macOS.
- **Flexible:** Users can perform a multitude of tasks, such as converting between different formats, resizing videos, adding watermarks, extracting audio from video, and more.
- **Extensible:** FFmpeg offers a rich set of filters and effects that can be applied during transcoding or playback.
- **Speed:** It's optimized for performance and can efficiently handle large files and high-resolution content.

## Basic Usage

To use FFmpeg, simply invoke it from the command line followed by the desired options and arguments. Here's a basic example to convert a video file from one format to another:

```bash
ffmpeg -i input.mp4 output.avi
```

## Introduction to Pytube

Pytube is a lightweight, simple-to-use Python library aimed at downloading YouTube videos. It provides an intuitive interface to interact with YouTube's video streams, making it easy to fetch metadata, download videos, and manage various aspects of YouTube content.

## Features

- **YouTube Video Download:** Pytube enables users to download videos from YouTube effortlessly.
- **Stream Handling:** It allows users to access different video and audio streams associated with a YouTube video, providing flexibility in selecting the desired quality and format.
- **Metadata Retrieval:** Pytube can fetch metadata such as video title, description, uploader, view count, and more.
- **Pythonic API:** With a Pythonic API design, Pytube offers a straightforward and intuitive way to work with YouTube content programmatically.

## Working of Streams

In Pytube, streams represent individual pieces of multimedia content associated with a YouTube video. These streams come in various formats and qualities, including video streams (containing both video and audio) and separate audio streams.

### Basic Workflow

1. **Fetching Streams:** Pytube retrieves available streams for a given YouTube video URL.
2. **Stream Selection:** Users can choose the desired video and audio streams based on their preferred quality and format.
3. **Downloading:** Once the streams are selected, Pytube handles the download process, fetching the content and saving it to the local filesystem.

### Stream Formats and Qualities

Pytube provides access to streams with different combinations of video and audio codecs, resolutions, and bitrates. Users can select streams based on factors like video quality, file size, or compatibility with their playback devices.

## Example Usage

Here's a simple example demonstrating how to download a YouTube video using Pytube:

```python
from pytube import YouTube

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=your_video_id_here"

# Create a YouTube object
yt = YouTube(video_url)

# Access the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download(output_path="/path/to/save")
```

- to get this repo working on your machine you need to add FFmpeg on the env variable, after that install all the dependencies in a python environment like Tkinter and Pytube
- then run the application by "python youtube.py"
-  this will run our GUI application
![image](https://github.com/shreshth65968/Download-Youtube-Playlists-and-Videos-program/assets/96594936/c2ae29f6-d8ed-4296-aaf0-41ebfd84cbbf) 

- then go to the video you want to download, copy its link

![Screenshot (3)](https://github.com/shreshth65968/Download-Youtube-Playlists-and-Videos-program/assets/96594936/5472eec3-5f45-422d-84fd-28ab292e6e89)


- then paste the link and type the resolution of your choice like 360 in my case

![resolution setting](https://github.com/shreshth65968/Download-Youtube-Playlists-and-Videos-program/assets/96594936/76a0c326-1d57-45dd-893c-e205f6efb3c3)

- then click the download button, wait for a few seconds when download has finished  in

![downloaded](https://github.com/shreshth65968/Download-Youtube-Playlists-and-Videos-program/assets/96594936/4ba299b8-ce42-4b02-8939-8577cd33ae47)


- it will display the success dialog box and the video will get downloaded in the same directory you are running you program

![downloaded in the directory](https://github.com/shreshth65968/Download-Youtube-Playlists-and-Videos-program/assets/96594936/780bab5f-5908-496a-8a84-8e281aeb4340)

- same procedure to be followed to download the youtube playlist videos


