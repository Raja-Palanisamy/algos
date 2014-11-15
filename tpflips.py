# Enter your code here. Read input from STDIN. Print output to STDOUT

def boolFlips(row):
    flipsarrT = []
    flipsarrP = []
    for i in row:
        if i=='T':
            flipsarrT.append(0)
            flipsarrP.append(1)
        else:
            flipsarrT.append(1)
            flipsarrP.append(0)
    return (tuple(flipsarrT),tuple(flipsarrP))

if __name__ == "__main__":
    mn = raw_input().split()
    (m,n) = (int(mn[0]),int(mn[1]))
    row = []
    flips = {}
    max_count = 0
    for i in range(0,m):
        row.append(list(raw_input()))
        
        (tflips,pflips) = boolFlips(row[-1])
        flips[tflips] = flips.get(tflips,0)+1
        flips[pflips] = flips.get(pflips,0)+1
        
        max_count = max(flips[tflips], flips[pflips], max_count)

    print max_count
