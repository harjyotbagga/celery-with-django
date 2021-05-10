from celery import shared_task
from celery.utils.log import get_task_logger
import time, random, string
from datetime import datetime
from tasks.models import UserInstance
from simple_chalk import chalk

logger = get_task_logger(__name__)

@shared_task()
def perform_add(x, y):
    logger.info(chalk.blue(__name__))
    logger.info(chalk.blue(f"Result is {x + y}"))
    logger.info(get_task_logger())
    return x + y

@shared_task()
def add_user_timestamp():
    username = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
    user = UserInstance(name=username, time=datetime.now())
    user.save()
    logger.info(chalk.green(f"User Successfully created and saved at {datetime.now()}"))
    return