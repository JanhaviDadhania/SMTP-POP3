import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8080));
serv.listen()

def check_if_string_in_file(file_name, string_to_search):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False

check = 1
finalise = 0

while True:
    conn, addr = serv.accept()
    from_client = ''

    while True:
        data = conn.recv(4096)
        if not data: break
        from_client = data.decode()
        print(from_client)

        if from_client=='1':
            print("stat")

            out_file = open("user1/mymailbox", "r")
            lines = out_file.readlines()
            print(lines[0])

            byte = lines[0].encode()
            conn.send(byte)
        elif from_client == '2':
            print("list")

            out_file = open("user1/mymailbox", "r")
            lines = out_file.readlines()
            total = 0

            byte = lines[0].encode()
            conn.send(byte)
            for line in lines:
                if "From:" in line:
                    one = line.replace('From: ', '')
                    one = one.rstrip('\n')
                    total = total + 1
                if "Received: " in line:
                    two = line.replace('Received: ', '')
                    two = two.rstrip('\n')
                    total = total + 1
                if "Subject: " in line:
                    three = line.replace('Subject: ', '')
                    three = three.rstrip('\n')
                    total = total + 1
                if total==3:
                    last = one + two + three
                    byte = last.encode()
                    conn.send(byte)
                    print(last)
                    total = 0
                #last = "."
                #/byte = last.encode()
                #conn.send(byte)
                out_file.close()
        elif from_client == '3':
            print("successful")
            receive = conn.recv(4096)
            sr_nu = receive.decode()
            print(type(sr_nu))
            out_file = open("user1/mymailbox", "r")
            lines = out_file.readlines()
            sr_nu = sr_nu + '.'
            blocked = 1
            five = ''
            for line in lines:

                if sr_nu in line:
                    print("gotcha")
                    blocked = 0
                    continue
                if blocked==0:
                    if 'From: ' in line:
                        print(line)
                        one = line.rstrip('\n')
                    elif 'To: ' in line:
                        print(line)
                        two = line.rstrip('\n')
                    elif 'Subject: ' in line:
                        print(line)
                        three = line.rstrip('\n')
                    elif 'Received: ' in line:
                        print(line)
                        four = line.rstrip('\n')
                    elif '.' not in line:
                        print(line)
                        five += line.rstrip()
                    else:
                        blocked = 1
            last = one + two + three + four + five
            byte = last.encode()
            conn.send(byte)
        elif from_client == '4':
            print("deleting")
            receive = conn.recv(4096)
            sr_nu = receive.decode()
            print(type(sr_nu))
            print(sr_nu)
            index = 1













        if check_if_string_in_file("auth.txt", from_client):
            str="2"

        else :
            str="0"
        print(str)
        byte = str.encode()
        conn.send(byte)



    conn.close()
    print("client disconnected")
