#!/bin/bash

# Check if filename is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

filename="$1"
git add "$filename"
git commit -m "$filename"
git push
