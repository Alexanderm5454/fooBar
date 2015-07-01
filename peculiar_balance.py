def answer(x):
    scaleArrangement = []
    leftScale = []
    rightScale = []
    powersOfThree = []
    setItem = 0
    powersSum = 0
    leftSum = 0
    rightSum = 0
    magOfDiff = 0
    staticPowersOfThree = []

    for i in range(x):
        setItem = 3**i
        if setItem <= x:
            powersOfThree.append(setItem)
            staticPowersOfThree.append(setItem)
        else:
            break

    powersSum = sum(powersOfThree)
    powersLength = len(powersOfThree)
    
    if powersSum == x:
        for i in range(len(powersOfThree)):
            scaleArrangement.append("R")
        return scaleArrangement
    elif powersSum < x:
        nextPowerOfThree = 3**(powersLength)
        rightScale.append(nextPowerOfThree)
        staticPowersOfThree.append(nextPowerOfThree)
    elif powersSum > x:
        nextPowerOfThree = powersOfThree[powersLength-1]

    leftScale.append(x)
    for i in range(powersLength-1,-1,-1):
        leftSum = sum(leftScale)
        rightSum = sum(rightScale)
        magOfDiff = abs(leftSum - rightSum)
        if magOfDiff != 0:
            
            for j in range(i,-1,-1):
               
                if leftSum < rightSum:
                    
                    if magOfDiff >= abs(powersOfThree[j] - sum(powersOfThree[0:j])):
                        leftScale.append(powersOfThree[j])
                        powersOfThree.remove(powersOfThree[j])
                    else:
                        powersOfThree.remove(powersOfThree[i])
                elif leftSum > rightSum:
                    if magOfDiff >= abs(powersOfThree[j] - sum(powersOfThree[0:j])):
                        rightScale.append(powersOfThree[j])
                        powersOfThree.remove(powersOfThree[j])
                    else:
                        powersOfThree.remove(powersOfThree[i])
                                                                             
                break
        else:
            break
    leftSum = sum(leftScale)
    rightSum = sum(rightScale)
    leftScale.remove(x)
    leftScale.sort()
    rightScale.sort()
    
    for n in range(len(staticPowersOfThree)):
        if staticPowersOfThree[n] in leftScale:
            scaleArrangement.append("L")
            
        elif staticPowersOfThree[n] in rightScale:
            scaleArrangement.append("R")
            
        else:
            scaleArrangement.append("-")
    
    if leftSum == rightSum:
        return scaleArrangement, "SOLUTION", leftSum, rightSum, leftScale, rightScale
    else:
        print staticPowersOfThree
        
        difference = leftSum - rightSum
        
        if leftSum == rightSum:
            return  "SOLUTION", leftSum, rightSum, leftScale, rightScale
        else:               
            return  "ERROR", leftSum, rightSum, leftScale, rightScale, "ERROR---------Difference:", difference
 
    
