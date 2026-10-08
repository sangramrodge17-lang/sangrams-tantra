import os
from functools import lru_cache

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL_ID = os.getenv("MODEL_ID", "Qwen/Qwen3-1.7B")
MAX_NEW_TOKENS = int(os.getenv("MAX_NEW_TOKENS", "256"))
SYSTEM_PROMPT = os.getenv(
    "SYSTEM_PROMPT",
    "You are Sangram's Tantra, a helpful, clear, and practical AI assistant. "
    "Answer honestly, explain difficult ideas simply, and say when you are uncertain."
)


@lru_cache(maxsize=1)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
    )
    model.eval()
    return tokenizer, model


def answer(message: str, history: list | None):
    if not message or not message.strip():
        return "Please enter a question."

    tokenizer, model = load_model()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for item in history or []:
        if isinstance(item, dict) and item.get("role") in {"user", "assistant"}:
            content = item.get("content", "")
            if isinstance(content, str) and content.strip():
                messages.append({"role": item["role"], "content": content})

    messages.append({"role": "user", "content": message.strip()})
    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        enable_thinking=False,
        return_tensors="pt",
    )

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


demo = gr.ChatInterface(
    fn=answer,
    title="Sangram's Tantra",
    description="A personal AI assistant powered by Qwen3-1.7B. The first response may take longer while the model loads.",
    examples=[
        "Explain artificial intelligence in simple words.",
        "Help me plan a small business idea.",
        "Write a professional email for me.",
    ],
    textbox=gr.Textbox(
        placeholder="Ask Sangram's Tantra anything...",
        container=True,
        scale=7,
    ),
)

if __name__ == "__main__":
    demo.launch()
