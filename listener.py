# -*- coding: utf-8 -*-
import socket

my_listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bu listenerı kullanarak devamlı bağlantı yapacağımızı belirtmeliyiz bunuda şöyle yapıyoruz
my_listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# birden fazla kullanılmasını sağlıyor bu işlem

my_listener.bind(("192.168.64.4", 8080))
# dinleyeceğimiz cihazın ip adresi ve portumuzu yazıyoruz
my_listener.listen(0)
# dinlemeye başlıyoruz, içersine kaç tane bağlantı gelirse belli biyerden sonra bu bağlantıları almak istemezsem diye bir parametre verebiliyorum
# 0 verirsem böyle bir sınırlama olmaz
print("Listening...")
(my_connection, my_address) = my_listener.accept()
# bağlantımızı kabul etmek icin bunu yazıyoruz
# .accept bize iki elemanlı bir tuple döndürüyor
# my_connection değişkeni MySockettekiyle aynı işlevi görüyor gibi düşünebiliriz
# bağlantı olduktan sonra açılan bağlantı my_connectiondur
# my_address'te bağlantı olduktan sonra hangi ip adresine bağlandıysak onu döndürür

print("Connection OK " + str(my_address))

# komutumuzu my_connection.send() yazarak yollayabiliriz
# bunun icin sürekli çalışan  bir mekanizmamız olması gerkeiyor


while True:
    # kullanıcı inputu almamız gerkeiyor
    # şimdilik komutumuzu python2 ile alacağız
    command_input = raw_input("Enter Command: ")  # komutu kullanıcıdan alıyoruz
    my_connection.send(command_input)  # komutu yolluyoruz
    # cevap gelince okuyacak kısım
    command_output = my_connection.recv(1024)  # gelen veri 1024byte olacak
    print(command_output)
