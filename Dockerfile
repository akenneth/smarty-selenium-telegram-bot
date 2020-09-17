FROM python:3.7

# set display port to avoid crash
# ENV DISPLAY=:99


RUN apt-get -y update \
    && apt-get -y install curl \
    && apt-get -y install firefox-esr=68.12.0esr-1~deb10u1 \
    && rm -rf /var/lib/apt/lists/*

# wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
RUN GECKODRIVER_VERSION=`curl https://github.com/mozilla/geckodriver/releases/latest | grep -Po 'v[0-9]+.[0-9]+.[0-9]+'` && \
    wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz && \
    tar -zxf geckodriver-v0.26.0-linux64.tar.gz -C /usr/local/bin && \
    chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-v0.26.0-linux64.tar.gz

# upgrade pip
RUN pip install --upgrade pip

# # create project folder with the name code
RUN mkdir /code

# # project scope
WORKDIR /code

# # install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY *.py /code/
COPY fetchers /code/fetchers/
COPY handlers /code/handlers/

CMD ["/code/webserver.py"]
ENTRYPOINT ["python"]