FROM borda/docker_python-opencv-ffmpeg:cpu-py3.9-cv4.8.0
COPY requirements.txt ./

ENV OPENCV_VIDEOIO_DEBUG=1
ENV OPENCV_FFMPEG_DEBUG=1
ENV OPENCV_LOG_LEVEL=DEBUG
ENV OPENCV_FFMPEG_LOGLEVEL=48

RUN apt-get update
RUN apt-get install ssh -y
RUN apt-get install libgl1 ffmpeg yasm libvpx. libx264. -y
RUN apt-get install build-essential libgtk2.0-dev libgtk-3-dev libavcodec-dev libavformat-dev libjpeg-dev libswscale-dev libtiff5-dev -y


RUN pip install --no-cache-dir -r requirements.txt

# RUN apt-get update
# RUN apt-get install libgl1 ffmpeg libsm6 libxext6 -y
# RUN ffmpeg -decoders 2>/dev/null | grep h264_cuvid

# RUN ffmpeg -codecs | grep h264