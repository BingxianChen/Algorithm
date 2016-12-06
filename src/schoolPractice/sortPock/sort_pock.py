# coding=utf8
puke = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', 'joker', 'JOKER']
while True:
    try:
        line = raw_input().split("-")
        A = line[0].split()
        B = line[1].split()
        if " ".join(A) == "joker JOKER" or " ".join(B) == "joker JOKER":
            print "joker JOKER"
            continue
        if len(A) == 4 and len(B) != 4:
            print " ".join(A)
            continue
        if len(B) == 7 and len(A) != 7:
            print " ".join(B)
            continue
        if len(A) != len(B):
            print "ERROR"
            continue
        if puke.index(A[0]) > puke.index(B[0]):
            print " ".join(A)
        else:
            print " ".join(B)
            continue

    except:
        break