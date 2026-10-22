# 📁 Drive & FileSync Manager — Automação de Backup e Sincronização

> **Sistema inteligente de sincronização e espelhamento redundante de mídias, gravações de tela e arquivos de agência via Google Drive, FreeFileSync e automações em Python para macOS.**

Desenvolvido por **Daniel Júnior Barbosa da Silva (DL MIDIA)** em coautoria com **Antigravity AI**.

---

[![Platform](https://img.shields.io/badge/Platform-macOS-000000?style=flat-square&logo=apple)](https://apple.com)
[![Google Drive](https://img.shields.io/badge/Cloud-Google%20Drive%20Workspace-34A853?style=flat-square&logo=googledrive)](https://drive.google.com)
[![FreeFileSync](https://img.shields.io/badge/Engine-FreeFileSync%20%2F%20Rsync-green?style=flat-square)](https://freefilesync.org/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

---

## 📌 Visão Geral

Projetado para estúdios, produtoras e agências que lidam diariamente com mídias pesadas (vídeos 4K de drone DJI, fotos RAW, capturas de tela e materiais de clientes).

O **Drive & FileSync Manager** garante que nenhum arquivo fique preso localmente ou sem backup em nuvem:
1. **Detecção Automática:** Localiza automaticamente a partição do Google Drive Workspace conectada ao Mac.
2. **Integração com FreeFileSync:** Gera arquivos de lote `.ffs_batch` sob medida para sincronização em duas vias ou espelhamento com lixeira inteligente.
3. **Fallback Nativo em Rsync:** Se o FreeFileSync não estiver aberto, roda comandos `rsync` de alto desempenho com exclusão de arquivos de cache (`.DS_Store`, arquivos parciais `.tmp`).
4. **Watcher de Cartões de Drone/Câmera:** Detecta quando um cartão SD (com diretório `DCIM` ou `DJI`) é inserido e faz a importação automática para a nuvem.

---

## 🏗️ Estrutura do Projeto

```
drive-filesync-manager/
├── sync_manager.py     # Script principal de sincronização e geração de configs FFS
├── drive_watcher.py    # Daemon de monitoramento contínuo de cartões SD e novos arquivos
├── run_sync.sh         # Atalho de execução rápida em 1 clique
├── configs/            # Modelos de configuração FreeFileSync
├── LICENSE             # Licença MIT Open-Source
└── README.md           # Documentação e instruções de uso
```

---

## 🚀 Como Executar

### 1. Sincronização Imediata
```bash
python3 sync_manager.py
# ou:
./run_sync.sh
```

### 2. Iniciar o Monitor em Segundo Plano (Watcher)
```bash
python3 drive_watcher.py
```

---

## 👨‍💻 Autores & Créditos

- **Autor:** Daniel Júnior Barbosa da Silva
- **Empresa / Marca:** [DL MIDIA](https://dlmidia.com.br)
- **Coautoria:** Antigravity AI (Google DeepMind)
- **Licença:** [MIT License](LICENSE)
