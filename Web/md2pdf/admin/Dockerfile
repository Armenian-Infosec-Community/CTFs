FROM debian:bullseye

WORKDIR /app
COPY . /app

# Install system dependencies for WeasyPrint
RUN apt-get update \
    && apt-get install -y python3 python3-pip curl \
    && apt-get clean

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
