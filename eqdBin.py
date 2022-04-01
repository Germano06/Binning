bins = {}
dataList = list(input("Enter the data: ").split())
s = int(input("Enter the depth of the bin: "))
l = len(dataList)


def bin_mean():
    print("\nAfter smoothing by bin mean:")
    binsM = {}
    for bin in bins:
        m = 0
        lis = []
        for i in bins[bin]:
            m += int(i)

        m = int(m/s)
        for i in range(s):
            lis.append(m)

        binsM[bin] = lis
        print(bin, " : ", binsM[bin])


def binMid():
    print("\nAfter smoothing by bin midean:")
    binsMid = {}
    m = int(s/2)
    for bin in bins:
        lis = []
        a = bins[bin]
        if s % 2:
            x = a[m]
        else:
            x = int((int(a[m])+int(a[m-1]))/2)

        for i in range(s):
            lis.append(x)

        binsMid[bin] = lis
        print(bin, " : ", binsMid[bin])


def binBound():
    print("\nAfter smoothing by bin boundary:")
    binB = {}
    for bin in bins:
        lis = []
        for i in range(s):
            a = int(bins[bin][0])
            z = int(bins[bin][-1])
            m = int(bins[bin][i])
            if((i > 0) & (i < s-1)):
                if ((m-a) < (z-m)):
                    m = a
                else:
                    m = z

            lis.append(m)

        binB[bin] = lis
        print(bin, " : ", binB[bin])


for i in range(int(l/s)):
    x = "bin"+str(i+1)
    bins[x] = dataList[s*i:s*(i+1)]

print("\nAfter partitioning into equidepth bins:")
for bin in bins:
    print(bin, " : ", bins[bin])

bin_mean()
binBound()
binMid()
