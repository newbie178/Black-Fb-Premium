import time,os,sys
def main(arg):
	for t in arg+"\n":
#		for t2 in text2+"\n":
		sys.stdout.write(t)
		sys.stdout.flush()
		time.sleep(0.1)

if __name__ == '__main__':
	main("\033[31m[-] Closed \n")
	main("\033[32m[+] Please Contact 'BL4CK DR460N' or 'MrF??'")
