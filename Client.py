import socket
import threading
import datetime

STUN_SERVER_IP = "localhost"
STUN_SERVER_PORT = 12345


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # register client
    client_socket.sendto("REGISTER".encode(), (STUN_SERVER_IP, STUN_SERVER_PORT))

    # Receive own IP and port from the STUN server
    response = client_socket.recv(1024).decode()
    my_id , my_ip , my_port = response.split(',')
    print(f"Registered as client {my_id} with IP {my_ip} and port {my_port}")

    # create a thread to listen for messages from other clients

    client_id = int(input("Enter client number\n"))
    # Request the IP and port of desired client
    client_socket.sendto(f"REQUEST {client_id}".encode(), (STUN_SERVER_IP, STUN_SERVER_PORT))
    response = client_socket.recv(1024).decode()
    if response == "NOT_FOUND":
        print(f"Client {client_id} not found")
    else:
        client_ip, client_port = response.split(',')
        print(f"connected to client {client_id}.")
    print("ready to send")
    client_handler = threading.Thread(target=listen, args=(client_socket,))
    client_handler.start()

    while(True):
        # ask for the message to send
        message = input()
        # attach the date and time of sending to the message
        message = f"{message} (sent at {datetime.datetime.now()})"
        # send the message to the desired client
        client_socket.sendto(message.encode(), (client_ip, int(client_port)))

def listen(client_socket):

    print(f"ready to listen")

    while True:
        message, addr = client_socket.recvfrom(1024)
        print(f"Received message: {message.decode()}")
    
if __name__ == "__main__":
    main()
