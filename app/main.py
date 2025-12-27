# Copyright (c) 2025 Raquel Souza
# Licensed under the Apache License, Version 2.0


"""
===========================================================
Aplicação mínima — POC DevOps / SRE
===========================================================

OBJETIVO GERAL:
- Subir um serviço HTTP simples
- Servir como base para:
  - Docker
  - Kubernetes
  - CI/CD
  - Observabilidade (SRE)
- NÃO é foco em regra de negócio
- Foco total em operação, confiabilidade e infraestrutura

Esta aplicação é propositalmente simples.
Ela existe para ser OPERADA, não para ser um produto final.
===========================================================
"""

# ==========================================================
# 📦 IMPORTAÇÕES PADRÃO
# ==========================================================

# Biblioteca padrão para logging (observabilidade básica)
import logging

# Biblioteca padrão para obter o hostname da máquina/pod
import socket

# Biblioteca padrão para variáveis de ambiente
import os

# Framework web moderno e leve
from fastapi import FastAPI


# ==========================================================
# 📊 CONFIGURAÇÃO DE LOGS (BASE SRE)
# ==========================================================

"""
Aqui definimos o formato e o nível dos logs.

Por que isso é importante?
- Logs são a PRIMEIRA ferramenta de um SRE
- Em Kubernetes, logs são coletados automaticamente
- Logs estruturados facilitam debug, auditoria e observabilidade

Formato:
DATA | NÍVEL | MENSAGEM
"""

logging.basicConfig(
    level=logging.INFO,  # INFO é ideal para produção básica
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Cria um logger nomeado com base no módulo
# Isso permite rastrear a origem do log
logger = logging.getLogger(__name__)


# ==========================================================
# 🚀 CRIAÇÃO DA APLICAÇÃO FASTAPI
# ==========================================================

"""
A aplicação FastAPI é criada com metadados claros.

Essas informações:
- Aparecem na documentação automática (/docs)
- Ajudam equipes e ferramentas a entender o serviço
"""

app = FastAPI(
    title="POC DevOps",
    description="Aplicação mínima para prova de conceito DevOps/SRE",
    version="1.0.0"
)


# ==========================================================
# 🌐 ENDPOINT RAIZ (/)
# ==========================================================

@app.get("/")
def root():
    """
    Endpoint principal da aplicação.

    FUNÇÃO:
    - Retornar informações básicas do ambiente
    - Confirmar que a aplicação está viva
    - Facilitar debug em ambientes distribuídos

    INFORMAÇÕES RETORNADAS:
    - status: estado geral da aplicação
    - message: mensagem amigável
    - hostname: identifica o pod/container
    - environment: identifica o ambiente (local / container / kubernetes)
    """

    # Loga o acesso ao endpoint principal
    # Isso permite saber:
    # - Se o serviço está sendo acessado
    # - Quando foi acessado
    logger.info("Endpoint '/' acessado com sucesso")

    return {
        "status": "ok",
        "message": "POC DevOps rodando com sucesso 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "local")
    }


# ==========================================================
# ❤️ ENDPOINT DE SAÚDE (/health)
# ==========================================================

@app.get("/health")
def health():
    """
    Endpoint de healthcheck (CRÍTICO para SRE).

    USADO POR:
    - Kubernetes (livenessProbe / readinessProbe)
    - Monitoramento
    - Load Balancers
    - Verificações automatizadas

    REGRAS IMPORTANTES:
    - Deve ser RÁPIDO
    - Deve ser SIMPLES
    - Não deve acessar recursos externos
    """

    # Loga cada execução do healthcheck
    # Útil para:
    # - Diagnóstico de loops de restart
    # - Entender comportamento do cluster
    logger.info("Healthcheck executado")

    return {
        "health": "healthy"
    }
# ==========================================================