#!/bin/bash

# Read the lines of the original and changed files into arrays
readarray -t original_lines < he.txt
readarray -t changed_lines < she.txt

# Loop through each line of the files and tokenize them into words
for i in "${!original_lines[@]}"; do
    original_line="${original_lines[$i]}"
    changed_line="${changed_lines[$i]}"
    original_words=($original_line)
    changed_words=($changed_line)
    for j in "${!original_words[@]}"; do
        original_word="${original_words[$j]}"
        changed_word="${changed_words[$j]}"
        if [[ "$original_word" != "$changed_word" ]]; then
            echo "Changed word: $original_word"
            echo "Changed to: $changed_word"
            echo ""
        fi
    done
done
