CC = icc
CFLAGS = -O3 -qopenmp -xHost
LDFLAGS = -lm

SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
INCLUDE_DIR = include

# List your source files (excluding speedtest.c)
SRCS = $(wildcard $(SRC_DIR)/*.c)
OBJS = $(patsubst $(SRC_DIR)/%.c, $(OBJ_DIR)/%.o, $(SRCS))

# Main program
SPEEDTEST_SRC = speedtest.c
SPEEDTEST_OBJ = $(OBJ_DIR)/speedtest.o
EXECUTABLE = $(BIN_DIR)/speedtest

# Targets
all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJS) $(SPEEDTEST_OBJ)
	$(CC) $(CFLAGS) $^ -o $@ $(LDFLAGS)

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c
	$(CC) $(CFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

$(SPEEDTEST_OBJ): $(SPEEDTEST_SRC)
	$(CC) $(CFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

clean:
	rm -f $(OBJ_DIR)/*.o
	rm -f $(EXECUTABLE)

.PHONY: all clean