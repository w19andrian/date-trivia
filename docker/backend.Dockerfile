FROM python:3.6-alpine3.10

COPY requirements.txt /tmp/

RUN \
	apk update && \
	apk add tzdata && \
	pip install -r /tmp/requirements.txt && \
	rm -rf /tmp/requirements.txt

COPY src/backend.py /opt/app/

ENV DEBUG FALSE
ENV HOST "0.0.0.0"
ENV PORT 5000
ENV TZ "Asia/Jakarta"

WORKDIR /opt/app

CMD ["python", "backend.py"]