def main():

	S = 1

	for i in range(2,101):
		S += 1/i

	print("%.2f" % S)



if __name__ == '__main__':
	main()