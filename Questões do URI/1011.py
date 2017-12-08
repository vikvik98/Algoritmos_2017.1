def main():

	r = int(input())
	

	print("VOLUME = %.3f" % volume(r))

def volume(r):
	volume = (4/3) * 3.14159 * (r**3)
	return volume


if __name__ == '__main__':
	main()