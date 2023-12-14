import socket

#socket instancesi oluşturuyoruz
#ağ ailesini ve hangi yolla transfer edeceğimiz
my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_connection.connect(("192.168.64.4",8080))#ip adresini ve portu tuple olarak vereceğiz

my_connection.send(("Connection OK").encode("utf-8"))