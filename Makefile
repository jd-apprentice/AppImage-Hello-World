## Description
## Use the name of the project as the name of the executable
## This because the unistall target will use the name of the executable
## With this I mean the `Exec` of your .desktop file

NAME = hello

build:
	cd usr && make build

build-dev:
	cd usr && make build-dev

run-dev:
	cd usr && make run-dev

clean:
	cd usr && make clean

start:
	cd usr && make start

uninstall:
	sudo rm -rf /usr/local/bin/$(NAME)