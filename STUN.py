import socket
import threading

STUN_SERVER_IP = "localhost"
STUN_SERVER_PORT = 12345

id_generator_lock = threading.Lock()
id_generator = 0
clients  = {}

def handle_client(server_socket,data, addr):
    request = data.decode().split(' ')
    if request[0] == "REGISTER":
        register_client(server_socket,addr)
    elif request[0] == "REQUEST":
        request_client(server_socket,addr, request[1])


def register_client(server_socket,addr):
    global id_generator
    id_generator_lock.acquire()
    client_id = id_generator
    id_generator += 1
    id_generator_lock.release()
    clients[client_id] = addr
     # Send the client's IP and port back to the client
    ip , port = addr
    response = f"{client_id},{ip},{port}"
    server_socket.sendto(response.encode(), addr)

    
def request_client(server_socket,addr,client_id):
    if int(client_id) in clients:
        des_addr = clients[int(client_id)]
        ip , port = des_addr
        response = f"{ip},{port}"
        server_socket.sendto(response.encode(), addr)
    else:
        server_socket.send("NOT_FOUND".encode(),addr)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((STUN_SERVER_IP, STUN_SERVER_PORT))

    print(f"STUN Server listening on {STUN_SERVER_IP}:{STUN_SERVER_PORT}")

    while True:
        data, addr = server_socket.recvfrom(4096)
        client_handler = threading.Thread(target=handle_client, args=(server_socket,data,addr))
        client_handler.start()

if __name__ == "__main__":
    main()
