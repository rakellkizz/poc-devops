<!--
=========================================================
POC 4 — ARQUITETURA CLOUD (VISÃO GERAL)
=========================================================

OBJETIVO DESTE ARQUIVO (linguagem humana):
- Explicar "o que é o sistema" e "como ele seria em produção"
- Deixar claro o RACIOCÍNIO arquitetural (isso vale ouro em entrevista)
- Ser simples: sem exagero, sem jargão desnecessário

IMPORTANTE:
- POC 1/2/3 = execução (Docker/K8s/SRE)
- POC 4 = desenho + decisões (Arquitetura Cloud)

Este arquivo é o "mapa do projeto" para qualquer pessoa entender rápido.
=========================================================
-->

# ☁️ POC 4 — Arquitetura Cloud (Visão Geral)

## 🎯 O que é este projeto?
Esta POC é uma **API simples** (FastAPI) criada para demonstrar competências de:

- **DevOps** (empacotar, automatizar)
- **Kubernetes** (orquestrar, expor serviço, health)
- **SRE** (logs, resiliência, comportamento em falhas)
- **Arquitetura Cloud** (como isso vira produção de verdade)

> ⚠️ O foco NÃO é negócio (features). O foco é **operação confiável**.

---

## 🧩 O “tipo” de aplicação (isso guia TODA arquitetura)
**Aplicação stateless** (sem estado local).

<!--
Por que isso importa?
- Stateless escala fácil (várias cópias)
- Se um pod morre, outro assume sem perder dados locais
- É o padrão ideal para microserviço/API
-->

O serviço:
- Responde `GET /` (info do ambiente, hostname do pod)
- Responde `GET /health` (saúde)
- Pode incluir observabilidade (logs/métricas) conforme POC 3

---

## 👥 Usuários e tráfego (cenário realista de portfólio)
<!--
Não inventamos números absurdos.
Aqui mostramos bom senso:
- baixo a médio tráfego
- escalável por replicação
- custo controlado
-->
- Uso esperado: **baixo → médio**
- Picos: possíveis (ex.: testes, demos, tráfego)
- Resposta esperada: rápida, API leve
- Disponibilidade: alta, com auto-recuperação

---

## 🗺️ Arquitetura alvo em produção (visão de cima)

<!--
Este diagrama mostra o fluxo do usuário até os pods.

"Load Balancer" é a "porta da rua".
"Kubernetes" é o "condomínio inteligente".
"Pods" são as "casas" (instâncias) da aplicação.
Observabilidade são as "câmeras + registros".
-->

```mermaid
flowchart TD
  U[Usuários/Clientes] -->|HTTPS| LB[Load Balancer / Ingress]
  LB --> K8S[Kubernetes Gerenciado (EKS/AKS/GKE)]
  K8S --> PODS[Pods da API (réplicas)]
  PODS --> OBS[Logs + Métricas]

🧱 Componentes (o que existe em produção)
1) Entrada (acesso público)

HTTPS (segurança)

Load Balancer / Ingress (roteamento e TLS)

2) Execução do serviço

Kubernetes gerenciado (EKS/AKS/GKE)

Deployment (define réplicas, rollouts)

Service (endereçamento interno + exposição via Ingress)

3) Observabilidade (SRE)

Logs centralizados

Métricas e alertas básicos

Healthchecks (liveness/readiness)

✅ O que já foi provado nas POCs anteriores (ponte para credibilidade)
<!-- Aqui você deixa explícito que: "isso não é teoria, eu validei na prática" -->

POC 1: Docker + CI ✅

POC 2: Kubernetes (Minikube) + Service/Deployment ✅

POC 3: SRE (logs, falhas controladas, auto-recuperação) ✅

POC 4: Arquitetura Cloud (decisões e desenho) ✅

📌 Regras de ouro desta arquitetura (bem “SRE/Arquiteta”)

Escalar por replicação (horizontal)

Sem estado local (stateless)

Mudanças sem downtime (rolling updates)

Observabilidade desde o começo (logs/health/métricas)

Segurança mínima bem feita (TLS, secrets, privilégio mínimo)

🧭 Próximos passos naturais (não obrigatórios)
<!-- Isso deixa o projeto “vivo” e com roadmap. -->

Deploy público (ex.: Vercel como vitrine ou Cloud real como evolução)

Métricas com Prometheus/Grafana

Alertas e SLO/SLA

Pipeline com build + testes + deploy


---

## ✅ `architecture/cloud.md`

```markdown
<!--
=========================================================
POC 4 — CLOUD (EKS/AKS/GKE)
=========================================================
OBJETIVO:
- Mostrar que você entende os equivalentes nas 3 clouds
- Escolher uma "principal" (opcional) sem brigar de fanboy
- Explicar serviços gerenciados que reduzem dor operacional
=========================================================
-->

# ☁️ Cloud alvo (AWS / Azure / GCP)

## 🧠 Ideia central (popular)
Em produção, a gente prefere **Kubernetes gerenciado**, porque:
- dá menos manutenção
- é mais seguro
- é mais confiável
- escala com menos dor

---

## 🌎 Opções equivalentes (o mesmo conceito em clouds diferentes)

| O que precisamos | AWS | Azure | GCP |
|---|---|---|---|
| Kubernetes gerenciado | EKS | AKS | GKE |
| Load Balancer | ELB/ALB/NLB | Azure Load Balancer / App Gateway | Cloud Load Balancing |
| Registro de imagens | ECR | ACR | Artifact Registry |
| Logs | CloudWatch | Azure Monitor | Cloud Logging |
| Métricas | CloudWatch | Azure Monitor | Cloud Monitoring |

<!--
Por que essa tabela é forte?
- Mostra visão multi-cloud
- Mostra que você entende equivalências
-->

---

## ✅ Escolha recomendada para o “modelo mental” da POC
<!--
Aqui você pode dizer:
"Eu uso AWS como referência por ser comum, mas sei traduzir para Azure/GCP."
-->
Usarei **AWS como referência** (EKS/ECR/CloudWatch), mas a arquitetura vale igual para **AKS/GKE**.

---

## 🧱 Serviços mínimos em uma implantação real (sem exagero)

### 1) Registro de imagem (onde fica seu Docker)
- **AWS ECR** (ou ACR / Artifact Registry)
- A pipeline (CI) builda e publica a imagem versionada

### 2) Cluster Kubernetes gerenciado
- **EKS** (AKS/GKE equivalentes)
- Worker nodes (ou modo serverless, dependendo do caso)
- Addons de rede e DNS

### 3) Entrada HTTPS
- Load balancer + Ingress Controller
- Certificado TLS (pode ser gerenciado)

### 4) Observabilidade
- Logs centralizados
- Métricas e alertas mínimos
- Healthchecks

---

## 📌 O que muda do Minikube para Cloud (bem direto)
- No Minikube, tudo é local
- Na Cloud:
  - imagens ficam em registry (ECR/ACR/GAR)
  - entrada pública via LB/Ingress real
  - logs/métricas centralizados com serviços gerenciados
  - permissões e segurança ficam mais importantes

---

## 🧭 “Como eu explicaria isso numa entrevista”
> “Em cloud, eu rodaria essa API em Kubernetes gerenciado (EKS/AKS/GKE), com imagem em registry (ECR/ACR), entrada via Ingress com TLS e observabilidade básica (logs/métricas/healthchecks).”
