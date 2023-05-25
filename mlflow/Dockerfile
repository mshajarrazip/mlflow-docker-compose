FROM python:3.10-slim-buster
# Install python packages
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /mlruns/tracking
RUN mkdir -p /mlruns/artifacts
RUN chmod -R 777 /mlruns