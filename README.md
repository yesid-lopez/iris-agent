# IRIS

CMS: https://iris-agent.yesidlopez.de
IRIS: https://iris-agent.yesidlopez.de

## Setup

Firs clone the repo:
```bash
git clone https://github.com/yesid-lopez/iris
```

remember to set the env variables in the .env file

Build the docker image:
```bash
docker build -t iris:1.0 .
```

Run the app:
```bash
docker run -p 8501:8501 iris:1.0
```
