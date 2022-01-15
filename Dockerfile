FROM alpine as base

RUN apk update \
    && apk add --no-cache \
        bash \
        python3 \
        openssl-dev \
        cargo \
        rust \
        build-base \
        python3-dev \
        openssh \
        ca-certificates \
        groff \
        git \
        zip \
        git-subtree \
        jq \
        unzip \
        busybox-extras \
        libffi-dev \
        py3-pip \
    && pip install --force-reinstall --no-binary :all: cffi \
    && python3 -m pip install \
        cryptography --no-binary cryptography \
        pylint \
        boto3 \
        jinja2 \
        twine \
        awscli \
    && rm -rf /opt/build/* \
    && rm -rf /var/cache/apk/* \
    && rm -rf /root/.cache/* \
    && rm -rf /tmp/*

FROM scratch as user
COPY --from=base . .

ARG HOST_UID=${HOST_UID:-4000}
ARG HOST_USER=${HOST_USER:-nodummy}

RUN [ "${HOST_USER}" == "root" ] || \
    (adduser -h /home/${HOST_USER} -D -u ${HOST_UID} ${HOST_USER} \
    && chown -R "${HOST_UID}:${HOST_UID}" /home/${HOST_USER})

USER ${HOST_USER}
WORKDIR /home/${HOST_USER}
COPY files/profile .profile
