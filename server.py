import random
import socket
from multiprocessing import Pool
import shifr

def get_ports(args):
    port, shifr = args
    sock = socket.socket()
    sock.bind(('localhost', port))
    print(f'Listening {port}...')
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        try:
            mes = conn.recv(2024).decode()
            encoded_mes = shifr.crypt(msg, "D")
            print(f'Encrypt message: {mes} \nDecrypt message: {encoded_mes}\n')
            conn.send(str(cipher.crypt(str(encoded_mes).upper(),"E")).encode())
        except ConnectionError as e:
            print(e)
            conn.close()
            break

if __name__=="__main__":
    HOST = 'localhost'
    PORT = 8080
    ports = []
    ports.append(PORT)
    try:
        print(f'Listening {PORT}...')
        sock = socket.socket()
        sock.bind((HOST, PORT))
        sock.listen(1)
        conn, addr = sock.accept()
        answer = conn.recv(2054).decode().split()
        shifr = shifr(int(answer[0]), int(answer[1]), random.randint(1, 200))
        if shifr.check_key():
            conn.send("Access is allowed".encode())
            conn.send(str(shifr.generate_B()).encode())
            A = int(conn.recv(1024).decode())
            shifr.generate_K(A)
            msg = conn.recv(2024).decode().split()
            conn.close()
            sock.close()
            ports.append(int(sifr.crypt(msg[1], "D")))
            with Pool() as p:
                print(p.map(get_ports, zip(ports, [shifr]*len(ports))))

        else:
            conn.close()

    except ZeroDivisionError as e:
        print(e)
    except ConnectionError as e:
        print(e)
        sock.close()