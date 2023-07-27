FROM python:3.9-buster
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN sudo -v ; curl https://rclone.org/install.sh | sudo bash 
COPY rclone.conf /root/.config/rclone/
RUN apt install dos2unix
RUN pip3 install -U pip
COPY start.sh /start.sh
COPY requirements.txt /requirements.txt
RUN cd /
RUN pip3 install -U -r requirements.txt
WORKDIR /LazyDeveloper
RUN dos2unix /start.sh 
CMD ["/bin/bash", "/start.sh"]
