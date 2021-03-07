import multiprocessing
import os
import shutil
import subprocess
import time


def generate_class_file(filepath, classname):
    with open(filepath, "w") as file:
        file.write(generate_class_file_content(classname))


def generate_class_file_content(classname):
    return (
        "#include <iostream>\n"
        "#include <string>\n"
        "class " + classname + " {\n"
        "public:\n"
        "    void func(const std::string& str) {\n"
        '        std::cout << "Hello from class '
        + classname
        + ': " + str << std::endl;\n'
        "    }\n"
        "};\n"
    )


def generate_unity_file(filepath, index_generator):
    with open(filepath, "w") as file:
        file.write(generate_unity_file_content(index_generator))


def generate_unity_file_content(index_generator):
    content = ""
    for index in index_generator:
        content += '#include "test{}.cc"\n'.format(str(index))

    content += "int main() {\n"

    for index in index_generator:
        content += "{ MyTestClazz" + str(index) + ' var; var.func("testing"); }\n'
    content += "}\n"
    return content


def main():
    src_dir = "src/"
    num_files = 10_000

    try:
        shutil.rmtree(src_dir)
        os.mkdir(src_dir)
    except FileNotFoundError:
        os.mkdir(src_dir)
    else:
        print("Cleaning {} directory".format(src_dir))

    print("Generating {} files...".format(num_files))

    for i in range(0, num_files):
        filepath = "src/test{}.cc".format(i)
        classname = "MyTestClazz{}".format(i)
        generate_class_file(filepath, classname)

    generate_unity_file("src/unity.cc", range(0, num_files))

    print("Compiling unity build... [g++]")

    start = time.time()
    subprocess.run(
        "g++ -pipe src/unity.cc -o unity_gcc".split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    end = time.time()
    print("\tDONE. The process took {:.2f} seconds".format(end - start))

    print("Compiling unity build using... [clang++]")
    start = time.time()
    subprocess.run(
        "clang++ -pipe src/unity.cc -o unity_clang".split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    end = time.time()
    print("\tDONE. The process took {:.2f} seconds".format(end - start))

    num_cores = multiprocessing.cpu_count()
    print("Compiling normal build using {} cores... [clang++]".format(num_cores))

    start = time.time()
    subprocess.run(
        "make -j{}".format(num_cores).split(),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT,
    )
    end = time.time()
    print("\tDONE. The process took {:.2f} seconds".format(end - start))


if __name__ == "__main__":
    main()
