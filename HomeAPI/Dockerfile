FROM openjdk:8-jdk-alpine
LABEL maintainer="kani@kanistyle.com"

COPY build/libs/home-api.jar /usr/webapp/home-api.jar
WORKDIR /usr/webapp/
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","-Dspring.profiles.active=production","home-api.jar"]
