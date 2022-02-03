FROM fedora:latest AS standalone

RUN dnf -y update
RUN dnf -y install curl vim tmux

ENTRYPOINT [ "sleep", "infinity" ]

FROM standalone AS extended

RUN dnf -y install cowsay