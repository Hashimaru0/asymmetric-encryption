from cryptography.fernet import Fernet
import rsa
import pathlib
import os

keys_path = str(pathlib.Path(__file__).parent.resolve()).replace(os.sep,'/') + '/keys.txt'
to_encrypt_path = str(pathlib.Path(__file__).parent.resolve()).replace(os.sep, '/') + '/toEncrypt'
encrypted_path = str(pathlib.Path(__file__).parent.resolve()).replace(os.sep, '/') + '/encrypted'

# Gets keys from keys.txt
try:
  with open(keys_path, 'r') as kp:
    lines = kp.readlines()
    sym_key = lines[0].split(' = ',1)[1].removesuffix('\n')
    pub_key = tuple(map(int, lines[1].split(' = ',1)[1].removesuffix(')\n').removeprefix('PublicKey(').split(', ')))
    pub_key = rsa.PublicKey(pub_key[0], pub_key[1])
    priv_key = tuple(map(int, lines[2].split(' = ',1)[1].removesuffix(')').removeprefix('PrivateKey(').split(', ')))
    priv_key = rsa.PrivateKey(priv_key[0], priv_key[1], priv_key[2], priv_key[3], priv_key[4])
except:
  print("KEYS NOT GENERATED")

# Generates symmetric, private and public key, encrypts symmetric key and writes them to a file
def generateKeys():
  sym_key = Fernet.generate_key()
  (pub_key, priv_key) = rsa.newkeys(1024)
  with open(keys_path, 'w') as kp:
    kp.write(f'symmetric key = {sym_key.decode("utf-8")}\n')
    kp.write(f'public key = {pub_key}\n')
    kp.write(f'private key = {priv_key}')

# Encrypts all files inside toEncrypt folder
def encryptFiles():
  cipher = Fernet(sym_key)
  for file_name in os.listdir(to_encrypt_path):
    file_path = os.path.join(to_encrypt_path, file_name).replace(os.sep, '/')
    with open(file_path, 'rb') as f:
      file = f.read()
      encrypted_file = cipher.encrypt(file)
      encrypted_file_path = os.path.join(encrypted_path, file_name + 'encrypted').replace(os.sep, '/')
      with open(encrypted_file_path, 'wb') as ef:
        ef.write(encrypted_file)

# Decrypts all files inside encrypted folder
def decryptFiles():
  cipher = Fernet(sym_key)
  for file_name in os.listdir(encrypted_path):
    file_path = os.path.join(encrypted_path, file_name).replace(os.sep, '/')
    with open(file_path, 'rb') as f:
      file = f.read()
      encrypted_file = cipher.decrypt(file)
      encrypted_file_path = os.path.join(encrypted_path, file_name.removesuffix('encrypted')).replace(os.sep, '/')
      with open(encrypted_file_path, 'wb') as ef:
        ef.write(encrypted_file)

# Pick your action
#generateKeys()
#encryptFiles()
#decryptFiles()