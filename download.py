from huggingface_hub import snapshot_download

model_ids = [
    "meta-llama/CodeLlama-7b-hf",
    "meta-llama/Llama-2-7b-chat-hf",
    "meta-llama/Meta-Llama-3-8B-Instruct",
    "meta-llama/Meta-Llama-3.1-8B-Instruct",
]

for model_id in model_ids:
    snapshot_download(
        repo_id=model_id,
        local_dir=model_id.split("/")[-1].lower().replace("-", "_"),
        local_dir_use_symlinks=False,
    )
