## Scheduling tasks periodically using Celery

### Installation
```angular2html
sudo apt-get install rabbitmq-server
pip install celery
```

For saving task results to the db
```angular2html
pip install django-celery-results
```

For creating a schedule of periodic tasks
```angular2html
pip install django-celery-beat
```

### Pre-excecution steps
1. Make sure ```celery.py``` is setup properly
2. Add ```django_celery_results``` and ```django_celery_beat``` in INSTALLED_APPS (in ```settings.py```)
3. Make migrations and migrate the celery_beats and celery_results classes.
    ```angular2html
    python manage.py makemigrations
    python manage.py migrate
    ```

### Execution steps
1. Run to see logs of celery workers
    ```angular2html
    celery -A src worker -l info
    ```
2. Run to start scheduled / periodic celery tasks
   ```angular2html
   celery -A src beat -l INFO 
   ```
3. Run the Django server
   ```angular2html
   python manage.py runserver
   ```
   
### Visualization of Task Queue
1. Install ```Flower``` for task-queue visualization
   ```angular2html
   pip install flower
   ```
2. Run it to record and visualize the task queues in real-time.
   ```angular2html
   flower -A src --port=5555 
   ```
3. Goto ```http://localhost:5555/``` for the visualization.