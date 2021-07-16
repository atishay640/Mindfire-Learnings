## Celery with RabbitMQ

### Steps to run the project:
#### Step-1 : Install Rabbitmq-server and make sure it is running. 
#### Step-2 : Create env and install all requirements.
#### Step-3 : Start celery workers and celery beat using below commands.

- celery -A mailshooter worker -l INFO
- celery -A mailshooter beat -l info
