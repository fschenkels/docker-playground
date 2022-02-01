# docker-playground
Free area to test whatever you want to

## Current state of the `main` branch
There are 4 services in the `main` branch:
* nginx
* ubuntu1 (container `my-ubuntu`)
* ubuntu2
* httpbin (container `local-httpbin`)

The containers `nginx`, `ubuntu1` and `ubuntu2` are connected through the network `common`. However, the container `local-httpbin` is only connected to the container `ubuntu2` through the `separate` network. Just like in the following diagram:
```
            +-----------+
            |   NGINX   |
            +-----.-----+
                  | ,common network
                  |/                     ,separate network
+-----------+     |     +-----------+   /       +-----------+
|  ubuntu1  |-----+-----|  ubuntu2  |-----------|  local-   |
+-----------+           +-----------+           |  httpbin  |
                                                +-----------+
```
The `local-httpbin` is only reachable from the `ubuntu2` container.

Besides that, when you try to access the `httpbin.org` from the containers `nginx` and `ubuntu1` your request goes to the official's `httpbin` website. However, when you try to do this from the `ubuntu2` container your request goes to the `local-httpbin` container instead (because the `local-httpbin` container defines a label inside the `separate` network).

## Tips and Tricks
* When you run `docker-compose exec` you must specify the service name, not the container name. Like in `docker-compose exec ubuntu1 /bin/bash`.
* When you run `docker exec` you must specify the container name. Like in `docker exec -i -t my-ubuntu /bin/bash`.