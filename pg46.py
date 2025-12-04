# Remove a line from a particular position in a file.
inf = False

try:
    n = int(input("Enter line number: "))
    inf = open('outs.txt', 'r+', encoding='UTF-8')

    lines = inf.readlines()
    lines.pop(n - 1)

    inf.truncate(0)
    inf.seek(0)
    inf.writelines(lines)

except IOError as ie:
    print(ie)

finally:
    if inf:
        inf.close()
