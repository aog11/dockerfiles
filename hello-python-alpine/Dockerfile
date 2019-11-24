FROM alpine:latest

COPY hello_world.py / 

RUN apk add python3 && chmod +x /hello_world.py

CMD ["./hello_world.py"]