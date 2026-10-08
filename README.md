# Sangram's Tantra

A personal AI assistant powered by Gemini Flash-Lite, Google AI Studio, and Streamlit.

## Deploy on Streamlit Community Cloud

1. Sign in at [Streamlit Community Cloud](https://share.streamlit.io/) with the GitHub account that can access this repository.
2. Click **Create app**.
3. Select repository: `sangramrodge17-lang/sangrams-tantra`.
4. Select branch: `main`.
5. Set the main file path to `streamlit_app.py`.
6. Click **Deploy**.

## Add the Gemini API key

1. Open [Google AI Studio API Keys](https://aistudio.google.com/apikey).
2. Sign in with your Google account.
3. Click **Create API key** and copy it privately.
4. In Streamlit, open **Manage app → Settings → Secrets**.
5. Remove old `HF_TOKEN` or `GROQ_API_KEY` entries if present.
6. Add exactly:

```toml
GEMINI_API_KEY = "your_gemini_key_here"
```

7. Save and reboot the app.

Never put the API key in GitHub code or send it in chat. Google AI Studio has a free tier with rate limits; Google may require billing for higher limits or some models. This app uses `gemini-2.5-flash-lite`.

## Current model

```text
gemini-2.5-flash-lite
```

The model runs in Google’s cloud, so your computer does not download or run PyTorch.

## Configuration

Optional Streamlit secrets/environment variables:

- `MAX_OUTPUT_TOKENS` — defaults to `512`
- `SYSTEM_PROMPT` — the assistant's behavior instructions

## License and attribution

The application code is provided under the MIT License in `LICENSE`. Gemini is a Google-hosted proprietary model accessed through the Gemini API and is subject to Google’s applicable terms and policies.
