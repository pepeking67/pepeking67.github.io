<file src="notion-file-block://a5e0ad69-a5f8-8303-833c-81955ffde80c/f3fdbfa8-6f7e-4b71-87c8-ba0f3b696ab2?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=CamScanner_2026-07-13_22.07.pdf"></file>
<table_of_contents color="gray"/>
# Actor-Critic Method
Actor-Critic method consists of two networks.
1. **Critic network**: update $`\phi`$ for **value function** $`V(s;\phi)`$ or $`Q(s,a;\phi)`$
2. **Actor network**: update $`\theta`$ for **policy** $`\pi_\theta(a|s)`$ using policy gradient $`\nabla_\theta J(\theta)`$
As in REINFORCE with baseline to reduce variance, learning value function to policy is valuable.
REINFORCE with baseline is unbiased but learns slowly because of high variance of $`G_t`$.
Thus we use TD Actor-Critic method with bootstrapped Critic.
Practically, critic and actor networks share the network, but use their own weight parameters.
![](notion-file-block://9c00ad69-a5f8-834d-99b0-81adfd11aed8/ef9658a4-8bff-4263-9fc0-d123305a2b47?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031650.jpg)
PG has many equivalent forms.
$$
\begin{aligned}
\nabla_\theta J(\theta) &= \mathbb{E}_{\pi_\theta} \left[ \sum_{t=0}^{T-1} G_t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \right] && \\
&= \mathbb{E}_{\pi_\theta} \left[ \sum_{t=0}^{T-1} (G_t - V_\phi(s_t)) \nabla_\theta \log \pi_\theta(a_t \mid s_t) \right] && \text{REINFORCE with baseline} \\
&= \mathbb{E}_{\pi_\theta} \left[ Q_\phi(s, a) \nabla_\theta \log \pi_\theta(a \mid s) \right] && \text{Q-value Actor-Critic} \\
&= \mathbb{E}_{\pi_\theta} \left[ A_{\phi_1, \phi_2}(s, a) \nabla_\theta \log \pi_\theta(a \mid s) \right] && \text{Advantage Actor-Critic} \\
&= \mathbb{E}_{\pi_\theta} \left[ (r + \gamma V_\phi(s') - V_\phi(s)) \nabla_\theta \log \pi_\theta(a \mid s) \right] && \text{TD Actor-Critic}
\end{aligned}
$$
1. MC target(REINFORCE with baseline)
Actor: $`\Delta\theta = \alpha(G_t-V_\phi(s_t))\nabla_\theta \log \pi_\theta (a_t|s_t)`$ ⇒ $`\theta \leftarrow \theta + \alpha\gamma^t \delta \nabla_\theta \log \pi(a_t|s_t;\theta)`$
Critic: $`\Delta \phi =\beta (G_t - V_\phi(s_t)) \nabla_\phi V_\phi(s_t)`$ ⇒ $`\delta \leftarrow G_t-V(s_t;\phi)`$ and $`\phi \leftarrow \phi + \beta \delta \nabla_\phi V(s_t;\phi)`$
1. TD target
Actor: $`\Delta\theta = \alpha(r_{t+1}+\gamma V_\phi(s_{t+1})-V_\phi(s_t))\nabla_\theta \log \pi_\theta (a_t|s_t)`$ ⇒ $`\theta \leftarrow \theta + \alpha\gamma^t \delta \nabla_\theta \log \pi(a_t|s_t;\theta)`$
Critic: $`\Delta \phi =\beta (r_{t+1} + \gamma V_\phi(s_{t+1}) - V_\phi(s_t)) \nabla_\phi V_\phi(s_t)`$ ⇒ $`\delta \leftarrow r+\gamma V(s_{t+1};\phi)-V(s_t;\phi)`$ and $`\phi \leftarrow \phi + \beta \delta \nabla_\phi V(s_t;\phi)`$
![](notion-file-block://1540ad69-a5f8-83e1-b097-0166a82754f9/227ec4ae-96b3-441d-9404-92b0a71f7aed?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031652.jpg)
# Introduction
Experience replay has several drawbacks.
1. It uses more memory and computation.
2. It requires **off-policy** learning algorithms.
Instead of experience replay, A3C asynchronously executes multiple agents in parallel.
At DQN, it updates the action-value function $`Q(s,a)`$ toward the **one-step** return 
$`r+ \gamma \max_{a'}Q(s',a';\theta)`$. So this can make the learning process slow since many updates are required.
Thus it uses **n-step** return.
$$
r_t+\gamma r_{t+1} + \cdots + \gamma^{n-1}r_{t+n-1}+\max_a \gamma^nQ(s_{t+n},a)
$$
In contrast to value-based methods, policy-based methods directly parametrize the policy $`\pi(a|s;\theta)`$ and update the $`\theta`$ by performing gradient ascent on $`\mathbb{E}[R_t]`$. For example, REINFORCE with baseline has the gradient $`\nabla_\theta \log \pi (a_t|s_t;\theta)(R_t-b_t(s_t))`$. 
Commonly $`b_t(s_t) \approx V^\pi(s_t)`$ is used, and it can be seen as an estimate of the **advantage** of action $`a_t`$ in state $`s_t`$, $`A(a_t,s_t)=Q(a_t,s_t)-V(s_t)`$, because $`R_t`$ is an estimate of $`Q^\pi(a_t,s_t)`$ and $`b_t`$ is an estimate of $`V^\pi(s_t)`$. 
This approach can be viewed as an actor-critic architecture where the policy $`\pi`$ is the actor and the baseline $`b_t`$ is the critic.
In this paper, it presents multi-threaded **asynchronous** variants of one-step Sarsa, one-step Q-learning, n-step Q-learning, and advantage actor-critic. There are two main ideas.
1. Ascynchronous actor-learners
Using multiple CPU threads on a single machine, so it removes the communication costs of sending gradients and parameters.
1. Running in parallel to explore different parts of the environments
It does not use replay memory and rely on parallel actors employing different exploration policies. By using asynchronous multi-threading, parallel agents can collect uncorrelated data without a replay buffer. This allows the algorithm to remain on-policy, avoiding the high variance caused by importance sampling in off-policy learning.
## Asynchronous one-step Q-learning
![](notion-file-block://a840ad69-a5f8-836a-9006-8144eebe10ad/cf4bb7cc-246e-4884-95cc-f56569e06cc1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031661.jpg)
## Asynchronous one-step Sarsa
It uses a different target value $`r+\gamma Q(s',a';\theta^-)`$
## Asynchronous n-step Q-learning
![](notion-file-block://5860ad69-a5f8-8233-8868-81fe0535633a/c9309b12-eee5-4be6-a619-9d7b119ad5f5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031662.jpg)
By adopting a forward view, n-step returns can be accumulated to form a standard mini-batch, generating a single clean gradient per update. This aligns directly with how momentum-based optimizers (e.g., Adam, RMSProp) operate, as they expect standard mini-batch gradients to update their internal momentum states. In contrast, using a backward view with eligibility traces requires maintaining additional trace vectors for every neural network weight alongside optimizer states, introducing unnecessary memory overhead and algorithmic complexity.
## Asynchronous advantage actor-critic
Like n-step Q-learning, variant of actor-critic also operates in the forward view and uses the same mix of n-step returns $`G_t^{(n)}`$ to update both the policy and the value-function.
$$
\text{Agent actor: }\Delta \theta' \leftarrow \Delta \theta ' + (G_t^{(n)}-V_{\phi'}(s_t))\nabla _{\theta'}\log \pi_{\theta'}(a_t|s_t) \\ \text{Agent critic: }\Delta \phi' \leftarrow \Delta \phi ' + (G_t^{(n)}-V_{\phi'}(s_t))\nabla _{\phi'}V_{\phi'}(s_t)
$$
![](notion-file-block://3ef0ad69-a5f8-82ca-8825-8198c30f2eed/990afa3c-c6fb-4e82-9449-ca315098819a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031663.jpg)
Note that it shares some of the parameters $`\theta`$ and $`\theta_v`$ in practical. It typically uses a convolutional neural network that has one softmax output for the policy $`\pi(a_t|s_t;\theta)`$ and one linear output for the value function $`V(s_t;\theta_v)`$.
And adding the **entropy** of the policy to the objective function improved exploration by discouraging premature convergence to suboptimal deterministic policies. 
$`\nabla_{\theta'} \log \pi(a_t|s_t;\theta')(R_t-V(s_t;\theta_v))+\beta \nabla_{\theta'}H(s_t;\theta'))`$, where H is the entropy.
The overall process of A3C is as fallows.
(1) Each worker agent runs separately for parallel training.
(2) Between each update, each agent takes a copy of the global network's shared parameters.
(3) During $`t_\text{max}`$ steps, each agent computes an accumulated gradient and finally updates the shared paramters.
<empty-block/>