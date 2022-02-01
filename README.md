# docker-playground
Free area to test whatever you want to

## Current state of the `main` branch

## Tips and Tricks
* When you run `docker-compose exec` you must specify the service name, not the container name. Like in `docker-compose exec ubuntu /bin/bash`.
* When you run `docker exec` you must specify the container name. Like in `docker exec -i -t my-ubuntu /bin/bash`.