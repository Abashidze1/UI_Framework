import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}"
)

logger.add(
    "logs/ui_tests.log",
    level="INFO",
    rotation="1 MB",
    encoding="utf-8"
)