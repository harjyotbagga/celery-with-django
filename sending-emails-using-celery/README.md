## Sending Emails in Django using Celery

Installation
```angular2html
pip install celery
sudo apt-get install rabbitmq-server
```

Running
```angular2html
celery -A NAME_OF_INSTANCE worker --loglevel=info
celery -A src worker --loglevel=info
```
