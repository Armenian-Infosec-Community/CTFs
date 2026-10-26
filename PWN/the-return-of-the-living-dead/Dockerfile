FROM debian:bookworm-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends socat \
 && rm -rf /var/lib/apt/lists/* \
 && useradd -M -s /usr/sbin/nologin gravedigger

WORKDIR /app

# chal's PT_INTERP is "./ld-linux-x86-64.so.2" and its RUNPATH is $ORIGIN,
# so it loads the bundled glibc 2.44 as long as it is started from /app.
COPY chal libc.so.6 ld-linux-x86-64.so.2 /app/
RUN echo -n "ZmxhZ3tyM3R1cm5fMGZfdGgzX2wxdjFuZ19kMzRkX2NoNDFuM2RfZnIwbV9zcDRyM19iMG4zc30K" | base64 -d > /app/flag.txt

# Everything owned by root; the unprivileged service can read/exec but not write.
RUN chown -R root:root /app \
 && chmod 555 /app/chal /app/ld-linux-x86-64.so.2 /app/libc.so.6 \
 && chmod 444 /app/flag.txt

USER gravedigger
EXPOSE 1339

# One fresh instance per connection, idle clients reaped after 60s, 5 minute cap per session
CMD ["socat", "-T60", "TCP-LISTEN:1339,reuseaddr,fork", "EXEC:timeout -k 10 300 /app/chal,stderr"]
