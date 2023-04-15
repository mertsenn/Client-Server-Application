import socket
from datetime import datetime as datetime
import datetime as dt
import pickle

HOST = "127.0.0.1"
PORT = 555

HEADERSIZE = 20



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()


def printCapOfTurkey(conn):
    answer = "Capital city of Turkey is Gaziosmanpasa"
    return conn.send(bytes(answer, "utf-8"))


def quit(conn):
    sendOff = "See you later alligator"
    conn.close()
    return conn.send(bytes(sendOff, "utf-8"))
    


def currentDate(conn):
    current_Date = dt.date.today().strftime('%d-%m-%Y')
    print(current_Date)
    return conn.send(current_Date.encode("utf-8"))


def currentTime(conn):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return conn.send(current_time.encode("utf-8"))


def selection(decodedOperationSelection,conn):
    if decodedOperationSelection == "date":
        currentDate(conn)
    elif decodedOperationSelection == "time":
        currentTime(conn)
    elif decodedOperationSelection == "capTurkey":
        printCapOfTurkey(conn)
    elif decodedOperationSelection == "quit":
        return quit(conn)
    else:
        print("Please enter a valid string")





while True:
    conn, addr = s.accept()

    conn.send(bytes("Please enter your name", "utf-8"))
    conn.send(bytes("Please enter your password", "utf-8"))

    dataName = conn.recv(1024)
    dataSurname = conn.recv(1024)

    name = dataName.decode("utf-8")
    surname = dataSurname.decode("utf-8")

    
    arrOperations = ["date", "time", "capTurkey", "quit"]
    sendArrOprerations= pickle.dumps(arrOperations)
    


    while True:
        if name == "1" and surname == "1":
            conn.send(bytes(f"Welcome to the server {name}. Which operation do you want to use here is your options:  ", "utf-8"))
            print(f"{addr} has connected to the server")
            while True:
                print("I am in while loop")
                conn.sendall(sendArrOprerations)
                operationSelection = conn.recv(1024)
                decodedOperationSelection = operationSelection.decode("utf-8")
                selection(decodedOperationSelection, conn)
        else:
            conn.send(bytes("Wrong name", "utf-8"))
            break
    break
