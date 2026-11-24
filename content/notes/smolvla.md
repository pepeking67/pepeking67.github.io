

![](notion-file-block://4210ad69-a5f8-80e4-ac82-d7f8c3c56e94/133ad340-2eca-4d7b-b696-fdc55c8eca6a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

# Introduction

We introduce a small, efficient, and community-driven VLA: <b>SmolVLA</b>.

1. Skipping layers in the VLM
2. Using a minimal number of visual tokens
3. Small pretrained VLMs
4. Interleaving self-attention with cross-attention layers

In addition, we introduce an asynchronous inference stack that decouples <b>action execution</b> from <b>observation processing</b> and <b>action prediction</b>. As a result, it reduces latency and enables fast inference.

![](notion-file-block://4210ad69-a5f8-8037-8c02-d01db395b472/39e72892-5da2-47f9-b5b9-aaf9f17e15be?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

# SmolVLA

SmolVLA is a VLA consisting of compact pretrained VLM and trained with flow matching.

## Model architecture

SmolVLA is composed of two main parts:

1. Pretrained VLM
2. Action expert

We use SmolVLM-2, whose vision encoder reduces token count through a <b>token-shuffling</b>.

![](notion-file-block://4210ad69-a5f8-80ef-b4c5-f12325a1c4f0/00f5ea52-1f4c-4e93-991c-7373b3a3ae17?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

Since self-attention has $`O(N^2D)`$, reducing the number of tokens reduces the computational cost.

<details>
<summary>Note: Why the self-attention’s computational complexity is $`O(N^2D)`$</summary>

$$
\operatorname{Attention}(Q,K,V)=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$

For $`QK^T`$, $`(N\times D)(D \times N) \Rightarrow O(N^2D)`$.

For inner production, we need $`O(N^2)`$ complexity.

$`S=\operatorname{softmax}(\frac{QK^T}{\sqrt{d_k}})`$, $`SV = (N\times N)(N\times D)\Rightarrow O(N^2D)`$

Thus $`O(N^2D)+O(N^2)+O(N^2D) = O(N^2D)`$.
</details>

To match the dimension of states, VLM features, and action expert, we use <b>linear projections</b>.

While SmolVLM-2 is trained by tiling, which is trained by global image and its multiple crops, we <b>do not use tiling</b> for fast inference. We use global image only with pixel shuffle.

Recently, <b>last layer of a VLM is not necessary</b> for the best features, out action expert accesses up to a specified layer $`N`$(<b>Layer skipping</b>).

We <b>interleave </b>cross and self-attention layers and use conditional <b>flow matching</b>:

$$
\mathcal{L}^\tau(\theta)=\mathbb{E}_{p(A_t|o_t),q(A_t^\tau|A_t)}[||v_\theta(A_t^\tau,o_t)-u(A_t^\tau|A_t)||^2]
$$

where $`o_t`$ represents VLM features and $`A_t^\tau=\tau A_t+(1-\tau)\epsilon,\ \epsilon\sim\mathcal{N}(0,I)`$.

$`v_\theta`$ is predicted vector field and trained to true vector field $`u(A_t^\tau|A_t)=-\frac{d A_t^\tau}{d \tau}=\epsilon-A_t`$.

## Pretraining data collected by the community

In robotics, large-scale pretrining data is still smaller than vision and language data.

We use a subset of 481 community datasets from Hugging Face.

![](notion-file-block://4220ad69-a5f8-80da-85b8-e60ea2a560ff/53a97278-8b57-48f3-8857-d7065037f793?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

For community data, there are stanrdization challenges, in particular, <b>noise in annotations</b>. To improve on the annotation quality, we use VLM such as Qwen2.5-VL-3B-Instruct.

Another challenge is <b>variable camera viewpoints</b>. We normalize the camera naming and viewpoint ordering.

## Asynchronous inference

Prior models are one-loop inference, which executes the action chunk after observation is passed to the policy.

![](notion-file-block://4220ad69-a5f8-809c-b38e-f71e2539a168/09328608-48e0-4faa-a8fb-fc78b4de3908?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

![](notion-file-block://4220ad69-a5f8-8050-a937-dc865a90ed8d/aaf2a81d-7d7e-4229-ac3b-29011ea626b9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

To avoid redundant server calls and erratic behavior, observations are compared in joint-space and <b>similar actions are dropped</b>. If the queue of robot client becomes <b>empty, then the most observation is processed regardless of similarity</b>.

$`l`$: time needed to receive an action chunk after sending an observation $`o`$.

$`l_S`$: inference latency on POLICYSERVER.

Then $`\mathbb{E}[l]=\mathbb{E}[t_{C \rightarrow S}] + \mathbb{E}[l_S]+\mathbb{E}[t_{S\rightarrow C}]`$ and $`\mathbb{E}[l] \simeq \mathbb{E}[l_S]`$.

$`\Delta t`$: environment’s control cycle.

Thus the condition for <b>preventing the existing action queue from being exhausted</b> before a new action chunk arrives is given as follows:

$$
g \geq \frac{\mathbb{E}[l_S]/\Delta t}{n}
$$





The threshold $`g`$ can be interpreted as the proportion of remaining actions in the queue.

![](notion-file-block://4220ad69-a5f8-8051-a465-ea2e6d4372b5/f09596b1-2cd5-47a6-99f5-6f98a0bc6ee3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)




At $`g=0`$, the action chunks are predicted after queue becomes empty. 




With observation filtering that drops the similar action, (B) shows that action chunks are predicted after empty queue despite $`g=0.5`$.

# Experiments

## Simulation evaluation

![](notion-file-block://4220ad69-a5f8-8086-b74d-f2f2ca902ad9/13198f72-f866-475d-ac80-dbb3d8de9feb?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Real-world evaluation

![](notion-file-block://4220ad69-a5f8-80cc-9731-c57f871d310c/da16c0e7-d05e-4cba-9d75-1f8819e3a1e1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Effect of pretraining and multitask learning

![](notion-file-block://4220ad69-a5f8-808a-9f49-e35a71b517ce/a2bd9ec3-5a5e-44e1-aa26-4c3f266fc421?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

This shows that pretraining on community datasets improves the performance and multitask finetuning leads to further performance improvement. This implies the importance of knowledge tranfer across tasks.

## Asynchronous inference

![](notion-file-block://4220ad69-a5f8-8088-88be-cfc08b5fdd00/e8171d96-f664-4c73-b44a-59624e7932b3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Ablation study

S, O, G, 10 are 4 LIBERO benchmarks.

S: LIBERO-Spatial

O: LIBERO-Object

G: LIBERO-Goal

10: LIBERO-Long

### 1. CA vs SA

![](notion-file-block://4220ad69-a5f8-8006-b446-e83c7ccfefef/2704b914-f143-4bd9-9584-fb5243f4e8df?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

### 2. Bidirectional vs causal attention

![](notion-file-block://4220ad69-a5f8-8032-9a6e-c6195dd2b0ed/89a1a0e8-4bc8-4c57-b9ec-425b9ac1b7a6?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

### 3. Skipping layers

![](notion-file-block://4220ad69-a5f8-80f8-a292-d7a645dbb323/b61167ef-1367-423f-8269-5ed8e13a264d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

Skipping layers gives good trade-off between performacne and compute.

### 4. Expert capacity

![](notion-file-block://4220ad69-a5f8-80f9-976c-e4767c559993/4cefc68d-5eb5-400b-bc3f-3f7cb6292171?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

### 5. Training objective

![](notion-file-block://4220ad69-a5f8-805c-8328-e651bd9a77d4/97254463-c55a-43c7-a057-25dee322e556?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

### 6. States to the VLM or action expert

![](notion-file-block://4220ad69-a5f8-8045-9629-e0032cdef7c8/001492a8-ecb9-49b7-9567-ee281bf38433?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

This compares two variants:

1. Feeding the sensorimotor states to the VLM
2. Passinf them directly to the action expert

### 7. Action chunk size

![](notion-file-block://4220ad69-a5f8-806d-a78c-e6cfe2a4d964/1cf8045f-a667-49dc-9ea3-5564d84f1d0d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

### 8. Action execution steps

![](notion-file-block://4220ad69-a5f8-80ca-9e46-da9a22ab5dad/dd542e22-62a5-4695-a845-1f03a77f4dc2?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)




<b>Action Steps</b> refers to the number of actions executed by the robot before receiving a new observation and predicting a new action chunk. 




Even though acting entire chunk speeds up the inference, it reduces the responsiveness.