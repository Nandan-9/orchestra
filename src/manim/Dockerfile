FROM python:3.10-slim

# Install dependencies for ffmpeg, Cairo, Pango, and LaTeX
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libcairo2 \
    libpango1.0-0 \
    pkg-config \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-fonts-extra \
    texlive-science \
    dvisvgm \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Manim
RUN pip install --no-cache-dir manim

# Create a non-root user
RUN adduser --disabled-password --gecos '' manimuser
USER manimuser

WORKDIR /app
ENTRYPOINT ["manim"]
