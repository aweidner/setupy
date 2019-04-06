FROM python:3.6-alpine

RUN adduser -D setupy

WORKDIR /home/setupy
COPY setup.py setup.py 
COPY README.md README.md
COPY VERSION.txt VERSION.txt
COPY scripts/start-gunicorn.sh start-gunicorn.sh
COPY setupy setupy
RUN python -m venv venv && \
    venv/bin/pip install gunicorn && \ 
    venv/bin/pip install . && \
    chmod +x start-gunicorn.sh

USER setupy
EXPOSE 5000
ENTRYPOINT ["./start-gunicorn.sh"]
