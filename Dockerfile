FROM jjanzic/docker-python3-opencv:latest
# RPI: FROM sgtwilko/rpi-raspbian-opencv:latest

WORKDIR /src

COPY requirements.txt /src/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src/ /src

CMD ["/bin/bash"]
