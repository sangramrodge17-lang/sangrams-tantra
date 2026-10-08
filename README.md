---
title: Sangram's Tantra
emoji: ""
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.20.0
app_file: app.py
pinned: false
---

# Sangram's Tantra

A personal AI assistant powered by [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) and Gradio.

## What this repository contains

- `app.py` — the web chat application
- `requirements.txt` — cloud dependencies
- The model weights are **not** stored in this GitHub repository. They are downloaded from Hugging Face when the app starts.

## Deploy for free on Hugging Face Spaces

1. Create a new **Gradio Space** on [Hugging Face Spaces](https://huggingface.co/new-space).
2. Choose **CPU Basic** hardware for the first test.
3. Upload these files, or connect/sync this GitHub repository.
4. Wait for the Space to build and open its public URL.
5. The first response may take time because the model must download and load.

Free CPU Spaces may be slow and can sleep after inactivity. Upgrade hardware only if you need faster or always-on service.

## Configuration

You can set these environment variables in the Space settings:

- `MODEL_ID` — defaults to `Qwen/Qwen3-1.7B`
- `MAX_NEW_TOKENS` — defaults to `256`
- `SYSTEM_PROMPT` — the assistant's behavior instructions

## License and attribution

Qwen3 open-weight models are released under Apache 2.0 according to the official Qwen repository. Keep the model's license and notices when redistributing or modifying this project. This application code is provided under the MIT License in `LICENSE`.

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
