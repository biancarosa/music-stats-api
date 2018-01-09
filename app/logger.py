# encoding: utf-8
"""Encapsula a criação do logger da aplicação"""
import logging

LOG_FORMAT = (
    '%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s')

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)


def new(owner):
    """Cria um novo logger"""
    logger = logging.getLogger(owner)
    return logger
