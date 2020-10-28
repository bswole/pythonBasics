han = open('../ex_07_01/mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print('Line:',line)
    if line == '':
        # print('Skip Blank')
        continue
    wds = line.split()
    # print('Words:',wds)
    # Guardian
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])