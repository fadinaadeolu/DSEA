FROM cluster-base

ARG spark_version=3.0.0
ARG jupyterlab_version=2.1.5

COPY requirements.txt ./

RUN apt-get update -y && \
    apt-get install -y python3-pip && \
    pip3 install pyspark==${spark_version} jupyterlab==${jupyterlab_version} &&  \
    pip3 install -r requirements.txt

EXPOSE 8888
WORKDIR ${SHARED_WORKSPACE}
CMD jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token=