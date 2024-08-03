#!/bin/bash

INPUT_DIR="../src/jsonschema"
OUTPUT_DIR="endpoints"

echo "Warning: This script will delete the current contents of the directory $OUTPUT_DIR."
read -p "Are you sure you want to proceed? (y/n): " CONFIRM

# Check if the user input is 'y' or 'n'
if [ "$CONFIRM" = "y" ]; then
    echo "Deleting contents of $OUTPUT_DIR..."
    rm -rf "$OUTPUT_DIR"/*
    echo -e "Directory contents deleted.\n"
elif [ "$CONFIRM" = "n" ]; then
    echo "Operation canceled."
else
    echo "Invalid input. Please enter 'y' or 'n'."
fi

generate-schema-doc --config-file .jsonschema-doc-conf.json ../src/jsonschema endpoints

DOC_PATHS=$(find "$OUTPUT_DIR" -type f -name "*.md")
echo "$DOC_PATH"

for DOC_PATH in $DOC_PATHS; do
  DOC=$(basename "$DOC_PATH")
  SCHEMA=$(echo "$DOC" | sed 's/\.md$/.json/')
  SCHEMA_PATH=$(find "$INPUT_DIR" -type f -name "$SCHEMA")
  DIR_NAME=$(basename "$(dirname "$SCHEMA_PATH")")
  mkdir -p "endpoints/$DIR_NAME"
  mv "endpoints/$DOC" "endpoints/$DIR_NAME/"
done

echo "Endpoint Documentation created."
