import scapy.all as sc

def scan(ip):
    arp_req = sc.ARP(pdst=ip)
    broadcast = sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered = sc.srp(arp_req_broadcast, timeout=1, verbose=False)[0]

    for sent, received in answered:
        print(f"IP: {received.psrc}, MAC: {received.hwsrc}")

scan("192.168.1.1/24")
