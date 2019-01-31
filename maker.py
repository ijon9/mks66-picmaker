import random

identifier = "P3"
rows = 500 #Number of rows
cols = 500
max = 255

out = "foo.ppm"

def header(f):
    f.write(identifier + " ")
    f.write(str(rows) + " ")
    f.write(str(cols) + " ")
    f.write(str(max) + "\n")

def body(f):
    for i in range(0, rows):
        for i in range(0, cols):
            r = 255#random.randint(0, max)
            g = 0#random.randint(0, max)
            b = 0#random.randint(0, max)
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
