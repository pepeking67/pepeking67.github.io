<table_of_contents color="gray"/>
# Introduction
This paper only uses **attention **without any RNN or CNN architectures. For many prior works, they used RNN, however, this sequential nature **limits parallelization** within training examples, so that it is critical at longer sequence length. Thus we rely on only an attention to draw **global dependencies** between input and output. Since single-head attention average attention-weight, so we use **multi-head attention**.
![](notion-file-block://3d50ad69-a5f8-8077-8d01-e3355a95cb77/3e361d43-7e3f-448f-97b5-9d6369e329ac?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
# Architecture
![](notion-file-block://3d50ad69-a5f8-80f9-bf01-f284bbd82517/54710ddc-8287-4eb9-865b-e7a43f5e27d9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
At decoder, to prevent positions from attending to subsequent positions, we use **masking**(set scaled dot product attention as $`-\infty`$).
$$
\text{Attention}(Q,K,V)=\text{softmax}(\frac{QK^T}{\sqrt{d_k}})V
$$
If query or key dimension($`d_k`$) grows large, then the dot products grow, pushing the softmax function into regions where it has **extreme small gradients**. So we divide attention distribution by $`\sqrt{d_k}`$. 
Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. 
$$
\text{MultiHead}(Q,K,V)=\text{Concat}(\text{head}_1, \cdots, \text{head}_h)W^O,\\ \text{where head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V) 
$$
FFN layer consists two linear transformations with a ReLU activation between.
$$
\text{FFN}(x)=\max (0, xW_1+b_1)W_2 + b_2
$$
Since transformer has no recurrence and no convolution, so we must inject some information about the position of tokens(**positional encoding**). 
$$
\text{PE}_{(pos, 2i)} = sin(pos/10000^{2i/d_{\text{model}}}) \\ \text{PE}_{(pos, 2i+1)} = cos(pos/10000^{2i/d_{\text{model}}})
$$
Since $`\text{PE}_{pos+k}`$ can be represented as a **linear transformation**(by using Trigonometric addition formulas) of $`\text{PE}_{pos}`$, It would allow the model to easily learn the positions.
## Why Self-attention?
![](notion-file-block://3d50ad69-a5f8-809f-a258-d6e9df4ecea4/48750253-0a91-41eb-b158-6d20bdc1666a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
If the sequence length n is smaller than the representation dimensionality d, then self-attention is faster than recurrent layer(according to this paper, most often case). To improve computational performance for **very long sequences**, self-attention could be **restricted to a neighborhood of size r**. We can see this issues at early GPT model, it has input limit.
# Experiments
![](notion-file-block://3d50ad69-a5f8-8036-b068-f8aa913bce54/06ca43dc-304b-406d-9d0a-149092124733?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://3d50ad69-a5f8-80b9-93d8-f5bfdbe7b7e0/9e8eea37-bfc1-49bd-b4c2-daa8b57aebef?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We used **beam search**, where beam search is for K, we infer K first words, and then for each K words re-infer most available K words, and so on.