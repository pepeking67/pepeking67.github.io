Reference: [https://rlwithme.tistory.com/6](https://rlwithme.tistory.com/6)
<table_of_contents color="gray"/>
# Introduction
The performance of DDPG does not improve monotonically. TRPO addresses the problem by adopting two concepts: **Minorization-Maximization algorithm** and **trust region**. Policy updates on the trust region guarantee monotonic improvement of the expected return. Its implementation is complicated so being not practical.
# Background
$`c:S\rightarrow \mathbb{R}`$ is the cost function. 
$`\pi:S\times A \rightarrow [0,1]`$ is a stochastic policy.
$`\eta(\pi)=\mathbb{E}_{s_0.a_0.\cdots}\left[ \sum\limits^\infty_{t=0}\gamma^t c(s_t) \right]`$, where $`s_0\sim\rho(s_0), \ a_t\sim \pi(a_t|s_t), \ s_{t+1} \sim P(s_{t+1}|s_t, a_t)`$ is expected discounted cost.
The state-action value function $`Q_\pi(s_t, a_t)=\mathbb{E}_{s_{t+1}, a_{t+1},\cdots}\left[ \sum\limits^\infty_{l=0}\gamma^l c(s_{t+l}) \right]`$.
The value function $`V_\pi(s_t)=\mathbb{E}_{a_t, s_{t+1},\cdots}\left[ \sum\limits^\infty_{l=0}\gamma^l c(s_{t+l}) \right]`$.
The advantage function $`A_\pi(s,a)=Q_\pi(s,a)-V_\pi(s)`$.
Alternatively we compute $`\eta(\tilde{\pi})`$ from the old policy $`\pi`$.
$$
(1)\ \ \ \ \eta(\tilde{\pi})=\eta(\pi)+\mathbb{E}_{s_0,a_0,s_1,a_1,\cdots}\left[ \sum\limits^\infty_{t=0}\gamma^t A_\pi(s_t,a_t) \right]
$$
$$
\because \mathbb{E}\left[ \sum\limits^\infty_{t=0}\gamma^t A_\pi(s_t,a_t) \right]=\mathbb{E}\left[ \sum\limits^\infty_{t=0}\gamma^t (r(s_t)+\gamma V_\pi(s_{t+1})-V_\pi (s_t)) \right]=\eta(\pi)+\mathbb{E}\left[ \sum\limits^\infty_{t=0}\gamma^{t+1}V_\pi(s_{t+1})-\sum\limits^\infty_{t=0}\gamma^{t}V_\pi(s_{t}) \right]=\eta(\tilde{\pi})-\mathbb{E}\left[ V_\pi(s_0) \right]=\eta(\tilde{\pi})-\eta(\pi)
$$
$`\rho_\pi`$: discounted visitation frequencies
$$
\rho_\pi(s)=P(s_0=s)+\gamma P(s_1=s)+\gamma^2 P(s_2=s)+\cdots
$$
$`\mathbb{E}_{s_0,a_0,s_1,a_1,\cdots}\left[ \sum\limits^\infty_{t=0}\gamma^t A_\pi(s_t,a_t) \right]=\sum\limits^\infty_{t=0}\sum\limits_s P(s_t=s|\tilde{\pi})\sum\limits_a \tilde{\pi}(a|s) \gamma^t A_\pi(s,a) = \sum\limits_s\sum\limits^\infty_{t=0}\gamma^t P(s_t=s|\tilde{\pi})\sum\limits_a \tilde{\pi}(a|s)  A_\pi(s,a)=\sum\limits_s \rho_{\tilde{\pi}}(s)\sum\limits_a \tilde{\pi} A_\pi(s,a)`$
$$
(2)\ \ \ \ \eta(\tilde{\pi})=\eta(\pi)+\sum\limits_s \rho_{\tilde{\pi}}(s)\sum\limits_a \tilde{\pi} A_\pi(s,a)
$$
This equation implies that any policy update $`\pi \rightarrow \tilde{\pi}`$ that has a **non-positive expected advantage** at every state s is guaranteed to reduce $`\eta`$. However, due to estimation and approximation error, there will be some states s for which the expected advantage is positive. The complex dependency of $`\eta_{\tilde{\pi}}(s)`$ on $`\tilde{\pi}`$ makes (2) difficult to optimize directly, so instead we use $`\eta_\pi`$.
$$
(3)\ \ \ \ L_\pi(\tilde{\pi})=\eta(\pi)+\sum\limits_s \rho_\pi(s)\sum\limits_a \tilde{\pi} A_\pi(s,a)
$$
It ignores changes in state visitation density due to changes in the policy.
$$
(4)\ \ \ \ L_{\pi_{\theta_0}}(\pi_{\theta_0})=\eta(\pi_{\theta_0}), \\ \nabla_\theta L_{\pi_{\theta_0}}(\pi_\theta)|_{\theta=\theta_0}=\nabla_\theta \eta (\pi_\theta)|_{\theta=\theta_0}
$$
We can see that $`L_\pi`$ matches $`\eta`$ to first order(same gradient). Thus a sufficiently small step 
$`\pi_{\theta_0} \rightarrow \tilde{\pi}`$ that reduces $`L_{\pi_\text{old}}`$ will also reduce $`\eta`$. But it **does not give us any guidance on how big of a step to take**.
Use the **conservative policy iteration** update(Kakade & Langford) to address this problem. 
The new policy $`\pi_\text{new}`$ is taken to be the following **mixture policy**.
$$
(5)\ \ \ \ \pi_\text{new}(a|s)=(1-\alpha)\pi_\text{old}(a|s)+\alpha \pi'(a|s)
$$
Then by Kakade & Langford proved that it has the lower bound:
$$
(6) \ \ \ \ \eta(\pi_\text{new}) \leq L_{\pi_\text{old}}(\pi_\text{new})+\frac{2\epsilon\gamma}{(1-\gamma(1-\alpha))(1-\gamma)}\alpha^2,\ \text{where}
$$
$$
(7)\ \ \ \ \epsilon=\max_s|\mathbb{E}_{a\sim\pi'(a|s)}[A_\pi(s,a)]|
$$
We can express (6) more simpler bound.
$$
(8) \ \ \ \ \eta(\pi_\text{new}) \leq L_{\pi_\text{old}}(\pi_\text{new})+\frac{2\epsilon\gamma}{(1-\gamma)^2}\alpha^2
$$
Note that this bound is only applies to the **mixture policy, which is restrictive in practice**.
# Monotonic Improvement
The policy improvement bound in [(6)](/p/2ea0ad69a5f8836996ae81c945577ee5?pvs=25#64f0ad69a5f882f2b13a81d0a58ede92) can be extended to general **stochastic policies** rather than mixture polices by replacing $`\alpha`$ with a distance meqsure between $`\pi`$ and $`\tilde{\pi}`$.
We use the total variation divergence $`D_\text{TV}^{\max}(\pi, \tilde{\pi})=\frac{1}{2}\sum_i|p_i-q_i|`$.
$$
(9)\ \ \ \ D_{\text{TV}}^{\max}(\pi, \tilde{\pi})=\max_s D_{\text{TV}}(\pi(\cdot |s) || \tilde{\pi}(\cdot|s))
$$
**Thm.** Let $`\alpha = D_{\text{TV}}^{\max}(\pi_\text{old}, \pi_\text{new})`$, and $`\epsilon=\max_s\max_a|A_\pi(s,a)|`$. Then (8) holds.
Note that $`D_\text{TV}(p||q)^2 \leq D_\text{KL}(p||q)`$. Let $`D_{\text{KL}}^{\max}(\pi, \tilde{\pi})=\max_s D_{\text{KL}}(\pi(\cdot |s) || \tilde{\pi}(\cdot|s))`$.
Then we can get following bound.
$$
(10)\ \ \ \ \eta(\tilde{\pi}) \leq L_\pi(\tilde{\pi})+CD_{\text{KL}}^{\max}(\pi, \tilde{\pi}),\ \text{where }C=\frac{2\epsilon\gamma}{(1-\gamma)^2}
$$
**Majorization-Minimization** algorithm using the lower bound as a **surrogate objective** guarantees to generate a monotonically improving policies.
![](notion-file-block://ed10ad69-a5f8-82e9-a90d-01d8c9b94c75/8a93c6e8-d0c8-44b9-afc2-0bcb4ebc41ca?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Let $`M_i(\pi)=L_{\pi_i}(\pi) + CD^{\max}_{\text{KL}}(\pi_i,\pi)`$. Then
$$
(11)  \ \ \ \ \begin{aligned}\eta(\pi_{i+1}) &\le M_i(\pi_{i+1}) \quad \text{by Equation (10)} \\\eta(\pi_i) &= M_i(\pi_i), \quad \text{therefore,} \\\eta(\pi_{i+1}) - \eta(\pi_i) &\le M_i(\pi_{i+1}) - M_i(\pi_i).\end{aligned}
$$
By minimizing $`M_i`$ at each iteration, objective $`\eta`$ is non-increasing.
<columns>
	<column ratio="68.75">
		![](notion-file-block://e380ad69-a5f8-8395-9015-014ecfeb5f3d/2f4dd6db-d788-4f28-8b22-1fc6dbd59462?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
	<column ratio="31.25">
		![](notion-file-block://2560ad69-a5f8-83b8-ae79-0190307cb2d4/c9f44766-a314-45a9-9cde-073b4849f89d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
	</column>
</columns>
# Optimization of Parameterized Policies
Since we use parameterized policies $`\pi_\theta`$ with parameter $`\theta`$, so we use notation $`\theta`$ rather than $`\pi`$. For example, $`\eta(\theta)=\eta(\pi_\theta)`$. We can express [(10)](/p/2ea0ad69a5f8836996ae81c945577ee5?pvs=25#51e0ad69a5f883929bb981c56bc7d7b5) using this notation.
$$
\eta(\theta) \leq L_{\theta_{\text{old}}}(\theta)+CD_{\text{KL}}^{\max}(\theta_{\text{old}}, \theta)
$$
Thus by majorization-minimization  algorithm we are guaranteed to improve the objective $`\eta`$:
$$
\operatorname*{minimize}_{\theta} \left[ L_{\theta_{\text{old}}}(\theta) + C D_{\text{KL}}^{\max}(\theta_{\text{old}}, \theta) \right]
$$
In practice, $`C`$ would be very small, so we use a **robust constraint** on the KL divergence.
$$
(12)\ \ \ \ \operatorname*{minimize}_{\theta} L_{\theta_{\text{old}}}(\theta) \\ \ \ \ \ \text{subject to }D_{\text{KL}}^{\max}(\theta_{\text{old}}, \theta) \leq \delta
$$
Since using max in $`D_{\text{KL}}^{\max}(\theta_{\text{old}}, \theta)`$, so we should calculate at every state space. Therefore, we use **heuristic approximation** which considers the average KL divergence.
$$
\bar{D}^\rho_\text{KL}(\theta_1, \theta_2) = \mathbb{E}_{s\sim \rho}[D_\text{KL}(\pi_{\theta_1}(\cdot|s) || \pi_{\theta_2}(\cdot|s)]
$$
$$
(13)\ \ \ \ \operatorname*{minimize}_{\theta} L_{\theta_{\text{old}}}(\theta) \\ \ \ \ \ \text{subject to }\bar{D}^{\rho_{\theta_{\text{old}}}}_\text{KL}(\theta_{\text{old}}, \theta) \leq \delta
$$
# Sample-based Estimation
Our goal is to approximate objective and constraint functions using Monte Carlo simulation(sample-based estimation).
We can describe (13) as fallow.
$$
(14)\ \ \ \ \operatorname*{minimize}_{\theta} \sum_s\rho_{\theta_\text{old}}(s)\sum_a \pi_\theta(a|s)A_{\theta_\text{old}}(s,a) \\ \ \ \ \ \text{subject to }\bar{D}^{\rho_{\theta_{\text{old}}}}_\text{KL}(\theta_{\text{old}}, \theta) \leq \delta
$$
First, we replay the fallowing terms.
1. $`\sum_s \rho_{\theta_\text{old}}(s)[\cdots]`$ by $`\frac{1}{1-\gamma} \mathbb{E}_{s\sim\rho_{\theta_\text{old}}}[\cdots]`$.
2. $`A_{\theta_\text{old}}`$ by $`Q_{\theta_\text{old}}`$.
3. Importance sampling: $`\sum_a \pi_\theta(a|s)A_{\theta_\text{old}}(s,a)=\mathbb{E}_{a\sim \pi_{\theta_\text{old}}}\left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_\text{old}}(a|s)} A_{\theta_\text{old}}(s,a) \right]`$.
By (a), we make the equation as estimation form. Directly computing $`\sum_a \pi_\theta(a|s)A_{\theta_\text{old}}(s,a)=\mathbb{E}_{a\sim\pi_\theta} [A_{\theta_\text{old}}]`$, but we cannot get any information from the new policy. Thus by (c), using importance sampling, we can use samples from an old policy.
Final optimization problem:
$$
(15)\ \ \ \ \min_{\theta} \mathbb{E}_{s \sim \rho_{\theta_{\text{old}}}, a \sim \pi_{\theta_{\text{old}}}} \left[ \frac{\pi_\theta(a|s)}{\pi_{\theta_{\text{old}}}(a|s)} Q_{\theta_{\text{old}}}(s, a) \right] \\ \text{subject to} \quad \mathbb{E}_{s \sim \rho_{\theta_{\text{old}}}} \left[ D_{\text{KL}}(\pi_{\theta_{\text{old}}}(\cdot|s) \parallel \pi_{\theta}(\cdot|s)) \right] \le \delta
$$
All that remains is to replace the expectations by **sample averages**(Monte Carlo simulation) and replace the Q-value by an **empirical estimate**.
There are two sampling schemes.
## Single Path
Simulating the policy $`\pi_\text{old}`$ to generate $`s_0,a_0,s_1,a_1,\cdots , s_{T-1},a_{T-1},s_T`$. Hence the behavior policy $`q(a|s)=\pi_\text{old} (a|s)`$. $`Q_{\theta_\text{old}}(s,a)`$ is computed at each state-action pair $`(s_t,a_t)`$ from the trajectory.
![](notion-file-block://80c0ad69-a5f8-83db-ba20-81c1c4efadb0/770db79c-e1fc-4034-93d5-c2f57dcddebb?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## Vine
Since single path considers only **one** sample trajectory, so it has high variance. To solve this problem, vine uses **rollout set**. Simulating $`\pi_{\theta_i}`$ to generate a number of trajectories. We choose a subset of N states along these trajectories(rollout set). Then we sample K actions for each state $`s_n`$ in the rollout set according to $`a_{n,k}\sim q(\cdot|s_n)`$. In practice, $`q(\cdot|s_n)=\pi_{\text{old}}(\cdot|s_n)`$ works well.
![](notion-file-block://9030ad69-a5f8-830c-817c-81aca507bab1/94ec801d-ba28-4343-8bab-7eec28c1b025?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
 We estimate $`\hat{Q}_{\theta_i}(s_n, a_{n,k})`$ by performing a rollout(short trajectory) starting with state $`s_n`$. We can construct an estimator of the surrogate loss using importance sampling.
$$
(16)\ \ \ \ L_n(\theta)=\frac{\sum_{k=1}^K \frac{\pi_\theta (a_{n,k}|s_n)}{\pi_{\text{old}}(a_{n,k}|s_n)}\hat{Q}(s_n,a_{n,k})}{\sum_{k=1}^K \frac{\pi_\theta (a_{n,k}|s_n)}{\pi_{\text{old}}(a_{n,k}|s_n)}}
$$
# Practical Algorithm
1. Get Monte-Carlo estimates using single path or vine.
2. By averaging over samples, construct [(15)](/p/2ea0ad69a5f8836996ae81c945577ee5?pvs=25#a5e0ad69a5f88354a2c081af5bc784b6).
3. Use **conjugate gradient** algorithm followed by **line search**.
## Natural Policy Gradient(NPG)
Reference: [NPG](https://rlwithme.tistory.com/5)
Since Hessian of KL divergence is **Fisher information matrix**, so (15) is similar to **natural gradient** descent. Use Taylor series up to the 1st order for $`L_{\theta_\text{old}}`$ and the 2nd order for $`\bar{D}_\text{KL}(\theta_\text{old}|| \theta)`$.
$$
\min_\theta \nabla _\theta L_{\theta_\text{old}}(\theta)|_{\theta=\theta_\text{old}} \ \text{subject to }\frac{1}{2}(\theta-\theta_\text{old})^T H(\theta-\theta_\text{old}) \leq \delta
$$
Note that Fisher information matrix $`H=\nabla_\theta ^2 \bar{D}_\text{KL}(\theta_\text{old}||\theta)`$. In practical, we use 
$$
H\approx \frac{1}{N}\sum_{n=1}^N \frac{\partial^2}{\partial \theta_i \partial \theta_j}D_\text{KL}(\pi_{\theta_\text{old}}(\cdot|s_n) || \pi_\theta(\cdot |s_n)|_{\theta=\theta_\text{old}}
$$
Natural gradient $`H^{-1} \nabla_\theta L_{\theta_\text{old}} (\theta)|_{\theta=\theta_\text{old}}`$ is the steepest direction. $`\nabla_\theta L_{\theta_\text{old}} (\theta)|_{\theta=\theta_\text{old}}`$ is the policy gradient and $`H`$ measures the curvature of the policy.
By natural policy gradient update, policy update can be obtained analytically.
Since we update $`\theta=\theta_\text{old} + \beta H^{-1} g\text{ satisfies }\frac{1}{2}(\beta H^{-1}g)^T H(\beta H^{-1} g) \leq \delta`$, so step length $`\beta`$ would be maximal when $`\frac{1}{2}(\beta H^{-1}g)^T H(\beta H^{-1} g) = \delta`$. The natural polict gradient update equation is as fallow:
$$
\theta=\theta_\text{old} + \sqrt{\frac{2\delta}{g^T H^{-1} g}}H^{-1}g \ \ \ \text{ where }g=\nabla_\theta L_{\theta_\text{old}}(\theta)|_{\theta=\theta_\text{old}}
$$
## Conjugate Gradient
However, $`H^{-1}`$ is expensive, so we compute $`x=H^{-1}g`$ instead directly as in the form $`Hx=g`$.
Since $`f'(x)=Hx-g=0`$, so we can find $`Hx`$ by $`\min_x f(x)=\frac{1}{2}x^THx-gx`$ in few iterations.
## Line Search
Starting with the maximal value $`\beta`$, we shrink $`\beta`$ by multiplying $`\alpha(0<\alpha<1)`$ repeatedly:
$$
\theta = \theta_\text{old} + \alpha \cdot \beta H^{-1}g
$$
In this way, we can ensure the objective term improvement and KL constraint term satisfaction.
![](notion-file-block://33f0ad69-a5f8-822a-aea2-8101ba5ffff5/56a1ca8f-fa0f-4679-8a9d-a6441a351699?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
<empty-block/>