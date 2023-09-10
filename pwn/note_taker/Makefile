CC=arm-linux-gnueabi-gcc
CC=aarch64-linux-gnu-gcc

all:
	${CC} note_keeper.c -o note_keeper_arm

host: all
	docker build .
	./host.sh

clean:
	rm note_keeper_arm