import socket
import sys
import time
import threading
import os
import argparse

# Création du dossier de log
if not os.path.exists('/var/log/bs_server'):
    os.makedirs('/var/log/bs_server')

argparser = argparse.ArgumentParser()
argparser.add_argument("-p", "--port", help="Port d'écoute du serveur", type=int, default=13337)

args = argparser.parse_args()
port = args.port


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", port))
os.system(f"echo 'INFO : Serveur démarré sur le port {port}.'")


last_connection_time = time.time()

def check_connections():
    global last_connection_time
    while True:
        time.sleep(60)  # Attendre une minute
        if time.time() - last_connection_time > 60:
            os.system(f"echo 'WARN : Aucun client depuis plus de une minute.'")

# Démarrer le thread de vérification des connexions
threading.Thread(target=check_connections, daemon=True).start()



s.listen(1)


while True:
    conn, addr = s.accept()
    last_connection_time = time.time() 
    os.system(f"echo 'INFO : Un client {addr[0]} s'est connecté.'")
    try:
        data = conn.recv(1024)
        if not data: break
        else:
            os.system(f"echo 'INFO : Le client {addr[0]} a envoyé une opération : {data.decode()}.'")
            conn.sendall(str(eval(data.decode())).encode())
            os.system(f"echo 'INFO : Le résultat de l'opération {data.decode()} a été envoyé au client {addr[0]}.'")
    except socket.error:
        os.system(f"echo 'ERROR : Le client {addr[0]} a fermé la connexion.'")
        break

# On ferme proprement la connexion TCP
conn.close()
