from __future__ import annotations

from typing import List




class LoggingManager:
    def __init__(self):
        self.loggers: List[Logger] = []

    def add_logger(self, logger: Logger):
        self.loggers.append(logger)

    def log(self, message: str):
        for logger in self.loggers:
            logger.log(message)