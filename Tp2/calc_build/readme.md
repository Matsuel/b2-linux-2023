# Commande pour lancer l'app calculatrice python:

## Build de l'image
```bash
PS C:\Users\User\Documents\b2-linux-2023\Tp2\calc_build> docker compose build
[+] Building 0.9s (8/8) FINISHED                                                                             docker:default
 => [calculatrice internal] load build definition from Dockerfile                                                      0.0s
 => => transferring dockerfile: 223B                                                                                   0.0s
 => [calculatrice internal] load .dockerignore                                                                         0.0s
 => => transferring context: 2B                                                                                        0.0s 24e56b4db
 => [calculatrice internal] load metadata for docker.io/library/python:3.12                                            0.8s
 => [calculatrice 1/3] FROM docker.io/library/python:3.12@sha256:3733015cdd1bd7d9a0b9fe21a925b608de82131aa4f3d397e465  0.0s 24e56b4db
 => [calculatrice internal] load build context                                                                         0.0s
 => => transferring context: 29B                                                                                       0.0s 24e56b4db
 => CACHED [calculatrice 2/3] WORKDIR /calc                                                                            0.0s
 => CACHED [calculatrice 3/3] COPY calc.py .                                                                           0.0s 24e56b4db
 => [calculatrice] exporting to image                                                                                  0.0s
 => => exporting layers                                                                                                0.0s 24e56b4db
 => => writing image sha256:4fa74226d3f00ce6d5b8fcaef24254b8f5e02599b2e3925f987ccf112403c2b3                           0.0s
 => => naming to docker.io/library/calc:latest                                                                         0.0s 24e56b4db
```

# Création d'un conteneur
```bash
PS C:\Users\User\Documents\b2-linux-2023\Tp2\calc_build> docker run -e CALC_PORT=9854 -d calc 
93978d74cb2218502aaa116cd54dcb77a494488162066780fd5c20ae16c981fe      
```

**CALC_PORT est une variable d'environnement on peut lui donner la valeur souhaitée**

## Consultation des logs
```bash
PS C:\Users\User\Documents\b2-linux-2023\Tp2\calc_build> docker logs 93978d74cb2218502aaa116cd54dcb77a494488162066780fd5c20ae16c981fe
INFO : Serveur démarré sur le port 9854.
```