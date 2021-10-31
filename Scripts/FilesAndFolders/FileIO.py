
f = open('inputFile.txt', 'r')
passFile = open('PassFile', 'w')
failFile = open('FailFile', 'w')
for line in f:
    splited = line.split()
    if splited[2] == 'P':
        print(line)
        passFile.write(line)
    else:
        failFile.write(line)

f.close()
passFile.close()
failFile.close()