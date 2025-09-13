#!/bin/bash
set -euo pipefail
mkdir -p /var/app/tmp
chmod 1777 /var/app/tmp
# Send all /tmp writes to the big EBS volume:
if ! mountpoint -q /tmp; then
  mount --bind /var/app/tmp /tmp
fi
