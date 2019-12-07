import os
import logging
from logging import handlers

# 项目路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 请求头
HEADERS = {}
# 员工ID
EMP_ID = None


def init_logger():
    # 实例化日志器、设置日志等级
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 初始化处理器
    sh = logging.StreamHandler()
    # 初始化文件处理器
    log_path = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(log_path, when='S', interval=60, backupCount=7, encoding='utf-8')

    # 初始化格式化器
    # 2019-12-04 15:46:36,306 INFO [root] [__init__.py(<module>:7)] - test
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 添加格式化器到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 添加处理器到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)

