#!/bin/bash
set -euxo pipefail
# make a bigger temp area and make sure it's writable for everyone
mkdir -p /var/tmp/pip
chmod 1777 /var/tmp /var/tmp/pip

# Some tools only read TMPDIR, some read PIP_TMPDIR. Export for this step as well.
export TMPDIR=/var/tmp/pip
export PIP_TMPDIR=/var/tmp/pip

# Optional: purge any pip cache if present (should be off, but just in case)
command -v pip3 >/dev/null 2>&1 && pip3 cache purge || true

# Show disk usage to logs to help debugging if it ever fails again
df -h || true
