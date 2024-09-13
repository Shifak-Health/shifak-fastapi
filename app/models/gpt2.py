import os
import torch
from transformers import GPT2Tokenizer, GPT2Config, GPT2LMHeadModel

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model_path = os.path.join(os.path.dirname(__file__), '../../pretrained_model/content/model_save')

configuration = GPT2Config.from_pretrained(model_path, output_hidden_states=False)
tokenizer = GPT2Tokenizer.from_pretrained(model_path, bos_token='<|startoftext|>', eos_token='<|endoftext|>', pad_token='<|pad|>')
model = GPT2LMHeadModel.from_pretrained(model_path, config=configuration).to(device)

def answer_question(question: str) -> str:
    model.eval()
    prompt = f'<|startoftext|>{question}'
    generated = torch.tensor(tokenizer.encode(prompt)).unsqueeze(0)
    generated = generated.to(device)
    sample_outputs = model.generate(
        generated,
        do_sample=True,
        top_k=50,
        max_length=300,
        min_length=120,
        top_p=0.95,
        temperature=0.7,
        num_return_sequences=3
    )
    return tokenizer.decode(sample_outputs[0], skip_special_tokens=True)