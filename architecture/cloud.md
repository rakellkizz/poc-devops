
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
