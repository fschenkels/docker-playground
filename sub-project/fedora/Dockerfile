FROM fedora:latest AS base

ARG DEPENDENCIES_PATH=fedora/dependencies

RUN dnf -y update
RUN dnf -y install curl vim tmux python3-pip
RUN python3 -m pip install requests
RUN useradd -ms /bin/bash jacare

USER jacare
WORKDIR /home/jacare
# after the WORKDIR directive, all the ADD directives relative destination paths are
# relative to the WORKDIR, however, you still can use absolute paths
ADD ${DEPENDENCIES_PATH}/dependency.py .

RUN mkdir ~/log

ENTRYPOINT [ "sleep", "infinity" ]

FROM base AS extended

ADD root-fedora/app/ .