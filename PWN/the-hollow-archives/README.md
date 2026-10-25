# The Hollow Archives

The Hollow Archives have a peculiar way of keeping things in order. Shelves are emptied, desks are cleared, and yet certain entries never quite disappear. Somewhere in the records, an old mistake has become part of the routine.

Books can be borrowed, read, and returned. The usual rules apply, and some doors remain firmly shut. Still, not everything in the archives is accounted for in the way it should be.

Look closely at what remains after the work is done. The answer may be hiding in a place no one thinks to check.

NOTE: The binary is statically linked, the container runs it exactly as provided.
`flag.txt` here is a placeholder, the real flag is only inside the container.

The server is binded to your localhost port 1337, you can interact with the binary using `nc localhost 1337` or a custom script

## Build
```
docker build -t the-hollow-archives .
```

## Run
```
docker run -p 1337:1337 the-hollow-archives
```
