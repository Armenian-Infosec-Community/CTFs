# 🏴 Armenian Infosec Community CTFs

A collection of Capture The Flag challenges built by members of the **Armenian Infosec Community**.
Pick a category, spin up a challenge locally, break it, and grab the flag.

> Every challenge runs on your own machine. There is no shared server to attack, so please don't go looking for one.

---

## 📚 Challenges

### 💥 PWN (binary exploitation)

| Challenge | Difficulty | Contributor |
|---|---|---|
| [The Hollow Archives](PWN/the-hollow-archives) | 🟢 Easy | [@s0g3king](https://github.com/s0g3king) |
| [The Return of the Living Dead](PWN/the-return-of-the-living-dead) | 🟡 Medium | [@s0g3king](https://github.com/s0g3king) |
| [The Echo Chamber](PWN/the-echo-chamber) | 🟡 Medium | [@s0g3king](https://github.com/s0g3king) |
| [Infiltrator](PWN/infiltrator) | 🟡 Medium | [@s0g3king](https://github.com/s0g3king) |

### 🔍 Reverse (reverse engineering)

| Challenge | Difficulty | Contributor |
|---|---|---|
| [boundaries](Reverse/boundaries) | 🟢 Easy | [@s0g3king](https://github.com/s0g3king) |
| [Wait For It](Reverse/wait-for-it) | 🟡 Medium | [@s0g3king](https://github.com/s0g3king) |
| [perf3cti0nist](Reverse/perf3cti0nist) | 🟡 Medium | [@var77](https://github.com/var77) |
| [Firmware Jumpscare](Reverse/firmware-jumpscare) | 🔴 Hard | [@s0g3king](https://github.com/s0g3king) |

### 🌐 Web

| Challenge | Difficulty | Contributor |
|---|---|---|
| [ImgShare](Web/ImgShare) | 🟢 Easy | [@p055e55eD](https://github.com/p055e55eD) |
| [web_lab_101](Web/web_lab_101) | 🟡 Medium | [@Sevada797](https://github.com/Sevada797) |
| [MD2PDF](Web/md2pdf) | ⚪ Undefined | [@sud0usr](https://github.com/sud0usr) |

### 🕵️ OSINT

| Challenge | Difficulty | Contributor |
|---|---|---|
| [Geocache Gone Digital](OSINT/Geocache%20Gone%20Digital) | 🔴 Hard | [@p055e55eD](https://github.com/p055e55eD) |
| [Leaf No Trace](OSINT/Leaf%20No%20Trace) | 🟣 Insane | [@p055e55eD](https://github.com/p055e55eD) |

### 🖼️ Stegano

| Challenge | Difficulty | Contributor |
|---|---|---|
| [1](Stegano/1) | 🟢 Easy | [@PizzaPablo666](https://github.com/PizzaPablo666) |

---

## 🚀 How to play

Each challenge has its own requirements and its own build and start process.
Open the folder of the challenge you want to solve and follow its `README.md`.

---

## 🏁 Flags

- Flag formats differ between challenges (`flag{...}`, `FLAG{...}`, `infosec{...}`). Each challenge's README says which one it uses.
- `flag.txt` files in this repo are **placeholders** (`flag{fake_flag}`). The real flag is set inside the running container.
- The real flags can be found in some of the challenge files. You're solving these for yourself, so whether you look at them is up to you.

## 🤝 Rules of play

- Only attack challenges running on **your own machine**.
- Stuck? Ask for a hint in the community instead of asking for the answer.

---

## ✍️ Contributing a challenge

New challenges are welcome. Just open a pull request.

### Folder layout

```
<Category>/<challenge-name>/
├── README.md        # story, notes, build & run steps, flag format
├── Dockerfile       # or docker-compose.yml, if the challenge is a service
├── flag.txt         # placeholder only, e.g. flag{fake_flag}
└── <challenge files>
```

- **Categories:** `PWN`, `Reverse`, `Web`, `OSINT`, `Stegano` (propose a new one in your PR if needed).
- **Names:** no naming convention yet, so name the folder however you like.
- **One challenge per PR**, with a commit like `feat: new PWN challenge (The Echo Chamber)`.

### Challenge README template

````markdown
# Challenge Name

Short story / description shown to players.

## Notes
Anything players need to know (bundled libc, files provided, warnings).

## Flag Format
`flag{...}`

## Build
```
docker build -t challenge-name .
```

## Run
```
docker run --rm -p <port>:<port> challenge-name
```
````

### Checklist for services

- Run as a **non-root** user; make challenge files read-only.
- If the binary needs a specific glibc, ship the matching `libc.so.6` and `ld-linux-x86-64.so.2`.

---

## 👥 Contributors

Thanks to everyone who has built challenges here:
[@PizzaPablo666](https://github.com/PizzaPablo666) ·
[@s0g3king](https://github.com/s0g3king) ·
[@p055e55eD](https://github.com/p055e55eD) ·
[@Sevada797](https://github.com/Sevada797) ·
[@var77](https://github.com/var77) ·
[@sud0usr](https://github.com/sud0usr)

Happy hacking! 🎃
