import sys
from scapy.all import srp, sr1, Ether, ARP, conf, IP, ICMP, TCP, ls

if len(sys.argv) != 2:
    print("Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24")
    sys.exit(1)

conf.verb = 0

ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=sys.argv[1]), timeout=2)

for snd, rcv in ans:
    mac = rcv.hwsrc
    ip = rcv.psrc

    packet = IP(dst=ip)/TCP(flags="S")

    ans = sr1(packet)

    if ans is None:
        continue

    ans.show()