#written with pyhton
import socket #need for creating socket object
from datetime import datetime as datetime # needed for geting time and date 
import datetime as dt
import pickle#needed for sending array to client

HOST = "127.0.0.1"
PORT = 555




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creating socket object
s.bind((HOST, PORT))#binding host and port to socket object
s.listen()#listening for connections

#these are my functions
def printCapOfTurkey(conn):
    answer = "Capital city of Turkey is Ankara"
    return conn.send(bytes(answer, "utf-8"))


def currentDate(conn):
    current_Date = dt.date.today().strftime('%d-%m-%Y')
    return conn.send(current_Date.encode("utf-8"))

def currentTime(conn):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return conn.send(current_time.encode("utf-8"))
#and fucntion is my main function which is used for selecting operation
def selection(decodedOperationSelection,conn):
    if decodedOperationSelection == "date":
        print("Current date is sended")
        currentDate(conn)
    elif decodedOperationSelection == "time":
        print("Current time is sended")
        currentTime(conn)
    elif decodedOperationSelection == "capTurkey":
        print("Capital city of Turkey is sended")
        printCapOfTurkey(conn)
    elif decodedOperationSelection == "quit":
        conn.send(bytes("See you later alligator ", "utf-8"))
        return conn.close()
    else:
        print("Please enter a valid string")




while True:
    conn, addr = s.accept()#creating connection object and address object

    print("Hello from server. server is ready to get your name and password")

    conn.send(bytes("Please enter your name", "utf-8"))#to get input from client's name and password
    conn.send(bytes("Please enter your password", "utf-8"))

    dataName = conn.recv(1024)#this is for getting name and password from client
    dataSurname = conn.recv(1024)

    name = dataName.decode("utf-8")#decoding name and password
    surname = dataSurname.decode("utf-8")

    
    arrOperations = ["date", "time", "capTurkey", "quit"]#these are my operations for client
    sendArrOprerations= pickle.dumps(arrOperations)#sending array to client
    
    
    
    if name == "cmpe322" and surname == "bilgiuni":#required name and password
        conn.send(bytes(f"Welcome to the server {name}. Which operation do you want to use here is your options:  ", "utf-8"))#send welcome message to client and type client's name
        print(f"{addr} has connected to the server")#type client's address
        while True:#this is for client's operations
            
            conn.sendall(sendArrOprerations)
            operationSelection = conn.recv(1024)
            decodedOperationSelection = operationSelection.decode("utf-8")
            selection(decodedOperationSelection, conn)
            if decodedOperationSelection == "quit":
                print("client send a quit message")
                break
        break    
    else:
        conn.send(bytes("Wrong name", "utf-8"))#if client's name and password is wrong send wrong message to client
        break
        
    