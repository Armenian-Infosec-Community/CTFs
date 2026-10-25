# The Return of the Living Dead

rop in peace

NOTE: The binary ships with its own loader/libc where needed, the container runs it exactly as provided.
`flag.txt` here is a placeholder, the real flag is only inside the container.

The server is binded to your localhost port 1339, you can interact with the binary using `nc localhost 1339` or a custom script

## Build
```
docker build -t the-return-of-the-living-dead .
```

## Run
```
docker run -p 1339:1339 the-return-of-the-living-dead
```
