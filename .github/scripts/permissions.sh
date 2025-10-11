#!/usr/bin/env bash
set +e
source /tmp/safe_run.sh
safe_run "chmod -R u+rwX,go+rX ."
safe_run "find . -type f -not -path './.git/*' -exec chmod ${CHMOD_MODE:-644} {} + || true"
safe_run "find . -type d -not -path './.git/*' -exec chmod 755 {} + || true"
