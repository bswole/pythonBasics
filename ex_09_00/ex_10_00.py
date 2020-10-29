# https://www.youtube.com/watch?v=PrhZ9qwBDD8&ab_channel=freeCodeCampConcepts
print('Exercise 10.0')

fname = input('Enter File: ')
if len(fname) < 1:
    fname = 'clown.txt'
    print('Using clown.txt')
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w, 0) + 1

# print(di)

tmp = list()
for k,v in di.items():
    newt = (v, k)
    tmp.append(newt)

# print('Flipped:', tmp)
tmp = sorted(tmp, reverse=True)
# print('Sorted:', tmp[:5])

# pretty print
for v,k in tmp[:5]:
    print(k,v)