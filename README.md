# OpenFaas Python3 FastAPI Template

A Python [FastAPI](https://github.com/tiangolo/fastapi) template for [OpenFAAS](https://www.openfaas.com/)


## Downloading the templates

`faas template pull https://github.com/JustinGuese/openfaas-python3-fastapi-template
`

## Using the python3-fastapi templates

Two versions are available, the python3-fastapi which is built on the python3-alpine image, and the python3-fastapi-debian, which is built on top of the python3-slim package. Some python packages can't be installed using pip (pandas, numpy, etc), if you experience this issue just switch to the python3-fastapi-debian function.

Create a new function

```
faas new --lang python3-fastapi <fn-name>
```

Build, push, and deploy

```
faas up -f <fn-name>.yml
```

Set your OpenFaaS gateway URL. For example:

```
OPENFAAS_URL=http://127.0.0.1:8080
```

Test the new function

```
curl -i $OPENFAAS_URL/function/<fn-name>
```

## Usage



### secrets

secrets are automatically read into the matching env. Meaning if you are creating secrets in e.g. kubernetes with 

`kubectl create secret generic POSTGRES_PASSWORD --from-literal=POSTGRES_PASSWORD=1234 -n openfaas-fn`


