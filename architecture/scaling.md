<!--
=========================================================
POC 4 — ESCALA E CONFIABILIDADE
=========================================================
OBJETIVO:
- Explicar como cresce (sem reinventar roda)
- Explicar como atualiza (sem downtime)
- Mostrar que você entende "princípios" e não só comandos
=========================================================
-->

# 📈 Escala, disponibilidade e atualizações

## 🧠 Escalar (popular)
Escalar aqui significa:
- se tiver mais gente acessando, o sistema cria mais cópias
- se uma cópia morrer, o sistema cria outra
- o usuário continua sendo atendido

---

## ✅ Escala horizontal (a mais usada em APIs)
<!--
Por que horizontal?
- mais simples
- mais barato de crescer aos poucos
- combina com stateless
-->
- Aumentar réplicas do **Deployment**
- Distribuir requisições entre pods

---

## ⚙️ Autoscaling (HPA) — como seria em produção
<!--
HPA = Horizontal Pod Autoscaler
Ele sobe/baixa o número de pods baseado em CPU/memória (ou métricas).
-->
Em cloud, o ideal:
- HPA por CPU/memória
- limites/requests bem definidos
- mínimo de réplicas (ex.: 2) para alta disponibilidade

---

## ❤️ Liveness e Readiness (por que existem 2 “saúdes”?)

### Readiness (pronto para receber tráfego)
- Quando a aplicação está pronta
- Se não estiver pronta, o LB não manda tráfego

### Liveness (está viva ou travou?)
- Se travar/entrar em estado ruim, o Kubernetes reinicia

<!--
Isso é core de SRE:
- prevenir “pod morto atendendo usuário”
- reiniciar sozinho quando travar
-->

---

## 🔄 Atualizações sem downtime (Rolling Update)
<!--
Rolling update troca um pod por vez.
Se algo der errado, dá rollback.
-->
- Troca gradual de pods
- Mantém serviço disponível
- Evita “apagão” durante deploy

---

## 🧪 Teste de resiliência (o que você já fez)
- Derrubar pod de propósito
- Ver outro nascer automaticamente

Isso prova:
- auto-recuperação
- operação sem intervenção manual

---

## ✅ Como explicar isso em 1 frase
> “Eu escalo horizontalmente por réplicas, uso probes de saúde, rolling updates e autoscaling (HPA) para manter disponibilidade.”
