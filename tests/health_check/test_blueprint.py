# encoding: utf-8
"""Testes para o módulo blueprint do módulo health_check"""
import os
from unittest import TestCase
from mock import patch, MagicMock

from app.health_check.blueprint import setup
from app.health_check.health_check import HealthCheck

class TestHealthCheckBlueprint(TestCase):
    """A classe TestHealthCheckBlueprint testa as funções do módulo health_check"""
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('app.health_check.blueprint.Api')
    def test_health_check_blueprint(self, api):
        mock_blueprint = MagicMock()
        api.return_value = mock_blueprint
        blueprint = setup()
        self.assertIsNotNone(blueprint)
        api.assert_called_with(blueprint)
        mock_blueprint.add_resource.assert_called_with(HealthCheck, '/health-check')