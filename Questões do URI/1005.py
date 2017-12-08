def main():

	a = float(input())
	b = float(input())
	print("MEDIA = %.5f" % media(a,b))

def media(a,b):
	media = ((a*3.5)+(b*7.5)) / 11
	return media


if __name__ == '__main__':
	main()