FROM debian:bookworm-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends socat \
 && rm -rf /var/lib/apt/lists/* \
 && useradd -M -s /usr/sbin/nologin caller

WORKDIR /app

# main's PT_INTERP is "./ld-linux-x86-64.so.2" and its RUNPATH is $ORIGIN,
# so it loads the bundled glibc 2.44 as long as it is started from /app.
COPY main libc.so.6 ld-linux-x86-64.so.2 /app/
RUN echo -n "ZmxhZ3t0NGxrMW5nX3QwX2doMHN0c18wbmVfZjBybWF0X3N0cjFuZ19hdF9hX3QxbWV9Cg==" | base64 -d > /app/flag.txt

# Everything owned by root; the unprivileged service can read/exec but not write.
RUN chown -R root:root /app \
 && chmod 555 /app/main /app/ld-linux-x86-64.so.2 /app/libc.so.6 \
 && chmod 444 /app/flag.txt

USER caller
EXPOSE 1338

# One fresh instance per connection, idle clients reaped after 60s, 5 minute cap per session
CMD ["socat", "-T60", "TCP-LISTEN:1338,reuseaddr,fork", "EXEC:timeout -k 10 300 /app/main,stderr"]
