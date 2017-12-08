def main():
	
	n = int(input())
	z = 0
	y = 0

	for i in range(n):
		x = int(input())
		if x in range(10,20):
			z += 1
		else:
			y += 1
	print("%d in" % z)
	print("%d out" % y)
	
if __name__ == '__main__':
	main()