import socket

HOST = '192.168.18.222'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #af_inet == ipv4, sock_stram == port
s.connect((HOST, PORT))

