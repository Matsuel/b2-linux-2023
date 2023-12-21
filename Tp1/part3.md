# III. Docker compose

Pour la fin de ce TP on va manipuler un peu `docker compose`.

🌞 **Créez un fichier `docker-compose.yml`**

- dans un nouveau dossier dédié `/home/<USER>/compose_test`
- le contenu est le suivant :

```yml
version: "3"

services:
  conteneur_nul:
    image: debian
    entrypoint: sleep 9999
  conteneur_flopesque:
    image: debian
    entrypoint: sleep 9999
```

Ce fichier est parfaitement équivalent à l'enchaînement de commandes suivantes (*ne les faites pas hein*, c'est juste pour expliquer) :

```bash
$ docker network create compose_test
$ docker run --name conteneur_nul --network compose_test debian sleep 9999
$ docker run --name conteneur_flopesque --network compose_test debian sleep 9999
```

🌞 **Lancez les deux conteneurs** avec `docker compose`

- déplacez-vous dans le dossier `compose_test` qui contient le fichier `docker-compose.yml`
- go exécuter `docker compose up -d`

```bash
[mat@tp1 ~]$ docker compose up -d
[+] Running 3/3
 ✔ conteneur_nul Pulled                                                                                         5.3s
 ✔ conteneur_flopesque 1 layers [⣿]      0B/0B      Pulled                                                      5.3s
   ✔ bc0734b949dc Already exists                                                                                0.0s
[+] Running 3/3
 ✔ Network mat_default                  Created                                                             0.3s
 ✔ Container mat-conteneur_nul-1        Started                                                             0.1s
 ✔ Container mat-conteneur_flopesque-1  Started                                                             0.1s
```

🌞 **Vérifier que les deux conteneurs tournent**

- toujours avec une commande `docker`
- tu peux aussi use des trucs comme `docker compose ps` ou `docker compose top` qui sont cools dukoo
  - `docker compose --help` pour voir les bails

```bash
[mat@tp1 ~]$ docker compose ps
NAME                            IMAGE     COMMAND        SERVICE               CREATED              STATUS              PORTS
mat-conteneur_flopesque-1   debian    "sleep 9999"   conteneur_flopesque   About a minute ago   Up About a minute
mat-conteneur_nul-1         debian    "sleep 9999"   conteneur_nul         About a minute ago   Up About a minute
[mat@tp1 ~]$ docker compose top
mat-conteneur_flopesque-1
UID    PID    PPID   C    STIME   TTY   TIME       CMD
root   9676   9644   0    12:14   ?     00:00:00   sleep 9999

mat-conteneur_nul-1
UID    PID    PPID   C    STIME   TTY   TIME       CMD
root   9677   9628   0    12:14   ?     00:00:00   sleep 9999
```

🌞 **Pop un shell dans le conteneur `conteneur_nul`**

- référez-vous au mémo Docker
- effectuez un `ping conteneur_flopesque` (ouais ouais, avec ce nom là)
  - un conteneur est aussi léger que possible, aucun programme/fichier superflu : t'auras pas la commande `ping` !
  - il faudra installer un paquet qui fournit la commande `ping` pour pouvoir tester
  - juste pour te faire remarquer que les conteneurs ont pas besoin de connaître leurs IP : les noms fonctionnent

```bash
[mat@tp1 ~]$ docker exec -it mat-conteneur_nul-1 bash
```

```bash
root@6b2717f63b65:/# apt update
root@6b2717f63b65:/# apt install iputils-ping
```

```bash
root@6b2717f63b65:/# ping conteneur_flopesque -c 6
PING conteneur_flopesque (172.18.0.2) 56(84) bytes of data.
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=1 ttl=64 time=0.034 ms
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=2 ttl=64 time=0.064 ms
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=3 ttl=64 time=0.058 ms
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=4 ttl=64 time=0.060 ms
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=5 ttl=64 time=0.060 ms
64 bytes from 6b2717f63b65 (172.18.0.2): icmp_seq=6 ttl=64 time=0.059 ms

--- conteneur_flopesque ping statistics ---
6 packets transmitted, 6 received, 0% packet loss, time 5116ms
rtt min/avg/max/mdev = 0.034/0.055/0.064/0.009 ms
```