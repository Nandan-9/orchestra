FROM python:3.10-slim

RUN apt update && apt install -y ffmpeg libcairo2
RUN pip install manim

WORKDIR /app
ENTRYPOINT ["manim"]
