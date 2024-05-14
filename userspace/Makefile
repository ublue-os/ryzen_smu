CC = gcc
STRIP = strip

CFLAGS = -O3
LDFLAGS = -lm

SFLAGS = --strip-all

PATHS = -I"../lib"

OUT = monitor_cpu

SRC = monitor_cpu.c
SRC += "../lib/libsmu.c"

all: monitor_cpu.c ../lib/libsmu.c
	$(CC) $(PATHS) $(CFLAGS) $(LDFLAGS) -o $(OUT) $(SRC)
	$(STRIP) $(SFLAGS) $(OUT)
