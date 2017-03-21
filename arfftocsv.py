def getCSVFromArff(fileNameArff):
    with open(fileNameArff + '.arff', 'r') as fin:
        data = fin.read().splitlines(True)

    i = 0
    cols = []
    for line in data:
        if ('@data' in line):
            i += 1
            break
        else:
            # print line
            i += 1
            if (line.startswith('@attribute')):
                if ('{' in line):
                    cols.append(line[11:line.index('{') - 1])
                elif('string' in line):
                    cols.append(line[11:line.index('string') - 1])
                else:
                    cols.append(line[11:line.index('numeric') - 1])

    headers = ",".join(cols)

    with open('newenglishcsv' + '.csv', 'w') as fout:
        fout.write(headers)
        fout.write('\n')
        fout.writelines(data[i:])
getCSVFromArff('/home/julie-ju/PycharmProjects/EmotionRecog/English')

