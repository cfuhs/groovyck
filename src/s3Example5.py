finished = False
while not finished:
    total = 0
    print('Please enter a number (end with 0):')
    s = input()
    num = int(s)
    if num != 0:
        total = total + num
        print('Total is ' + str(total))
    else:
        finished = True

