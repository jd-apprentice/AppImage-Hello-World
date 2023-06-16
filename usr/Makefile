include config.mk

ROUTE = $(ROUTE)
FILE = $(NAME)

# For development purposes
run-dev:
	$(ROUTE)/$(FILE)

# You can do something like this if you need to compile a file
# Modify this to your needs
prepare:
	gcc $(ROUTE)/$(FILE).c -o $(ROUTE)/$(FILE)

# Clean the build folder
clean:
	rm -rf build

# Give permission to the AppImage
permission:
	chmod +x ./build/"$(FILE)"-x86_64.AppImage

# Run the actual AppImage
start: permission
	./build/"$(FILE)"-x86_64.AppImage

# Use this to compile and build the AppImage
compile_and_build: prepare
	sh build.sh

# Use this to only build the AppImage
build:
	sh build.sh