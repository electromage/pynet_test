#!/usr/bin/env python

outfile = open("new_file.txt", "w")
outfile.write("Some text for my file\n")
outfile.close()

with open("new_file.txt", "a") as myfile:
    myfile.write("some more text!\n")
