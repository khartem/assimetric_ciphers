import socket
import time
import shifr

HOST = 'localhost'
PORT = 8080

def generate_port(K):
   global PORT
   NEW_PORT = PORT + (PORT - K)%K
   try:
       if int(NEW_PORT)<9999:
           return NEW_PORT
       else:
           return -1
   except:
       return -1
try:
    sock = socket.socket()
    sock.connect((HOST, PORT))
    shifr = shifr()
    if not shifr.read_ready_keys():
        shifr.create_bunch()
    sock.send((str(shifr.g)+" "+str(shifr.p)).encode())
    if sock.recv(1024).decode() == "Access is allowed":
        server_key_partial = int(sock.recv(1024).decode())
        client_partial_key = shifr.generate_B()
        sock.send(str(client_partial_key).encode())
        shifr.generate_K(server_key_partial)
        NEWPORT = generate_port(shifr.K)
        if NEWPORT == -1:
            print("Incorrect port!")
            sock.close()
        else:
            sock.send((shifr.crypt("Connection", "E") +" "+ shifr.crypt(str(NEWPORT), "E")).encode())
            sock.close()
            sock = socket.socket()
            time.sleep(5)
            sock.connect((HOST, NEWPORT))
            while True:
                msg = input(">")
                if msg.lower()=="exit":
                    break
                sock.send((shifr.crypt(msg, "E")).encode())
                ans = sock.recv(1024).decode()
                print("response: "+shifr.crypt(ans,"D"))

    else:
        print("Access not allowed")
        sock.close()

except ZeroDivisionError as e:
    print(e)