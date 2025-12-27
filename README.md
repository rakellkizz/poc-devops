# 🧪 POC DevOps

Prova de Conceito para demonstrar fundamentos de DevOps:
- Aplicação mínima
- Containerização
- Orquestração
- Automação

## 🎯 Objetivo
Demonstrar, de forma prática, a criação e operação de uma aplicação
containerizada preparada para ambientes modernos.

## 🛠 Tecnologias
- Python
- FastAPI

## ▶️ Executar localmente (sem Docker ainda)

```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload
Acesse:

http://localhost:8000

http://localhost:8000/health