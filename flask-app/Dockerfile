FROM alpine:3.18

RUN apk add --update py-pip

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

EXPOSE 5000

ENTRYPOINT ["python3", "/usr/src/app/app.py"]


