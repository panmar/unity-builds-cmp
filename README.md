# unity-builds-cmp

A simple python script comparing C++ compilation speed of unity builds vs normal builds.

## Requirements
- python3
- g++
- clang++
- make

## Example output
```
➜  unity-builds-cmp git:(main) ✗ python test_unity_build.py
Cleaning src/ directory
Generating 10000 files...
Compiling unity build... [g++]
	DONE. The process took 28.57 seconds
Compiling unity build using... [clang++]
	DONE. The process took 16.65 seconds
Compiling normal build using 8 cores... [clang++]
	DONE. The process took 673.51 seconds
```
