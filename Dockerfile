FROM python:3.8-bullseye
RUN apt update
# RUN apt -y install software-properties-common 
# RUN add-apt-repository ppa:deadsnakes/ppa
# RUN apt -y install python3.9
RUN apt -y install curl python3-pip sox

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# RUN mkdir -p /root/.ssh
# ADD id_rsa /root/.ssh/id_rsa
# RUN chmod 700 /root/.ssh/id_rsa
# RUN echo "Host gitlab.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/
RUN poetry install
COPY . /code/

EXPOSE 8000

CMD ["./run.sh"]