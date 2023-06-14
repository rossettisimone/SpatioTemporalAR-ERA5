# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.229.0/containers/python-3/.devcontainer/base.Dockerfile

FROM tf/tf

RUN apt-get install -y libgeos++-dev
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/