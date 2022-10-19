# https://docs.docker.com/compose/gettingstarted/
# get image for docker public image repository
FROM python:3.7-alpine
# create directory
RUN mkdir /app
# switch to created directory
WORKDIR /app
# set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
# transfer files
COPY requirements.txt requirements.txt
ADD requirements.txt /app
ADD app.py /app
# update pip and install libraries
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# expose port 5000
EXPOSE 5000
COPY . .
CMD ["flask", "run"]