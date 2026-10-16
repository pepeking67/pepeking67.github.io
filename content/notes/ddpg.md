<empty-block/>
<table_of_contents color="gray"/>
# Introduction
DQN still handles only low-dimensional action spaces such as curse of dimensionality. A naive application of actor-critic method with neural function approximators can solve this problem. Deterministic policy gradient(**DPG**) learns a deterministic policy $`a=\mu(s)`$ as an **actor** on continuous action spaces and an action-value function $`Q(s,a)`$ as a **critic**. We can make this algorithm stable using two innovations of DQN. 
1. replay buffer
2. target Q-network
DDPG is designed to handle continuous action spaces by replacing DQN's argmax operation with a neural network. 
# Background
At each timestep $`t`$ the agent receives an observation $`x_t`$, takes an action $`a_t`$ and receives a scalar reward $`r_t`$. In general, the environment may be **partially** observed so that the entire history of the observation, action pairs $`s_t=(x_1, a_1, \cdots , a_{t-1}, x_t)`$ may be required to describe the state. However, we assumed the environment is **fully-observed** so $`s_t=x_t`$.
The action-value function describes the expected return after taking an action $`a_t`$ in state $`s_t`$.
$$
Q^\pi (s_t,a_t)=\mathbb{E} _{r_{i\geq t},s_{i >t} \sim E, a_{i>t}\sim \pi} [R_t|s_t,a_t]
$$
There is a recursive relationship known as the Bellman equation.
$$
Q^\pi (s_t,a_t)=\mathbb{E}_{r_t,s_{t+1}\sim E }[r(s_t,a_t)+\gamma \mathbb{E}_{a_{t+1}\sim\pi}[Q^\pi(s_{t+1},a_{t+1})]]
$$
If the target policy is deterministic, we can decribe it as a function $`\mu:S\leftarrow A`$ and **avoid the inner expectation**.
$$
Q^\mu (s_t,a_t)=\mathbb{E}_{r_t,s_{t+1}\sim E }[r(s_t,a_t)+\gamma Q^\mu(s_{t+1},\mu(s_{t+1}))]
$$
Thus, the expectation depends only on the environment, so it is possible to learn $`Q^\mu`$ off-policy, using transitions wich are generated from a different stochastic behaviour policy $`\beta`$.
Note that DQN applied off-policy learning by obtaining a deterministic policy through the max operation.
# Algorithm
We used an actor-critic approach baed on the DPG algorithm. The DPG algorithm maintains a parametrized actor function $`\mu(s|\theta^ \mu)`$ which specifies current policy by deterministically mapping states to a specific action. The critic $`Q(s,a)`$ is learned using the Bellman equation as in Q-learning. The actor is updated by following.
$$
\nabla_{\theta^\mu}J \approx \mathbb{E}_{s_t\sim \rho ^\beta }[\nabla_{\theta^\mu}Q(s,a|\theta^Q)|_{s=s_t,a=\mu(s_t|\theta^\mu)}]\\= \mathbb{E}_{s_t\sim \rho ^\beta }[\nabla_a Q(s,a|\theta^Q)|_{s=s_t,a=\mu(s_t)}\nabla_{\theta_\mu}\mu(s|\theta^\mu)|_{s=s_t}]
$$
This is based on the deterministic policy gradient theorem, analogous to stochastic PG theorem.
![](notion-file-block://f200ad69-a5f8-8272-8a9f-01f2e0297dcb/65308f15-ab63-42b7-959b-740115fdf5f4?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031667.jpg)
It applies chain rule to the expected return with respect to the actor parameters.
Its contribution is to provide modifications to DPG, inpired by DQN, which allow it to use neural network function approximators to learn in large state and action spaces.
DDPG adapts DQN's two innovations: replay buffer and target network. But the target network is modified for actor-critic and using **soft** target updates: $`\theta' \leftarrow \tau \theta  + (1-\tau)\theta'`$ with $`\tau \ll 1`$.
When learning from low dimensional feature vector observations, the different components of the observation may have different physical units. This can make it difficult for the network to learn effectively. One approach to this problem is to manually scale the features so they are in similar ranges across environments and units: **batch normalization**.
Since DDPG uses deterministic policy, we must add exploration. However, in contrast to DQN, action spaces are continuous, so we could not apply $`\epsilon`$-greedy(product $`\frac{1}{N}`$ where $`N`$ is finite) algorithm. So we constructed an exploration policy $`\mu'`$ by adding noise to our actor policy.
 
$$
\mu'(s_t)=\mu(s_t|\theta^\mu_t)+\mathcal{N}
$$
![](notion-file-block://bf10ad69-a5f8-8287-a23c-816f234b2f72/a12d5900-8f1c-4847-aee6-a1486e84c04a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031668.jpg)
<empty-block/>