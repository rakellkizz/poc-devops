<!--
=========================================================
POC 4 — SEGURANÇA (MÍNIMO BEM FEITO)
=========================================================
OBJETIVO:
- Mostrar o essencial que qualquer produção precisa
- Sem paranoia, sem “inventar 200 controles”
- Segurança pragmática, do jeito que empresas gostam
=========================================================
-->

# 🔐 Segurança (mínimo bem feito)

## 🧠 Ideia principal (popular)
Segurança não é “trancar tudo”.
É:
- proteger dados
- evitar vazamento
- reduzir impacto se algo acontecer

---

## ✅ Controles essenciais (o pacote básico de produção)

### 1) HTTPS/TLS na borda
- Todo acesso público deve ser HTTPS
- Certificado no Load Balancer / Ingress

### 2) Secrets fora do código
- Nunca colocar senha/token dentro do repositório
- Usar:
  - Kubernetes Secrets (ou serviços gerenciados equivalentes)

### 3) Menor privilégio (Least Privilege)
- Cada componente com permissão mínima necessária
- Evitar “admin para tudo”

### 4) Imagens seguras
- Base image pequena (ex.: `python:slim`)
- Atualização periódica
- Scanner (em pipeline, se desejar evoluir)

### 5) Isolamento por namespace (quando crescer)
- separar ambientes (dev/staging/prod)
- reduzir risco de “um mexer no outro”

---

## 🧭 Segurança “SRE-friendly”
<!--
SRE e Segurança se cruzam em:
- auditabilidade
- rastreabilidade
- incident response
-->
- Logs ajudam a investigar incidentes
- Health + métricas ajudam a detectar anomalias rápido

---

## ✅ Como explicar isso em 1 frase
> “Eu uso TLS na borda, secrets fora do código, menor privilégio e boas práticas de imagens para manter segurança pragmática.”
