import logging

# 创建一个logger
logger = logging.getLogger('flask_demo')             # 记录app日志到文件
logger_sql = logging.getLogger('sqlalchemy.engine')  # 记录sql 到文件
logger_werkzeug = logging.getLogger('werkzeug')   # 记录werkzeug 日志输出到文件

logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('flask.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)
# 给logger添加handler
logger_sql.addHandler(fh)
logger_werkzeug.addHandler(fh)
