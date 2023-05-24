#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    size = len(argv)
    if size == 1:
        print("{} arguments.".format(size - 1))
    elif size == 2:
        print("{} argument:".format(size - 1))
    elif size > 2:
        print("{} arguments:".format(size - 1))
    for count in range(1, size):
        print("{}: {}".format(count, argv[count]))
