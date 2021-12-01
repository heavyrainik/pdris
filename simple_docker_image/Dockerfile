FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
RUN apt-get install git -y

EXPOSE 5000

WORKDIR /app

RUN git clone https://github.com/XD-DENG/flask-example.git .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
