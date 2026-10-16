<table_of_contents color="gray"/>
# Introduction
Unlike previous works that directly repurpose VLM for action, we propose a **componentized** VLA that a specialized action module conditioned on VLM output. We use the cognitive information by VLM to condition the action prediction process. We employ diffusion-based transformers(DiT) to do this process. In addition, we propose an **adaptive action ensemble(AAE)** to fuse the past action in an adaptive manner.
![](notion-file-block://12f0ad69-a5f8-823a-9c13-81438a7fef50/f53db3ee-5f79-4e5e-8ec1-215bda09f6d4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
# Method
## Problem formulation
$$
\bm{\pi}:(\bm{l}, \bm{o}_t) \rightarrow (\bm{a}_t, \bm{a}_{t+1}, \cdots, \bm{a}_{t+N})
$$
We define the each action space of a gripper as 7 DoF, $`\bm{a}_t = [\Delta x, \Delta y, \Delta z, \Delta \phi, \Delta \theta, \Delta \psi, g]`$, where $`g \in \{ 0,1 \}`$ indicates the gripper’s open/close state.
## Architecture
![](notion-file-block://e950ad69-a5f8-8374-bfd9-019f28635253/2dd57713-9979-487c-9c9a-cfb8eb24435a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We componentize the model into 3 parts:
1. **Vision** module
2. **Language** module
3. **Action** module
Vision and language module follows the **Prismatic VLM**, which is base VLM of openVLA. For vision module, the image observation is fed into the DINOv2 and SigLIP models, and then produce **visual perceptual tokens** $`\mathcal{V}=\{ v_1, v_2, \cdots, v_{N_v} \}`$. LLAMA-2 model is applied as the language module backbone. The language instruction $`\bm{l}`$ is converted into **linguistic tokens** $`\mathcal{T}=\{ l_1, l_2, \cdots, l_{N_\mathcal{T}}  \}`$. These tokens are concatenated with $`\mathcal{V}`$ and an additional learnable cognition token $`\bm{c}`$, and processed by the model using a causal attention mechanism. The resulting output is **cognition token** $`\bm{f}_t^c`$.
### Diffusion action module
Action module takes the cognition feature $`\bm{f}_t^c`$ along with noisy actions $`(a_t^i, a_{t+1}^i, \cdots, a_{t+N}^i)`$ as input, where $`i`$ denotes the current denoising step. We add step information $`i`$ with a **sinusoidal positional encoding**. Since Transformers struggle to directly process the integer $`i`$, it is encoded using sine and cosine functions for positional encoding. Model predicts **action chunk** $`(a_t, a_{t+1}, \cdots, a_{t+N})`$. 
## Training objective
Out 3 modules are trained by **MSE **between the predicted noises and the ground truth noises. 
$$
\mathcal{L}_\text{MSE} = \mathbb{E} _{\epsilon \sim \mathcal{N} (0,1),i}||\hat{\epsilon}^i-\epsilon||_2
$$
## Adaptive action ensemble
Model predicts actions for multiple time steps. ACT is to execute **actions consecutively**. However, this does not fully leverage the visual information. ACT also introduced a **temporal ensemble** strategy that combines current actions from both present and past using preset aggregation weights. But action tasks can have different modes(ex. right or left move), so that simply aggregating them could result in an action that is suboptimal.
![](notion-file-block://5190ad69-a5f8-821f-af71-816227f365cd/3bc9259f-a3f0-4a45-9f05-52f6dfc029d9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Instead of generating a single action, the model produces action chunks, resulting in multiple action candidates for a given time step $`t`$, as shown in the figure above. While previous methods simply averaged these predictions, the **adaptive action ensemble(AAE)** strategy computes weights based on their similarity to the prediction made at the current time step.
$$
\hat{a}_t=\sum ^K_{k=0} w_k^\text{ada} \cdot a_t|o_{t-k}
$$
where $`w_k^\text{ada}=\exp (\alpha \cdot < a_t|o_t, a_t|o_{t-k}>)`$. $`<\cdot, \cdot>`$ calculates the cosine similarity between two actions, and $`\alpha`$ is a hyperparameter. 
# Experiments
We evaluate the model with Google Robot and WidowX Robot. We use the standard deviation of actions from training set to determine K, for Google Robot K = 2 and for WidowX Robot K=7.
## SIMPLER simulation evaluation
We evaluate the model within the SIMPLER evaluation environment.
### Google Robot
![](notion-file-block://d3a0ad69-a5f8-82ba-8c72-81ce4b7729b2/a2064ec1-0bef-411a-8d76-37d86e34e053?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
<empty-block/>
### WidowX Robot
![](notion-file-block://9c60ad69-a5f8-82ac-9cca-012035e771d0/cdda0460-886a-4731-a1fa-d6b2f0541b47?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## Real-world evaluation
We perform real-world experiments with Real man Arm robot. We design 3 tasks for real-world experiments: **Pick, Stack, Place.**
![](notion-file-block://4d00ad69-a5f8-83b2-abc5-01a50218321e/7850f3cf-3a0d-4971-9023-d0e6e1074674?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=aed1e283-0b12-414a-91a9-7d68d977d25e.png)
### Unseen tasks
![](notion-file-block://6d90ad69-a5f8-821c-a112-81c3aa90e7ed/6ad5fd62-e27f-462b-9e44-f343c43f9680?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://4e40ad69-a5f8-83c4-8c7b-01335beaf870/7e97b186-77c6-45e5-ae74-cf2e678f12f6?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### Real-world evaluation with Franka robot
![](notion-file-block://ebd0ad69-a5f8-83ac-9912-018b147d440b/9172f051-9394-472e-9878-1082e87d5205?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## Ablation study
### Model architecture
![](notion-file-block://b130ad69-a5f8-835c-9304-0171ebb29e5a/f1a03cd0-440e-465f-bb32-f04b756d3ba5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### Multi-step number
![](notion-file-block://78c0ad69-a5f8-83b3-95b3-81f474e89f75/91f1683e-9284-404a-8634-205e50db6f97?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### Ensemble strategy
![](notion-file-block://a470ad69-a5f8-8336-aed4-815f0d61c90e/5a9c7c0d-2b15-4650-9508-d0735c892c8f?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
<empty-block/>