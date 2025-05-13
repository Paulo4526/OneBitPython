#Criptografando textos com hashlib
import hashlib

# 1 - Verificar os algoritimos disponíveis
print(hashlib.algorithms_available)

# 2 - Algorítimos disponíveis de acordo com o sistema operacional da nossa máquina.
print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o sha256 mais utilizado para segurança
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro com a onebitcode!".encode('utf-8')
algorithm.update(message) #Passando o valor de menssagem decodificado para o algorithm
print(algorithm.hexdigest()) #Texto criptografado em hexa decimal

# 4 - Utilizando a codificação MD5 pouco indicado para segurança
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())
