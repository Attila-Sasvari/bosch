FROM ubuntu:focal as builder
RUN apt-get update && \
    apt-get -y install g++
COPY . /usr/src/helloworld
WORKDIR /usr/src/helloworld
RUN g++ -o helloworld -static helloworld.cpp

FROM alpine:latest
COPY --from=builder /usr/src/helloworld/helloworld /helloworld
CMD ["./helloworld"]