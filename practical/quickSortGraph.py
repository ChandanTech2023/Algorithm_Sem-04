import matplotlib.pyplot as plt 
import subprocess as sb 

option = input("1.Quick Sort \n2.Random Quick Sort\n")
if option == '1':
    sb.run(['powershell','g++ quickSort.cpp -o quickSort'])
    sb.run(['powershell','./quickSort'])
else:
    sb.run(['powershell','g++ randomQuickSort.cpp -o randomQuickSort'])
    sb.run(['powershell','./randomQuickSort'])


with open("quickSortSizes.txt") as f:
    sizes = f.read()

with open("quickSortAverages.txt") as f:
    average = f.read()

sizes = [int(i) for i in sizes.split(",")]
average = [int(i) for i in average.split(',')]

plt.plot(sizes,average)

plt.xlabel("Sizes of Array")
plt.ylabel("Averages of Arrays")
plt.grid(True)
plt.show()