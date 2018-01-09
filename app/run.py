# encoding: utf-8
"""Roda a aplicação usando o server default do flask"""
import os
from app.server import setup


def main():
    """Roda a aplicação na porta definida na variável de ambiente PORT ou na porta padrão."""
    port = int(os.environ.get("PORT", 5000))
    api = setup()
    api.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    main()
