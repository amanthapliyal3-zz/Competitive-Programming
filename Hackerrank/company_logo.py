'''from sys import stdin,stdout
logo = stdin.readline().strip()

dict ={}
for i in logo :
	if i in dict.keys() :
		dict[i] += 1
	else :
		dict[i] = 1

for keys in dict.keys() :
	a = -1
	b = -1
	c = -1

	if a > dict[keys] :
		a = dict[keys]
		

print(dict)
'''
logo = "google"
dict = {}
dict2 = {}
list =[]
for i in logo :
	if i in dict.keys() :
		dict[i] += 1
	else :
		dict[i] = 1
#print(dict)
max = -1
for _ in range(3) :
	max = -1
	max_key = logo[0]
	for key in dict.keys():
		if dict[key] > max :
			max_key = key
			max = dict[key]
		elif dict[key] == max :
			if max_key > key :
				max_key = key
	dict2[max_key] = dict[max_key]
	dict[max_key] = -1
	#print(dict)
	

#print(list)
for i in dict2 :
    print(i," ",dict2[i])



