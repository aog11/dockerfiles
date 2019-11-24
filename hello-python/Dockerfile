FROM ubuntu:latest

COPY hello_world.py / 

RUN apt-get update -y \ 
    && apt-get install python3 -y \
    && rm -rf /var/lib/apt \
    && mkdir -p /log \
    && chmod +x /hello_world.py

CMD ["./hello_world.py"]