"""
Aplicação mínima para POC DevOps / SRE

Objetivo:
- Subir um serviço HTTP simples
- Servir como base para Docker, Kubernetes e CI
- Não é foco em negócio, apenas em operação
"""

from fastapi import FastAPI
import socket
import os

# Cria a aplicação FastAPI
app = FastAPI(
    title="POC DevOps",
    description="Aplicação mínima para prova de conceito DevOps/SRE",
    version="1.0.0"
)

# Endpoint raiz
@app.get("/")
def root():
    """
    Endpoint principal.
    Retorna informações básicas do ambiente.
    """
    return {
        "status": "ok",
        "message": "POC DevOps rodando com sucesso 🚀",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "local")
    }

# Endpoint de saúde (muito importante para Kubernetes e SRE)
@app.get("/health")
def health():
    """
    Endpoint de healthcheck.
    Usado por:
    - Kubernetes
    - Monitoramento
    - Load balancer
    """
    return {
        "health": "healthy"
    }
