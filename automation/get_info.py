from netmiko import ConnectHandler
from devices import R1

def get_router_info(device):
    print(f"Connexion à {device['host']}...")
    try:
        net_connect = ConnectHandler(**device)
        hostname = net_connect.find_prompt().strip('#>')
        print(f"✅ Connecté à {hostname}")
        
        # Récupérer la version
        version = net_connect.send_command('show version | include Version')
        print(f"Version: {version.strip()}")
        
        # Récupérer l'état des interfaces
        interfaces = net_connect.send_command('show ip interface brief')
        print("\n--- Interfaces ---")
        print(interfaces)
        
        # Fermeture propre
        if hasattr(net_connect, 'disconnect'):
            net_connect.disconnect()
        return True
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False

if __name__ == "__main__":
    get_router_info(R1)