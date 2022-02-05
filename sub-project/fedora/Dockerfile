FROM fedora:latest AS base

ARG DEPENDENCIES_PATH=fedora/dependencies

RUN dnf -y update
RUN dnf -y install curl vim tmux python3-pip
RUN python3 -m pip install requests
RUN useradd -ms /bin/bash jacare

USER jacare
WORKDIR /home/jacare
ADD ${DEPENDENCIES_PATH}/dependency.py .

ENTRYPOINT [ "sleep", "infinity" ]

FROM base AS extended

ADD root-fedora/app/ /home/jacare