import os

import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen3-1.7B")
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "256"))
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are Sangram's Tantra, a helpful, clear, and practical AI assistant. "
    "Answer honestly, explain difficult ideas simply, and say when you are uncertain.",
)

st.set_page_config(page_title="Sangram's Tantra", page_icon="✦", layout="centered")


@st.cache_resource(show_spinner=False)
def load_model():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    dtype = torch.float16 if device == "cuda" else torch.float32
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
    )
    model.to(device)
    model.eval()
    return tokenizer, model, device


def generate_answer(message: str, history: list[dict[str, str]]) -> str:
    tokenizer, model, device = load_model()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": message})

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        enable_thinking=False,
        return_tensors="pt",
    ).to(device)

    with torch.inference_mode():
        output = model.generate(
            inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=True,
            temperature=0.7,
            top_p=0.8,
            repetition_penalty=1.05,
            pad_token_id=tokenizer.eos_token_id,
        )

    new_tokens = output[0][inputs.shape[-1] :]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


st.title("Sangram's Tantra")
st.caption("Your personal AI assistant, powered by Qwen3-1.7B")
st.info("The first answer may take a few minutes while the model downloads and loads.", icon="ℹ️")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Sangram's Tantra anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    history = st.session_state.messages[:-1]
    with st.chat_message("assistant"):
        with st.spinner("Sangram's Tantra is thinking..."):
            try:
                response = generate_answer(prompt, history)
                st.markdown(response)
            except Exception as exc:
                response = "I could not load the model. Please check the app logs and try again."
                st.error(f"{response}\n\nTechnical details: {exc}")

    st.session_state.messages.append({"role": "assistant", "content": response})

with st.sidebar:
    st.header("About")
    st.write("Sangram's Tantra runs Qwen3-1.7B from Hugging Face.")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()
