import random

identifier = "P6"
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
            r = random.randint(0, max)
            g = random.randint(0, max)
            b = random.randint(0, max)
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
