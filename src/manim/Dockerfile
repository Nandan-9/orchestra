FROM python:3.10-slim

RUN apt update && apt install -y ffmpeg libcairo2 && \
    pip install manim && \
    adduser --disabled-password --gecos '' manimuser

USER manimuser
WORKDIR /app

ENTRYPOINT ["manim"]
