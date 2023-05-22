FROM ubuntu:18.04

RUN apt-get clean && apt-get update && apt-get install g++ make -y && apt-get install python3.7 -y