# encoding: utf-8
"""Inicia aplicação flask."""

from flask import Flask, jsonify
from app.health_check import blueprint as health_check_blueprint
from app import logger

LOG = logger.new(__name__)

def setup():
    """Monta uma API flask e registra seus blueprints."""
    LOG.info("Creating API.")
    api = Flask(__name__)
    LOG.info("Registering blueprints.")
    api.register_blueprint(health_check_blueprint.setup())
    LOG.info("Registering error handlers.")
    api.register_error_handler(Exception, default_error_handler)
    LOG.info("Setting up config variables.")
    api.config['PROPAGATE_EXCEPTIONS'] = True
    return api

def default_error_handler(exception):
    LOG.error(exception)
    response = jsonify({"success": False, "message": exception.message})
    response.status_code =500
    return response