def in_both(word1,word2):
	if word1>word2:
		m=word1
		other=word2
	else:
		m=word2
		other=word1
	for x in m:
		if x in other:
			print(x)

in_both('python is easy','not really')

def sum_element(l):
	sum=0
	for x in range (len(l)):
		if type(l[x]) == list:
			for y in range(len(l[x])):
				sum+=l[x][y]
		else:
			sum+=l[x]
	print(sum)

sum_element([1,2,[4,5],3])

