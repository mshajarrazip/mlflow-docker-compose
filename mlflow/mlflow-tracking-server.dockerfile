FROM base-ubuntu-python:latest

ARG MLFLOW_BACKEND_URI
ARG MLFLOW_ARTIFACTS_URI

ENV MLFLOW_BACKEND_URI=${MLFLOW_BACKEND_URI}
ENV MLFLOW_ARTIFACTS_URI=${MLFLOW_ARTIFACTS_URI}

# Install python packages
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

CMD mlflow server \
    --backend-store-uri ${MLFLOW_BACKEND_URI} \
    --default-artifact-root ${MLFLOW_TRACKING_DIRECTORY} \
    --host 0.0.0.0