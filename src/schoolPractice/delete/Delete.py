# coding=utf8
while True:
    try:
        n = input()
        lst = range(n)
        cnt = 0
        while len(lst)>1:
            ln = len(lst)
            cnt = (cnt + 2)%ln
            lst.remove(lst[cnt])
        print lst[0]

    except:
        break

