# 🔮 Transformers

**💙 Attention Is All You Need**
Revolutionary architecture based entirely on attention mechanisms. Foundation for modern LLMs like GPT, BERT, and T5. Replaced RNNs as the dominant architecture for sequential data.

---

## 📚 Topics Covered

### Core Concepts
- **Self-Attention Mechanism** - Query, Key, Value
- **Multi-Head Attention** - Parallel attention heads
- **Positional Encoding** - Sequence order information
- **Transformer Architecture** - Encoder-decoder structure
- **Layer Normalization & Residual Connections**
- **Feed-Forward Networks**
- **Masked Attention** - For autoregressive generation
- **Cross-Attention** - Encoder-decoder attention

---

## 🎯 Learning Objectives

By the end of this section, you should be able to:
- [ ] Understand self-attention and scaled dot-product attention
- [ ] Explain multi-head attention mechanism
- [ ] Implement the Transformer architecture
- [ ] Know the difference between encoder-only, decoder-only, and encoder-decoder models
- [ ] Use pre-trained Transformers (BERT, GPT, T5)
- [ ] Fine-tune Transformers for downstream tasks
- [ ] Understand positional encodings and why they're needed

---

## 📝 Key Notes

### [[self-attention|Self-Attention Mechanism]]
- **Query, Key, Value (Q, K, V)** matrices
- Scaled dot-product attention formula
- Attention weights computation
- Why attention solves long-range dependencies

### [[multi-head-attention|Multi-Head Attention]]
- Multiple parallel attention mechanisms
- Different representation subspaces
- Concatenation and linear projection
- Typical: 8-16 heads

### [[positional-encoding|Positional Encoding]]
- Sinusoidal positional encoding
- Learned positional embeddings
- Why Transformers need position information
- Relative vs absolute positions

### [[transformer-architecture|Transformer Architecture]]
- **Encoder:** Self-attention + feed-forward (BERT-style)
- **Decoder:** Masked self-attention + cross-attention + feed-forward (GPT-style)
- **Encoder-Decoder:** Full Transformer (T5-style)
- Layer normalization and residual connections

---

## 💻 Code Examples

**✅ Scaled Dot-Product Attention**
```python
import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(query, key, value, mask=None):
    """
    Args:
        query: [batch, n_heads, seq_len, d_k]
        key: [batch, n_heads, seq_len, d_k]
        value: [batch, n_heads, seq_len, d_v]
        mask: Optional mask for padding or causal attention
    """
    d_k = query.size(-1)
    
    # Attention scores: Q * K^T / sqrt(d_k)
    scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d_k)
    
    # Apply mask (if provided)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -1e9)
    
    # Softmax to get attention weights
    attention_weights = F.softmax(scores, dim=-1)
    
    # Apply attention to values
    output = torch.matmul(attention_weights, value)
    
    return output, attention_weights
```

**✅ Multi-Head Attention**
```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        # Linear projections
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
        
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        
        # Linear projections and split into heads
        Q = self.W_q(query).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        K = self.W_k(key).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        V = self.W_v(value).view(batch_size, -1, self.num_heads, self.d_k).transpose(1, 2)
        
        # Apply attention
        output, attention = scaled_dot_product_attention(Q, K, V, mask)
        
        # Concatenate heads
        output = output.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)
        
        # Final linear projection
        output = self.W_o(output)
        
        return output, attention
```

**✅ Positional Encoding**
```python
class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        super().__init__()
        
        # Create positional encoding matrix
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * 
                           (-math.log(10000.0) / d_model))
        
        # Apply sin to even indices, cos to odd indices
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        
        pe = pe.unsqueeze(0)  # [1, max_len, d_model]
        self.register_buffer('pe', pe)
        
    def forward(self, x):
        # x: [batch_size, seq_len, d_model]
        return x + self.pe[:, :x.size(1)]
```

**✅ Using Pre-trained BERT**
```python
from transformers import BertTokenizer, BertModel

# Load pre-trained BERT
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize and encode text
text = "Transformers are powerful models for NLP."
inputs = tokenizer(text, return_tensors='pt')

# Get embeddings
with torch.no_grad():
    outputs = model(**inputs)
    last_hidden_state = outputs.last_hidden_state  # [batch, seq_len, 768]
    pooled_output = outputs.pooler_output  # [batch, 768]
```

---

## ⚠️ Common Pitfalls

**⚠️ Quadratic Memory Complexity**
- **Problem:** Attention is O(n²) in sequence length
- **Solution:** Use efficient attention variants (FlashAttention, linear attention), limit sequence length, or use sliding window attention

**⚠️ Forgetting Positional Encoding**
- **Problem:** Model has no notion of token order
- **Solution:** Always add positional encodings to input embeddings

**⚠️ Wrong Attention Mask**
- **Problem:** Model sees future tokens (causal modeling) or attends to padding
- **Solution:** Use causal mask for autoregressive tasks, padding mask for batching

**⚠️ Insufficient Warmup**
- **Problem:** Training instability with Adam optimizer
- **Solution:** Use learning rate warmup (typically 4000-10000 steps)

---

## 💡 Best Practices

**💡 Architecture Choices**
- **Encoder-only (BERT):** Classification, NER, question answering
- **Decoder-only (GPT):** Text generation, autoregressive tasks
- **Encoder-Decoder (T5):** Translation, summarization, seq2seq
- **Typical sizes:** d_model=512/768, num_heads=8/12, num_layers=6/12

**💡 Training Strategies**
- Use **learning rate warmup** (linear warmup over first N steps)
- Apply **gradient clipping** (max_norm=1.0)
- Use **label smoothing** (0.1) for classification
- Implement **gradient accumulation** for larger effective batch sizes
- Monitor **learning rate schedule** (cosine decay after warmup)

**💡 Fine-Tuning Tips**
- Start with **lower learning rates** (1e-5 to 5e-5)
- **Freeze lower layers** if dataset is small
- Use **task-specific heads** on top of pre-trained models
- Apply **discriminative learning rates** (lower for early layers)
- **Gradual unfreezing:** Fine-tune top layers first, then unfreeze lower layers

**💡 Optimization**
- Use **AdamW optimizer** (Adam with weight decay)
- Enable **mixed precision training** (FP16/BF16)
- Use **FlashAttention** for memory-efficient attention
- Apply **gradient checkpointing** to trade compute for memory

---

## 🔬 Advanced Topics

**🔮 Efficient Transformers**
- **Linformer:** Linear attention complexity O(n)
- **Reformer:** Locality-sensitive hashing for attention
- **Longformer:** Sparse attention with sliding windows
- **BigBird:** Combination of global, windowed, and random attention
- **FlashAttention:** IO-aware exact attention algorithm

**🔮 Architectural Innovations**
- **Sparse Transformers:** Factorized attention patterns
- **Universal Transformers:** Recurrent processing with ACT
- **Transformer-XL:** Recurrence mechanism for longer context
- **Perceiver:** Cross-attention to fixed latent array
- **Switch Transformer:** Sparse mixture of experts (MoE)

**🔮 Vision Transformers (ViT)**
- Split image into patches (16x16 or 32x32)
- Linear projection of patches as tokens
- Self-attention over image patches
- State-of-the-art on ImageNet when pre-trained on large datasets

**🔮 Pre-Training Objectives**
- **Masked Language Modeling (MLM):** BERT-style bidirectional
- **Causal Language Modeling (CLM):** GPT-style autoregressive
- **Prefix Language Modeling:** T5-style span corruption
- **Contrastive Learning:** CLIP-style image-text alignment

---

## 🔗 Related Topics

- [[04-Deep-Learning/LLMs/README|Large Language Models]] - Scaled-up Transformers
- [[04-Deep-Learning/RNNs-LSTMs/README|RNNs & LSTMs]] - Alternative for sequences
- [[05-NLP/Advanced/README|Advanced NLP]] - Transformer applications
- [[04-Deep-Learning/Neural-Networks/README|Neural Networks]] - Foundational concepts

---

## 📚 Resources

**Papers:**
- **"Attention Is All You Need"** (Vaswani et al., 2017) - Original Transformer
- "BERT: Pre-training of Deep Bidirectional Transformers" (Devlin et al., 2018)
- "Language Models are Unsupervised Multitask Learners" (GPT-2, 2019)
- "Exploring the Limits of Transfer Learning with T5" (2019)
- "An Image is Worth 16x16 Words" (ViT, 2020)
- "FlashAttention: Fast and Memory-Efficient Exact Attention" (2022)

**Courses:**
- Stanford CS224n: NLP with Deep Learning (Transformer lectures)
- Hugging Face NLP Course
- The Illustrated Transformer (Jay Alammar's blog)

**Libraries:**
- **Hugging Face Transformers** - Pre-trained models
- **PyTorch/TensorFlow** - Custom implementations
- **FlashAttention** - Optimized attention kernels
- **xFormers** - Facebook's efficient transformers

**Key Resources:**
- The Annotated Transformer (Harvard NLP)
- The Illustrated Transformer (Jay Alammar)
- Attention? Attention! (Lilian Weng's blog)

---

## 📊 Transformer Variants Comparison

| Model | Type | Use Case | Key Feature |
|-------|------|----------|-------------|
| **BERT** | Encoder-only | Classification, NER | Bidirectional, MLM |
| **GPT** | Decoder-only | Text generation | Autoregressive, CLM |
| **T5** | Encoder-Decoder | Seq2seq tasks | Text-to-text framework |
| **ViT** | Encoder-only | Image classification | Patch embeddings |
| **CLIP** | Dual encoder | Image-text | Contrastive learning |

---

**Tags:** #transformers #attention #bert #gpt #self-attention #positional-encoding
**Difficulty:** 🔥🔥🔥🔥 Expert
**Last Updated:** 2026-11-11
