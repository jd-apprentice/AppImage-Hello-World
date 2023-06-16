# AppImage Hello-World - Example #1 📔

This branch is the same as the master branch, but different types of files are used to build the AppImage.

## Requirements 🔨

- curl
- git
- make
- python3

## Clone the repo 📥

```bash
git clone -b example-1 git@github.com:jd-apprentice/AppImage-Hello-World.git
cd AppImage-Hello-World
```

## Build the AppImage 📦

```bash
make build
```

## Run the AppImage 🚀

```bash
make start
```

### Build your own AppImage ⭐

1. Now if you want to modify the AppImage, start working inside the `src` folder.
2. Then when you are finished go back to `Build the AppImage` section.

#### Notes

- Complete the `config.mk` file with your own information.
- When providing an icon, make sure its in the same folder.
- Your `AppRun` should be modified to your needs for example here we are running a python script, instead if we were running a nodejs script we would have to change the `AppRun` file to something like this:

```bash
#!/bin/bash

cd "$(dirname "$0")"
node ./main.js
```

- Becareful about `config.mk` to not leave spaces between the `=` sign or at the end of the line.