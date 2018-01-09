# encoding: utf-8
"""Define os blueprints para as rotas de health check"""
from flask_restful import Api
from flask import Blueprint

from .health_check import HealthCheck


def setup():
    """Retorna um blueprint para a função de health check"""
    blueprint = Blueprint(
        'health-check', __name__,
    )

    api = Api(blueprint)
    api.add_resource(HealthCheck, '/health-check')
    return blueprint
