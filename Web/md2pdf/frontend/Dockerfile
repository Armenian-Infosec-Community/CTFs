FROM debian:buster

WORKDIR /app
COPY . /app

# Install system dependencies for WeasyPrint
RUN echo "deb http://archive.debian.org/debian buster main contrib non-free" > /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until \
    && apt-get update \
    && apt-get install -y python3 python3-pip curl wget \
    && apt-get clean

RUN pip3 install -r requirements.txt

RUN apt-get install -y xfonts-75dpi fontconfig libjpeg62-turbo libx11-6 libxcb1 libxext6 libxrender1 xfonts-base \
    && wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.buster_amd64.deb -O wkhtmltopdf.deb \
    && dpkg -i wkhtmltopdf.deb \
    && rm wkhtmltopdf.deb

CMD ["python3", "app.py"]
