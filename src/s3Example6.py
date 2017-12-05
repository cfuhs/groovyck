m = 0
finished = False
while not finished:
    print('Enter another whole number (0 to finish): ', end = '')
    s = input()
    num = int(s)    
    if num != 0:
        if num > m:
            m = num
    else:
        finished = True
print(str(m))
