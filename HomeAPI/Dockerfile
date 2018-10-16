FROM resin/raspberry-pi-buildpack-deps:jessie-scm
LABEL maintainer="kani@kanistyle.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
		bzip2 \
		unzip \
		xz-utils \
	&& rm -rf /var/lib/apt/lists/



ENV LANG C.UTF-8

RUN { \
		echo '#!/bin/sh'; \
		echo 'set -e'; \
		echo; \
		echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
	} > /usr/local/bin/docker-java-home \
	&& chmod +x /usr/local/bin/docker-java-home

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-armhf

ENV JAVA_VERSION 8u40~b04
ENV JAVA_DEBIAN_VERSION 8u40~b04-2

ENV CA_CERTIFICATES_JAVA_VERSION 20140324

RUN set -x \
	&& apt-get update \
	&& apt-get install -y  \
		openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \
	ca-certificates-java=$CA_CERTIFICATES_JAVA_VERSION && rm -rf /var/lib/apt/lists/* \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure


COPY build/libs/home-api.jar /usr/webapp/home-api.jar
WORKDIR /usr/webapp/
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","-Dspring.profiles.active=production","home-api.jar"]
