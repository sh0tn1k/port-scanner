from scapy.layers.inet import ICMP, IP, TCP, sr1
import socket
from datetime import datetime

start = datetime.now()
# Здесь проверяется, в сети ли сервер
def icmp_probe(ip):
    icmp_packet = IP(dst=ip) / ICMP()
    # Отправка и прием одного пакета
    resp_packet = sr1(icmp_packet, timeout=10)
    return resp_packet is not None

def scan(ip, ports):
    # Проходимся по каждому порту
    for port in ports:
        # Флаг S означает SYN-пакет
        syn_packet = IP(dst=ip) / TCP(dport=port, flags="S")
        # Время ожидания пакета можно ставить свое
        resp_packet = sr1(syn_packet, timeout=10)
        if resp_packet is not None:
            if resp_packet.getlayer('TCP').flags & 0x12 != 0:
                print(f"{ip}:{port} is open/{resp_packet.sprintf('%TCP.sport%')}")
ends = datetime.now()

def main():
    name = input("Hostname / IP Address: ")
    # Узнаем IP цели
    ip = socket.gethostbyname(name)
    # Обозначаем порты для сканирования
    ports = [20, 21, 22, 23, 25, 43, 53, 80,
             115, 123, 143, 161, 179, 443, 445,
             514, 515, 993, 995, 1080, 1194,
             1433, 1723, 3128, 3268, 3306, 3389,
             5432, 5060, 5900, 8080, 8888, 10000]
    # Перехватываем исключения в момент, когда заканчивается кортеж
    try:
        # Если не удалось подключиться к серверу, выводим ошибку
        try:
          if icmp_probe(ip):
              syn_ack_packet = scan(ip, ports)
              syn_ack_packet.show()
          else:
              print("Failed to send ICMP packet")
        except Exception:
            print("Please run script as root")
    except AttributeError:
        print("Scan completed!")
        print("<Time:{}>".format(ends - start))

if __name__ == "__main__":
    main()