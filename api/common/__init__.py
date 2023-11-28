from .okx import update_okx_funding_balance
from loguru import logger
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = BackgroundScheduler()

scheduler.add_job(update_okx_funding_balance, 'interval', minutes=10)
scheduler.start()

logger.info("定时任务启动")