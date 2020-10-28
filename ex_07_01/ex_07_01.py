# https://www.youtube.com/watch?v=il1j4wkte2E&ab_channel=freeCodeCampConcepts
print('Exercise 7.1')

fh = open('mbox-short.txt')
print(fh)

for line in fh:
    ly = line.rstrip()
    print(ly.upper())