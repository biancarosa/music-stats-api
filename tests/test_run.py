# encoding: utf-8
"""Testes para o módulo run"""
import os
from unittest import TestCase
from mock import patch, MagicMock

from app import run

class TestRun(TestCase):
    """A classe TestRun testa as funções do módulo run.py e garante que tudo funciona ao rodar a aplicação"""
    
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch.dict(os.environ, {'PORT':'666'})
    @patch('app.run.setup')
    def test_run(self, setup):
        api = MagicMock()
        setup.return_value = api
        run.main()
        setup.assert_called_once()
        api.run.assert_called_once_with(host='0.0.0.0', port=666)