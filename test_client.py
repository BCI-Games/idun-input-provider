from socket import create_connection


s = create_connection(('localhost', 8005))

try:
    while True:
        data = s.recv(32)
        if len(data) > 0:
            print(data.decode())
        else: break

except KeyboardInterrupt: pass