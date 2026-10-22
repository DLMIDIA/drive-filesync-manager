#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Drive & FileSync Manager - Gerenciador Inteligente de Sincronização & Backup
Desenvolvido por: Daniel Júnior Barbosa da Silva (DL MIDIA) & Antigravity AI
"""

from __future__ import annotations

import os
import sys
import subprocess
import shutil
import time
from pathlib import Path


HOME = Path.home()
DESKTOP = HOME / "Desktop"

# Pastas Padrão de Mídia da Agência
DEFAULT_WATCH_DIRS = [
    DESKTOP / "03 - Fotos, Vídeos & Drone",
    DESKTOP / "06 - Capturas e Gravações de Tela",
    DESKTOP / "07 - Backups & Arquivos"
]

# Caminhos do Google Drive no macOS
GOOGLE_DRIVE_LOCATIONS = [
    HOME / "Library/CloudStorage/GoogleDrive-contato@dlmidia.com.br/Discos partilhados",
    HOME / "Library/CloudStorage/GoogleDrive-contato@dlmidia.com.br/O meu disco",
    HOME / "Google Drive",
    Path("/Volumes/GoogleDrive")
]


def find_active_google_drive() -> Path | None:
    for loc in GOOGLE_DRIVE_LOCATIONS:
        if loc.exists() and loc.is_dir():
            return loc
    return None


def generate_ffs_batch_config(source_dir: Path, target_dir: Path, output_file: Path):
    """Gera um arquivo XML de configuração .ffs_batch para o FreeFileSync"""
    xml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<FreeFileSync XmlType="BATCH">
    <MainConfig>
        <Comparison>
            <Variant>TimeAndSize</Variant>
            <Symlinks>Exclude</Symlinks>
            <IgnoreTimeShift>0</IgnoreTimeShift>
        </Comparison>
        <SyncConfig>
            <Variant>Update</Variant>
            <DetectMovedFiles>true</DetectMovedFiles>
            <DeletionPolicy>RecycleBin</DeletionPolicy>
        </SyncConfig>
        <Filter>
            <Include>*</Include>
            <Exclude>
                <Item>*/.DS_Store</Item>
                <Item>*/.localized</Item>
                <Item>*/.Spotlight-V100</Item>
                <Item>*/.Trashes</Item>
                <Item>*.tmp</Item>
                <Item>*.crdownload</Item>
            </Exclude>
        </Filter>
        <FolderPairs>
            <Pair>
                <Left>{source_dir}</Left>
                <Right>{target_dir}</Right>
            </Pair>
        </FolderPairs>
        <BatchConfig>
            <HandleError>Ignore</HandleError>
            <RunMinimized>true</RunMinimized>
            <PostSyncCommand/>
            <LogPath>{HOME}/Library/Logs/DLMIDIA_Sync.log</LogPath>
        </BatchConfig>
    </MainConfig>
</FreeFileSync>
"""
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(xml_content)
    print(f"✓ Configuração FreeFileSync gerada em: {output_file}")


def run_sync(source: Path, target: Path):
    """Executa a sincronização segura via FreeFileSync ou rsync nativo"""
    print(f"\n🚀 Iniciando sincronização: {source.name} ➔ {target.name}...")

    ffs_bin = Path("/Applications/FreeFileSync.app/Contents/MacOS/FreeFileSync")
    batch_config = HOME / ".dlmidia_sync_job.ffs_batch"

    if ffs_bin.exists():
        generate_ffs_batch_config(source, target, batch_config)
        print("Executando sincronização via FreeFileSync...")
        subprocess.run([str(ffs_bin), str(batch_config)])
        print("✓ Sincronização FreeFileSync concluída!")
    else:
        print("FreeFileSync não encontrado em /Applications. Utilizando rsync nativo de alta velocidade...")
        cmd = [
            "rsync", "-avz", "--progress",
            "--exclude=.DS_Store",
            "--exclude=.localized",
            "--exclude=*.tmp",
            "--exclude=*.crdownload",
            f"{source}/", f"{target}/"
        ]
        subprocess.run(cmd)
        print("✓ Sincronização rsync concluída com sucesso!")


def main():
    print("==========================================================")
    print("📁 Drive & FileSync Manager — DL MIDIA")
    print("Sistema de Backup Redundante & Sincronização de Mídias")
    print("==========================================================")

    drive_path = find_active_google_drive()
    if drive_path:
        print(f"✓ Google Drive detectado em: {drive_path}")
    else:
        print("⚠️ Google Drive local não encontrado no caminho padrão.")
        print("Você pode sincronizar para outro volume ou SSD externo.")

    for watch_dir in DEFAULT_WATCH_DIRS:
        if watch_dir.exists() and drive_path:
            dest_dir = drive_path / "00 - DL MIDIA" / "BACKUP_AUTOMATICO" / watch_dir.name
            dest_dir.mkdir(parents=True, exist_ok=True)
            run_sync(watch_dir, dest_dir)

    print("\n🎉 Todas as sincronizações foram finalizadas!")


if __name__ == "__main__":
    main()
