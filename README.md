# ConnectUs


## Step to run ConnectUs in local machine

> **Step to run `virtualenv`**

```sh
python -m venv env
source env/bin/activate
```

> **Install all Dependencies `requirements.txt`**

```sh
pip3 install requirements.txt
```

> **Start `Django project`**

```sh
cd ConnectUs
python3 manage.py runserver
```

## Install Docker

> **Run following Code in Terminal Start `Redis-server`**

```sh
docker run -p 6379:6379 -d redis:5
```
