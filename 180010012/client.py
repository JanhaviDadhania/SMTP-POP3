import socket
import sys
import re
from datetime import datetime

today = datetime.now()
print("today:", today)

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def check(email):
      if(re.search(regex,email)):
        print("valid email")
        return 1
      else:
        print("invalid email")
        return 0


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

username = input("username- ")
password = input("password- ")

out_file = open("user.txt", "a")
out_file.write(username + "\n" + password + "\n" )
out_file.close()

print("\nHello, Mail user :) Options are as below")
print("1 - Manage Mail")
print("2 - Send Mail")
print("3 - Quit\n")

client.connect(('127.0.0.1', 8900))
while 1:
    username = input("username- ")
    password = input("password- ")
    answer = int(input())
    if answer==1:
        str = username + password
        byte = str.encode()
        client.send(byte)
        from_server = client.recv(4096)
        print(from_server)

        if from_server.decode()=='0':

            continue
            print(3)
        else :
            print("Successful Logged In -")
            print("You have following options")
            print("1.STAT")
            print("2.LIST")
            print("3.RETR")
            print("4.DELE")
            print("5.QUIT")
            option = int(input())
            if option==1:
                str = '1'
                byte = str.encode()
                client.send(byte)
                print(1)
                from_server = client.recv(4096)
                print("You have these number of mails")
                print(from_server)
            elif option==2:
                str = '2'
                byte = str.encode()
                client.send(byte)
                print(2)
                print("List of your email")
                from_server = client.recv(4096)
                index = int(from_server.decode())
                print(from_server)
                while index:
                    from_server = client.recv(4096)
                    if from_server.decode()==".":
                        break
                    print(from_server)
                    index = index - 1
            elif option==3:
                str = '3'
                byte = str.encode()
                client.send(byte)
                print(3)
                string = input()
                byte = string.encode()
                client.send(byte)
                last = client.recv(4049)
                output = last.decode()
                print(output)
            elif option==4:
                str = '4'
                byte = str.encode()
                client.send(byte)
                delete = input()
                byte = delete.encode()
                client.send(byte)
                print(4)
            elif option==5:
                print("Bye Bye.................")
                exit()







    elif answer==2:
        print("oh, want to send mail ! :)")
        with open('user.txt') as file:
            contents = file.read()
            if username not in contents:
                print("username invalid")
                continue
            if password not in contents:
                print("password invalid")
                continue
            while 1:
                print("From - ", end=" ")
                from_id = input()
                result = check(from_id)
                print(result)
                if result==0:
                    continue

                print("To - ", end=" ")
                to_id = input()
                result = check(from_id)
                print(result)
                if result==0:
                    continue

                print("Subject - ", end=" ")
                subject = input()
                if subject == '':
                    print("subject can't be empty")
                    continue
                print("Now type your Email below ")
                body = input()

                print("done")

                message = "HELO"
                byte = message.encode()
                client.send(byte)
                from_server = client.recv(4049)
                print(from_server.decode())
                message = "MAIL FROM: " + from_id
                byte = message.encode()
                client.send(byte)
                from_server = client.recv(4049)
                print(from_server.decode())
                message = "MAIL FROM: " + from_id
                byte = message.encode()
                client.send(byte)
                from_server = client.recv(4049)
                print(from_server.decode())
                message = "DATA"
                byte = message.encode()
                client.send(byte)
                from_server = client.recv(4049)
                print(from_server.decode())


                from_id = "From: " + from_id + "\n"
                byte = from_id.encode()
                client.send(byte)
                to_id = "To: " + to_id + "\n"
                byte = to_id.encode()
                client.send(byte)
                subject = "Subject: " + subject + "\n"
                byte = subject.encode()
                client.send(byte)
                string = "Received: " + str(today) + "\n"
                byte = string.encode()
                client.send(byte)
                byte = body.encode()
                client.send(byte)

                from_server = client.recv(4049)
                print(from_server.decode())
                message = "QUIT"
                byte = message.encode()
                client.send(byte)


    elif answer==3:
        exit()
    else :
        print("Please Enter Valid Option")

client.close()
