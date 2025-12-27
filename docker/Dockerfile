# ============================================================
# Dockerfile — POC DevOps / SRE
# ============================================================

# 1️⃣ Imagem base
FROM python:3.11-slim

# 2️⃣ Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV ENV=container

# 3️⃣ Diretório de trabalho
WORKDIR /app

# 4️⃣ Copia o código da aplicação
COPY app/ /app/

# 5️⃣ Instala dependências
RUN pip install --no-cache-dir fastapi uvicorn

# 6️⃣ Copia o script de inicialização
COPY scripts/start.sh /start.sh

# 7️⃣ Permissão de execução
RUN chmod +x /start.sh

# 8️⃣ Porta exposta
EXPOSE 8000

# 9️⃣ Comando de inicialização
CMD ["/start.sh"]
