from socket import create_connection


s = create_connection(('localhost', 8005))

try:
    while True:
        data = s.recv(32)
        print(data.decode())
except KeyboardInterrupt: pass