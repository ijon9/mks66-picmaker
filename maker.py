import random

identifier = "P6"
rows = 500 #Number of rows
cols = 500
max = 255

out = "foo.ppm"

def header(f):
    writeFile.write(identifier + " ")
    writeFile.write(str(rows) + " ")
    writeFile.write(str(cols) + " ")
    writeFile.write(str(max) + "\n")

def body(f):
    for i in range(0, rows):
        for i in range(0, cols):
            r = random.randint(0, max)
            g = random.randint(0, max)
            b = random.randint(0, max)
            writeFile.write(str(r) + " ")
            writeFile.write(str(g) + " ")
            writeFile.write(str(b) + "\t")
        writeFile.write("\n")

def main():
    writeFile = open(f, 'w')
    header(out)
    body(out)
    writeFile.close()
