# Avaliacao de um Modelo de RI

Esse repositório contém os arquivos referentes a um trabalho da cadeira de Busca e Mineração de Texto.
Essa branch contém, além dos modelo de IR, a comparação do modelo com ou sem o uso do stemmer de Porter.

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
