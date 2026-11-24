

# Introduction




Existing models use high-end sensors for precise estimation. Our goal is to develop a low-cost and imprecise hardware to perform fine manipulation tasks. Since the performance depends on the training data, so we build <b>ALOHA</b>, which is <b>dexterous teleoperation system</b> for data collection. 




![](notion-file-block://4210ad69-a5f8-80c1-9e8b-db3637fea610/7f12b085-8510-40c3-9282-2823957a81de?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

We show two main ideas:

1. <b>Teleoperation system: ALOHA</b>
2. <b>Imitation learning algorithm: ACT</b>

<b>Action chunking</b> is a concept that the policy predicts the next k target joint positions. This reduces the <b>effective horizon</b>, which is<b> </b>the number of decision-making, and <b>compounding errors</b>.

To make the policy more smooth, we use <b>temporal ensembling</b>, which averages overlapping action chunks predicted at different time steps.

# Action chunking with transformers

## Action chunking and temporal ensemble

![](notion-file-block://4210ad69-a5f8-8097-bc52-e4a6575961b6/27936836-e2cc-4401-84c8-8a56a4f56ac6?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

Temporal ensemble performs a weighted average using <b>exponential weight</b> $`w_i=\exp(-m*i)`$, where $`w_0`$ is the weight of the oldest action. For large $`m`$, it weights older data more and for small $`m`$, recent predictions receive more weight, so that the model can <b>incorporate new observations quickly</b>.

## Modeling human data




To tackle challenge of training noisy human demonstration, we train the policy by conditional variational autoencoder(<b>CVAE</b>), which is conditioned on current observations. 




![](notion-file-block://4210ad69-a5f8-8070-93ef-c2de3f40afae/7fd8405e-be83-473e-a43e-d15a9174ea14?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Implementation

![](notion-file-block://4210ad69-a5f8-8080-a269-ed12c8c54d30/cd7456e5-d3b3-43c7-b5d8-8efff2ed8cd4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

![](notion-file-block://4210ad69-a5f8-80a2-a489-dada64119d5a/c1e99174-23e5-437c-bc8a-40b3c6202150?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

![](notion-file-block://4210ad69-a5f8-8047-9f85-e4825daa15db/1f7af0b6-31ac-443a-89e3-6c53605e430f?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

# Experiments

![](notion-file-block://4210ad69-a5f8-807a-887b-cc02327a3465/0f1d10c3-d2c9-4aa3-bf87-fe0857c7cfc8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)




Prior methods have poor performance since they cannot treat the <b>compounding errors</b> and <b>non-Markovian behaviors</b>. Especially, with a single-action prediction, it is difficult for the robot to determine when to pause and when to move based solely on its current state. 




![](notion-file-block://4210ad69-a5f8-808d-ad20-e829cfc1238f/f3be4ff9-c30e-46aa-ab87-94c252620041?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

We observe low performance at Thread Velcro task. We hypothesize this is due to <b>low contrast</b> between background and <b>small fraction</b> of cable ties in the images. So it is hard to determine the exact position of the cable ties from image observations.

<figure markdown="1">

![](notion-file-block://4210ad69-a5f8-8003-ad3b-ffd5a0cb72a6/a5009932-ee44-49c6-a1f2-85c485f33ae8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

<figcaption>Fig. 10: Example of Thread Velcro task image observation.</figcaption>

</figure>

# Ablations

![](notion-file-block://4210ad69-a5f8-809e-8ece-c125fa025273/546127de-8535-4399-aa2e-8474bb46cb14?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## (a): Action chunking




From (a), we disable temporal ensembling to measure only effect of action chunking. From k=1 to k=100, ACT performance improves. Predicting <b>too many chunkings</b> has the difficulty in modeling long action sequences and lack of receive behaviors. 




Other model with action chunking improves, so we can see that action chunking is <b>generally beneficial</b>.

## (b): Temporal ensembling

We hypothesize that the temporal ensembling <b>benefits parametric methods by sampling smoothly</b>, but the VINN is a non-parametric model, so it doesn’t suffer from this problem.

## (c): CVAE

Since the scriped data is deterministic, there is no difference in the CVAE objective.

However, probabilistic action prediction using a CVAE is beneficial for learning from non-deterministic human demonstrations.




Note that [The Latent That Never Was: A Forensic Re-run of the CVAE Ablation in Action Chunking Transformers](https://arxiv.org/abs/2609.16745) reported improved performance after removing the CVAE encoder, these findings are limited to specific simulation settings and require further validation. 




## (d): High-frequency

50Hz performs highly dexterous and precise tasks in a short time, but 5Hz results in a 62% increase in teleoperation time.



