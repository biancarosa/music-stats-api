# encoding: utf-8
"""Define funções que retornam a saúde da aplicação"""

from flask import jsonify
import flask_restful as restful


class HealthCheck(restful.Resource):
    """Retorna informações básicas de saúde da aplicação"""

    def get(self):
        """Retorna informações sobre health check."""
        return jsonify({
            "message": "I'm alive and well, thank you very much for caring!"
        })
