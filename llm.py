from ctransformers import AutoModelForCausalLM

llama = AutoModelForCausalLM.from_pretrained(
    "./models/mistral",
    model_file="mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    model_type="mistral",
    gpu_layers=60,
    context_length=8192,
    temperature=0.3,
)
