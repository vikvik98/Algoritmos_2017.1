def main():

	n = int(input())
	
	for i in range(0, 10000):
		if (i % n == 2):
			print(i)
			

if __name__ == '__main__':
	main()
