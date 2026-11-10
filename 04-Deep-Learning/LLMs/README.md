# 🤖 Large Language Models (LLMs)

> [!blue] 💙 **Foundation Models**
> Large-scale pre-trained language models that exhibit emergent capabilities. Learn about GPT, BERT, T5, LLaMA, and how to work with billion-parameter models.

---

## 📚 Topics Covered

### Core Concepts
- **Pre-training Objectives** - MLM, CLM, span corruption
- **Scaling Laws** - Model size, data, compute relationships
- **Emergent Abilities** - In-context learning, chain-of-thought
- **Popular Models** - GPT-4, Claude, LLaMA, BERT, T5
- **Fine-Tuning Methods** - Full fine-tuning, LoRA, QLoRA, PEFT
- **Prompting Techniques** - Zero-shot, few-shot, chain-of-thought
- **Alignment** - RLHF, DPO, constitutional AI
- **Evaluation** - Perplexity, downstream tasks, benchmarks

---

## 🎯 Learning Objectives

By the end of this section, you should be able to:
- [ ] Understand how LLMs are pre-trained at scale
- [ ] Use pre-trained LLMs via APIs (OpenAI, Anthropic, etc.)
- [ ] Fine-tune LLMs on custom datasets
- [ ] Apply parameter-efficient fine-tuning (LoRA, QLoRA)
- [ ] Design effective prompts for LLMs
- [ ] Understand RLHF and alignment techniques
- [ ] Evaluate LLM performance on benchmarks
- [ ] Deploy LLMs for production use

---

## 📝 Key Notes

### [[llm-architectures|LLM Architectures]]
- **GPT Family** (GPT-3, GPT-4) - Decoder-only autoregressive
- **BERT Family** - Encoder-only bidirectional
- **T5/FLAN** - Encoder-decoder
- **LLaMA/Mistral** - Open-source decoder models
- **Claude/Gemini** - Commercial frontier models

### [[pre-training|Pre-Training]]
- Massive web-scale datasets (CommonCrawl, Books, Code)
- Self-supervised learning objectives
- Compute requirements (thousands of GPUs for months)
- Scaling laws (Chinchilla, Kaplan)

### [[fine-tuning-methods|Fine-Tuning Methods]]
- **Full Fine-Tuning:** Update all parameters
- **LoRA:** Low-Rank Adaptation (parameter-efficient)
- **QLoRA:** Quantized LoRA (4-bit)
- **Prefix Tuning:** Learn soft prompts
- **Prompt Tuning:** Optimize prompt embeddings

### [[alignment-techniques|Alignment & RLHF]]
- Supervised fine-tuning (SFT)
- Reward modeling from human feedback
- Proximal Policy Optimization (PPO)
- Direct Preference Optimization (DPO)
- Constitutional AI

### [[prompting-strategies|Prompting Strategies]]
- Zero-shot, few-shot, many-shot
- Chain-of-Thought (CoT)
- ReAct (Reasoning + Acting)
- Tree of Thoughts (ToT)
- Self-consistency

---

## 💻 Code Examples

> [!green] ✅ **Using OpenAI GPT API**
> ```python
> import openai
> 
> openai.api_key = "your-api-key"
> 
> response = openai.ChatCompletion.create(
>     model="gpt-4",
>     messages=[
>         {"role": "system", "content": "You are a helpful assistant."},
>         {"role": "user", "content": "Explain quantum computing in simple terms."}
>     ],
>     temperature=0.7,
>     max_tokens=500
> )
> 
> print(response.choices[0].message.content)
> ```

> [!green] ✅ **Loading LLaMA with Hugging Face**
> ```python
> from transformers import AutoTokenizer, AutoModelForCausalLM
> import torch
> 
> # Load model and tokenizer
> model_name = "meta-llama/Llama-2-7b-chat-hf"
> tokenizer = AutoTokenizer.from_pretrained(model_name)
> model = AutoModelForCausalLM.from_pretrained(
>     model_name,
>     torch_dtype=torch.float16,
>     device_map="auto"
> )
> 
> # Generate text
> prompt = "Explain the theory of relativity:"
> inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
> 
> with torch.no_grad():
>     outputs = model.generate(
>         **inputs,
>         max_new_tokens=200,
>         temperature=0.7,
>         top_p=0.9,
>         do_sample=True
>     )
> 
> text = tokenizer.decode(outputs[0], skip_special_tokens=True)
> print(text)
> ```

> [!green] ✅ **Fine-Tuning with LoRA**
> ```python
> from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
> from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
> from datasets import load_dataset
> 
> # Load base model
> model = AutoModelForCausalLM.from_pretrained(
>     "meta-llama/Llama-2-7b-hf",
>     load_in_8bit=True,
>     device_map="auto"
> )
> 
> # Prepare model for training
> model = prepare_model_for_kbit_training(model)
> 
> # LoRA configuration
> lora_config = LoraConfig(
>     r=8,  # Rank
>     lora_alpha=32,
>     target_modules=["q_proj", "v_proj"],
>     lora_dropout=0.05,
>     bias="none",
>     task_type="CAUSAL_LM"
> )
> 
> # Apply LoRA
> model = get_peft_model(model, lora_config)
> model.print_trainable_parameters()  # Shows only ~0.1% params trainable
> 
> # Training arguments
> training_args = TrainingArguments(
>     output_dir="./llama-lora",
>     per_device_train_batch_size=4,
>     gradient_accumulation_steps=4,
>     learning_rate=2e-4,
>     num_train_epochs=3,
>     logging_steps=10,
>     save_strategy="epoch"
> )
> 
> # Train
> trainer = Trainer(
>     model=model,
>     args=training_args,
>     train_dataset=train_dataset,
>     data_collator=data_collator
> )
> 
> trainer.train()
> ```

> [!green] ✅ **Chain-of-Thought Prompting**
> ```python
> # Zero-shot CoT
> prompt = """
> Question: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. 
> Each can has 3 tennis balls. How many tennis balls does he have now?
> 
> Let's think step by step:
> """
> 
> # Few-shot CoT
> prompt = """
> Question: Mary has 3 apples. She buys 2 more. How many does she have?
> Answer: Let's think step by step.
> 1. Mary starts with 3 apples
> 2. She buys 2 more
> 3. 3 + 2 = 5
> Therefore, Mary has 5 apples.
> 
> Question: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. 
> Each can has 3 tennis balls. How many tennis balls does he have now?
> Answer: Let's think step by step.
> """
> ```

---

## ⚠️ Common Pitfalls

> [!red] ⚠️ **Not Using Prompt Templates**
> - **Problem:** Different models expect different formats (Llama-2, ChatML, etc.)
> - **Solution:** Use model-specific chat templates from tokenizer

> [!red] ⚠️ **Ignoring Context Window Limits**
> - **Problem:** Truncation or errors when input exceeds max tokens
> - **Solution:** Track token count, implement chunking strategies

> [!red] ⚠️ **Overfitting During Fine-Tuning**
> - **Problem:** Model memorizes training data, loses general capabilities
> - **Solution:** Use LoRA, small learning rates, early stopping, larger datasets

> [!red] ⚠️ **Not Setting Temperature/Top-p**
> - **Problem:** Too deterministic (temp=0) or too random (temp=1)
> - **Solution:** temperature=0.7, top_p=0.9 for balanced generation

---

## 💡 Best Practices

> [!yellow] 💡 **Choosing a Model**
> - **API models:** GPT-4, Claude 3.5 for best performance
> - **Open models:** LLaMA 2, Mistral 7B for deployment control
> - **Small models:** Phi-3, Gemma 2B for edge devices
> - **Code:** CodeLlama, StarCoder for programming tasks

> [!yellow] 💡 **Efficient Inference**
> - Use **quantization** (8-bit, 4-bit) to reduce memory
> - Enable **Flash Attention 2** for faster attention
> - Apply **KV cache** optimization
> - Use **vLLM** or **TGI** for production serving
> - Implement **batching** for throughput

> [!yellow] 💡 **Fine-Tuning Strategy**
> 1. **Start with prompting** - Try zero-shot and few-shot first
> 2. **Use LoRA/QLoRA** - Parameter-efficient, prevents catastrophic forgetting
> 3. **Small learning rates** - 1e-5 to 1e-4
> 4. **Monitor validation loss** - Stop early if diverging
> 5. **Keep base model frozen** - Only train adapters unless necessary

> [!yellow] 💡 **Prompt Engineering**
> - Be **specific and detailed** in instructions
> - Use **examples** (few-shot) for complex tasks
> - Request **step-by-step reasoning** (Chain-of-Thought)
> - Specify **output format** (JSON, markdown, etc.)
> - **Iterate** on prompts based on outputs

---

## 🔬 Advanced Topics

> [!purple] 🔮 **Scaling Laws**
> - **Kaplan Scaling Laws:** Performance scales with model size, data, compute
> - **Chinchilla Optimal:** More data, smaller model is better than less data, larger model
> - **Emergent Abilities:** Capabilities appear suddenly at scale (few-shot learning, reasoning)

> [!purple] 🔮 **Advanced Fine-Tuning**
> - **QLoRA:** 4-bit quantization + LoRA (fine-tune 70B on single GPU)
> - **PEFT Methods:** Adapter layers, IA3, (IA)³
> - **Mixture of LoRAs:** Multiple task-specific LoRA adapters
> - **Continuous Pre-training:** Adapt to new domain with raw text

> [!purple] 🔮 **Alignment Methods**
> - **RLHF:** Reward model + PPO for human preference learning
> - **DPO (Direct Preference Optimization):** Simpler alternative to RLHF
> - **Constitutional AI:** Self-critique and refinement
> - **RLAIF:** AI feedback instead of human feedback

> [!purple] 🔮 **Inference Optimization**
> - **Speculative Decoding:** Use small model to draft, large model to verify
> - **Flash Attention:** Memory-efficient attention computation
> - **Continuous Batching:** Dynamic batching for variable-length sequences
> - **PagedAttention:** Efficient KV cache management (vLLM)

> [!purple] 🔮 **Multimodal LLMs**
> - **GPT-4V, Gemini Pro Vision:** Vision + language
> - **CLIP:** Contrastive image-text pretraining
> - **LLaVA:** Visual instruction tuning
> - **Flamingo:** Few-shot visual question answering

---

## 🔗 Related Topics

- [[04-Deep-Learning/Transformers/README|Transformers]] - Architecture foundation
- [[06-AI-Systems/Prompt-Engineering/README|Prompt Engineering]] - Effective prompting
- [[06-AI-Systems/RAG/README|RAG]] - Retrieval-augmented generation
- [[07-MLOps-Deployment/LLMOps/README|LLMOps]] - Deploying LLMs

---

## 📚 Resources

**Papers:**
- "Language Models are Few-Shot Learners" (GPT-3, 2020)
- "LLaMA: Open and Efficient Foundation Language Models" (2023)
- "LoRA: Low-Rank Adaptation of Large Language Models" (2021)
- "QLoRA: Efficient Finetuning of Quantized LLMs" (2023)
- "Training language models to follow instructions with human feedback" (InstructGPT, 2022)
- "Direct Preference Optimization" (DPO, 2023)

**Courses:**
- Stanford CS224n: NLP with Deep Learning
- DeepLearning.AI LLM courses
- Hugging Face LLM Course

**Benchmarks:**
- **MMLU:** Massive Multitask Language Understanding
- **HumanEval:** Code generation
- **TruthfulQA:** Truthfulness
- **BBH (BIG-Bench Hard):** Challenging reasoning tasks
- **Chatbot Arena:** Human preference rankings

**Tools & Libraries:**
- **Hugging Face Transformers:** Model hub and APIs
- **vLLM:** High-throughput inference
- **Text Generation Inference (TGI):** HuggingFace serving
- **Ollama:** Run LLMs locally
- **LM Studio:** GUI for local LLMs
- **LitGPT:** Lightweight LLM implementations

**APIs:**
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Google (Gemini, PaLM)
- Cohere
- Together AI, Anyscale (open models)

---

## 📊 Model Comparison

| Model | Size | Type | Context | Strength |
|-------|------|------|---------|----------|
| **GPT-4** | Unknown | Decoder | 128K | Best overall, reasoning |
| **Claude 3.5** | Unknown | Decoder | 200K | Long context, coding |
| **LLaMA 3** | 8B-70B | Decoder | 8K | Open, efficient |
| **Mistral 7B** | 7B | Decoder | 8K-32K | Open, fast, capable |
| **Gemini Pro** | Unknown | Decoder | 32K-1M | Multimodal, long context |

---

**Tags:** #llm #large-language-models #gpt #bert #llama #fine-tuning #lora #rlhf
**Difficulty:** 🔥🔥🔥🔥 Expert
**Last Updated:** 2026-11-11
