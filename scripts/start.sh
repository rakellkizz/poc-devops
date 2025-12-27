#!/bin/sh
# ==========================================================
# start.sh — Script de inicialização da aplicação
# ----------------------------------------------------------
# Responsabilidades:
# - Preparar ambiente
# - Exibir contexto de execução
# - Iniciar o servidor FastAPI
# ==========================================================

echo "🚀 Iniciando POC DevOps..."
echo "📦 Ambiente: ${ENV:-local}"
echo "🖥 Hostname: $(hostname)"
echo "📁 Diretório atual: $(pwd)"

# Porta padrão (pode ser sobrescrita por variável de ambiente)
PORT=${PORT:-8000}

echo "🌐 Aplicação será exposta na porta: $PORT"

# Inicia o servidor FastAPI
# exec substitui o processo shell pelo processo da aplicação
# Isso é MUITO importante para Docker/Kubernetes
exec uvicorn main:app \
  --host 0.0.0.0 \
  --port "$PORT"
