# 📊 Desafio de Modelagem Preditiva: Churn e NPS

## 🎯 Objetivo
1. Identificar os principais fatores que influenciam o **churn** e propor ações preventivas.  
2. Mapear os **drivers de NPS** e sugerir iniciativas para melhoria da satisfação.  
3. Reduzir o impacto financeiro do churn, considerando o custo elevado de instalação.  
4. Aumentar a **retenção e fidelização**, com foco em experiência e valor percebido.  

---

## 📂 Bases de Dados
- **customer_original.csv** → Dados cadastrais, contratos e cobranças.  
- **customer_social.csv** → Informações sociais/demográficas.  
- **customer_nps.csv** → Pesquisas de satisfação e NPS.  

---

## 🔍 Estratégia Analítica

### 1. Integração e tratamento de dados
- Normalização e unificação por CPF.  
- Conversão de variáveis inconsistentes (ex.: `TotalCharges`).  
- Exclusão de registros incompletos relevantes.  

### 2. Exploração inicial
- Distribuição do churn (% de clientes que cancelam).  
- Correlação entre **tempo de contrato (tenure)** e **NPS**.  
- Perfil dos clientes que mais cancelam (idade, plano, mensalidade).  

### 3. Modelagem preditiva
- **Churn** → Classificação  
  - Modelos testados: Regressão Logística, Random Forest.  
  - Métricas: ROC-AUC, Precision, Recall, F1-score.  
- **NPS** → Regressão  
  - Modelos testados: Random Forest Regressor.  
  - Métricas: R², RMSE.  

### 4. Fórmula preditiva de churn (proposta inicial)

```math
P(\text{Churn}=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 \cdot \text{NPS} + \beta_2 \cdot \text{Tenure} + \beta_3 \cdot \text{MonthlyCharges} + \dots)}}









