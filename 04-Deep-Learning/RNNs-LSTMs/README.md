# 🔄 Recurrent Neural Networks (RNNs) & LSTMs

> [!blue] 💙 **Sequential Data Processing**
> Recurrent Neural Networks and Long Short-Term Memory networks for processing sequential data. Learn about temporal dependencies, vanishing gradients, and sequence modeling.

---

## 📚 Topics Covered

### Core Concepts
- **Vanilla RNNs** - Basic recurrent architecture
- **LSTM (Long Short-Term Memory)** - Gated recurrent units
- **GRU (Gated Recurrent Unit)** - Simplified LSTM
- **Bidirectional RNNs** - Processing sequences in both directions
- **Sequence-to-Sequence Models** - Encoder-decoder architecture
- **Attention Mechanism** - Focusing on relevant parts
- **Applications** - Time series, NLP, speech recognition

---

## 🎯 Learning Objectives

By the end of this section, you should be able to:
- [ ] Understand how RNNs process sequential data
- [ ] Explain the vanishing gradient problem in RNNs
- [ ] Implement LSTMs and GRUs in PyTorch/TensorFlow
- [ ] Build sequence-to-sequence models
- [ ] Apply attention mechanisms
- [ ] Use RNNs for time series forecasting
- [ ] Understand when to use RNNs vs Transformers

---

## 📝 Key Notes

### [[rnn-basics|RNN Basics]]
- Recurrent connections and hidden states
- Backpropagation Through Time (BPTT)
- Vanishing/exploding gradient problem

### [[lstm-architecture|LSTM Architecture]]
- **Gates:** Forget gate, input gate, output gate
- **Cell state:** Long-term memory
- How LSTMs solve vanishing gradients

### [[gru-architecture|GRU (Gated Recurrent Unit)]]
- Simplified alternative to LSTM
- Reset gate and update gate
- Fewer parameters, faster training

### [[seq2seq-models|Sequence-to-Sequence]]
- Encoder-decoder architecture
- Applications: translation, summarization
- Teacher forcing during training

### [[attention-mechanism|Attention Mechanism]]
- Bahdanau attention (additive)
- Luong attention (multiplicative)
- Attention weights and alignment

---

## 💻 Code Examples

> [!green] ✅ **Simple RNN in PyTorch**
> ```python
> import torch
> import torch.nn as nn
> 
> class SimpleRNN(nn.Module):
>     def __init__(self, input_size, hidden_size, output_size, num_layers=1):
>         super(SimpleRNN, self).__init__()
>         self.hidden_size = hidden_size
>         self.num_layers = num_layers
>         
>         # RNN layer
>         self.rnn = nn.RNN(input_size, hidden_size, num_layers, 
>                          batch_first=True)
>         
>         # Output layer
>         self.fc = nn.Linear(hidden_size, output_size)
>         
>     def forward(self, x):
>         # Initialize hidden state
>         h0 = torch.zeros(self.num_layers, x.size(0), 
>                         self.hidden_size).to(x.device)
>         
>         # Forward propagate RNN
>         out, hidden = self.rnn(x, h0)
>         
>         # Decode the hidden state of the last time step
>         out = self.fc(out[:, -1, :])
>         return out
> ```

> [!green] ✅ **LSTM for Sequence Classification**
> ```python
> class LSTMClassifier(nn.Module):
>     def __init__(self, vocab_size, embedding_dim, hidden_dim, 
>                  output_dim, n_layers, dropout):
>         super().__init__()
>         
>         # Embedding layer
>         self.embedding = nn.Embedding(vocab_size, embedding_dim)
>         
>         # LSTM layer
>         self.lstm = nn.LSTM(embedding_dim, hidden_dim, n_layers,
>                            batch_first=True, dropout=dropout,
>                            bidirectional=True)
>         
>         # Fully connected layer
>         self.fc = nn.Linear(hidden_dim * 2, output_dim)
>         self.dropout = nn.Dropout(dropout)
>         
>     def forward(self, text):
>         # text shape: [batch_size, seq_len]
>         embedded = self.dropout(self.embedding(text))
>         
>         # LSTM
>         output, (hidden, cell) = self.lstm(embedded)
>         
>         # Concatenate final forward and backward hidden states
>         hidden = torch.cat((hidden[-2,:,:], hidden[-1,:,:]), dim=1)
>         hidden = self.dropout(hidden)
>         
>         return self.fc(hidden)
> ```

> [!green] ✅ **Sequence-to-Sequence with Attention**
> ```python
> class Seq2SeqWithAttention(nn.Module):
>     def __init__(self, encoder, decoder, device):
>         super().__init__()
>         self.encoder = encoder
>         self.decoder = decoder
>         self.device = device
>         
>     def forward(self, src, trg, teacher_forcing_ratio=0.5):
>         # src: [batch_size, src_len]
>         # trg: [batch_size, trg_len]
>         
>         batch_size = src.shape[0]
>         trg_len = trg.shape[1]
>         trg_vocab_size = self.decoder.output_dim
>         
>         # Tensor to store decoder outputs
>         outputs = torch.zeros(batch_size, trg_len, 
>                              trg_vocab_size).to(self.device)
>         
>         # Encoder
>         encoder_outputs, hidden = self.encoder(src)
>         
>         # First input to decoder is <sos> token
>         input = trg[:, 0]
>         
>         for t in range(1, trg_len):
>             # Decoder with attention
>             output, hidden, attention = self.decoder(
>                 input, hidden, encoder_outputs)
>             
>             outputs[:, t] = output
>             
>             # Teacher forcing
>             teacher_force = random.random() < teacher_forcing_ratio
>             input = trg[:, t] if teacher_force else output.argmax(1)
>         
>         return outputs
> ```

---

## ⚠️ Common Pitfalls

> [!red] ⚠️ **Vanishing Gradient Problem**
> - **Problem:** Vanilla RNNs struggle with long sequences (gradients vanish)
> - **Solution:** Use LSTM or GRU; apply gradient clipping; use shorter sequences

> [!red] ⚠️ **Exploding Gradients**
> - **Problem:** Gradients grow exponentially during BPTT
> - **Solution:** Gradient clipping (`torch.nn.utils.clip_grad_norm_`)

> [!red] ⚠️ **Overfitting on Small Sequences**
> - **Problem:** Model memorizes training sequences
> - **Solution:** Use dropout, regularization, data augmentation

> [!red] ⚠️ **Slow Training**
> - **Problem:** Sequential processing prevents parallelization
> - **Solution:** Use Transformers for long sequences; use bidirectional RNNs only when necessary

---

## 💡 Best Practices

> [!yellow] 💡 **Choosing RNN Variants**
> - **LSTM:** Default choice for most sequence tasks
> - **GRU:** Faster, fewer parameters, similar performance to LSTM
> - **Vanilla RNN:** Only for very short sequences
> - **Bidirectional:** When full sequence is available (not streaming)

> [!yellow] 💡 **Training Tips**
> - Always use **gradient clipping** (threshold ~1.0)
> - Apply **dropout** between RNN layers (0.2-0.5)
> - Use **teacher forcing** with decay schedule for seq2seq
> - Start with **small learning rates** (1e-4 to 1e-3)
> - **Batch padding:** Pad sequences to same length, use pack_padded_sequence

> [!yellow] 💡 **Sequence Length Management**
> - **Truncate** very long sequences (>500 tokens)
> - Use **sliding windows** for very long sequences
> - Consider **hierarchical models** for documents
> - Use **Transformers** if sequences are >1000 tokens

> [!yellow] 💡 **When NOT to Use RNNs**
> - Very long sequences (>1000 tokens) → Use Transformers
> - Parallel processing needed → Use CNNs or Transformers
> - No temporal order (bag of words) → Use feedforward networks

---

## 🔬 Advanced Topics

> [!purple] 🔮 **Advanced Architectures**
> - **Stacked LSTMs:** Multiple LSTM layers for hierarchical features
> - **Peephole Connections:** Cell state directly influences gates
> - **Layer Normalization:** Stabilize training in RNNs
> - **Highway Networks:** Skip connections in RNNs

> [!purple] 🔮 **Attention Mechanisms**
> - **Bahdanau (Additive) Attention:** Original attention for NMT
> - **Luong (Multiplicative) Attention:** More efficient variant
> - **Self-Attention:** Attention within same sequence (precursor to Transformers)
> - **Multi-Head Attention:** Parallel attention mechanisms

> [!purple] 🔮 **Specialized RNN Applications**
> - **Time Series Forecasting:** Multi-step prediction with RNNs
> - **Speech Recognition:** CTC loss for alignment-free training
> - **Video Analysis:** 3D CNNs + LSTMs for temporal modeling
> - **Anomaly Detection:** RNN autoencoders for reconstruction

> [!purple] 🔮 **Optimization Techniques**
> - **Truncated BPTT:** Limit backpropagation steps for memory
> - **Gradient Checkpointing:** Trade computation for memory
> - **Mixed Precision Training:** FP16 for faster training
> - **Stateful RNNs:** Preserve hidden state across batches

---

## 🔗 Related Topics

- [[04-Deep-Learning/Neural-Networks/README|Neural Networks]] - Foundational concepts
- [[04-Deep-Learning/Transformers/README|Transformers]] - Modern alternative to RNNs
- [[05-NLP/Basics/README|NLP Basics]] - Text preprocessing for RNNs
- [[02-Statistics-and-Data/Time-Series/README|Time Series]] - Sequential data analysis

---

## 📚 Resources

**Courses:**
- Stanford CS224n: NLP with Deep Learning
- Fast.ai Deep Learning Part 2
- Sequence Models (DeepLearning.AI)

**Papers:**
- "Long Short-Term Memory" (Hochreiter & Schmidhuber, 1997)
- "Learning Phrase Representations using RNN Encoder-Decoder" (GRU, 2014)
- "Neural Machine Translation by Jointly Learning to Align and Translate" (Attention, 2014)
- "Sequence to Sequence Learning with Neural Networks" (2014)

**Key Concepts:**
- Understanding LSTM Networks (Chris Olah's blog)
- The Unreasonable Effectiveness of RNNs (Andrej Karpathy)

**Implementation:**
- PyTorch RNN Tutorial
- TensorFlow RNN Guide
- Keras Recurrent Layers Documentation

---

## 📊 RNN vs Transformer

| Feature | RNN/LSTM | Transformer |
|---------|----------|-------------|
| **Sequential Processing** | ✅ Sequential | ❌ Parallel |
| **Long Dependencies** | ⚠️ Struggles | ✅ Excellent |
| **Training Speed** | ⚠️ Slow | ✅ Fast (parallel) |
| **Memory** | ✅ Lower | ⚠️ O(n²) attention |
| **Best For** | Streaming, short sequences | Long sequences, batch processing |

---

**Tags:** #rnn #lstm #gru #sequence-modeling #time-series #attention
**Difficulty:** 🔥🔥🔥 Advanced
**Last Updated:** 2026-11-11
