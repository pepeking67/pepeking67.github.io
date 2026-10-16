<file src="notion-file-block://ecf0ad69-a5f8-8224-ae2f-017b91bf124e/ac6b6251-1cec-4a05-b299-afa167d2af34?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=CamScanner_07-07-2026_22.21.pdf"></file>
<table_of_contents color="gray"/>
# Introduction
Learning to control agents directly from high-dimensional sensory inputs like vision and speech is one of the long-standing challenge of RL. And deep learning can be used to resolve this issue. However, RL has several challenges from a DL perspective. 
## Problems
1. DL applications require large amounts of hand-labelled training data. RL algorithms, on the other hand, must be able to learn from a scalar reward signal that is delayed. The delay between actions and rewards seems daunting compared to supervised learning.
2. DL assumes the data samples to be independent, while in RL one encounters sequences of highly **correlated states. **
3. In RL **the data distribution changes as learning** new behaviours, while DL algorithms assume a fixed distribution.
This paper demonstrates that a CNN can overcome these challenges to learn successful control policies from raw video data.
To alleviate the problems of correlated data(2) and non-stationary distributions(3), we use an **experience replay** which randomly samples previous transitions, and thereby smooths the training distribution over many past behaviors.
# Background
Environment: $`\mathcal{E}`$, in this paper, the Atari emulator
Action space: $`\mathcal{A} = \{ 1, \cdots, K \}`$
<empty-block/>
The emulator’s internal state is not observed by agent. Instead, it observes an image $`x_t \in \mathbb{R}^d`$ from the emulator, representing the current screen.
Since the agent only observes current screen, many emulator states are perceptually aliased. Therefore, we consider sequences of actions and observations,
$`s_t=x_1, a_1, x_2, \cdots , a_{t-1}, x_t`$, and learn depending on these sequences.
This formalism gives MDP in which each sequence is distinct state. So, we can simply use complete sequence $`s_t`$ as the state at time $`t`$.
<empty-block/>
Return: $`R_t = \sum^T_{t'=t} \gamma^{t'-t} r_{t'}`$, where $`T`$ is the time-step at which the game terminates.
Optimal action-value function $`Q^*(s,a)`$: the maximum expected return achievable by fallowing any strategy.
$$
\begin{align*}
Q^*(s,a) &= \max_\pi \mathbb{E} [R_t | s_t =s, a_t=a, \pi] \\
         &= \mathbb{E}_{s' \sim \mathcal{E}}[r+\gamma \max_{a'}Q^*(s', a') | s, a]
\end{align*}
$$
Previously, by using Bellman equation, many RL algorithms estimate the action-value function. Instead, we use a function approximator to estimate the action-value function, $`Q(s,a;\theta) \approx Q^*(s,a)`$. Typically a linear function approximator is used, but non-linear function approximator such as a neural network can be used. We refer to a neural network function approximator with weights $`\theta`$ as a **Q-network**. 
<empty-block/>
Q-network can be trained by minimising a sequence of loss functions $`L_i(\theta_i)=\mathbb{E}_{s,a \sim \rho(\cdot)}[(y_i-Q(,sa;\theta_i))^2]`$, where $`y_i=\mathbb{E}_{s' \sim \mathcal{E}}[r+\gamma \max_{a'}Q^*(s', a';\theta_{i-1}) | s, a]`$ is the **target** and $`\rho(s,a)`$ is a probability distribution over s, a as **behaviour distribution**.
The paramters from the previous iteration $`\theta_{i-1}`$ are held fixed when optimising the $`L_i(\theta_i)`$.  {color="yellow_bg"}
The targets depend on the network weights in contrast with the supervised learning which are fixed.
$$
\nabla_{\theta_i} L_i (\theta_i) = \mathbb{E}{s,a \sim \rho(\cdot); s' \sim \mathcal{E}} \left[ \left( r + \gamma \max{a'} Q(s', a'; \theta_{i-1}) - Q(s, a; \theta_i) \right) \nabla_{\theta_i} Q(s, a; \theta_i) \right]
$$
By using stochastic gradient descent(SGD), rather than computing the full expectations in the above gradient, it is efficient to optimise the loss function.
This algorithm is model-free and off-policy. In practice, the behaviour distribution is often selected by $`\epsilon`$-greedy strategy.
# Deep Reinforcement Learning
## Experience Replay
**Experience replay**: store the agent’s experiences at each time-step, $`e_t = (s_t, a_t, r_t, s_{t+1})`$ in a dataset $`\mathcal{D} = e_1, \cdots, e_N`$, into a replay memory.
$`e \sim \mathcal{D}`$ drawn at random from the pool of stored samples. After performing experience replay, the agent selects and excutes an action according to an $`\epsilon`$-greedy policy.
![](notion-file-block://70d0ad69-a5f8-8277-a59b-010b2a88d4c4/db7e2e7a-a5cc-4c0e-9b17-676fe32369ad?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
**Advantages**
1. Each step of experience can be used in many weight updates, allowing greater data efficiency.
2. Randomizing the samples breaks correlations and therefore reduces the variance of updates.
<empty-block/>
In practice, it stores N experience tuples in the replay memory, and samples uniformly at random from $`\mathcal{D}`$.
<empty-block/>