#Copy one file to another file.
inf = False
outf = False

try:
    inf = open("python.txt", "r")
    outf = open("outs.txt", "w")

    line = inf.readline()
    while line:
        outf.write(line)
        line = inf.readline()

    inf.close()
    outf.close()

    inf = False
    inf = open("outs.txt", "r")
    line = inf.read()
    print(line)

except IOError as io:
    print(io)

finally:
    if inf:
        inf.close()
    if outf:
        outf.close()
