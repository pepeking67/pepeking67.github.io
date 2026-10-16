<table_of_contents color="gray"/>
# Introduction
In NLP and CV, fine-tuning the general foundation model tends to outperform narrowly trained models. Similarly, for specialized robot, it is more effective to first pre-train on highly diverse robot data, and then fine-tune for desired task. This process can be seen as a solution the data scarcity, because many more sources including from other tasks, robots can be available to a generalist model. We call this **robot foundation model** as generalist robot policy. 
![](notion-file-block://d140ad69-a5f8-8303-ba31-81045e4e5ff8/baa1b0a1-30ec-4d20-9d1c-a36d08d8245a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
To perform dexterous tasks, we use an **action chunking** architecture with **flow matching** to represent complex continuous action distributions. To combine flow matching with VLMs, we use an **action expert** that augments the standard VLM with flow-based outputs. We train model via diffusion-style(flow matching) loss, instead of the standard cross-entropy loss. 
# Model
![](notion-file-block://fcb0ad69-a5f8-825e-8d42-019e7bab7de0/df4db4ed-5bd3-4fcf-a329-a9fda090cd43?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Image encoders embed the robot’s image observations into the same embedding space as language tokens. $`\pi_0`$ uses conditional flow matching to model the continuous action distributions, making it suited to high-frequency dexterous tasks. We trains a single transformer using multiple objectives(**Transfusion**), with continuous outputs supervised via flow matching loss and discrete outputs via cross-entropy loss. We also use a separate set of weights for the robotics-specific tokens(**mixture of experts**). First element is used for image and text inputs, and second is used for robotics-specific inputs and outputs(**action expert**).
## Flow matching
Reference: [**Flow Matching for Generative Modeling**](https://arxiv.org/abs/2210.02747)
Goal: $`p(A_t|o_t),\ \text{where } A_t = [a_t, a_{t+1}, \cdots, a_{t+H-1}]`$.
$`A_t`$ corresponds to an **action chunk**(H = 50), and $`o_t`$ is an observation(images, language command, and robot’s proprioceptive state). $`o_t=[I_t^l, \cdots, I_t^n, l_t, q_t]`$, where $`I_t^i`$ is i-th image, $`l_t`$ is a sequence of language tokens, and $`q_t`$ is a vector of joint angles. $`I_t^i,\ q_t`$ are encoded via corresponding encoders and then projected via a **linear projection to the same embedding space as the language tokens**.
We supervise action tokens using a conditional **flow matching loss**: 
$$
L^\tau(\theta) = \mathbb{E}_{p(\mathbf{A}_t \vert{} \mathbf{o}_t), q(\mathbf{A}_t^\tau \vert{} \mathbf{A}_t)} \Vert \mathbf{v}_\theta(\mathbf{A}_t^\tau, \mathbf{o}_t) - \mathbf{u}(\mathbf{A}_t^\tau \vert{} \mathbf{A}_t) \Vert^2
$$
$`t`$ is robot timesteps and $`\tau \in [0,1]`$ is flow matching timesteps. Flow Matching trains a continuous vector field using a simple **linear-Gaussian (optimal transport) probability path**, given by:
$$
q(A_t^\tau|A_t)= \mathcal{N}(\tau A_t, (1-\tau)I)
$$
In practice, $`A_t^\tau = \tau A_t + (1-\tau) \epsilon, \text{ where } \epsilon \sim \mathcal{N} (0,I)`$. Then training the network outputs $`\mathbf{v}_\theta (A_t^\tau, o_t)`$ to match the denoising vector field $`u(A_t^\tau|A_t) = A_t - \epsilon`$.
The $`\mathbf{v}_\theta`$ is the velocity vector needed to move from a noisy state toward the ground-truth action. Differentiating the noisy action $`A_t^\tau = \tau A_t + (1-\tau)\epsilon`$ with respect to time $`\tau`$ gives its rate of change (velocity):$`\frac{d A_t^\tau}{d\tau} = \frac{d}{d\tau} [\tau A_t + (1-\tau) \epsilon] = A_t - \epsilon`$.
In practice, the ground-truth action $`\mathbf{A}_t`$ is unknown at inference, meaning the model only receives a noisy action state; thus, training teaches the neural network how to process this noisy state and predict the velocity vector required to get the optimal action.
The action expert uses a full bidirectional attention mask, allowing action tokens from $`t_1`$ to $`t_H`$ to attend to one another, so the model ensures structural consistency and global smoothness across the entire trajectory.
During training, we sample the flow matching timestep $`\tau`$ from a **beta distribution** that emphasizes lower(noisier, $`\tau=0`$) timesteps. 
![](notion-file-block://3b00ad69-a5f8-8244-8b19-014bbec2b5eb/ac7abb6b-bceb-4a7c-8efb-8fbbb8e81300?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
At inference time, we generate actions by **integrating the learned vector field** starting with random noise $`A_t^0 \sim \mathcal{N} (0, I)`$, using the **forward Euler integration rule**:
$$
A_t^{\tau + \delta} = A_t^\tau + \delta \mathbf{v}_\theta (A_t^\tau, o_t)
$$
# Data & Training recipe
We employ a **multi-training** procedure, so the pre-training and post-training datasets require different elements. 
![](notion-file-block://d820ad69-a5f8-83a2-aca5-815e3db18973/a9524bf7-652b-40aa-b32c-50ec2f319bba?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
In the dataset for learning dexterous tasks, this task is **composed of complex behaviors**. For example, “bussing” task involves putting different dishes into the different bin. This definition of task is different from prior work such as combination of noun and verb. Since the more difficult tasks are overrepresented, so the datasets are **imbalanced** in size. Thus, we weight each task-robot combination by $`n^{0.43}`$, where n is the number of samples for that combination.
# Experiments
## 1. Out-of-box evaluation
![](notion-file-block://b220ad69-a5f8-82a0-87ea-811812bb779c/832a13e3-a179-40f8-899a-aaf28d17fa1f?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
To campare for performance of diffusion process, we compare with Octo, while Octo is not a VLA. Since we cannot train OpenVLA and Octo for the same number of epochs as Pi0, so we also compare with parity version of Pi0. We also compare with Pi0-small, which is a model without VLM pre-training.
![](notion-file-block://1910ad69-a5f8-83cc-906b-01a4f7c78d50/e70b59d6-dea9-4fdd-b16c-8a1331459e6a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
OpenVLA has lower performance since it does not support action chunks(discretization architecture). However, Octo supports action chunks, but it has limited capacity. Thus, we can see the importance of VLMs. 
## 2. Language evaluation
![](notion-file-block://1380ad69-a5f8-83c7-97dd-81798739debc/54be3281-0261-40ce-b90c-e030c7a682e4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
**Pi0-flat** is the model without **intermediate language commands**. **Pi0-human** provides intermediate step commands. **Pi0-HL** evaluates Pi0 with high-level commands provided by a high-level VLM. 
![](notion-file-block://9180ad69-a5f8-8216-a3d5-811f1463c7fc/545d635d-5ebc-48de-911f-37ec3271b967?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
For Pi0-small, it has limited language ability, so it does not gain a benefit from high-level expert.
## 3. Dexterous tasks evaluation
![](notion-file-block://8a80ad69-a5f8-822c-9b0f-01ef0729eac2/ab377bc3-157a-4bfb-b090-837e7627a736?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We compare to ACT and Diffusion policy. We also compare Pi0 by fine-tuning from pre-trained base model with by training from **scratch**. 
![](notion-file-block://0850ad69-a5f8-8316-91d4-0124f386c133/e74216d4-84b8-4a48-9ae2-5ffe68270cd3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## 4. Complex multi-stage tasks evaluation
![](notion-file-block://d200ad69-a5f8-82a7-9e95-8165bbec8632/40d288f8-0a66-4ac3-b2ab-fc0927109f40?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://7030ad69-a5f8-83be-9d88-01382b07e3df/b9d78a6a-ac23-466b-8347-915c82998d6e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
**Out-of-box**: pre-training only
**Scratch**: fine-tuning data without any pre-training
# Limitations
1. Do not understanding what type of data is more helpful
2. Not all task work reliably