# Sangram's Tantra

A personal AI assistant powered by Llama 3.1 8B, the Groq API, and Streamlit.

## Deploy on Streamlit Community Cloud

1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
2. Click **Create app**.
3. Select repository: `sangramrodge17-lang/sangrams-tantra`.
4. Select branch: `main`.
5. Set the main file path to `streamlit_app.py`.
6. Click **Deploy**.

## Add the Groq API key

1. Create a free developer account at [Groq Console](https://console.groq.com/).
2. Open [Groq API Keys](https://console.groq.com/keys).
3. Create an API key and copy it privately.
4. In Streamlit, open **Manage app → Settings → Secrets**.
5. Add exactly:

```toml
GROQ_API_KEY = "gsk_your_key_here"
```

6. Save and reboot the app.

Never put the API key in GitHub code or send it in chat. Groq’s free developer tier has rate and usage limits; do not add billing unless you choose to do so.

## Current model

The app uses Groq’s fast hosted model:

```text
llama-3.1-8b-instant
```

The model runs in the cloud, so your computer does not download or run Qwen/PyTorch.

## Configuration

Optional Streamlit secrets/environment variables:

- `MAX_NEW_TOKENS` — defaults to `512`
- `SYSTEM_PROMPT` — the assistant's behavior instructions

## License and attribution

The application code is provided under the MIT License in `LICENSE`. The hosted Llama model is provided by Groq/Meta under its applicable terms; review the current model and API terms before commercial use.
