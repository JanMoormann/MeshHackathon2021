FROM python:3.7

RUN apt-get update && apt-get dist-upgrade -y

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "meshflask.py" ]