FROM python:3.7

LABEL maintainer="oooo1463@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8081
ENTRYPOINT ["python"]
CMD ["app/app.py"]
