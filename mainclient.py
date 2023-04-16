import socket
import pickle

HOST="127.0.0.1"
PORT=555
HEADERLEN=20



s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    
    msgdataName=s.recv(1024)
    msgdataSurname=s.recv(1024)

    print(msgdataName.decode("utf-8"))
    print(msgdataSurname.decode("utf-8"))

    Name=input("Enter your name: ")
    Surname=input("Enter your surname: ")

    #send name and surname
    s.send(bytes(Name,"utf-8"))
    s.send(bytes(Surname,"utf-8"))

    #greetings part
    greetings=s.recv(1024)
    print(greetings.decode("utf-8"))
    
    while True:
        #printing options part
        optionArray=s.recv(1024)
        myOptionArray=pickle.loads(optionArray)
        for i in myOptionArray:
            print(i)

        #operation selection part
        operationSelection=input("Enter your operation: ")
        s.send(bytes(operationSelection,"utf-8"))

        operationInfo=s.recv(1024)
        print(operationInfo.decode("utf-8"))

        if operationSelection == "quit":
            print("See you later alligator")
            break
    break
