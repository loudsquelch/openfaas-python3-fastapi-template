# OpenFaas Python3 FastAPI Template

A Python [FastAPI](https://github.com/tiangolo/fastapi) template that make use of the incubator project [of-watchdog](https://github.com/openfaas-incubator/of-watchdog).

Templates available in this repository:
- python3-fastapi


## Downloading the templates
```
$ faas template pull https://github.com/loudsquelch/openfaas-python3-fastapi-template
```

## Using the python3-fastapi templates
Create a new function

```
$ faas new --lang python3-fastapi <fn-name>
```

Build, push, and deploy

```
$ faas up -f <fn-name>.yml
```

Set your OpenFaaS gateway URL. For example:

```
$ OPENFAAS_URL=http://127.0.0.1:8080
```

Test the new function

```
$ curl -i $OPENFAAS_URL/function/<fn-name>
```

## Usage

### Request Body
The function handler is passed one argument - *req* which contains the request body.

### Response Bodies
By default, the template will automatically attempt to set the correct Content-Type header for you based on the type of response. 
