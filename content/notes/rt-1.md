<table_of_contents color="gray"/>
# Introduction
End-to-end robotic learning such as imitation or RL, collects **task-specific** data. Since robotic datasets might require engineering-heavy operation or expensive human demonstrations, so removing the need for task-specific datasets is more critical in robotics. The goal is 
> Can we train a single, capable, large multi-task backbone model on data consisting of a wide variety of robotic tasks?
# Model
![](notion-file-block://a3e0ad69-a5f8-8382-9294-81fb33374ccd/8743ba7d-03d0-4598-a610-23408a6bab92?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031694.jpg)
## 1. Image tokenization
### a. EfficientNet-B3
RT-1 tokenizes 6 images by using **EfficientNet-B3**. Unlike GATO and ViT, we do not patchify the images into visual tokens prior to Transformer backbone. Instead flatten the output feature map from the EfficientNet into 81 visual tokens which are passed on to the later layers of the network.
### b. Universal Sentence Encoder & FiLM
We should make the language instruction allow extraction of task-relevant image features early on. The instruction is embedded by **Universal Sentence Encoder**. Then this embedding is used as input of **identity-initialized FiLM** layers. Note that FiLM layer extracts task-relevant information from image features based on the given instruction: $`\text{FiLM}(x)=\gamma \odot x + \beta`$, where x is a feature image. FiLM layer updates $`\gamma`$($`f_c`$ layer) and $`\beta`$($`h_C`$ layer) to learn instruction information relative to a image. 
Since if FiLM layer is initialized randomly, then pre-trained weight of EfficientNet is disrupted, so we initialize $`f_c`$ and $`h_C`$ as zero(identity-initialized). Therefore FiLM layer acts as identity at first and preserves the function of pre-trained weights.
**MBConv **uses an inverted bottleneck structure of resNet that receives narrow-channel inputs, expands channels internally for rich computation, and outputs back to a narrow channel. This preserves compressed information in low-dimensional spaces while minimizing information loss through rich internal representations(MobileNetV2).
## 2. TokenLearner
TokenLearner is an element-wise attention module that maps a large number of tokens into a much smaller number of tokens. 
## 3. Transformer
After TokenLearner, there are 8 tokens and these are concatenated with the other images in history, so forming 48 tokens. The Transformer is a decoder-only sequence model.
# Experiments
There are 4 experimental criteria.
1. Seen task performance
2. Unseen task generalization
3. Robustness: Distractor and background robustness
4. Long-horizon scenarios
## 1. Generalization to Unseen Tasks and Environments
![](notion-file-block://ff20ad69-a5f8-82ad-a6b1-814875b8e342/e4abb685-8517-48c9-83dd-7250fbd3858c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
This generalization is due to natural language conditioning.
![](notion-file-block://99b0ad69-a5f8-8256-ba71-81b3889a5a87/d15d0342-f299-429f-beb7-d65eec391cd5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
From L1 to L3, additional generalization is assigned. This result shows that RT-1 perform well on more realistic instructions.
## 2. Generalization across Heterogeneous Datasets
### a. Simulation data
![](notion-file-block://2f70ad69-a5f8-8261-8e2f-81f2b12eebde/869d9a47-8744-436d-805e-78893ce9e488?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
The simulation data is never seen in the real world for robot. 
### b. Different robot data
![](notion-file-block://d840ad69-a5f8-8256-bf10-81ab49ce1577/7ece3a62-c043-4905-a83f-1d124146f797?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We evaluate the bin-picking tasks with the Everyday Robots(**EDR**). We can see that performance of EDR with only Kuka bin-picking data is **0%**. Thus it is difficult to transfer a behavior from another robot **morphology**. However, mixing the data form both robots allows RT-1 to infer the correct actions of EDR robot when faced with the states observed by Kuka robots.
## 3. Performance on Long-Horizon Scenarios
![](notion-file-block://7ed0ad69-a5f8-8288-b6ba-81b039cfa36c/e3803491-c0d6-4ae9-9090-6e0c0851cb5b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We execute RT-1 in the **SayCan **framework. SayCan is a robotic framework that combines an LLM for high-level task **planning **("Say") with a low-level policy for **execution **("Can") to complete long-horizon tasks.
## 4. Data Size and Diversity
![](notion-file-block://6e60ad69-a5f8-8395-a1f0-01d1aaa295cf/449f9e83-85b6-421d-b952-57aefb32c020?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
We can see that performance declines steeply when data diversity(%tasks) decreases compared to when data size(%data) decreases. Thus the data diversity is more essential than data quantity.
# Limitations
1. It is an imitation learning method
2. Generalization to new instructions is limited to the combinations of previously seen concepts
3. It cannot handle a dexterous set of manipulation tasks.
<empty-block/>
<empty-block/>
<empty-block/>