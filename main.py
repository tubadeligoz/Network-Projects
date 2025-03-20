import socket
def port_tarayici(hedef_ip,baslangic_port,bitis_port):
    print(f"{hedef_ip}adresindeki portlar taranıyor...")
    for port in range (baslangic_port,bitis_port+1):
        soket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        soket.settimeout(0.5)
        
        try:
            sonuc=soket.connect_ex((hedef_ip,port))
            if sonuc==0:
                print(f"Port {port}:AÇIK")
                soket.close()
        except Exception as e:
            print(f"Port{port}: HATA-{e}")
                    
if __name__ == "__main__":
    hedef_ip=input("Hedef IP adresini girin:")
    baslangic_port=int(input("Başlangıç port numarasını girin:"))
    bitis_port=int(input("Bitiş port numarasını girin:"))
    port_tarayici(hedef_ip,baslangic_port,bitis_port)