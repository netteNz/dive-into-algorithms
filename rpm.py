import math
import pandas as pd

n1 = 89
n2 = 18

halving = [n1]
doubling = [n2]

half_double = pd.DataFrame(zip(halving, doubling))

while(len(doubling) < len(halving)):
    doubling.append(max(doubling) * 2)

while min(halving) > 1:
    halving.append(math.floor(min(halving)/2))

answer = sum(half_double.loc[:,1])
print(answer)

#print(math.floor(halving[0]/2))
