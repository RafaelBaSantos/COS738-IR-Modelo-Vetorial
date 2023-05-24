# Avaliacao de um Modelo de RI

Esse repositório contém os arquivos referentes a um trabalho da cadeira de Busca e Mineração de Texto.
Essa branch contém, além dos modelo de IR, a comparação do modelo com ou sem o uso do stemmer de Porter.

### Resultos das avaliações

Foi realizada o Information Retrieval dos dados de teste com e sem o uso do stemmer de [Porter](http://tartarus.org/martin/PorterStemmer/). Os resultados foram avaliados com as métricas abaixo:

Scatterplot precisão por revocação, onde os valores são interpolados na evocação em 10 intervalos iguais:

![Gráfico de 11 pontos](https://github.com//RafaelBaSantos/COS738-IR-Modelo-Vetorial/blob/avaliacao_ri/result/diagramas/11pontos.png?raw=true)

$F_{1}$ score: Métrica de acuária dada pela média armônica da precisão e revocação
- Dados sem stemming: 0.2410
- Dados com stemming: 0.2553

Precision@5: Métrica de precisão calculada considerando os 5 primeiros resultados de cada consulta.
- Dados sem stemming: 0.2151
- Dados com stemming: 0.2353

Precision@10: Métrica de precisão calculada considerando os 10 primeiros resultados de cada consulta.
- Dados sem stemming: 0.2410
- Dados com stemming: 0.2553

Barplot de precisão por consulta:

![Gráfico de 11 pontos](https://github.com//RafaelBaSantos/COS738-IR-Modelo-Vetorial/blob/avaliacao_ri/result/diagramas/R-Precision comparativo.png?raw=true)

Mean Average Precision (MAP): Média do valor da precisão para os k primeiros documentos recuperados, calculados nos pontos onde um documento relevante é recuperado.
- Dados sem stemming: 0.2530
- Dados com stemming: 0.2711

Mean Reciprocal Rank (MRR): Média de 1/K, onde K é a posição do primeiro documento relevante recuperado
- Dados sem stemming: 0.7958
- Dados com stemming: 0.8344

Discounted Cumulative Gain (DCG): Soma da pontuação dos documentos relevantes, ponderados pela posição do documento entre os recuperados
- Dados sem stemming: 0.7958
- Dados com stemming: 0.8344

Normalized Discounted Cumulative Gain (N-DCG): DCG com valores normalizados pelo caminho de maior DCG possível
- Dados sem stemming: 0.795875420875421
- Dados com stemming: 0.8344276094276094

Os dados e imagens utilizados nos gráficos podem ser encontrados em [/result/diagramas](https://github.com/RafaelBaSantos/COS738-IR-Modelo-Vetorial/tree/avaliacao_ri/result/diagramas).


### Instalação via Pipenv

Esse projeto inclue um Pipfile e um Pipfile.lock, para a gestão de dependencias via Pipenv.

1. Clone o repositório para o seu computador
```bash
git clone https://github.com/RafaelBaSantos/COS738-IR-Modelo-Vetorial
```

2. Navegue até o diretório do projeto
```bash
cd COS738-IR-Modelo-Vetorial
```

3. Instale o Pipenv
```bash
pip install pipenv
```

4. Install os packages
```bash
pipenv install
```
Isso vai instalar todos os pacotes requeridos em uma virtual env. do Pipenv.

5. Ative a virtual env
```bash
pipenv shell
```
Isso vai ativar a virtual env., permitindo que você rode os scripts com as dependências corretas.


### Arquivos de configurações:
Caso necessário, é possível alterar o caminho das pastas que o script lerá a partir dos arquivos da pasta "config":
- PC.CFG: Referente ao Processador de Consultas
- GLI.CFG: Referente ao Gerador da Lista Invertida
- INDEX.CFG: Referente ao Gerador do Modelo
- BUSCA.CFG: Referente ao Buscador

### Rodando os scripts

Ative a virtual env
```bash
pipenv shell
```

Execute o arquivo main.py
```bash
python src\main.py
```
