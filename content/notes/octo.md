<table_of_contents color="gray"/>
# Introduction
We want to **fintune with only a little data** instead of training new policies from scratch. ⇒ **Generalist Policy**. With no additional training, this policy can accept different camera configurations and can control different robots. Model can be adapted to new robot setups with new sensory inputs, action spaces, and **morphologies**(Unlike RT-1,2)
Note that Octo is not based on VLM, so by definition of VLA in Rt-2, Octo is not VLA in that meaning.
# Model
Octo model emphasizes **flexibility and scale**, while providing generic and scalable recipe that can be trained on large amounts of data.
## Architecture
![](notion-file-block://2eb0ad69-a5f8-83a2-9bbb-01f5f24b6e8d/1ccc0e16-43a6-4f6b-b3e7-e3821071eebf?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### 1. Input tokenizer
Task definitions: language instructions $`l`$, goal images $`g`$ and observations $`o_1, \cdots, o_H`$.
For language inputs, we use pretrained transformer t5-base model.
For images, we use shallow convolution stack, then split into a sequence of flattened patches like ViT.
Finally we get tokens $`[\mathcal{T}_l, \mathcal{T}_g, \mathcal{T}_o]`$ as form $`[\mathcal{T}_T, \mathcal{T}_{o,1}, \mathcal{T}_{o,2} \cdots]`$ where $`T`$ means task.
### 2. Transformer backbone
Octo transformer **attention pattern is block-wise** masked. By grouping inputs—such as cameras, robot states, and action predictions—into individual token blocks, the **model can compute attention selectively using an attention mask**. **This enables adding or removing observations and tasks during finetuning**. The prior architectures would require re-training when adding or removing inputs. 
### 3. Readout head
The readout head extracts and compresses the contextualized information processed by the transformer backbone into a condition vector, passing it to the diffusion head to generate precise robot actions through a denoising process.
## Training data
We train Octo on a mizture of 25 datasets from the Open X-Embodiment Dataset.
## Training objective
We use a **conditional diffusion decoding head** to predict continuous, multi-modal action distributions. Where multi-modality refers to a situation where multiple valid choices exist for a single state—such as deciding to move either left or right when encountering an obstacle. In such scenarios, an MSE-based model fails because its loss function calculates the mean of the target distribution, causing it to average these two valid paths and mistakenly navigate directly through the center, which leads to a collision.
Only one forward pass of the transformer backbone is performed per action prediction, and then the multi-step denoising process is carried out within the small diffusion head.
1. Sample Gaussian noise vector $`x^K \sim \mathcal{N}(0, I)`$.
2. Apply K steps of denoising with a learned denoising network $`\epsilon_\theta(x^k, e, k)`$.
$`e`$ is a conditioning vector in diffusion model, FiLM adjusts scale and shifts parameter based on $`e`$.
Denoising network $`\epsilon_\theta(x^k, e, k)`$ is conditioned on the output $`x^k`$ of the previous step, and the output embedding $`e`$ of the transformer action readout. 
$$
x^{k-1}=\alpha (x^k-\gamma \epsilon _\theta (x^k, e, k) + \mathcal{N} (0, \sigma^2I))
$$
We train the diffusion head using **DDPM**.
# Experiments
## 1. Out-of-the-box
It tests the performance of the model itself.
![](notion-file-block://82b0ad69-a5f8-83df-a191-01ea1bfd4804/f2555503-7473-40ed-9ea7-8dc2b5e48813?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## 2. Data-efficient finetuning
![](notion-file-block://9190ad69-a5f8-82ef-ba72-8171cdaa9ff7/8c429913-7c58-4036-9e6e-c43c8c168769?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## 3. Design decisions
![](notion-file-block://0570ad69-a5f8-825f-b42c-8121e63777a4/4f55f824-9768-4189-a9a3-9d41bf92fb2d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### (1) Model architecture
We use **transformer-first** architecture. Developing a generalist policy requires large amounts of data, and as dataset sizes scale up, ViT (Vision Transformer) performance improves significantly. Therefore, through a transformer-first architecture, most of the **computation is concentrated in the central ViT to maximize scalability**(Linear improvements in performance with respect to model size and compute). For small dataset, ResNet performs better than ViT architecture.
### (2) Training data
Performance of Octo increases as we increase the number of training datasets.
### (3) Training objective
We compare with MSE and cross-entropy loss on discretized actions. The diffusion head can model **multi-modal action** unlike MSE, and can retain the precise **continuous actions** unlike CE.
### (4) Model scale
![](notion-file-block://a780ad69-a5f8-824a-8663-0111c889f448/224636bc-0193-4fd4-bdb8-b845a1eb549a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Larger model has better visual perception.
# Limitations
1. Cannot process **wrist camera **information
2. Train via **imitation**
# Conclusions
To construct a **generalist policy**, the Octo model leverages a massive dataset. To train on this data effectively, it employs a **blockwise** attention masking architecture that enables efficient fine-tuning. Furthermore, Octo utilizes a **transformer-first** design to maximize scalability, concentrating most of the computation in a central ViT. Finally, to accurately output complex and diverse behaviors—such as multi-modal action distributions—it incorporates a **diffusion action head**.
<empty-block/>