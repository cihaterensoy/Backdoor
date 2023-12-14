import socket

my_listener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bu listenerı kullanarak devamlı bağlantı yapacağımızı belirtmeliyiz bunuda şöyle yapıyoruz;
my_listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #birden fazla kullanılmasını sağlıyor bu işlem

my_listener.bind(("192.168.64.4",8080))#dinleyeceğimiz cihazın ip adresi ve portumuzu yazıyoruz
my_listener.listen(0)#dinlemeye başlıyoruz, içersine kaç tane bağlantı gelirse belli biyerden sonra bu bağlantıları almak istemezsem diye bir parametre verebiliyorum
#0 verirsem böyle bir sınırlama olmaz
print("Listening...")
my_listener.accept()#bağlantımızı kabul etmek icin bunu yazıyoruz
print("Connection OK")