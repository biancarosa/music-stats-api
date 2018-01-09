# encoding: utf-8
"""Testes para o módulo server"""
import os
from unittest import TestCase
from mock import patch, MagicMock, call

from app import server

class TestServer(TestCase):
    """A classe TestServer testa as funções do módulo server.py e garante que tudo funciona ao rodar a aplicação"""
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('app.server.Flask')
    @patch('app.server.health_check_blueprint.setup', return_value='health_check')
    @patch('app.server.cancellation_information_blueprint.setup', return_value='cancellation_information')
    def test_setup(self, bp2, bp1, flask):
        api = MagicMock()
        flask.return_value = api
        
        server.setup()

        flask.assert_called_with('app.server')
        bp1.assert_called()
        bp2.assert_called()
        api.register_blueprint.assert_has_calls([call('health_check'), call('cancellation_information')])

    @patch('app.server.jsonify')
    def test_default_error_handler(self, jsonify):
        msg = 'Erro.'
        exception = Exception(msg)
        response = server.default_error_handler(exception)
        jsonify.assert_called_with({"success": False, "message" : msg})
        self.assertEquals(response.status_code, 500)
