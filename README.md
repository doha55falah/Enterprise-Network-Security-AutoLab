# Enterprise Network Security & Automation Lab

##  Description
Ce projet simule une architecture réseau d'entreprise sécurisée et automatisée. 
Il comprend un siège principal avec plusieurs VLANs, un pare-feu OPNsense, 
et une automatisation via Python.

##  Technologies utilisées
*   **Simulation :** GNS3, VMware, VirtualBox
*   **Réseau :** Cisco IOS (c7200), VLANs, Routage Inter-VLAN, NAT
*   **Sécurité :** OPNsense (Pare-feu, NAT, VPN OpenVPN)
*   **Automatisation :** Python, Netmiko
*   **Systèmes :** Ubuntu Server, Kali Linux

##  Architecture
*   **VLAN 10 :** Utilisateurs (192.168.10.0/24)
*   **VLAN 20 :** Serveurs (192.168.20.0/24)
*   **VLAN 30 :** DMZ (192.168.30.0/24)
*   **VLAN 99 :** Administration (192.168.99.0/24)
*   Le routeur Cisco R1 fait le routage inter-VLAN et le NAT vers le pare-feu OPNsense.

##  Fonctionnalités
*   Segmentation réseau par VLANs.
*   Filtrage et NAT via OPNsense.
*   Automatisation de la récupération d'informations sur le routeur Cisco avec Python/Netmiko.

##  Structure du Dépôt
*   `/automation` : Scripts Python pour interroger et configurer le routeur Cisco.
*   `/firewall` : Captures d'écran et configurations d'OPNsense.
*   `/topology` : Schéma de l'architecture et configurations des équipements.

##  Comment exécuter l'automatisation
1. S'assurer que le routeur R1 est accessible via SSH.
2. Installer les dépendances : `pip install netmiko`
3. Lancer le script : `python3 automation/get_info.py`

##  Installation
1.  Importer la topologie dans GNS3.
2.  Configurer les VM (Ubuntu, Kali) dans VirtualBox/VMware.
3.  Lancer les scripts Python dans le dossier `automation/`.