import numpy  as np
import matplotlib.pyplot as plt
files=['tabularform','serialform','time20','time10','recall','animal']
print("Graphs")
print("1. Tabular Form ")
print("2. Serial Form")
print("3. Time provided 10s")
print("4. Time provided 20s ")
print("5. Recall tendancy data on 10 persons")
print("6. Comparsion with time 10s and time 20s")
print("7. Comparsion with orientation of info(i.e tabular and serial for 20s)")
print("8. Animals Recall")

ch=int(input("Enter the choice"))
if(ch<=5):
	data=np.loadtxt(files[ch-1]+'.txt')
elif(ch==8):
	data=np.loadtxt(files[5]+'.txt')
	x = data[:, 0]
	y = data[:, 1]
	plt.plot(x,y,label=files[5])
	plt.xlabel("Animal no.")
	plt.ylabel("Recall%(out of 100)")
	plt.legend()
	plt.show()
	exit(1)
elif (ch==6):
	for i in range (2):
		data=np.loadtxt(files[i]+'.txt')		
		x = data[:, 0]
		y = data[:, 1]
		plt.plot(x,y,label=files[i])
	plt.xlabel("No.of people")
	plt.ylabel("No.of correct ans")
	plt.legend()
	plt.show()
	exit(1)
elif (ch==7):
	for i in range (2,4):
		data=np.loadtxt(files[i]+'.txt')		
		x = data[:, 0]
		y = data[:, 1]
		plt.plot(x,y,label=files[i])
	plt.xlabel("No.of people")
	plt.ylabel("No.of correct ans")
	plt.legend()
	plt.show()
	exit(1)
else:
	print("Invalid choice")
	exit(1)	
x = data[:, 0]
y = data[:, 1]
plt.plot(x, y,label=files[ch-1])
if(ch<5):
	plt.xlabel("No.of people")
	plt.ylabel("No.of correct ans")
elif(ch==5):
	plt.xlabel("Word position")
	plt.ylabel("Recall ability of 10 persons (out of 100)")
plt.legend()
plt.show()
