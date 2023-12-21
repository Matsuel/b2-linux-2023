# I. Init

- [I. Init](#i-init)
  - [1. Installation de Docker](#1-installation-de-docker)
  - [2. Vérifier que Docker est bien là](#2-vérifier-que-docker-est-bien-là)
  - [3. sudo c pa bo](#3-sudo-c-pa-bo)
  - [4. Un premier conteneur en vif](#4-un-premier-conteneur-en-vif)
  - [5. Un deuxième conteneur en vif](#5-un-deuxième-conteneur-en-vif)

## 1. Installation de Docker

Pour installer Docker, il faut **toujours** (comme d'hab en fait) se référer à la doc officielle.

**Je vous laisse donc suivre les instructions de la doc officielle pour installer Docker dans la VM.**

> ***Il n'y a pas d'instructions spécifiques pour Rocky dans la doc officielle**, mais rocky est très proche de CentOS. Vous pouvez donc suivre les instructions pour CentOS 9.*

## 2. Vérifier que Docker est bien là

```bash
# est-ce que le service Docker existe ?
systemctl status docker

# si oui, on le démarre alors
sudo systemctl start docker

# voyons si on peut taper une commande docker
sudo docker info
sudo docker ps
```

## 3. sudo c pa bo

On va faire en sorte que vous puissiez taper des commandes `docker` sans avoir besoin des droits `root`, et donc de `sudo`.

Pour ça il suffit d'ajouter votre utilisateur au groupe `docker`.

> ***Pour que le changement de groupe prenne effet, il faut vous déconnecter/reconnecter de la session SSH** (pas besoin de reboot la machine, pitié).*

🌞 **Ajouter votre utilisateur au groupe `docker`**

```bash
[mat@tp1 ~]$ sudo usermod -aG docker mat
```

- vérifier que vous pouvez taper des commandes `docker` comme `docker ps` sans avoir besoin des droits `root`

```bash
[mat@tp1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES


[mat@tp1 ~]$ docker | head -n 1

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers
```

➜ Vous pouvez même faire un `alias` pour `docker`

Genre si tu trouves que taper `docker` c'est long, et tu préférerais taper `dk` tu peux faire : `alias dk='docker'`. Si tu écris cette commande dans ton fichier `~/.bashrc` alors ce sera effectif dans n'importe quel `bash` que tu ouvriras plutar.

```bash
[mat@tp1 ~]$ alias dk=docker
[mat@tp1 ~]$ dk

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers
```

## 4. Un premier conteneur en vif

> *Je rappelle qu'un "conteneur" c'est juste un mot fashion pour dire qu'on lance un processus un peu isolé sur la machine.*

Bon trève de blabla, on va lancer un truc qui juste marche.

On va lancer un conteneur NGINX qui juste fonctionne, puis custom un peu sa conf. Ce serait par exemple pour tester une conf NGINX, ou faire tourner un serveur NGINX de production.

> *Hé les dévs, **jouez le jeu bordel**. NGINX c'est pas votre pote OK, mais on s'en fout, c'est une app comme toutes les autres, comme ta chatroom ou ta calculette. Ou Netflix ou LoL ou Spotify ou un malware. NGINX il est réputé et standard, c'est juste un outil d'étude pour nous là. Faut bien que je vous fasse lancer un truc. C'est du HTTP, c'est full standard, vous le connaissez, et c'est facile à tester/consommer : avec un navigateur.*

🌞 **Lancer un conteneur NGINX**

- avec la commande suivante :

```bash
[mat@tp1 ~]$ docker run -d -p 9999:80 nginx
bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db
```

> Si tu mets pas le `-d` tu vas perdre la main dans ton terminal, et tu auras les logs du conteneur directement dans le terminal. `-d` comme *daemon* : pour lancer en tâche de fond. Essaie pour voir !

🌞 **Visitons**

- vérifier que le conteneur est actif avec une commande qui liste les conteneurs en cours de fonctionnement

```bash
[mat@tp1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS         PORTS                                   NAMES
bd9ac2727525   nginx     "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes   0.0.0.0:9999->80/tcp, :::9999->80/tcp   nervous_raman
```

- afficher les logs du conteneur

```bash
[mat@tp1 ~]$ docker logs bd9ac2727525
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2023/12/21 09:57:10 [notice] 1#1: using the "epoll" event method
2023/12/21 09:57:10 [notice] 1#1: nginx/1.25.3
2023/12/21 09:57:10 [notice] 1#1: built by gcc 12.2.0 (Debian 12.2.0-14)
2023/12/21 09:57:10 [notice] 1#1: OS: Linux 5.14.0-284.30.1.el9_2.x86_64
2023/12/21 09:57:10 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 1073741816:1073741816
2023/12/21 09:57:10 [notice] 1#1: start worker processes
2023/12/21 09:57:10 [notice] 1#1: start worker process 29
2023/12/21 09:57:10 [notice] 1#1: start worker process 30
```

- afficher toutes les informations relatives au conteneur avec une commande `docker inspect`

<details>
<summary>Détails</summary>

```bash
[mat@tp1 ~]$ docker inspect bd9ac2727525
[
    {
        "Id": "bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db",
        "Created": "2023-12-21T09:57:09.850759597Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1828,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-12-21T09:57:10.419258073Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:d453dd892d9357f3559b967478ae9cbc417b52de66b53142f6c16c8a275486b9",
        "ResolvConfPath": "/var/lib/docker/containers/bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db/hostname",
        "HostsPath": "/var/lib/docker/containers/bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db/hosts",
        "LogPath": "/var/lib/docker/containers/bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db/bd9ac27275254042cab075ccbeab1e66849a0b9485bcca1226831339b55db6db-json.log",
        "Name": "/nervous_raman",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "80/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "9999"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                63,
                117
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/0b0775697e4db118d1fe0fc4f7f53e00e0bd2f5c8f561e845db7f5b537642675-init/diff:/var/lib/docker/overlay2/95f81120cc028b539ec78a711ff096649570e9c884e894087a6d0a4482f0a880/diff:/var/lib/docker/overlay2/66b293e3189248ff13170db07a37189c7e917c60f8840bd5a4e72010eac33ead/diff:/var/lib/docker/overlay2/bafac2c9476c4c6e8f3c37f7df06dff455fcc3045c3a0c3b08e1eec6a49ee7ec/diff:/var/lib/docker/overlay2/a3e91fba52901d43bb0f050374f0b6c88778910e96093bc12a39a20463a9b896/diff:/var/lib/docker/overlay2/af6cde245b9c58f142097e4a122e1d3bfe14a86fd473d2890cf0a24a3974d960/diff:/var/lib/docker/overlay2/9f23eb4a34543c59b0a8eb57797ffebbb7b1b36d11f83f8dfdf18a579e42c01a/diff:/var/lib/docker/overlay2/270d1f9775a54ea19f69f8772a36805c0d7c719ab34c6a82da1cbd876f0b2195/diff",
                "MergedDir": "/var/lib/docker/overlay2/0b0775697e4db118d1fe0fc4f7f53e00e0bd2f5c8f561e845db7f5b537642675/merged",
                "UpperDir": "/var/lib/docker/overlay2/0b0775697e4db118d1fe0fc4f7f53e00e0bd2f5c8f561e845db7f5b537642675/diff",
                "WorkDir": "/var/lib/docker/overlay2/0b0775697e4db118d1fe0fc4f7f53e00e0bd2f5c8f561e845db7f5b537642675/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "bd9ac2727525",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "80/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "NGINX_VERSION=1.25.3",
                "NJS_VERSION=0.8.2",
                "PKG_RELEASE=1~bookworm"
            ],
            "Cmd": [
                "nginx",
                "-g",
                "daemon off;"
            ],
            "Image": "nginx",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": [
                "/docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {
                "maintainer": "NGINX Docker Maintainers <docker-maint@nginx.com>"
            },
            "StopSignal": "SIGQUIT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "89cbe70acdfeec2bf1b03e91e1afc311afd14cc9d346c2a931b340e6ef8ca738",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "80/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "9999"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "9999"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/89cbe70acdfe",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "7a7bca7af0c65fd82421ed8d31759791ca5e4749a269645b39a312f071f6a4a0",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "241c051e8d0d70782855eab7dcf7eb50dde5249fb3418c091720f3021142701b",
                    "EndpointID": "7a7bca7af0c65fd82421ed8d31759791ca5e4749a269645b39a312f071f6a4a0",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```
</details>

- afficher le port en écoute sur la VM avec un `sudo ss -lnpt`

```bash
[mat@tp1 ~]$ sudo ss -lnpt | grep 9999
LISTEN 0      4096         0.0.0.0:9999      0.0.0.0:*    users:(("docker-proxy",pid=1783,fd=4))
LISTEN 0      4096            [::]:9999         [::]:*    users:(("docker-proxy",pid=1789,fd=4))
```

- ouvrir le port `9999/tcp` (vu dans le `ss` au dessus normalement) dans le firewall de la VM

```bash
[mat@tp1 ~]$ sudo firewall-cmd --add-port=9999/tcp --permanent
success
[mat@tp1 ~]$ sudo firewall-cmd --reload
success
[mat@tp1 ~]$ sudo firewall-cmd --list-all | grep 9999
  ports: 9999/tcp
```

- depuis le navigateur de votre PC, visiter le site web sur `http://IP_VM:9999`


```bash
C:\Users\User>curl 10.1.4.2:9999
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

➜ On peut préciser genre mille options au lancement d'un conteneur, **go `docker run --help` pour voir !**

➜ Hop, on en profite pour voir un truc super utile avec Docker : le **partage de fichiers au moment où on `docker run`**

- en effet, il est possible de partager un fichier ou un dossier avec un conteneur, au moment où on le lance
- avec NGINX par exemple, c'est idéal pour déposer un fichier de conf différent à chaque conteneur NGINX qu'on lance
  - en plus NGINX inclut par défaut tous les fichiers dans `/etc/nginx/conf.d/*.conf`
  - donc suffit juste de drop un fichier là-bas
- ça se fait avec `-v` pour *volume* (on appelle ça "monter un volume")

> *C'est aussi idéal pour créer un conteneur qui setup un environnement de dév par exemple. On prépare une image qui contient Python + les libs Python qu'on a besoin, et au moment du `docker run` on partage notre code. Ainsi, on peut dév sur notre PC, et le code s'exécute dans le conteneur. On verra ça plus tard les dévs !*

🌞 **On va ajouter un site Web au conteneur NGINX**

- créez un dossier `nginx`
  - pas n'importe où, c'est ta conf caca, c'est dans ton homedir donc `/home/<TON_USER>/nginx/`
- dedans, deux fichiers : `index.html` (un site nul) `site_nul.conf` (la conf NGINX de notre site nul)
- exemple de `index.html` :

```html
<h1>MEOOOW</h1>
```

- config NGINX minimale pour servir un nouveau site web dans `site_nul.conf` :

```nginx
server {
    listen        8080;

    location / {
        root /var/www/html/;
    }
}
```

- lancez le conteneur avec la commande en dessous, notez que :
  - on partage désormais le port 8080 du conteneur (puisqu'on l'indique dans la conf qu'il doit écouter sur le port 8080)
  - on précise les chemins des fichiers en entier
  - note la syntaxe du `-v` : à gauche le fichier à partager depuis ta machine, à droite l'endroit où le déposer dans le conteneur, séparés par le caractère `:`
  - c'est long putain comme commande

```bash
[mat@tp1 ~]$ docker run -d -p 9999:8080 -v /home/mat/nginx/index.html:/var/www/html/index.html -v /home/mat/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
ddd9aac0e0cc7399731f59936626b846fc9ff39e78b7441de48a696be1031d38
```

🌞 **Visitons**

- vérifier que le conteneur est actif

```bash
[mat@tp1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                               NAMES
ddd9aac0e0cc   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   sharp_poitras
```

- aucun port firewall à ouvrir : on écoute toujours port 9999 sur la machine hôte (la VM)
- visiter le site web depuis votre PC

```bash
C:\Users\User>curl 10.1.4.2:9999
<!DOCTYPE html>

<html lang="en">

<head>
        <meta charset="utf-8"/>

        <title>Your Page Title</title>
</head>

<body>

        <h1>MEOOOW</h1>
</body>
</html>
```

## 5. Un deuxième conteneur en vif

Cette fois on va lancer un conteneur Python, comme si on voulait tester une nouvelle lib Python par exemple. Mais sans installer ni Python ni la lib sur notre machine.

On va donc le lancer de façon interactive : on lance le conteneur, et on pop tout de suite un shell dedans pour faire joujou.

🌞 **Lance un conteneur Python, avec un shell**

- il faut indiquer au conteneur qu'on veut lancer un shell
- un shell c'est "interactif" : on saisit des trucs (input) et ça nous affiche des trucs (output)
  - il faut le préciser dans la commande `docker run` avec `-it`
- ça donne donc :

```bash
[mat@tp1 ~]$ docker run -it python bash
Unable to find image 'python:latest' locally
latest: Pulling from library/python
bc0734b949dc: Pull complete
b5de22c0f5cd: Pull complete
917ee5330e73: Pull complete
b43bd898d5fb: Pull complete
7fad4bffde24: Pull complete
d685eb68699f: Pull complete
107007f161d0: Pull complete
02b85463d724: Pull complete
Digest: sha256:3733015cdd1bd7d9a0b9fe21a925b608de82131aa4f3d397e465a1fcb545d36f
Status: Downloaded newer image for python:latest
```

> *Ce conteneur ne vit (comme tu l'as demandé) que pour exécuter ton `bash`. Autrement dit, si ce `bash` se termine, alors le conteneur s'éteindra. Autrement diiiit, si tu quittes le `bash`, le processus `bash` va se terminer, et le conteneur s'éteindra. C'est vraiment un conteneur one-shot quoi quand on utilise `docker run` comme ça.*

🌞 **Installe des libs Python**

- une fois que vous avez lancé le conteneur, et que vous êtes dedans avec `bash`
- installez deux libs, elles ont été choisies complètement au hasard (avec la commande `pip install`):
  - `aiohttp`
  - `aioconsole`
- tapez la commande `python` pour ouvrir un interpréteur Python
- taper la ligne `import aiohttp` pour vérifier que vous avez bien téléchargé la lib

```bash
root@47a457260e94:/# python
Python 3.12.1 (main, Dec 19 2023, 20:14:15) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
>>>
```

> *Notez que la commande `pip` est déjà présente. En effet, c'est un conteneur `python`, donc les mecs qui l'ont construit ont fourni la commande `pip` avec !*

➜ **Tant que t'as un shell dans un conteneur**, tu peux en profiter pour te balader. Tu peux notamment remarquer :

- si tu fais des `ls` un peu partout, que le conteneur a sa propre arborescence de fichiers
- si t'essaies d'utiliser des commandes usuelles un poil évoluées, elles sont pas là
  - genre t'as pas `ip a` ou ce genre de trucs
  - un conteneur on essaie de le rendre le plus léger possible
  - donc on enlève tout ce qui n'est pas nécessaire par rapport à un vrai OS
  - juste une application et ses dépendances