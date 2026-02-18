#!/bin/bash

# Prompt for input
read -p "Enter problem name: " input

# Trim leading/trailing whitespace
input="$(echo "$input" | sed 's/^ *//;s/ *$//')"

# Validate input
if [ -z "$input" ]; then
    echo "Error: Input cannot be empty."
    exit 1
fi

# Construct filename
filename="NeetCode ${input}.py"

# Prevent overwrite
if [ -e "$filename" ]; then
    echo "Error: File '$filename' already exists."
    exit 1
fi

# Create file
touch "$filename"

echo "Created: $filename"