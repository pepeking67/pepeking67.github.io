# Policy Gradient Algorithm
It is used in RL problems with **continuous** action spaces. It directly learns the optimal policy by a parametric probability distribution $`\pi_\theta(a|s)`$, which stochastically selects action a in state s according to parameter $`\theta`$. It typically proceeds by sampling this stochastic policy and adjusting $`\theta`$ in the direction of grater **total reward**, so there is no need for experience replay.
Trajectory: $`\tau = s_0, a_0, r_1, s_1, a_1, \cdots, s_T`$
Total reward: $`r(\tau)`$
Objective function: $`J(\theta)=\mathbb{E}_{\pi_\theta}[r(\tau)]=\int p(\tau;\theta)r(\tau)d\tau`$ where $`p(\tau;\theta)=\pi_\theta(\tau)`$
To find the optimal $`\theta^*`$ which maximizes $`J(\theta)`$, we use gradient ascent: $`\theta \coloneqq \theta + \alpha \nabla _\theta J(\theta)`$
<span color="yellow_bg">Note that </span>$`\nabla J(\theta) = \int \nabla p(\tau;\theta)r(\tau)d\tau`$<span color="yellow_bg">, but in model-free environment we dont't know </span>$`p(\tau ; \theta)`$<span color="yellow_bg">, so it cannot be computed directly.</span>
## Policy Gradient Theorem
$$
\nabla_\theta J(\theta)= \nabla_\theta \mathbb{E}_{\pi_\theta}[r(\tau)]= \mathbb{E}_{\pi_\theta}[r(\tau)\sum^{T-1}_{t=0}\nabla_\theta log \pi_\theta(a_t|s_t)]
$$
pf) 
$$
\begin{aligned}\nabla \mathbb{E}[r(\tau)] &= \nabla \int \pi(\tau) r(\tau)d\tau \\&= \int \nabla \pi(\tau)r(\tau)d\tau \\&= \int \pi(\tau) \frac{\nabla \pi(\tau)}{\pi(\tau)}r(\tau)d\tau \\&= \int \pi(\tau)r(\tau)\nabla \log \pi(\tau) d\tau \\&= \mathbb{E}_\pi \left[ r(\tau) \nabla \log \pi(\tau) \right]\end{aligned}
$$
And $`\pi(\tau)=p(s_0)\pi(a_0|s_0)p(s_1|s_0,a_0)\pi(a_1|s_0,a_0,s_1)p(s_2|s_0,a_0,s_1,a_1)\cdots`$.
By Markov property, $`\pi(\tau)=p(s_0)\prod^{T-1}_{t=0}\pi(s_t|s_t)p(s_{t+1}|s_t,a_t)`$.
And $`\nabla (\log p(s_0)+\sum \log p(s_{t+1}|s_t, a_t)) \rightarrow 0`$, so that $`\nabla \log \pi(\tau)=\sum \nabla \log \pi(a_t|s_t) \ _\square`$
<empty-block/>
Thus we can approximate the expectation by **sampling**.
### Markov Chain Monte Carlo(MCMC)
Sample a large number of trajectories using minibatch and take their average, which is an unbiased approximation. This is called **Morkov Chain Monte Carlo**.
Even though the gradient of the parametrized policy does not depend on $`r(\tau)`$, depending on $`\theta`$, this term adds high variance in MCMC sampling because of erratic trajectories. Instead, total reward $`r(\tau)`$ of the trajectory $`\tau`$ can be replaced by discounted return $`G_t`$.
This PG algorithm is called **REINFORCE**.
# REINFORCE
![](notion-file-block://e930ad69-a5f8-83fd-a108-815f31b920e7/93d59b46-502b-4a33-bd5b-70fc98cd5e0e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031643.jpg)
## REINFORCE with baseline
Data samples(erratic trajectories) are of high **variance. **To reduce the variance, we optimize for the difference in the discounted return $`G_t`$by a baseline $`b(s_t)`$, any function that not vary with $`a_t`$.
$$
\nabla_\theta J(\theta)=\nabla_\theta \mathbb{E} _{\pi_\theta}[r(\tau)]=\mathbb{E}_{\pi_\theta}[\sum^{T-1}_{t=0}(G_t-b(s_t))\nabla_\theta log \pi_\theta(a_t|s_t)]
$$
Here, the gradient is unchanged since baseline $`b(s_t)`$ does not vary with $`a_t`$.
Good baseline: state-value function $`V(s)=\mathbb{E}_{\pi_\theta}[G_t|S_t=s]`$
![](notion-file-block://45c0ad69-a5f8-834f-bc23-81785ff788c4/f7415aa2-a4ad-4a0f-bf7b-4c02a132cf0f?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=1000031642.jpg)
We use additional network for state-value function baseline.
<empty-block/>