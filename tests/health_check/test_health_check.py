# encoding: utf-8
"""Testes para o módulo health_check"""
import os
from unittest import TestCase
from mock import patch, MagicMock, call

from app.health_check.health_check import HealthCheck

class TestHealthCheck(TestCase):
    """A classe TestHealthCheck testa as funções do módulo health_check.py e garante que tudo funciona ao rodar a aplicação"""
    
    def setUp(self):
        self.health_check = HealthCheck()

    def tearDown(self):
        pass

    @patch('app.health_check.health_check.jsonify')
    def test_get(self, jsonify):
        self.health_check.get()
        jsonify.assert_called()
