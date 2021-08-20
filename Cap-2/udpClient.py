import socket

target_host = "127.0.0.1"
target_port = 80

# SOCK_DGRAM é para a conexão UDP

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("SeiLa".encode('utf-8'), (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)