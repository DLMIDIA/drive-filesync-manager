#!/bin/bash
# Script de disparo rápido da sincronização
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
python3 "$DIR/sync_manager.py"
