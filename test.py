with open('sales.txt') as f:
    lines = f.readlines()

temp=[]
file=[]
for i in lines:
	
	if i!='---\n':
		print(i)
		temp.append(i[:-1])
	else:
		print(temp)
		file.append(temp)
		temp=[]
print(file)