file = open("unboundPrimes.txt", "x")
file.write("\n")
unbindList = []
for j in range (2, 10000):
    jtemp = j
    unbindList=[]
    for i in range(2,j+1):
     while jtemp % i == 0:
            jtemp = jtemp/i
            unbindList.append(i)
    # print(f"{j} unbinds into {unbindList}")
    stringtoprint = ""
    if len(unbindList)>1:
        for i in range(0, len(unbindList)):
            stringtoprint = stringtoprint + str(unbindList[i])
            if (i != len(unbindList)-1):
                stringtoprint = stringtoprint + "x"
    else:
        stringtoprint = str(unbindList[0]) + " --> PRIME"
    stringtoprint = stringtoprint + "\n"

    file.write(stringtoprint)





    



