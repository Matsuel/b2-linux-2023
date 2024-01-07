# Commandes pour build et lancer le conteneur

## Build

```bash
PS C:\Users\User\Documents\b2-linux-2023\Tp2\chat> docker compose build
[+] Building 0.7s (8/8) FINISHED                                                                                                                                                                                                                      docker:default
 => [chat-py internal] load .dockerignore                                                                                                                                                                                                                       0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                 0.0s
 => [chat-py internal] load build definition from Dockerfile                                                                                                                                                                                                    0.0s
 => => transferring dockerfile: 206B                                                                                                                                                                                                                            0.0s
 => [chat-py internal] load metadata for docker.io/library/python:3.12                                                                                                                                                                                          0.5s
 => [chat-py 1/3] FROM docker.io/library/python:3.12@sha256:3733015cdd1bd7d9a0b9fe21a925b608de82131aa4f3d397e465a1fcb545d36f                                                                                                                                    0.0s
 => [chat-py internal] load build context                                                                                                                                                                                                                       0.0s
 => => transferring context: 29B                                                                                                                                                                                                                                0.0s
 => CACHED [chat-py 2/3] WORKDIR /chat                                                                                                                                                                                                                          0.0s
 => CACHED [chat-py 3/3] COPY chat.py .                                                                                                                                                                                                                         0.0s
 => [chat-py] exporting to image                                                                                                                                                                                                                                0.0s
 => => exporting layers                                                                                                                                                                                                                                         0.0s
 => => writing image sha256:32a2baa67eeff5fc74d90985e0f36f4ea3c7bca5216b0c969aa064137997981f                                                                                                                                                                    0.0s
 => => naming to docker.io/library/chat:latest                                                                                                                                                                                                                  0.0s
```

## Lancer un conteneur

```bash
PS C:\Users\User\Documents\b2-linux-2023\Tp2\chat>  docker run -e CHAT_PORT=30001 -e MAX_USERS=100 -d chat
2a04ae1c8633a080ff2e7a0f8553d1bf31098b4a2943cb8b1736dda0dd921a53
```

**Il peut etre nécessaire de modifier dans docker-compose.yml la valeur du port du contener en fonction du port ce lequel vous souhaitez le lancer**

```yml
ports:
      - "port-votre-machine:port-du-conteneur"
```