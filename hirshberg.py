import numpy as np
import copy

# INITIALIZATION
def init(s1, s2):

    m = np.empty((len(s1) + 1, len(s2) + 1))
    m[:] = np.inf
    # initializing the first row
    m[0] = np.arange(m.shape[1])
    # initializing the first column
    counter = 0
    for i in m:
        i[0] = counter
        counter += 1
    return m



# DIVIDE AND CONQUER APPROACH
def calcByRow(x, y):
    prev = np.arange(0, len(y) + 1)
    curr = np.zeros(len(y) + 1)
    for i in range(1,len(y)+1):
        prev[i]= prev[i-1]+1
    for i in range(1, len(x) + 1):
            curr[0] += 1
            for j in range(1, len(y) + 1):
                ins = curr[j - 1] + 1
                dele = prev[j] + 1
                if x[i - 1] == y[j - 1]:
                    sub = prev[j - 1]
                else:
                    sub = prev[j - 1] + 1
                curr[j] = min(ins, dele, sub)
            prev = copy.deepcopy(curr)
    # hirschberge(x, y)
    return curr

def calcByRow_experiment(x, y):
    prev = np.arange(0, len(y) + 1)
    curr = np.zeros(len(y) + 1)
    for i in range(1,len(y)+1):
        prev[i]= prev[i-1]+1
    for i in range(1, len(x) + 1):
            curr[0] += 1
            for j in range(1, len(y) + 1):
                ins = curr[j - 1] + 1
                dele = prev[j] + 1
                if x[i - 1] == y[j - 1]:
                    sub = prev[j - 1]
                else:
                    sub = prev[j - 1] + 1
                curr[j] = min(ins, dele, sub)
            prev = copy.deepcopy(curr)
    # hirschberge(x, y)
    return curr[-1]

def split(scoreF, scoreR):
    # scoreF front forward, scoreR Buttom up(Reversed)
    splitIndex = 0
    # to locate the best partition (part of the solution)
    minSum = np.inf
    for i, (f, r) in enumerate(zip(scoreF, scoreR[::-1])):
        # calculate the diagonal minimum index
        # iterating over the scores and their indexes
        if sum([f, r]) < minSum:
            minSum = sum([f, r])
            splitIndex = i
    return splitIndex

# Minimum Edit Distance (MED)
# Divide and Conquer DP
def hirschberge(x,y):
    firstString = ""
    secondString = ""
    operations = ""
    if len(x) <= 2 or len(y) <= 2:
        r = med_classicdq(x, y)
        return r
    else:
        xmiddle = int(len(x)/2)
        scoreL = calcByRow(x[:xmiddle], y)
        scoreR = calcByRow(x[xmiddle:][::-1], y[::-1])
        ymid = split(scoreL, scoreR)
        rowLeft, operationsLU, columnUp  = hirschberge(x[:xmiddle], y[:ymid])
        rowRight, operationsRD, columnDown  = hirschberge(x[xmiddle:], y[ymid:])
        firstString = rowLeft + rowRight
        operations = operationsLU + operationsRD
        secondString = columnUp + columnDown

    # if sys.exi
    # print(firstString)
    # print(operations)
    # print(secondString)
    #  editDistance = calcByRow(firstString,secondString)
    # print(editDistance[-1])
    return firstString, operations, secondString

# CLASSIC DYNAMIC PROGRAMMING ALGORITHM USED FOR DIVIDE AND CONQURE
def med_classicdq(s1,s2):
    # INITIALIZATION
    m = init(s1, s2)
    for i in range(1, m.shape[0]):
        for j in range(1, m.shape[1]):

            # first condition : i is an insertion
            con1 = m[i - 1, j] + 1

            # second condition : j is a deletion
            con2 = m[i, j - 1] + 1

            # third condition : i and j are a substitution
            if s1[i - 1] == s2[j - 1]:
                # if same letters, we add nothing
                con3 = m[i - 1, j - 1]
            else:
                # if different letters, we add one
                con3 = m[i - 1, j - 1] + 1

            # assign minimum value
            m[i][j] = min(con1, con2, con3)

    # Alignment
    zero = 0
    mm = np.c_[[zero] * len(m[:]), m]
    mmm = np.r_[[[zero] * len(mm[1, :])], mm]
    backmatrix = [[' ' for y in range(len(s2) + 2)] for x in range(len(s1) + 2)]
    backmatrix[1][1] = 0

    for i in range(2, len(s1) + 2):
        backmatrix[i][0] = s1[i - 2]
    for j in range(2, len(s2) + 2):
        backmatrix[0][j] = s2[j - 2]

    for i in range(2, len(s1) + 2):
        backmatrix[i][1] = '|'

    for j in range(2, len(s2) + 2):
        backmatrix[1][j] = '-'

    for i in range(2, len(s1) + 2):
        for j in range(2, len(s2) + 2):
            vertical = mmm[i - 1][j] + 1
            horizontal = mmm[i][j - 1] + 1
            if s1[i - 2] == s2[j - 2]:
                diagonal = mmm[i - 1][j - 1]
            else:
                diagonal = mmm[i - 1][j - 1] + 1

            mindist = min(diagonal, vertical, horizontal)
            mmm[i][j] = mindist

            if mindist == diagonal:
                backmatrix[i][j] = 'bn'
            elif mindist == vertical:
                backmatrix[i][j] = '|'
            else:
                backmatrix[i][j] = '-'

    ss1 = ""
    ss2 = ""
    op = ""

    i = len(s1) + 1
    j = len(s2) + 1
    while not (i == 1 and j == 1):
        c = backmatrix[i][j]
        if c == '|':
            ss1 += s1[i - 2] + ' '
            ss2 += '-' + ' '
            op += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            ss1 += s1[i - 2] + ' '
            ss2 += s2[j - 2] + ' '
            if s1[i - 2] == s2[j - 2]:
                op += '|' + ' '
            else:
                op += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            ss1 += '-' + ' '
            ss2 += s2[j - 2] + ' '
            op += ' ' + ' '
            j = j - 1
    return ss1[::-1],op[::-1], ss2[::-1]



# TESTING
def test_hirschberge():
    # Test case 1
    s1 = "AGTCT"
    s2 = "AGCT"
    distance = hirschberge(s1, s2)
    assert distance == 1


test_hirschberge()