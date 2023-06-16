ROUTE = ./bin
FILE = main

run-dev:
	$(ROUTE)/$(FILE)

build: prepare
	sh build.sh

prepare:
	gcc $(ROUTE)/$(FILE).c -o $(ROUTE)/$(FILE)

clean:
	rm -rf build

start:
	./build/hello-world-x86_64.AppImage