<table_of_contents color="gray"/>
# Introduction
Because of KL divergence constraint, TRPO is complicated and is not compatible with noise or parameter sharing. This paper introduces an algorithm that attains the data efficiency and reliable performance of TRPO, while using only **1st-order optimization**, proposing a novel objective with **clipped** probability ratios.
# Background
## Policy Gradient Methods
Reference: [REINFORCE](/p/5ae0ad69a5f883cd8d4b8137edfde19d?v=59d0ad69a5f883b0862508d57fc1e503&pvs=25)
Computing an estimator of the policy gradient and plugging into a stochastic gradient ascent algorithm. The common estimator is as fallow:
$$
\hat{g}=\hat{\mathbb{E}}_t[\nabla_\theta \log \pi_\theta (a_t|s_t) \hat{A}_t]
$$
The estimator of $`\hat{g}`$ is obtained by differentiating the objective:
$$
L^\text{PG}(\theta)=\hat{\mathbb{E}}_t[\log \pi_\theta (a_|s_t)\hat{A}_t]
$$
## Trust Region Methods
Reference: [TRPO](/p/2ea0ad69a5f8836996ae81c945577ee5?v=59d0ad69a5f883b0862508d57fc1e503&pvs=25)
$$
\begin{aligned}\underset{\theta}{\text{maximize}} \quad & \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)} \hat{A}_t \right] \\\text{subject to} \quad & \hat{\mathbb{E}}_t [\text{KL}[\pi_{\theta_{\text{old}}}(\cdot \mid s_t), \pi_\theta(\cdot \mid s_t)]] \le \delta.\end{aligned}
$$
In TRPO, this problem can be solved using conjugate gradient algorithm. TRPO, however, actually suggests using a **penalty** rather than constraint.
$$
(a)\ \ \ \ \underset{\theta}{\text{maximize}} \; \hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)} \hat{A}_t - \beta \, \text{KL}[\pi_{\theta_{\text{old}}}(\cdot \mid s_t), \pi_\theta(\cdot \mid s_t)] \right]
$$
We can recall that the theoretical starting point of TRPO was of the form 
$`\eta(\tilde{\pi}) \ge L_{\pi}( \tilde{\pi} ) - C D_{\text{KL}}^{\max}(\pi, \tilde{\pi})`$. 
TRPO uses a hard constraint since it is hard to choose $`\beta`$ that performs well across different problems.
To achieve goal of a 1st-order algorithm that emulates the **monotonic improvement** of TRPO, it is **not sufficient to just choose a fixed penalty coefficient **$`\beta`$** and optimize the (a) with SGD**. 
# Clipped Surrogate Objective
$$
(b) \ \ \ \ L^\text{CPI}(\theta)=\hat{\mathbb{E}}_t \left[ \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)} \hat{A}_t \right]=\hat{\mathbb{E}}_t \left[ r_t(\theta)\hat{A}_t \right]
$$
CPI: conservative policy iteration in TRPO.
Without a constraint, (b) would **lead to an excessively large policy update**. Hence this paper proposes the following with hyperparameter $`\epsilon`$:
$$
L^{\text{CLIP}}(\theta) = \hat{\mathbb{E}}_t \left[ \min(r_t(\theta)\hat{A}_t, \, \text{clip}(r_t(\theta), 1 - \epsilon, 1 + \epsilon)\hat{A}_t) \right]
$$
It removes the incentive for moving $`r_t`$ outside of the interval $`[1-\epsilon, 1+\epsilon]`$. Since we take the minimum of the clipped and unclipped objective, so it is a **lower bound** on the unclipped objective, which guarantees a lower bound of policy performance.
![](notion-file-block://2c50ad69-a5f8-83c0-b967-81f44735ca3d/9fa4baf8-e44d-452a-9268-7df4ff5ef943?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
# Algorithm
If using **parameter sharing** between the policy and value function, we must use a loss function that **combines the policy surrogate and a value function error term**. Furthermore, this objective can be augmented by adding an **entropy bonus**(noise) to apply exploration.
$$
L_t^{CLIP+VF+S}(\theta) = \hat{\mathbb{E}}_t \left[ L_t^{CLIP}(\theta) - c_1 L_t^{VF}(\theta) + c_2 S[\pi_\theta](s_t) \right]
$$
where $`L_t^{VF}`$ is a squared-error loss $`(V_\theta(s_t)-V_t^\text{targ})^2`$.
One style of policy gradient implementation(A2C) is running the policy for $`T`$ timesteps, and the estimator of advantage is
$$
(c)\ \ \ \  \hat{A}_t = -V(s_t) + r_t + \gamma r_{t+1} + \dots + \gamma^{T-t+1} r_{T-1} + \gamma^{T-t} V(s_T)
$$
While (c) was used to estimate the advantage within a fixed $`T`$-step segment, it suffered from high variance. To address this limitation, we adopt a truncated version of generalized advantage estimator, introducing a parameter $`\lambda`$ to balance variance and bias:
$$
\begin{aligned}
&\hat{A}_t = \delta_t + (\gamma\lambda)\delta_{t+1} + \dots + \dots + (\gamma\lambda)^{T-t+1}\delta_{T-1}, \\
&\text{where} \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)
\end{aligned}
$$
![](notion-file-block://3830ad69-a5f8-826e-9598-81def21e0da2/3cc0aa2e-46ab-426f-886e-eb92750911d8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
<empty-block/>