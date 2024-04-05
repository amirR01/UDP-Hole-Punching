all: stun_server client 

stun_server: STUN.py
	python3 STUN.py

client: Client.py
	python3 Client.py
