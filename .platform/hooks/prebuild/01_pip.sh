#!/bin/bash
set -e
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --no-cache-dir -r /var/app/staging/requirements.txt
