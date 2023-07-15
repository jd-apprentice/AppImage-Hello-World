###############
# Inside the `usr` folder is another Makefile with detailed instructions about what does each command
# This is just a wrapper to make it easier to use
###############

include config.mk

build: clean copy desktop
	cd usr && make build

prepare:
	cd usr && make prepare

run-dev:
	cd usr && make run-dev

clean:
	cd usr && make clean

copy:
	cp config.mk usr/config.mk

uninstall:
	sudo rm -rf /usr/local/bin/"$(NAME)"

start: copy
	cd usr && make start

desktop:
	echo "[Desktop Entry]\nName=$(NAME)\nIcon=$(ICON)\nType=Application\nCategories=$(CATEGORY)\nTerminal=true\nX-AppImage-Version=$(VERSION)" > ./usr/$(DESKTOP)

gui:
	python3 gui.py || python gui.py