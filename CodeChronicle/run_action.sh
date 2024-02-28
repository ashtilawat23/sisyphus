#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Run each script in sequence
python /path/to/analyze_code.py
python /path/to/update_readme.py
python /path/to/create_pr.py