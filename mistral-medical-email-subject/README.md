---
base_model: mistralai/Mistral-7B-Instruct-v0.1
library_name: peft
model_name: mistral-medical-email-subject
tags:
- base_model:adapter:mistralai/Mistral-7B-Instruct-v0.1
- lora
- sft
- transformers
- trl
licence: license
pipeline_tag: text-generation
---

# Model Card for mistral-medical-email-subject

This model is a fine-tuned version of [mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="None", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with SFT.

### Framework versions

- PEFT 0.17.1
- TRL: 0.24.0
- Transformers: 4.57.1
- Pytorch: 2.8.0+cu126
- Datasets: 4.0.0
- Tokenizers: 0.22.1