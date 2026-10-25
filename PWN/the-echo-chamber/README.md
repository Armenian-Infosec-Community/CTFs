# The Echo Chamber

There is a chamber carved into the bedrock below the old chapel, sealed since long before anyone living can remember. Those who pressed an ear to the stone swore they heard their own voice drifting back up — thinned, delayed, and wrong, as though something below had learned to wear it.

On the last night of October the seal thins, and the chamber will answer any who call into it. But whatever waits down there is old and patient and hungry, and it grants only three replies before the dark folds shut for another year.

NOTE: The binary ships with its own loader/libc where needed, the container runs it exactly as provided.
`flag.txt` here is a placeholder, the real flag is only inside the container.

The server is binded to your localhost port 1338, you can interact with the binary using `nc localhost 1338` or a custom script

## Build
```
docker build -t the-echo-chamber .
```

## Run
```
docker run -p 1338:1338 the-echo-chamber
```
