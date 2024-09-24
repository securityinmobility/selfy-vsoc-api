#!/bin/bash

# Base URL of the API
BASE_URL="http://localhost:8000"  # Replace with your actual base URL

# Function to test a single endpoint
test_endpoint() {
    local subdir=$1
    local filename=$2
    local json_file=$3

    # Construct the API endpoint URL
    endpoint="/${subdir}/${filename}"
    url="${BASE_URL}${endpoint}"

    echo "Testing endpoint: $url"

    # Check if the JSON file exists and is not empty
    if [ -s "$json_file" ]; then
        # Send a POST request with the JSON data
        response=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$url" -d @"$json_file" -H "Content-Type: application/json")
    else
        # Send a GET request (assuming the JSON is optional for GET)
        response=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    fi

    # Output the result of the request
    echo "Status: $response"
}

# Base directory containing the subdirectories
BASE_DIR="test-payload"

# Walk through the directories and find JSON files
find "$BASE_DIR" -type f -name "*.json" | while read -r json_file; do
    # Get the subdirectory and filename (without extension) from the JSON file path
    subdir=$(basename "$(dirname "$json_file")")
    filename=$(basename "$json_file" .json)

    # Test the endpoint with the subdir and filename
    test_endpoint "$subdir" "$filename" "$json_file"
done

