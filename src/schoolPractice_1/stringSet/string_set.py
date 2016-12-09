while True:
    try:
        line = raw_input()
        charset = []
        s = ""
        for i in line:
            if i not in charset:
                charset.append(i)
        for i in charset:
            s += i
        print s
    except:
        break