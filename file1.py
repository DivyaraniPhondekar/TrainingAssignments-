def largeNo(n1,n2,n3):
	"Find the large number"
	if (n1 >= n2) and (n1 >= n3):
	   largest = n1
	elif (n2 >= n1) and (n2 >= n3):
	   largest = n2
	else:
	   largest = n3

	print "The largest number between",n1,n2,"and",n3,"is",largest