from hashlib import sha1,sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, shake_256, blake2b, blake2s, md5

def ksha1(data):
	hash = sha1(data).hexdigest()
	return hash

def ksha224(data):
	hash = sha224(data).hexdigest()
	return hash

def ksha256(data):
	hash = sha256(data).hexdigest()
	return hash

def ksha384(data):
	hash = sha384(data).hexdigest()
	return hash

def ksha512(data):
	hash = sha512(data).hexdigest()
	return hash

def ksha3_224(data):
	hash = sha3_224(data).hexdigest()
	return hash

def ksha3_256(data):
	hash = sha3_256(data).hexdigest()
	return hash

def ksha3_384(data):
	hash = sha3_384(data).hexdigest()
	return hash

def ksha3_512(data):
	hash = sha3_512(data).hexdigest()
	return hash

def kshake_128(data):
	hash = shake_128(data).hexdigest(4)
	return hash

def kshake_256(data):
	hash = shake_256(data).hexdigest(4)
	return hash

def kblake2b(data):
	hash = blake2b(data).hexdigest()
	return hash

def kblake2s(data):
	hash = blake2s(data).hexdigest()
	return hash

def kmd5(data):
	hash = md5(data).hexdigest()
	return hash