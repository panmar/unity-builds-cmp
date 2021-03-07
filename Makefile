CPPFILES = $(wildcard src/*.cc)
OBJFILES = $(CPPFILES:.cc=.o)
OUT      = main

CC 	    = clang++
CCFLAGS = -pipe

$(OUT): $(OBJFILES)

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT)

