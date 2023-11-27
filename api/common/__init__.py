from threading import Timer
from .okx import update_okx_funding_balance
from loguru import logger

Timer(60*10, update_okx_funding_balance, args=[]).start()

logger.info("定时任务启动")