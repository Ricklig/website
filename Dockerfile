FROM ricklig/website
WORKDIR /code
RUN python3 server.py
