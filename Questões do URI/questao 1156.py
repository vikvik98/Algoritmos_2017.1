def main():

	S = 1
	x = 2

	for i in range(3,40,2):
		S += i/x
		x = x * 2

	print("%.2f" % S)



if __name__ == '__main__':
	main()