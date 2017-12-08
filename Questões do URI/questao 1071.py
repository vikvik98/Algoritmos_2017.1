def main():
	
	x = int(input())
	y = int(input())
	z = 0

	for i in range((y+1),x):
		if i % 2 != 0:
			z += i
	print(z)

if __name__ == '__main__':
	main()
