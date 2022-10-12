# C++ helloworld

This repository includes
- a `C++ script` which prints "Hello World" to the console, and
- a `Dockerfile` which compiles the .cpp file in a builder image, and starts the executable in a separate image.

## Procedure

### Build the image

```
docker build -t gcc_helloworld:1.0.0 .
```

### Run the container

```
docker run -it --rm --name gcc_helloworld gcc_helloworld:1.0.0
```