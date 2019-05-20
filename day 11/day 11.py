import numpy as np
from scipy import stats
x=np.array([13, 18, 13, 14, 13, 16, 14, 21, 13])
print(x)


print("Mean value is: ", np.mean(x))
print("Median value is: ", np.median(x))

print("Mode value is: ", stats.mode(x))


print("Minimum value is: ", np.min(x))
print("Maximum value is: ", np.max(x))
print("range is: ", np.max(x)-np.min(x))



#.....................................

import numpy as np
list1=input("enter any 9 space seperated values")

list1=list1.split()
list1=list(map(int,list1))
lis1=np.array(list1)
arr_reshapes=lis1.reshape(3,3)
print(arr_reshapes)

#.......................................

import numpy as np
x=np.random.randint(5,16,40)
print("original array")
print(x)
print("most frequent values in the above array" )
print(np.bincount(x).argmax())


#....................................

import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(100.0, 20.0, 10000)
print (incomes)
mean1=("mean is ",np.mean(incomes))
incomes2=np.append(incomes,3000000)
mean2=("mean is ",np.mean(incomes2))


plt.hist(incomes, normed=True, bins=50)

plt.show()
incomes.mean()

#...................................



import numpy as np
import matplotlib.pyplot as plt
incomes = np.random.normal(150.0, 20.0, 1000)

plt.hist(incomes,bins=100)
plt.show()
np.std(incomes)
np.var(incomes)






