from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


#def generate_keys():
#Generate keys
private_key = rsa.generate_private_key(
	public_exponent=65537,
	key_size=2048,
	backend=default_backend()

	)
public_key = private_key.public_key()
#return public_key, private_key

#def store_private(private_key):
#Store private key

pem = private_key.private_bytes(

	encoding = serialization.Encoding.PEM,
	format = serialization.PrivateFormat.PKCS8,
	encryption_algorithm = serialization.NoEncryption()

	)

with open("private_key.pem", "wb") as f:
	f.write(pem)

#def store_public(public_key):
#store public key

pem = public_key.public_bytes(

	encoding = serialization.Encoding.PEM,
	format = serialization.PublicFormat.SubjectPublicKeyInfo

	)

with open("public_key.pem", "wb") as f:
	f.write(pem)

#def read_keys():
#read the keys out
with open("private_key.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
		key_file.read(),
		password= None,
		backend = default_backend()

		)
with open("public_key.pem", "rb") as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend = default_backend()

		)






#encrypt jpegs
