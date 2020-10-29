# https://www.youtube.com/watch?v=PrhZ9qwBDD8&ab_channel=freeCodeCampConcepts
print('Exercise 9.0')

fname = input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)

    for w in wds:
        # if the key is not there, the count is zero
        # oldcount = di.get(w, 0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount
        # print(w, 'new', newcount)

        # here is a more efficient idiom of the above code
        # (retrieve/create/update counter)
        di[w] = di.get(w, 0) + 1
        print(w, 'new', di[w])

print(di)

# now we want to find the most common word (max dict loop)
largest = -1
for k,v in di.items():
    print(k, v)
    if v > largest:
        largest = v
        theword = k

print('Done: ', theword, largest)
