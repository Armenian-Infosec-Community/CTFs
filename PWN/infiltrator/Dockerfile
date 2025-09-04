FROM debian:stable-slim

RUN groupadd -r app && useradd -r -g app app

WORKDIR /app

COPY server /app/server
RUN touch /app/users.txt
RUN echo -n "RkxBR3tiMW40cmkzc183eXAzXzVoMX0K" | base64 -d > /app/flag.txt

RUN chown -R app:app /app && chmod -R 755 /app
USER app

EXPOSE 8000

ENTRYPOINT ["/app/server"]

