<h1 align="center">
  <img 
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&pause=1000&color=38B2AC&center=true&vCenter=true&width=700&lines=POC+DevOps;Docker+%7C+Kubernetes+%7C+CI;Base+para+SRE+e+Arquitetura+Cloud"
    alt="Typing SVG"
  />
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?logo=kubernetes&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white" />
  <img src="https://img.shields.io/badge/Linux-FCC624?logo=linux&logoColor=black" />
  <img src="https://img.shields.io/badge/CI-Automation-success" />
</p>

<p align="center">
  Prova de Conceito (POC) DevOps com foco em containerização, orquestração e automação.<br/>
  Projeto base para evolução em <strong>SRE</strong> e <strong>Arquitetura Cloud</strong>.
</p>

---

## 🧪 Sobre a POC

Esta POC foi criada com o objetivo de demonstrar fundamentos reais de **DevOps**, incluindo:

- Empacotamento de aplicações com Docker  
- Orquestração com Kubernetes (local)  
- Inicialização controlada via script  
- Pipeline de Integração Contínua (CI)  
- Base preparada para observabilidade e confiabilidade (SRE)  

> ⚠️ Não é um produto final — é uma prova técnica de viabilidade e boas práticas.

---

## 🛠️ Tecnologias

- Python + FastAPI  
- Docker  
- Kubernetes (Minikube / Kind)  
- GitHub Actions  
- Linux / WSL2  

---

## 📌 Status da POC

- ✅ Aplicação funcional  
- ✅ Dockerfile validado  
- ✅ Script de inicialização (`start.sh`)  
- ✅ Kubernetes manifests prontos  
- ✅ CI automatizado com GitHub Actions  

🚀 **POC 1 (DevOps) concluída com sucesso**

---

## ▶️ Executar localmente (sem Docker)

```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload
Acesse:

http://localhost:8000

http://localhost:8000/health

🔮 Próximos passos

🔍 Observabilidade (logs e métricas)

🚨 Simulação de falhas (SRE)

☁️ Arquitetura Cloud (AWS / Azure / GCP)

📊 Diagramas e decisões arquiteturais