#create a rhombus with n determining the length of the sides#

def diamonds(n):
    newnum = n
    j = 0
    if newnum == 1:
        print(1)
    else:
        print((newnum - 1)*" "+str(1))
        for i in range(2, newnum+1):
            print(((newnum - 2)*" ")+str(i)+(2 * i - 3)*" "+str(i))
            newnum -= 1
    if n == 1:
        print(1)
    else:
        for i in range(n, 1,-1):
            print(j*" "+str(i)+(2 * i - 3)*" "+str(i))
            j += 1
        print((n - 1)*" "+str(1))
    return
