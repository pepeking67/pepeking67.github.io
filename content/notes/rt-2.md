<table_of_contents color="gray"/>
# Introduction
Semantic reasoning and visual interpretation capabilities are useful for robots. Since robots need low-level action(not text) we cannot directly apply VLMs to robots, which generally address only the high-level robotic planning. 
>
	Can large pretrained VLMs be integrated directly into low-level robotic control to boost generalization and enable emergent semantic reasoning?
By tokenizing the actions into text tokens, we can train the model can be directly trained to act as instruction following robot policies. The unified output space enables model weights to be shared across language and action tasks, without introducing action-only components. We call this category of models as Vision-Language-Action(**VLA**)
# VLA models
## Pre-trained VLMs 
PaLI-X: An Encoder-Decoder vision-language model featuring a ViT backbone, specialized for  superior visual/spatial perception. And 1000 integers have a unique token, so we simply associate the action bins to token.
PaLM-E: A decoder-only multimodal model built on the PaLM LLM backbone, leveraging massive web-scale text and code pre-training for exceptional commonsense reasoning, logic, and mathematical calculation.
## Robot-action fine-tunig
We represent actions as language tokens in the model’s output. Action encoding is based on the RT-1 model method, the continuous dimensions of actions are discretized into 256 bins. This requires **reserving 256 tokens to serve as action tokens.** For PaLI-X, we just associate the action bins to unique integer tokens. At PaLM-E, we overwrite the 256 least frequently used tokens to represent actions. **Co-fine-tuning** robotics data with the original web data can improve robot performance. 
To allow the model to accurately process instructions semantically, it must also be trained to produce text outputs; therefore, prompting is configured to restrict outputs to action tokens only during robot-action tasks, while permitting full natural language outputs for all other tasks.
## Real-time inference
Using multi-TPU cloud service, 55B paramter RT-2-PaLI-X model can run at 1\~3Hz. For 5B model can run 5Hz.
# Experiments
## 1. Seen/unseen task performance
![](notion-file-block://be60ad69-a5f8-8312-9ad8-01d24f9e941b/ac29d064-3707-40e6-b3d7-e94fc74d344a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://b2f0ad69-a5f8-8284-892f-0136f15b3266/ee3c6630-67ac-4931-bf5d-2f33bab75816?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
For seen task, we use the same instructions in RT-1. Note that these in-distribution evaluations still have vary placement of objects and factors, requiring the skills to generalize. 
The strength of VLAs lies in transferring more generalizable and semantic concepts from their **internet-scale** pretraining data. 
## 2. Emergent capabilities of RT-2
We do not expect such transfer to enable new **robot motions**, but **semantic and visual concepts**.
There are 3 categories of emergent capabilities.
 
![](notion-file-block://dcb0ad69-a5f8-835c-b123-8154ae8565ad/99a49000-9f34-48ab-adb0-88ff8d0c9589?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://cb30ad69-a5f8-836b-9c87-01ef6ef75517/1f6312e2-3faf-4957-b923-46c117f18ef5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
![](notion-file-block://e260ad69-a5f8-830f-92f3-012f532f4d6d/f4d2bae2-1a35-431f-8da8-3be8351151c3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We can see that PaLM-E model has an edge on math reasoning, which results from its pre-training data mixture containing a higher proportion of mathematical content. 
## 3. Parameter count and design decisions
![](notion-file-block://6090ad69-a5f8-8329-8cce-012ae4be4aa2/bc3ef1e7-59ba-4d93-8a14-19f65a28c1a3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
In this experiment, we use RT-2-PaLI-X model because of its flexibility in terms of the model size. Co-fine-tuning keeps the original data around the fine-tuning part of training, so it allows the model to not forget its previous concepts.
## 4. Chain-of-thought reasoning
![](notion-file-block://7d10ad69-a5f8-82c4-8f51-818d545b1d7c/36bf9f32-0c91-4a9e-9eed-7af7aa25aba9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Include **Plan** step. This data augmentation schema acts as a bridge between VQA datasets and manipulation datasets. 
# Limitations
1. Robot cannot perform **new motions**.
2. **Real-time inference** becomes a major bottleneck.
3. Small number of available VLMs that can be used to create RT-2.
<empty-block/>