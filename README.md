# Sangram's Tantra

A personal AI assistant powered by [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) and Streamlit.

## Deploy on Streamlit Community Cloud

1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
2. Click **Create app**.
3. Select repository: `sangramrodge17-lang/sangrams-tantra`.
4. Select branch: `main`.
5. Set the main file path to `streamlit_app.py`.
6. Click **Deploy**.

The app downloads the model from Hugging Face when it starts. The first startup can take several minutes, and free CPU hosting may be slow or sleep when unused.

## What this repository contains

- `streamlit_app.py` — the Streamlit chat application
- `app.py` — the earlier Gradio version
- `requirements.txt` — cloud dependencies
- The model weights are **not** stored in this GitHub repository.

## Configuration

Optional environment variables can be added in Streamlit Cloud advanced settings:

- `MODEL_ID` — defaults to `Qwen/Qwen3-1.7B`
- `MAX_NEW_TOKENS` — defaults to `256`
- `SYSTEM_PROMPT` — the assistant's behavior instructions

## Troubleshooting

If the app runs out of memory, set `MODEL_ID` to `Qwen/Qwen3-0.6B` in the Streamlit app secrets/environment settings, or reduce `MAX_NEW_TOKENS` to `128`.

## License and attribution

Qwen3 open-weight models are released under Apache 2.0 according to the official Qwen repository. Keep the model's license and notices when redistributing or modifying this project. This application code is provided under the MIT License in `LICENSE`.
