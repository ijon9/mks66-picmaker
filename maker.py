import random

identifier = "P6"
rows = 500 #Number of rows
cols = 500
max = 255

out = "foo.ppm"

def header(f):
    writeFile = open(f, 'w')
    writeFile.write(identifier + " ")
    writeFile.write(rows + " ")
    writeFile.write(cols + " ")
    writeFile.write(max + "\n")

def body(f):
    writeFile = open(f, 'w')
    for i in range(0, rows):
        for i in range(0, cols):
            r = random.randint()
