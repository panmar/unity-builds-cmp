CPPFILES = $(wildcard src/*.cc)
OBJFILES = $(CPPFILES:.cc=.o)
OUT      = main

CXX 	= clang++
CXXFLAGS = -pipe

$(OUT): $(OBJFILES)

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT)

