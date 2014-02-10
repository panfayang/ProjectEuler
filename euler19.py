def count(n):
    a = 6
    count = 0
    for i in range(1901,n+1):
        #dec to jan
        a += 3
        if a%7 ==0:
            count += 1
        # jan to feb
        a+= 3
        if a%7 ==0:
            count += 1
        #feb to mar
        if i%4 ==0 and i%400 !=0:
            a +=1
            if a%7 ==0:
                count += 1
        else:
            if a%7 ==0:
                count += 1
        # mar to apr
        a+= 3
        if a%7 ==0:
            count += 1
        #apr to may
        a+= 2
        if a%7 ==0:
            count += 1
        #may to june
        a += 3
        if a%7 ==0:
            count += 1
        #june to jul
        a += 2
        if a%7 ==0:
            count += 1
        #jul to aug
        a += 3
        if a%7 ==0:
            count += 1
        #aug to sep
        a += 3
        if a%7 ==0:
            count += 1
        #sep to oct
        a += 2
        if a%7 ==0:
            count += 1
        #oct to nov
        a += 3
        if a%7 ==0:
            count += 1
        #nov to dec
        a += 2
        if a%7 ==0:
            count += 1

    return count

print count(2000)
