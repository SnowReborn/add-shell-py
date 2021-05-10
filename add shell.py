import hashlib
def main():
	while True:
		enc = hashlib.sha256
		global payload_path
		payload_path = input("What's payload path? \n")
		payload_data = open(payload_path,'r+b').read()
		sha256finger = enc(payload_data).hexdigest()
		print("The sha256 for payload is : {}".format(sha256finger))
		target_path = input("what's target path? \n")
		target_data = open(target_path, 'r+b').read()
		sha256finger = enc(target_data).hexdigest()
		print("The sha256 for target is : {}".format(sha256finger))
		if input("execute? yes or no \n") == "yes":
			ffile= open(target_path,'w+b')
			ffile.write(payload_data + target_data)
			ffile.close()
			altered_target_data= open(target_path,'r+b')
			sha256finger = enc(altered_target_data).hexdigest()
			print("DONE! The sha256 for target is NOW : {}".format(sha256finger))
		if input("Press anything other than R to continue\n") == 'r':
			break
main()
