output = []
def LCS(S1, S2):
    m = len(S1)
    n = len(S2)
    c = [[0 for x in range(n + 1)] for x in range(m + 1)]
    b = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3

    return c, b

def printLCS(b,S1,m,n):
    i = m
    j = n
    if i == 0 or j == 0:
        return
    if b[i][j] == 1:
        printLCS(b,S1,i-1,j-1)
        output.append(S1[i-1])
    elif b[i][j] == 2:
        printLCS(b, S1, i - 1, j)
    else:
        printLCS(b, S1, i, j - 1)

if __name__ == '__main__':
    strlen1 = 0
    strlen2 = 0
    str1 = []
    str2 = []
    while True:
        while True:
            try:
                strlen1, strlen2 = input("Input the length of string1 and string2 : ").split()
            except:
                print("Error Input!")
                continue

            if strlen1 == "0" and strlen2 == "0" :
                quit()
            try:
                if (int(strlen1) < 1 or int(strlen2) < 1) :
                    print("length must larger than 1!")
                    continue
                elif (int(strlen1) > 100 or int(strlen2) > 100) :
                    print("length must smaller than 100!")
                    continue
                else:
                    break
            except:
                print("Error Input!")
                continue


        while True:
            k = 0
            str1 = []
            temp =[i for i in input("Input subsequence1: ").split(' ')]
            if len(temp) != int(strlen1) :
                print("Error Input!")
                continue
            else:
                while k != int(strlen1):
                    if temp[k].isalpha() and len(temp[k]) == 1 :
                        str1.append(temp[k])
                        k = k + 1
                    else :
                        print("Error Input!")
                        break

                if k == int(strlen1):
                    break
        S1 = "".join(str1)
        while True:
            k = 0
            str2 = []
            temp =[i for i in input("Input subsequence2: ").split(' ')]
            if len(temp) != int(strlen2) :
                print("Error Input!")
                continue
            else:
                while k != int(strlen2):
                    if temp[k].isalpha() and len(temp[k]) == 1 :
                        str2.append(temp[k])
                        k = k + 1
                    else :
                        print("Error Input!")
                        break

                if k == int(strlen2):
                    break

        S2 = "".join(str2)
        # print(S1)
        # print(S2)
        # os.system("pause")
        #======================================
        c, b = LCS(S1,S2)
        printLCS(b, S1, len(S1), len(S2))
        ll = len(output)
        print("Length of LCS = " + str(ll))
        if ll == 0:
            print("LCS = ")
        else:
            print("LCS = " + "".join(output))

        output = []