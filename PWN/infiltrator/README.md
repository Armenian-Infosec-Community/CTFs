# Infiltrator

NOTE: This binary might not behave the same depending on your system, the container is using debian
This should not affect the way you solve the challenge.

The server is binded to your localhost port 8000, you can interact with the binary using `nc localhost 8000` or a custom script

## Build
```
docker build -t infiltrator .
```

## Run
```
docker run -p 8000:8000 infiltrator
```

