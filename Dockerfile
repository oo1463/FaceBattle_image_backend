FROM python:3.7.6

LABEL maintainer="oooo1463@gmail.com"
RUN apt-get update
RUN apt-get install -y python-pip python-dev build-essential libgl1-mesa-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python"]
CMD ["app/app.py"]