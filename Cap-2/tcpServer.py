import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Primeiro passamos o endereço ip e a porta que deseja
server.bind((bind_ip, bind_port))

# Agora colocamos o servidor para escutar com o atraso máximo de conexões definidas para 5
server.listen(5)
print(f"Escutando de: {bind_ip}:{bind_port}")


# Ele executa o recv e em seguida envar pacotes de teste para o servidor
def handle_client(client_socket):
    request = client_socket.recv(1024)

    print(f"Recebeu: {request}")

    client_socket.send("ACK")

    client_socket.close()


while True:
    # Quando o cliente se conecta mostra os detalhes da conexão remota
    client, addr = server.accept()
    print(f"Conexão aceita de: {addr[0], addr[1]}")

    # Inicia o thread para lidar com a conexão do cliente e o servidor conseguirá lidar com outra conexão de entrada
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()