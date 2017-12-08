def main():

	a = float(input())
	b = float(input())
	c = float(input())
	print("MEDIA = %.1f" % media(a,b,c))

def media(a,b,c):
	media = ((a*2)+(b*3)+(c*5)) / 10
	return media


if __name__ == '__main__':
	main()