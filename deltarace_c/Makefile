# --- LINUX BUILD INSTRUCTIONS START --- #
# uncomment if you want to compile for linux
# only tested on arch
#build:
#	gcc device.c -o deltarace -lraylib -lGL -lm -lpthread -ldl -lrt -lX11
# --- LINUX BUILD INSTRUCTIONS END --- #

# --- WINDOWS BUILD INSTRUCTIONS START --- #
# uncomment if you want to crosscompile from linux to windows
# only tested on arch, but the build results have been tested on windows
# you need two additional dlls for this to boot, you can find them in usr/x86_64-w64-mingw32/bin (arch)
build:
	x86_64-w64-mingw32-gcc device.c -o deltarace -lmingw32 -lraylib
# --- WINDOWS BUILD INSTRUCTIONS END --- #