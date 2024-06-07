
# Validando arquivos Json a partir de JsonSchemas


### Requisitos

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Python](https://img.shields.io/badge/Python-3.8%2B-E3E3E3)


### Clonando o repositório

```bash
git clone https://github.com/Renatoelho/valid-json.git valid-json
```


### Deploy do ambiente

```bash
cd valid-json/
```

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -U pip setuptools wheel --no-cache-dir && pip install -r requirements.txt --no-cache-dir
```


### Configurando o PYTHONPATH

```bash
export PYTHONPATH=$PWD/models
```

> ***Obs.:*** O PYTHONPATH também pode ser adicionado no ```.bashrc``` utilizando path absoluto do projeto.


### Convertendo os JsonSchemas em Modelos Pydantic

```bash
chmod +x generate_models.sh
```

```bash
sh ./generate_models.sh
```


### Testando aplicação

```bash
python3 app.py "./samples/sample-data.json"
```


# Referências

Installation, **Pydantic.** Disponível em: <https://docs.pydantic.dev/latest/install/>. Acesso em: 07 junho. 2024.

Why use Pydantic?, **Pydantic.** Disponível em: <https://docs.pydantic.dev/latest/why/>. Acesso em: 07 junho. 2024.

Code Generation with datamodel-code-generator, **Pydantic.** Disponível em: <https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/>. Acesso em: 07 junho. 2024.