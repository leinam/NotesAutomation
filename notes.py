import os
import sys

# recognized file format extensions for appending to file names
python = ".py"
text = ".txt"
java = ".java"

# dictionary of recognized file formats
extensions = {
    "python": python,
    ".py": python,
    "text": text,
    "java": java
    }


def create():
    #  print(sys.argv)

    #  get arguments from command line
    try:
        filename = str(sys.argv[1])
    except Exception:
        print("You must name your file. Try again")
        sys.exit()

    try:
        ext_input = str(sys.argv[2])
    except Exception:
        ext_input = text

    try:
        folder_name = str(sys.argv[3])
    except Exception:
        folder_name = "General"

    # map extension argument to correct . extension in stored dict
    ext = extensions.get(ext_input)

    # check folder
    if os.path.isdir("./Notes/{}".format(folder_name)):
        os.chdir("./Notes/{}".format(folder_name))

    else:
        os.mkdir("./Notes/{}".format(folder_name))
        os.chdir("./Notes/{}".format(folder_name))

    # check extension validity
    if extensions.get(ext_input):
        filename = filename+ext
    else:
        ext = text
        filename = filename+ext
        print("Unrecognized format '{}'. ".format(ext_input))

    # check file existence
    if not os.path.isfile("./Notes/{}".format(filename)):  # correct this condition (extensions)
        open(filename, "w+")
        print("Creating '{}' file.. in folder '{}'".format(ext, os.getcwd()))
    else:
        print("A file with that name already exists please choose another name and try again :D")

    # open file with default editor
    os.system("open -e " + filename)


if __name__ == "__main__":
    create()
