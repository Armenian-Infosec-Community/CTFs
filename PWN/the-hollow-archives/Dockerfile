FROM alpine:3.20

RUN apk add --no-cache socat \
 && adduser -D -H -s /sbin/nologin archivist

WORKDIR /app

# main is statically linked, so the image needs no libc/loader
COPY main the_dust_index.txt marginalia.txt overdue_ledger.txt /app/
RUN echo -n "ZmxhZ3thX2Nsb3NlZF9ib29rX3N0aWxsX2Fuc3dlcnNfdG9faXRzX2NhbGxfbnVtYmVyfQo=" | base64 -d > /app/flag.txt

# Everything owned by root; the unprivileged service can read but never write.
RUN chown -R root:root /app \
 && chmod 555 /app/main \
 && chmod 444 /app/the_dust_index.txt /app/marginalia.txt /app/overdue_ledger.txt /app/flag.txt

USER archivist
EXPOSE 1337

# One fresh binary per connection, idle clients reaped after 60s, 5 minute cap per session
CMD ["socat", "-T60", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:timeout -k 10 300 /app/main,stderr"]
