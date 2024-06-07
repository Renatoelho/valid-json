#!/bin/bash

path_jsonschemas="$(dirname "$(realpath "$0")")/jsonschemas"
path_models="$(dirname "$(realpath "$0")")/models"

list_jsonschemas() {
    find "$path_jsonschemas" -name "*.json" -type f
}

jsonschema_files=$(list_jsonschemas)
if [ -z "$jsonschema_files" ]; then
    echo "Não foram encontrados JsonSchemas para conversão."
    exit 1
fi

for jsonschema in $jsonschema_files; do
    input_jsonschema="$jsonschema"
    output_model="$path_models/$(basename "$jsonschema" .json).py"
    datamodel-codegen \
      --input "$input_jsonschema" \
      --input-file-type jsonschema \
      --output "$output_model"
done

echo "Modelo(s) Pydantic gerado(s) com sucesso!"
