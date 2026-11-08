Configuration du Pare-feu OPNsense (HQ) :

- Rôle : Passerelle Internet et Pare-feu principal.
- WAN : Connecté au NAT de VMware.
- LAN : Connecté au réseau VMnet1 (IP 192.168.19.2).
- Règles configurées : Autorisation du LAN vers Internet (NAT sortant).
- VPN : Serveur OpenVPN configuré (Road Warrior) avec authentification par certificats.