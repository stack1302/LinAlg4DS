#!/usr/bin/env bash
set +e
find . -type d -not -path './.git/*' -exec chmod 755 {} +
find . -type f -not -path './.git/*' -exec chmod ${CHMOD_MODE:-644} {} +
chmod +x .github/scripts/*.sh 2>/dev/null || true
