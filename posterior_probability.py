##########################################################
# UTA ID    : 1001348700
# Name      : Sagar Surendran
# Date      : 12/04/2019
# Brief     : This program that computes and prints 
#             the probability of any combination of events
#             given any other combination of events, for 
#             the below probability case.
#             P(B) = 0.001
#             P(E) = 0.002
#             P(A|B,E) = {0.95, 0.94, 0.29, 0.001} 
#                         # order - B,E is 00,01,10,11
#             P(J|A) = {0.90, 0.05} # order - A is 0, 1 
#             P(M|A) = {0.70, 0.01} # order - A is 0, 1
##########################################################
import sys

# Initialization
B = 0.001
E = 0.002
AgivenBE = [0.95, 0.94, 0.29, 0.001]
JgivenA = [0.90, 0.05]
MgivenA = [0.70, 0.01]

# BEF stores variables before "given" argument
# AFT stores variables after "given" argument
BEF = []
AFT = []

numerator = 0.0
denominator = 0.0

if (len(sys.argv) < 2) or (len(sys.argv) > 7):
    print("Number of arguments should be in range 1 to 6")
    sys.exit(0)

flag =1

# Store the input variable to BEF and AFT
for i in range(len(sys.argv)):
    if 0 == i:
        continue
    if "given" == sys.argv[i]:
        flag = 0
        continue
    if flag == 1:
        BEF.append(sys.argv[i])
    else:
        AFT.append(sys.argv[i])

def computeProbability(b, e, a, j, m):
    jointProbability = 0.0
    burglaryVal = 0.0
    earthquakeVal = 0.0
    alarmVal = 0.0
    johnCallVal = 0.0
    maryCallVal = 0.0

    if (True == b):
        burglaryVal = B
    else:
        burglaryVal = 1 - B

    if (True == e):
        earthquakeVal = E
    else:
        earthquakeVal = 1 - E

    if (True == a):
        if ((True == b) and (True == e)):
            alarmVal=AgivenBE[0]
        elif True == b and False == e:
            alarmVal=AgivenBE[1]
        elif False == b and True == e:
            alarmVal=AgivenBE[2]
        elif False == b and False == e:
            alarmVal=AgivenBE[3]
        elif True == b and True == e:
            alarmVal=1-AgivenBE[0]
    else:
        if (True == b and False == e):
            alarmVal=1-AgivenBE[1]
        elif (False == b and True == e):
            alarmVal=1-AgivenBE[2]
        elif (False == b and False == e):
            alarmVal=1-AgivenBE[3]

    if True == j:
        if True == a:
            johnCallVal=JgivenA[0]
        else:
            johnCallVal=JgivenA[1]
    else:
        if True == a:
            johnCallVal=1-JgivenA[0]
        else:
            johnCallVal=1-JgivenA[1]

    if True == m:
        if True == a:
            maryCallVal=MgivenA[0]
        else:
            maryCallVal=MgivenA[1]
    else:
        if True == a:
            maryCallVal=1-MgivenA[0]
        else:
            maryCallVal=1-MgivenA[1]

    jointProbability = alarmVal * burglaryVal * johnCallVal * maryCallVal * earthquakeVal
    return jointProbability

def callComputeFunction(bCount, eCount, aCount, jCount, mCount, arrayProc):
    probability = 0.0
    bBool = False
    eBool = False
    aBool = False
    jBool = False
    mBool = False

    if (0 == bCount):
        if "Bt" in arrayProc:
            bBool=True

    if (0 == eCount):
        if "Et" in arrayProc:
            eBool=True

    if (0 == aCount):
        if "At" in arrayProc:
            aBool=True

    if (0 == jCount):
        if "Jt" in arrayProc:
            jBool=True

    if (0 == mCount):
        if "Mt" in arrayProc:
            mBool=True
    for i in range(bCount+1):
        for j in range(eCount+1):
            for k in range(aCount+1):
                for l in range(jCount+1):
                    for m in range(mCount+1):
                        probability += computeProbability(bBool, eBool, aBool, jBool, mBool)
                        if ( (1 == mCount) and (False == mBool)):
                            mBool=True
                        elif ((1 == mCount) and (True == mBool)):
                            mBool=False
                    if ((1 == jCount) and (False == jBool)):
                        jBool=True
                    elif ((1 == jCount) and (True == jBool)):
                        jBool=False
                if ((1 == aCount) and (False == aBool)):
                    aBool=True
                elif ((1 == aCount) and (True == aBool)):
                    aBool=False
            if ( (1 == eCount) and (False == eBool)):
                eBool=True
            elif ((1 == eCount) and (True == eBool)):
                eBool=False
        if ((1 == bCount) and (False == bBool)):
            bBool=True
        elif ((1 == bCount) and (True == bBool)):
            bBool=False

    return probability


if len(BEF) < 1 or len(BEF) > 6:
    print("Number of conditions should be in range 1 to 5.\nExiting Program")
    sys.exit(0)

if ((flag == 0) and (len(AFT) < 1 or len(AFT) > 4)):
    print("Number of 'given' statements should be in range 1 to 4.\nExiting Program")
    sys.exit(0)


countB = 0
countE = 0
countA = 0
countJ = 0
countM = 0

BEF += AFT

#Append True and False to the missing variables in BEF

for i in BEF:
    if not ("Bt" in BEF or "Bf" in BEF):
        BEF.append("Bt")
        BEF.append("Bf")
        countB = 1

    if not ("Et" in BEF or "Ef" in BEF):
        BEF.append("Et")
        BEF.append("Ef")
        countE = 1

    if not ("At" in BEF or "Af" in BEF):
        BEF.append("At")
        BEF.append("Af")
        countA = 1

    if not ("Jt" in BEF or "Jf" in BEF):
        BEF.append("Jt")
        BEF.append("Jf")
        countJ = 1

    if not ("Mt" in BEF or "Mf" in BEF):
        BEF.append("Mt")
        BEF.append("Mf")
        countM = 1

numerator = callComputeFunction(countB, countE, countA, countJ, countM, BEF)

if len(AFT) == 0:
    print("Computed Probability: ", numerator)

countB = 0
countE = 0
countA = 0
countJ = 0
countM = 0

for k in AFT:
    if not ("Bt" in BEF or "Bf" in BEF):
        BEF.append("Bt")
        BEF.append("Bf")
        countB = 1

    if not ("Et" in BEF or "Ef" in BEF):
        BEF.append("Et")
        BEF.append("Ef")
        countE = 1

    if not ("At" in BEF or "Af" in BEF):
        BEF.append("At")
        BEF.append("Af")
        countA = 1

    if not ("Jt" in BEF or "Jf" in BEF):
        BEF.append("Jt")
        BEF.append("Jf")
        countJ = 1

    if not ("Mt" in BEF or "Mf" in BEF):
        BEF.append("Mt")
        BEF.append("Mf")
        countM = 1


denominator = callComputeFunction(countB, countE, countA, countJ, countM, AFT)

if len(AFT) > 0:
    value = numerator/denominator
    print("Computed Probability:", value)


