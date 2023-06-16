# AppImage Hello-World 🌍

This is a simple example of how to create an AppImage. It is based on this [REPO](https://github.com/ClonedRepos/hello-world-appimage)

## Requirements 🔨

- curl
- git
- make

## Clone the repo 📥

```bash
git clone git@github.com:jd-apprentice/AppImage-Hello-World.git
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

## Available commands 📜

```makefile
## Run the AppImage
start:
	cd usr && make start

## Build the AppImage from the compiled C code
build:
	cd usr && make build

## Compile the C code for development purposes
prepare:
	cd usr && make prepare

## Run the C code for development purposes
run-dev:
	cd usr && make run-dev

## Clean the build files in the usr directory
clean:
	cd usr && make clean

## Remove the executable from the system
uninstall:
	sudo rm -rf /usr/local/bin/$(NAME)
```
