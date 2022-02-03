# docker-playground
Free area to test interesting `docker` features. I hope that this repo will be an useful project templates library for you.

Remember to take a look at the other branches as well, probably you'll find nice things there ;)

## Current state of the `subfolder_docker_compose_file` branch:
There are 2 projects on this branch, with their individual `docker-compose` files:
* The root project (`./docker-compose.yml`); and
* The sub-project (`./sub-project/docker-compose.yml`)

The current root project has some differences from the `main` branch's root project:
1. The `local-httpbin` container has been moved to the `sub-project`;
2. The `common` network has been converted into an external network, and now it is shared with the `sub-project`'s services;
3. There is a new service `root-fedora`, which extends the `sub-project`'s `fedora` service; and
4. The `separate` network has been removed.

The `sub-project` has a simple `fedora` service connected to its `httpbin` service.

Below you find a diagram that represents the current branch configuration:
```
                 ............................................
                 :       :  sub-project/docker-compose.yml  :
                 :       :..................................:
                 :                                          :
                 :                    ,sub-project-network  :
                 :                   /                      :    .................
                 :   +-----------+  /       +-----------+   .....:  sub-project  :
            ,--------|  fedora   |----------|  httpbin  |   :    :...............:
            |    :   +-----------+          +-----------+   :
            |    :        /\                                :
            |    :        ||                                :
            |    :........||................................:
common      |    :        ||       :  ./docker-compose.yml  :
network     |    :        ||       :........................:
(external)  |    :        ||                                :
         \  |    :        ||== extension relationship       :
          \ |    :        ||                                :
           \|    :   +-----------+                          :
            |    :   |  root-    |                          :    .................
            +--------|  fedora   |                          :....:  root project :
            |    :   +-----------+                          :    :...............:
            |    :                                          :
            |    :   +-----------+                          :
            '--------|   NGINX   |                          :
                 :   +-----------+                          :
                 :                                          :
                 :..........................................:
```

### Getting started
**WARNING:**
You must either include the `sub-project/docker-compose.yml` file in all of your `docker-compose` commands or convert the `sub-project-network` into an external network.
```
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose ps
ERROR: Service "root-fedora" uses an undefined network "sub-project-network"
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f docker-compose.yml -f sub-project/docker-compose.yml ps
Name   Command   State   Ports
------------------------------
```

The following steps show you a way to run both projets at the same time:
1. Start the `root-fedora` service from the root project:
```
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f docker-compose.yml -f sub-project/docker-compose.yml up -d root-fedora
Building nginx
[...]
Building root-fedora
[...]
Creating docker-playground_nginx_1 ... done
Creating extended-fedora           ... done
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f docker-compose.yml -f sub-project/docker-compose.yml ps
          Name                         Command               State          Ports
-----------------------------------------------------------------------------------------
docker-playground_nginx_1   /docker-entrypoint.sh ngin ...   Up      0.0.0.0:9999->80/tcp
extended-fedora             sleep infinity                   Up
```
2. Start the services from the sub-project:
```
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f sub-project/docker-compose.yml up -d
Building fedora
[...]
Creating local-httpbin ... done
Creating fedora        ... done
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f sub-project/docker-compose.yml ps
    Name                   Command               State   Ports
---------------------------------------------------------------
fedora          sleep infinity                   Up
local-httpbin   gunicorn -b 0.0.0.0:80 htt ...   Up      80/tcp
```
3. Then, you can verify that both projects are running in separated environments:
```
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f docker-compose.yml -f sub-project/docker-compose.yml exec root-fed
ora curl http://httpbin.org/ip
{
  "origin": "*** my external IP appeared here ***"
}
➜  docker-playground git:(subfolder_docker_compose_file) ✗ docker-compose -f sub-project/docker-compose.yml exec fedora curl http://httpbin.org/ip
{
  "origin": "*** one local IP appeared here ***"
}
```

## Tips and Tricks
* When you run `docker-compose exec` you must specify the service name, not the container name. Like in `docker-compose exec ubuntu1 /bin/bash`.
* When you run `docker exec` you must specify the container name. Like in `docker exec -i -t my-ubuntu /bin/bash`.
* Services with `depends_on` cannot be extended (see [this](https://github.com/docker/compose/issues/7916#issuecomment-962869400) issue). For more information on extending services visit [this](https://docs.docker.com/compose/extends/) page.

