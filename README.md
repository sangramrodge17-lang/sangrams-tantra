# Sangram's Tantra

A personal AI assistant powered by [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct), Hugging Face Inference API, and Streamlit.

## Deploy on Streamlit Community Cloud

1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
2. Click **Create app**.
3. Select repository: `sangramrodge17-lang/sangrams-tantra`.
4. Select branch: `main`.
5. Set the main file path to `streamlit_app.py`.
6. Click **Deploy**.

## Add the Hugging Face token

The app uses hosted inference, so Streamlit does not download or run PyTorch locally. A Hugging Face access token is required.

1. Open the deployed app.
2. Click **Manage app**.
3. Open **Settings → Secrets**.
4. Add this TOML entry:

```toml
HF_TOKEN = "hf_your_token_here"
```

5. Save and reboot the app.

Create the token at [Hugging Face Settings → Access Tokens](https://huggingface.co/settings/tokens). Use a token with inference permission. Never put the token in GitHub code or send it in chat.

Free inference includes limited usage/credits and may have rate limits. The app no longer needs local PyTorch, Transformers, or model weights.

## Configuration

Optional Streamlit secrets/environment variables:

- `MODEL_ID` — defaults to `Qwen/Qwen2.5-1.5B-Instruct`
- `MAX_NEW_TOKENS` — defaults to `256`
- `SYSTEM_PROMPT` — the assistant's behavior instructions

## License and attribution

Qwen3 open-weight models are released under Apache 2.0 according to the official Qwen repository. Keep the model's license and notices when redistributing or modifying this project. This application code is provided under the MIT License in `LICENSE`.
