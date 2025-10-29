WireGuard VPN

Network Info
- VPN Network: 10.13.13.0/24
- Server: 10.13.13.1 (Raspberry Pi)
- Client: 10.13.13.2 (Connected device)
- Port: UDP 51820
- Endpoint: raspberry_pi_public_ipv6_address

Client Setup
- Config file: /home/rpi/files/wg-peers/peer1.conf
- QR code: /home/rpi/files/wg-peers/peer1.png
Import config or scan QR code with WireGuard app on your device.

Access Through VPN using raspberry pi private ip address 

Important Files
- Server config: /etc/wireguard/wg0.conf
- Encryption keys: /etc/wireguard/*.key
- Client configs: /home/rpi/files/wg-peers/

Router Setup (mine was IPv6 only by default)
- Forward UDP port 51820 to your Pi's IPv6 address with:
- Source ports: 1-65535
- Destination port: 51820