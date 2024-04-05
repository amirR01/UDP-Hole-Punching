# UDP-Hole-Punching
This is a simple implementation of UDP Hole Punching in Python. It is a simple P2P connection between two clients behind NATs. The server is used to exchange the public IPs and ports of the clients. The clients then use this information to establish a connection between themselves.

### CLIENT DETAILS ###
- the client will register itself in server. and it recevies client_id and its ip and port. then it will ask the server the ip and port of desired client. after that it will send messages to the desired client. and it will receive the messages from the desired client.

### SERVER DETAILS ###
- The server has 2 objectivity. first it will register the client and then it will send the ip and port of desired client to the client.

### HOW TO TEST ###
- run stun_server with the following command:
```
make stun_server
```
- Then run first client with the following command:
```
make client
```
- Then run second client with the following command:
```
make client
```
- Then each client will receive its id and stun_server will ask them for the desired client id. enter the client ids vice versa.

- Then each client will be ready to send and receive messages.

- you can see that if you send a message from client 1 to client 2, the message will be received by client 2 and vice versa.

- you can see the example usage screenshots in the screenshots folder.

