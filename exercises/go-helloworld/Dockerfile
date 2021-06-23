# docker build -t go-helloworld .
# docker tag go-helloworld XXXX/go-helloworld:v0.1.0
# docker push XXXX/go-helloworld:v0.1.0

FROM golang:alpine

WORKDIR /go/src/app

COPY . /go/src/app

RUN go mod init example.com/hello && go build -o helloworld

EXPOSE 6111

CMD ["./helloworld"]
