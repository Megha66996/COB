##N.Meghana Phase-2 Task 2

import socket
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


host = '127.0.0.1'
port = 5000


server_socket.bind((host, port))

server_socket.listen()


connections = []


def broadcast(message):
    for connection in connections:
        connection.send(message)


def handle_connection(connection, address):
    while True:
        try:
            message = connection.recv(1024)
            broadcast(message)
        except:
            connections.remove(connection)
            connection.close()
            break


def accept_connections():
    while True:
        connection, address = server_socket.accept()
        connections.append(connection)
        print(f"Connected to {address}")
        thread = threading.Thread(target=handle_connection, args=(connection, address))
        thread.start()


accept_connections()