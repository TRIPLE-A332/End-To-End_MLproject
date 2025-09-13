#!/bin/bash
set -e
if command -v dnf >/dev/null 2>&1; then
  dnf install -y gcc gcc-c++ make
elif command -v yum >/dev/null 2>&1; then
  yum install -y gcc gcc-c++ make
fi
