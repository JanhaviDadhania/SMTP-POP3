import socket
from datetime import datetime

today = datetime.now()
print("today:", today)
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8900));
serv.listen()

out_file = open("user1/mymailbox", "r")
lines = out_file.readlines()
index = int(lines[0])
print(lines[0])
out_file.close()

out_file = open("user1/mymailbox", "a")
#out_file.write("ttrr")
print("server on")

while True:
    conn, addr = serv.accept()
    print("accepted")
    from_client = ''
    flag = 0
    while True:
        data = conn.recv(4096)
        from_client = data.decode()
        print(from_client)
        message = "250 OK Hello"
        byte = message.encode()
        conn.send(byte)
        data = conn.recv(4096)
        from_client = data.decode()
        print(from_client)
        message = "250 OK...sender ok"
        byte = message.encode()
        conn.send(byte)
        data = conn.recv(4096)
        from_client = data.decode()
        print(from_client)
        message = "250 OK...Recipient ok"
        byte = message.encode()
        conn.send(byte)
        data = conn.recv(4096)
        from_client = data.decode()
        print(from_client)
        message = "350"
        byte = message.encode()
        conn.send(byte)



        data = conn.recv(4096)
        if not data: break
        from_client = data.decode()
        out_file.write(str(index+1))
        out_file.write("\n")
        out_file.flush()
        print(index+1)
        out_file.write(from_client)
        out_file.flush()
        print(from_client)
        data = conn.recv(4096)
        if not data: break
        from_client = data.decode()
        out_file.write(from_client)
        out_file.write("\n")
        out_file.flush()
        print(from_client)
        data = conn.recv(4096)
        if not data: break
        from_client = data.decode()
        out_file.write(from_client)
        out_file.write("\n")
        out_file.flush()
        print(from_client)

        out_file.write(".")
        out_file.flush()

    message = "Message accepted for delivery"
    byte = message.encode()
    conn.send(byte)
    from_client = conn.recv(4049)
    print(from_client.decode())
    print("closing connection")
    out_file.close()
