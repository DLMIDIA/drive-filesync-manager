#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Drive & FileSync Manager - Watcher Daemon de Mídias e Cartões SD
Detecta inserção de mídias de câmera/drone ou novos arquivos e sincroniza automaticamente.
Desenvolvido por: Daniel Júnior Barbosa da Silva (DL MIDIA) & Antigravity AI
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from sync_manager import find_active_google_drive, run_sync


VOLUMES_DIR = Path("/Volumes")


def check_external_cards():
    """Detecta se algum cartão SD de Drone (DJI) ou Câmera foi montado no Mac"""
    if not VOLUMES_DIR.exists():
        return []

    detected = []
    for vol in VOLUMES_DIR.iterdir():
        if vol.name in ("Macintosh HD", "GoogleDrive", "Recovery"):
            continue

        dcim = vol / "DCIM"
        dji = vol / "DJI"
        if dcim.exists() or dji.exists():
            detected.append(vol)

    return detected


def watch_loop():
    print("👀 Monitor de mídias DL MIDIA iniciado...")
    print("Aguardando inserção de cartões SD (DJI / Câmeras) ou novos arquivos...")

    seen_cards = set()

    try:
        while True:
            cards = check_external_cards()
            for card in cards:
                if card.name not in seen_cards:
                    print(f"\n📸 Cartão de memória detectado: {card.name}")
                    drive = find_active_google_drive()
                    if drive:
                        target = drive / "00 - DL MIDIA" / "IMPORTACAO_CARTAO" / card.name
                        target.mkdir(parents=True, exist_ok=True)
                        run_sync(card, target)
                        seen_cards.add(card.name)

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nWatcher encerrado pelo usuário.")


if __name__ == "__main__":
    watch_loop()
