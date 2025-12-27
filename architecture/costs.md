<!--
=========================================================
POC 4 — CUSTOS (BOM SENSO)
=========================================================
OBJETIVO:
- Mostrar que você entende que cloud custa dinheiro
- Mostrar escolhas que controlam custo sem perder qualidade
- Não inventar valores exatos (mudam muito), mas mostrar lógica
=========================================================
-->

# 💰 Custos e otimizações (visão prática)

## 🧠 Ideia principal (popular)
Cloud é tipo “conta de luz”:
- quanto mais você usa, mais paga
- deixar ligado sem necessidade custa
- serviços gerenciados custam mais, mas economizam tempo e risco

---

## 📌 Onde normalmente custa (top 5)
1) **Cluster/nós** (máquinas rodando)
2) **Load balancer** (porta HTTPS)
3) **Tráfego de rede** (saída para internet)
4) **Logs e métricas** (armazenamento + coleta)
5) **Registry de imagens** (armazenamento)

---

## ✅ Estratégias simples de custo (sem perder arquitetura)

### 1) Começar pequeno
- poucos nós
- poucas réplicas
- crescer conforme uso

### 2) Autoscaling
- sobe em pico
- desce quando está vazio

### 3) Log com bom senso
- logs úteis (INFO/WARN/ERROR)
- retenção limitada (ex.: 7/14 dias na POC)
- evitar log infinito sem propósito

### 4) Ambientes separados
- dev/staging/prod, quando necessário
- mas sem duplicar custo sem necessidade

### 5) Desligar recursos quando não usa (POC)
- para portfólio, não precisa rodar 24h em cloud paga

---

## 🧠 Como explicar isso em entrevista
> “Eu começo com recursos mínimos, uso autoscaling, retenção de logs limitada e dimensiono conforme demanda para controlar custo sem perder confiabilidade.”
