
import json
from sys import argv

from pydantic import ValidationError

from models.jsonschema01 import JsonShema01


json_file_path = argv[1]

def read_json_file() -> dict:
    try:
        with open(json_file_path, "r") as file:
            data_dict = json.load(file)
        return data_dict
    except FileNotFoundError:
        raise ValueError(f"O arquivo {json_file_path} não foi encontrado.")
    except json.JSONDecodeError as erro:
        raise ValueError(f"Erro ao decodificar o JSON: {erro}")

def valid_json(json_content: dict) -> dict:
    try:
        _ = JsonShema01(**json_content)
        return {"json": "JSON é válido!"}
    except ValidationError as error:
        errors = []
        for error in error.errors():
            error_info = {
                "local": error["loc"][0],
                "mensagem": error["msg"],
                "tipo": error["type"]
            }
            errors.append(error_info)
        return errors


if __name__ == "__main__":
    content_json = read_json_file()

    print("Conteúdo Json original:")
    print(content_json)
    print("*"*100)

    test = valid_json(content_json)

    print("Resultado Validação Json:")
    print(test)