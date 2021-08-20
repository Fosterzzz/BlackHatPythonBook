import socket

target_host = "www.google.com"
target_port = 80

# Criando socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar o cliente

client.connect((target_host, target_port))

# Enviar alguns dados

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode('utf-8'))

# Receber os dados
response = client.recv(4096)

print(response)
'''
AF_INET está dizendo que vamos usar IPv4 ou o nome do host
SOCK_STREAM indica que será um cliente TCP
'''
