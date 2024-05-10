from os import system
import module
import sqlite3

db = sqlite3.connect("db")
cur = db.cursor()
record=[]  #file, hash, original_checksum, file_checksum, result

def main():
	opt = input("Enter option (1/2):\n1. Compare checksum\n2. Exit\n\t")
	try: 
		opt = int(opt)
	except ValueError:
		print("Invalid option! Try again.")
		system("pause")
		print("\n\n")
		main()
	if opt == 1:
		file = input(r"Enter file path: ")
		file = file.strip()
		hashes = ["sha1", "sha224", "sha256", "sha384", "sha512", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256", "blake2b", "blake2s", "md5", "custom"]
		print("\n\tSupported checksums: ", hashes)
		hsh = input("What sort of checksum do you have? : ")  #type of checksum
		hsh = hsh.lower()
		hsh = hsh.strip()  #strip whitespace
		original_checksum = input("Enter checksum given by creator: ")
		print()
		checksum(file, hsh, original_checksum)
	elif opt == 2:
		db.close()
		exit()
	else:
		print("Wrong option. Try again!")
		system("pause")
		print("\n\n")
		main()		


def compare(original_checksum, file_checksum):
	original_checksum = original_checksum.strip()
	original_checksum = original_checksum.lower()
	file_checksum = file_checksum.strip()
	file_checksum = file_checksum.lower()
	print("The checksum given by creators: ", original_checksum)
	print("The checksum of the file: ", file_checksum)
	record.insert(2, original_checksum)
	record.insert(3, file_checksum)
	print()
	if original_checksum == file_checksum:
		print("The file has not been damaged!")
		record.insert(4, "The file had not been damaged")
		savetodb(record)
		system("pause")
		print("\n\n")
		main()
	elif original_checksum != file_checksum:
		print("The file has been damaged/ corrupted!")
		record.insert(4, "The file had been damaged/ corrupted!")
		savetodb(record)
		system("pause")
		print("\n\n")
		main()
	else:
		print("There has been an error. Restart the program or input checksums again.")
		system("pause")
		print("\n\n")
		main()
		

def checksum(file, hsh, original_checksum):
	dta = None
	try:
		ff= open(file, 'rb')
		dta = ff.read()
		record.insert(0, file)
	except FileNotFoundError:
		if hsh == "custom":
			x = input("Enter checksum you got: ")
			record.insert(0, "None")
			compare(original_checksum, x)
		print("The file does not exist. Try again!\n")
		system("pause")
		print("\n\n")
		main()
	except:
		print("Invalid file path! Try again")
		system("pause")
		print("\n\n")
		main()
	
	hashes = ["sha1", "sha224", "sha256", "sha384", "sha512", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256", "blake2b", "blake2s", "md5", "custom"]

	if hsh == "sha1":
		record.insert(1, "sha1")
		x = module.ksha1(dta)
		compare(original_checksum, x)
	if hsh == "sha224":
		record.insert(1, "sha224")
		x = module.ksha224(dta)
		compare(original_checksum, x)
	if hsh == "sha256":
		record.insert(1, 'sha256')
		x = module.ksha256(dta)
		compare(original_checksum, x)
	if hsh == "sha384":
		record.insert(1, 'sha384')
		x = module.ksha384(dta)
		compare(original_checksum, x)
	if hsh == "sha512":
		x = module.ksha512(dta)
		record.insert(1, 'sha512')
		compare(original_checksum, x)
	if hsh == "sha3_224":
		record.insert(1, 'sha3_224')
		x = module.ksha3_224(dta)
		compare(original_checksum, x)				
	if hsh == "sha3_256":
		record.insert(1, 'sha3_256')
		x = module.ksha3_256(dta)
		compare(original_checksum, x)
	if hsh == "sha3_384":
		record.insert(1, 'sha3_384')
		x = module.ksha3_384(dta)
		compare(original_checksum, x)
	if hsh == "sha3_512":
		record.insert(1, 'sha3_512')
		x = module.ksha3_512(dta)
		compare(original_checksum, x)
	if hsh == "shake_128":
		record.insert(1, 'shake_128')
		x = module.kshake_128(dta)
		compare(original_checksum, x)
	if hsh == "shake_256":
		record.insert(1, 'shake_256')
		x = module.kshake_256(dta)
		compare(original_checksum, x)
	if hsh == "blake2b":
		record.insert(1, 'blake2b')
		x = module.kblake2b(dta)
		compare(original_checksum, x)
	if hsh == "blake2s":
		record.insert(1, 'blake2s')
		x = module.kblake2s(dta)
		compare(original_checksum, x)
	if hsh == "md5":
		record.insert(1, 'md5')
		x = module.kmd5(dta)
		compare(original_checksum, x)
	if hsh == "custom":
		record.insert(1, 'custom')
		x = input("Enter checksum you got: ")
		compare(original_checksum, x)
	if hsh not in hashes:
		print("Checksum not supported. Try again!\n")
		main()
	else:
		print("There has been an error. Restart the program.")


def savetodb(record):
	#table creation command: CREATE TABLE checksums (id INTEGER PRIMARY KEY AUTOINCREMENT, date DATE, file VARCHAR(255), hash VARCHAR(12), original_checksum VARCHAR(60), file_checksum VARCHAR(60), result VARCHAR(30));
	cur.execute("INSERT INTO checksums (file, hash, original_checksum, file_checksum, result) VALUES(?, ?, ?, ?, ?)", (record[0], record[1], record[2], record[3], record[4]))
	record.clear()
	db.commit()
	