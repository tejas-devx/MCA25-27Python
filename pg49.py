# Remove comments from a file
inf = False
res = []

try:
    inf = open('outs.txt', 'r', encoding='UTF-8')
    lines = inf.readlines()

    for i in lines:
        if not i.strip().startswith('#'):
            res.append(i)

    print("\nLines without comment (#):")
    for line in res:
        print(line, end='')

except IOError as ie:
    print(ie)

finally:
    if inf:
        inf.close()
