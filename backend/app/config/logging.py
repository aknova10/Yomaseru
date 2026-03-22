# backend/app/config/logging.py

import logging
import sys
from logging.config import dictConfig

from app.config.settings import settings


def setup_logging():
    LOG_LEVEL = settings.log_level.upper()

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,

        "formatters": {
            "default": {
                "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            },
            "json": {
                "format": (
                    '{"time": "%(asctime)s", '
                    '"level": "%(levelname)s", '
                    '"logger": "%(name)s", '
                    '"message": "%(message)s"}'
                ),
            },
        },

        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": sys.stdout,
                "formatter": "default" if settings.ENV == "dev" else "json",
            },
        },

        "root": {
            "level": LOG_LEVEL,
            "handlers": ["console"],
        },
    }

    dictConfig(logging_config)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)