SP500['cumvol', column_header[1][1]] = SP500.iloc[:, 10].cumsum()
SP500["WMA Price", column_header[1][1]] = SP500.iloc[0:1, 1]
for i in range(1, len(SP500)):
    if SP500.iloc[i, 10] == 0:
        # take previous row value
        SP500.iloc[i, 74] = SP500.iloc[i - 1, 74]
    elif SP500.iloc[i, 10] > 0:
        # calculate new average
        SP500.iloc[i, 74] = ((SP500.iloc[i - 1, 73] * SP500.iloc[i - 1, 74]) + (
                    SP500.iloc[i, 10] * SP500.iloc[i, 1])) / (SP500.iloc[i, 73])
    elif (SP500.iloc[i, 74] < 0) & (SP500.iloc[i, 73] > 0):
        # take previous row value
        SP500.iloc[i, 74] = SP500.iloc[i - 1, 74]
    else:
        # vol < 0 and cumsum = 0
        SP500.iloc[i, 74] = 0


for n in range(1,10):
    n1 = 10
    n2 = 73
    n3 = 74
    SP500["WMA Price", column_header[n][1]] = SP500.iloc[0:1, n]
    for i in range(1,len(SP500)):
        if SP500.iloc[i, n1] == 0:
            # take previous row value
            SP500.iloc[i, n3] = SP500.iloc[i-1, n3]
        elif SP500.iloc[i, n1] > 0:
            # calculate new average
            SP500.iloc[i, n3] = ((SP500.iloc[i-1, n2]*SP500.iloc[i-1, n3]) + (SP500.iloc[i, n1]*SP500.iloc[i, 1])) / (SP500.iloc[i, n2])
        elif (SP500.iloc[i, n3] < 0) & (SP500.iloc[i, n2] > 0):
            # take previous row value
            SP500.iloc[i, n3] = SP500.iloc[i-1, n3]
        else:
            # vol < 0 and cumsum = 0
            SP500.iloc[i, n3] = 0
    n1 += 1
    n2 += 2
    n3 += 2