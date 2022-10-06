FROM ubuntu:focal as builder
RUN apt-get update && \
    apt-get -y install g++ cmake
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN g++ -o myapp -static helloworld.cpp

FROM alpine:latest
COPY --from=builder /usr/src/myapp/myapp /myapp
CMD ["./myapp"]