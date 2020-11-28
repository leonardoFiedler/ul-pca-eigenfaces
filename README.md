# Unsupervised Learning - PCA EigenFaces

## About the project

This project uses ORL dataset to apply PCA in facial recognition.

## Setup the project

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the project

Extract the `ORL.zip` file before run `python main.py`

## Parameters

| Name          | Description                       | Required | Default Value |
|---------------|-----------------------------------|----------|---------------|
| -d, --dataset | Path to the images dataset folder | False    | ./ORL         |

## Result after executing

```
Tamanho Total do Dataset: 410
Tamanho do Dataset de Treino: 287
Tamanho do Dataset de Teste: 123
10 componentes principais, acurácia: 89.43%
Número de acertos: 110/123
Distância Mínima: 129.90, Distância Máxima: 2962.27
Distância Média: 711.68
********************************************************************************
11 componentes principais, acurácia: 91.87%
Número de acertos: 113/123
Distância Mínima: 130.20, Distância Máxima: 2985.42
Distância Média: 731.72
********************************************************************************
12 componentes principais, acurácia: 91.87%
Número de acertos: 113/123
Distância Mínima: 131.84, Distância Máxima: 3015.35
Distância Média: 755.06
********************************************************************************
13 componentes principais, acurácia: 91.06%
Número de acertos: 112/123
Distância Mínima: 174.48, Distância Máxima: 3094.15
Distância Média: 795.47
********************************************************************************
14 componentes principais, acurácia: 91.87%
Número de acertos: 113/123
Distância Mínima: 174.48, Distância Máxima: 3175.62
Distância Média: 816.19
********************************************************************************
15 componentes principais, acurácia: 91.87%
Número de acertos: 113/123
Distância Mínima: 182.31, Distância Máxima: 3180.05
Distância Média: 839.43
********************************************************************************
16 componentes principais, acurácia: 93.50%
Número de acertos: 115/123
Distância Mínima: 189.45, Distância Máxima: 3203.38
Distância Média: 857.91
********************************************************************************
17 componentes principais, acurácia: 91.87%
Número de acertos: 113/123
Distância Mínima: 197.96, Distância Máxima: 3259.66
Distância Média: 881.11
********************************************************************************
18 componentes principais, acurácia: 93.50%
Número de acertos: 115/123
Distância Mínima: 199.30, Distância Máxima: 3267.87
Distância Média: 901.49
********************************************************************************
19 componentes principais, acurácia: 93.50%
Número de acertos: 115/123
Distância Mínima: 199.93, Distância Máxima: 3401.25
Distância Média: 913.15
********************************************************************************
20 componentes principais, acurácia: 92.68%
Número de acertos: 114/123
Distância Mínima: 204.23, Distância Máxima: 3418.22
Distância Média: 927.49
********************************************************************************
```