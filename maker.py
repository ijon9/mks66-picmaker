import random

identifier = "P3"
rows = 500 #Number of rows
cols = 500
max = 255

out = "image.ppm"

def header(f):
    f.write(identifier + " ")
    f.write(str(rows) + " ")
    f.write(str(cols) + " ")
    f.write(str(max) + "\n")

def body(f):
    for i in range(0, rows):
        for i in range(0, cols):
            r = 255
            g = i*2 % max
            b = 0
            f.write(str(r) + " ")
            f.write(str(g) + " ")
            f.write(str(b) + "\t")
        f.write("\n")

def main():
    writeFile = open(out, 'w')
    header(writeFile)
    body(writeFile)
    writeFile.close()

main()
