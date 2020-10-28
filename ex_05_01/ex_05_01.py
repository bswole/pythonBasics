# https://books.trinket.io/pfe/05-iterations.html
# exercise 5.1 - Iteration
num = 0
tot = 0.0
while True :
    sval = input('Enter a number ')
    if sval == 'done' :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval

# print('ALL DONE')
print(tot, num, tot/num)