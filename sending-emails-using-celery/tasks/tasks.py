from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger
from celery.decorators import task
from .email import send_review_email
from simple_chalk import chalk


logger = get_task_logger(__name__)


@task(name='send_review_email_task')
def send_review_email_task(name, email, review):
    try:
        send_review_email(name, email, review)
        logger.info(chalk.green(f"Sent review email to {email}"))
    except:
        logger.info(chalk.red(f"Email could not be sent to {email}"))
    finally:
        return
