<table_of_contents color="gray"/>
# Markov Decision Process
## Markov Process
![](notion-file-block://1f30ad69-a5f8-82aa-be03-8149caf6598f/b44e55b8-f7e5-4f78-b46a-c63ccfae346c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
최종 보상을 최대로 만드는 각 state에서의 action을 선택하고자 한다(optimal policy)
<empty-block/>
Action의 선택에 대해서 두 가지 방식으로 적용할 수 있다.
1. deterministic: output이 현재 state와 action에 의해서만 결정된다.
2. stochastic: 같은 state와 action이 랜덤성을 가지고 여러 outputs을 만들 수 있다.
Stochastic process $`\{ S_t\}`$는 Markov property를 만족하면 **Markov process**라고 한다.
$$
P(S_{t+1}=s' | S_t = s) = P(S_{t+1} = s' | S_0=s_0, S_1=s_1, \cdots, S_t = s)
$$
**즉, 미래 state **$`S_{t+1}`$**은 현재 state **$`S_t`$**에만 의존한다.**
<empty-block/>
이 때, $`P(S_{t+1}=s' | S_t = s)`$을 **state** **transition probability **from s to s’ 라고 한다.
Markov process는 tuple (S, P)로 나타낸다. 여기서 S는 state의 set이고, P는 state transition probability matrix $`\Bigl[ P_{ij} \Bigr] = P(S_{t+1} = s_j | S_t = s_i)`$이다.
## Markov Decision Process(MDP)
MDP는 tuple $`(S, A, P, R, \gamma)`$로 나타낼 수 있다.
여기서 P는 기존의 MP에서 action a가 주어졌을 때의 transition probability를 나타낸다.
R은 reward function으로 $`R^a_{ss'}`$는 s에서 s’으로 이동했을 때 얻어지는 보상을 의미한다. 
$`\gamma`$는 discount factor이다.
<empty-block/>
MDP에서 **model**이란 transition probability를 의미한다.
1. Model based = known MDP: P matrix를 알고 있는 경우이다 ⇒ Dynamic Programming
2. Model-free = unknown MDP: P matrix를 모르는 경우이다 ⇒ Reinforcement Learning
### Reward
RL은 reward hypothesis를 가정하여 MDP에서 cumulative rewards를 최대화하려고 한다. 
**Reward Hypothesis**: 모든 goals는 maximization of the expected value of the cumulative sum of rewards로 나타낼 수 있다. 
Reward function의 종류는 다양한데 예를 들어 바둑의 경우 매 step마다 보상을 줄 수 없기 때문에 게임이 끝났을 때 보상을 주고, 탁구의 경우 매 step마다 보상을 줄 수 있다.
<empty-block/>
Dynamics $`p(s', r | s, a)`$를 알고 있으면 state transition probability를 계산할 수 있다.
$$
P(s_{t+1}=s'|S_t = s, A_t = a) = \sum_{r \in R}p(s',r|s, a)
$$
또한 reward 함수의 종류에 따라 다음과 같이 보상을 계산할 수 있다.
1. (s, a)
$$
R^a_s=r(s,a)=\mathbb{E}[R_{t+1}|S_t=s,A_t=a]=\sum_{r\in R}r\sum_{s' \in S}p(s', r | s, a)
$$
1. (s, a, s’)
$$
R^a_{ss'}=r(s,a,s')=\mathbb{E}[R_{t+1}|S_t=s,A_t=a, S_{t+1}=s']=\frac{\sum_{r\in R}rp(s',r|s,a)}{p(s'|s,a)}
$$
### Return
Return은 total discounted reward이다.
$$
G_t = R_{t+1}+\gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum^\infty_{k=0}\gamma^k R_{t+k+1}
$$
Step 후반부에는 불확실성이 강해지기 때문에 현재 상태에 더 가중치를 주기 위해서 discount factor를 사용한다. 또한 발산하는 것을 방지할 수 있다.
### Policy
Policy $`\pi`$는 states에 대한 actions의 확률분포이다.
$$
\pi(a|s) = P(A_t=a|S_t=s)
$$
참고로 deterministic의 경우 $`\pi(s) = a`$이다.
# Bellman Equations
## Value functions
Value function은 state s가 주어진 policy를 따랐을 때 얼마나 좋은지를 나타낸다.
1. **state-value function**
$$
v_\pi (s)=\mathbb{E}_\pi [G_t|S_t=s]
$$
1. **action-value function**
$$
q_\pi (s,a) = \mathbb{E}_\pi [G_t|S_t = s, A_t = a]
$$
따라서 state-value function을 action-value function으로 나타내면 다음과 같다.
$$
v_\pi (s) = \sum_a \pi(a|s)q_\pi (s,a)
$$
**Advantage function**은 v와 q의 차이이다.
$$
A_\pi (s,a) = q_\pi (s,a)- v_\pi (s)
$$
이 값이 0보다 크면 action a가 다른 action들의 평균보다 좋다는 것을 의미한다.
### Law of probability
$$
P(A) = \sum_n P(A|B_n) \cdot P(B_n)
$$
$$
\mathbb{E}[X] = \sum_y \mathbb{E} [X|Y=y] \cdot P(Y=y)
$$
$$
\mathbb{E}[X|Z=z]=\sum_y \mathbb{E} [X|Y=y, Z=z] \cdot P(Y=y|Z=z)
$$
**Law of large numbers**: 매우 많은 데이터가 있으면 그 결과는 평균에 가까워진다. 
이는 RL의 근거가 된다.
## Bellman Equation
### Bellman expectation equation
기존의 value function을 보면 return $`G_t`$가 수식에 있는데, 이는 episode가 끝나야 알 수 있는 값이다. 그래서 episode가 끝나지 않아도 계산이 가능하도록 수식의 형태를 바꾸고자 한다.
$$
\begin{align*}
v_\pi(s) &= \mathbb{E}_\pi [G_t \mid S_t = s] \quad \text{by definition} \\
&= \sum\nolimits_{a} \mathbb{E}_\pi [G_t \mid S_t = s, A_t = a] \cdot P(A_t = a \mid S_t = s) \quad  \\
&= \sum\nolimits_{a} \pi(a \mid s) \mathbb{E}_\pi [R_{t+1} + \gamma G_{t+1} \mid S_t = s, A_t = a] \\
&= \sum\nolimits_{a} \pi(a \mid s) \sum\nolimits_{s', r} \mathbb{E}_\pi [R_{t+1} + \gamma G_{t+1} \mid S_t = s, A_t = a, S_{t+1} = s', R_{t+1} = r] \\
& \qquad \qquad \qquad \qquad \cdot P(S_{t+1} = s', R_{t+1} = r \mid S_t = s, A_t = a) \\
&= \sum\nolimits_{a} \pi(a \mid s) \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma \mathbb{E}_\pi [G_{t+1} \mid S_{t+1} = s']] \quad \\
&= \sum\nolimits_{a} \pi(a \mid s) \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma v_\pi(s')] \quad  \\
&= \mathbb{E}_\pi [R_{t+1} + \gamma v_\pi(S_{t+1}) \mid S_t = s] \\ \\
q_\pi(s, a) &= \mathbb{E}_\pi [G_t \mid S_t = s, A_t = a] \\
&= \sum\nolimits_{s', r} p(s', r \mid s, a) \left[ r + \gamma \sum\nolimits_{a'} \pi(a' \mid s') q_\pi(s', a') \right] \\ 
&= \mathbb{E}_\pi [R_{t+1} + \gamma q_\pi(S_{t+1}, A_{t+1}) \mid S_t = s, A_t = a]
\end{align*}
$$
### Optimal policy
**Optimal value function**은 value function의 최댓값이다.
$$
v_*(s) = \max v_\pi (s) \\ q_*(s,a) = \max q_\pi (s,a)
$$
이 때, optimal state-value function을 보면 state마다 optimal function이 달라질 수 있다. 
<empty-block/>
Policy의 **partial ordering**을 다음과 같이 정의한다. 
$$
\pi ' \geq \pi \text{ if } v_{\pi '}(s) \geq v_\pi(s) \text{ for all s}
$$
MDP 환경에서 다음과 같은 정리가 성립한다.
1. optimal policy $`\pi _* \geq \pi`$ for all $`\pi`$가 존재한다.
2. 모든 optimal policy는 optimal value function을 만족한다.
	$$
	v_{\pi_*}(s)=v_*(s) \\ q_{\pi_*}(s,a)=q_*(s,a)
	$$
$`q_*(s,a)`$를 최대화하여 optimal policy를 구할 수 있다.
$$
\pi_*(a \mid s) = 
\begin{cases} 
1 & \text{if } a = \arg\max_{a} q_*(s, a) \\ 
0 & \text{otherwise} 
\end{cases}
$$
즉, MDP에서는 optimal policy가 deterministic이다.
$`v_\pi (s) = \sum_a \pi(a|s)q_\pi (s,a)`$이기 때문에 $`v_*(s)=\max _a q_*(s,a)`$가 성립한다.
$`q_*(s, a) = r(s, a) + \gamma \sum_{s'} p(s' \mid s, a) v_*(s')`$도 성립하는 것을 알 수 있다.
이를 통해서 $`v_*(s)`$는 $`q_*(s,a)`$로부터 구할 수 있지만 $`q_*(s,a)`$는 $`v_*(s)`$로부터 구할 수 없다.
$`q_*(s,a)`$는 추가적으로 $`p(s'|s,a)`$를 알아야 구할 수 있다(model-based)
**따라서 model-free(RL)의 경우 optimal policy를 구하기 위해 Q(s,a)를 구해야 한다.**
### Bellman optimality equation
$$
\begin{align*}
v_*(s) &= \max_{a \in \mathcal{A}(s)} q_*(s, a) = \max_{a} \mathbb{E}_{\pi_*} [G_t \mid S_t = s, A_t = a] \\
&= \max_{a} \mathbb{E}_{\pi_*} [R_{t+1} + \gamma G_{t+1} \mid S_t = s, A_t = a] \\
&= \max_{a} \mathbb{E} [R_{t+1} + \gamma v_*(S_{t+1}) \mid S_t = s, A_t = a] \\
&= \max_{a} \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma v_*(s')] \quad \\
&\left(= \max_{a} \left[ R_s^a + \gamma \sum\nolimits_{s'} P_{ss'}^a v_*(s') \right]\right)
\\ \\
q_*(s, a) &= \mathbb{E} \left[ R_{t+1} + \gamma \max_{a'} q_*(S_{t+1}, a') \;\middle|\; S_t = s, A_t = a \right] \\
&= \sum\nolimits_{s', r} p(s', r \mid s, a) \left[ r + \gamma \max_{a'} q_*(s', a') \right] \\
&\left(= R_s^a + \gamma \sum\nolimits_{s'} P_{ss'}^a \max_{a'} q_*(s', a') \right)
\end{align*}
$$
# Dynamic Programming
## Value Iteration
$$
v_*(s) = \max_{a} \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma v_*(s')]
$$
Value iteration은 다음의 식을 수렴할 때까지 반복하여 **optimal value function**을 구한다.
$$
V_{k+1}=\max_{a} \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma V_k(s')]
$$
1. $`V_0(s)=0 \ \forall s`$로 초기화한다.
2. 점화식을 사용하여 수렴할 때까지 반복해서 계산을 해주는데 이 때 두 가지 방식이 있다.
	2.1. synchronous backups: 모든 s에 대해 $`V_{k+1}`$을 계산하고 동시에 update한다.
	2.2. asynchronous backups: 하나의 s에 대해 $`V_{k+1}`$을 계산하고 즉시 update한다.
3. optimal policy $`\pi_* = \argmax_a \sum\nolimits_{s', r} p(s', r \mid s, a) [r + \gamma V_*(s')]`$을 계산한다.
<empty-block/>
하지만 실제로는 V가 수렴하기 전에 policy가 사실 상 고정되기 때문에 optimal policy를 미리 알 수 있고, 매 반복마다 $`O(S^2A)`$의 시간이 필요하기 때문에 느리다는 단점이 있다. 이를 해결하기 위해 **policy iteration**을 사용한다.
![](notion-file-block://1aa0ad69-a5f8-83de-b2f2-01538bf7cd7c/3fe804ef-f52b-4206-901a-3d4b133e7684?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## Policy Iteration
### Policy evaluation
Deterministic $`\pi`$ 로부터 $`V^\pi`$를 계산하는 과정이다.
$$
V_{k+1}(s)\leftarrow \sum_{s',r}p(s',r|s, \pi(s))[r+\gamma V_k(s')]
$$
1. $`V_0(s)=0`$으로 초기화한다.
2. $`V^\pi`$로 수렴할 때까지 모든 $`V_k(s')`$로부터 $`V_{k+1}(s)`$를 계산한다(full backup)
이는 VI 보다 훨씬 빠르다 $`O(S^2)`$
### Policy improvement
Greedy policy를 사용해서 $`\pi`$에서 $`\pi'`$로 발전시키는 과정이다.
$$
\pi'(s) = \argmax _a \sum_{s', r} p(s',r| s,a)[r+\gamma V^\pi(s')]=\argmax_a Q^\pi(s,a)
$$
### Policy improvement theorem
만약 모든 s에 대해 $`Q^\pi (s, \pi'(s)) \geq V^\pi(s), \ V^{\pi'}(s) \geq V^\pi(s)`$이면, $`\pi'`$는 $`\pi`$보다 좋다.
따라서 policy improvement 과정을 거치면 policy가 더 좋아진다.
![](notion-file-block://5ce0ad69-a5f8-8324-8fb7-0162f8cd9b2a/a77fbaee-55a2-4612-baa2-4067f2637a1a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
마지막 부분을 보면 중간에 optimal policy가 결정되면 반복을 멈춘다.
# Reinforcement Learning
RL에는 Monte Carlo(MC)와 Temporal Difference(TD)가 있다.
이를 기존의 DP 방식과 비교하면 다음과 같다.
![](notion-file-block://a950ad69-a5f8-8335-b44d-81c109f5033b/64031048-9ac8-47ff-b5b1-8f11ebe447f1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
DP에서는 state 양이 많아서 $`G_t`$를 계산하지 못했었는데, MC를 보면 sample data를 사용하기 때문에 계산할 수 있는 것을 확인할 수 있다.
DP와 RL은 모두 **tabular updating methods**이다. Value function 표를 만들고 Bellman equation을 계산하여 optimal policy를 구한다.
DP에서는 table의 value를 full backup을 통해서 업데이트 한다. 그래서 Q(s,a)의 경우 V(s)에 비해 크기가 크기 때문에 VI에서는 주로 V(s)를 사용한다. V(s)를 통해 policy를 상향시키기 위해서는 known MDP가 필요하다.
$$
\pi'(s)=\argmax_a \sum_{s',r}p(s',r|s,a)[r+\gamma V^\pi(s')]
$$
RL은 sample backup을 통해서 일부 values를 업데이트 한다. 또한 Q(s,a)를 사용하여 optimal policy를 결정한다. Q(s,a)를 사용하여 model-free 환경에서도 policy를 상향시킬 수 있다.
$$
\pi'(s) = \argmax_a Q^\pi (s,a)
$$
RL은 sample backup을 사용하기 때문에 curse of dimensionality를 고려하지 않아도 된다.
## Generalized Policy Iteration(GPI)
Policy iteration은 두 가지 processes가 번갈아 반복한다.
- Policy evaluation은 현재 policy에 대한 value function을 구한다.
- Policy improvement는 policy를 발전시킨다.
기존에는 다른 process가 끝나야 시작을 했는데(full backup) 이는 실제로 불필요하다.
그래서 GPI는 **approximated value function**을 사용하여(sample backup) optimal policy를 구한다.
![](notion-file-block://cfd0ad69-a5f8-8210-8cf8-0106c0061a01/01059828-5ace-41a6-a92f-458e413febdf?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
대부분의 RL 방식은 GPI를 사용한다.
## Monte Carlo method(MC)
MC도 tabular updating을 사용한다(action-value function: Q-table).
Q value를 사용하기 때문에 model-free이다. 
MC는 PE에서 episode-by-episode(sample multi-step backup)을 사용하고, PI에서 $`\epsilon`$-greedy를 사용하여 Q값을 구한다.
![](notion-file-block://b450ad69-a5f8-82d3-b417-01e11ee1037b/7ca2665c-3d3b-45aa-8c88-4f1379b536a9?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Sample의 episodes에 대해 return의 평균값으로 value를 구하기 때문에 이러한 방식은 바둑과 같은 환경에도 적용할 수 있다. 또한 추정치를 통해 또 다른 추정치를 업데이트(Bootstrapping) 하지 않기 때문에 Markov property가 성립하지 않아도 큰 영향이 없다.
### MC Prediction(PE)
Policy $`\pi`$에 대해서 entire episodes of real experience를 통해 $`q_\pi`$를 계산하고자 한다.
$`q_\pi(s,a)=\mathbb{E}_\pi[G_t|S_t=s, A_t=a]`$인데 MC는 expected return 대신에 empirical mean을 사용한다. 첫 번째 (s,a)에 대해서만 return을 계산하는 first-visit 방식과 전체 return에 대해서 계산하는 Every-visit 방식이 있다.
개수 n(s,a)와 return S(s,a)를 기록하여 $`Q(s,a)=\frac{S(s,a)}{n(s,a)}`$로 value를 추정한다. 
큰 수의 법칙에 의해 n(s,a)가 커질수록 $`Q(s,a)\rightarrow q_\pi (s,a)`$이다.
### Incremental Monte Carlo updates
**Incremental mean**: partial mean $`\mu _k`$ of sequence $`x_1, x_2 ,\cdots`$을 점진적으로 계산한다.
$$
\mu_k=\frac{1}{k}\sum^k_{i=1} x_i = \frac{1}{k}(\sum^{k-1}_{i=1} x_i + x_k)=\frac{1}{k}((k-1)\mu_{k-1} + x_k)=\mu_{k-1} + \frac{1}{k}(x_k-\mu_{k-1})
$$
이를 MC 방식에 적용하면 return S를 계산하지 않고 업데이트할 수 있다.
각 state-action 쌍 $`(S_t, A_t)`$와 초기 return $`G_t`$에 대해 다음과 같이 계산한다.
$$
n(S_t, A_t) \leftarrow n(S_t, A_t) + 1
$$
$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \frac{1}{n(S_t, A_t)}[G_t - Q(S_t, A_t)]
$$
### Constant MC policy evaluation
위 식에서 $`\frac{1}{n(S_t, A_t)}`$에 의해 $`G_t`$가 미치는 영향이 점점 줄어든다. 그래서 최근의 데이터는 n이 매우 커지기 때문에 그 값이 매우 작아진다. 따라서 이를 상수로 고정하여 최근의 값에 더 큰 가중치를 부여한다.
$$
Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha[G_t - Q(S_t, A_t)]
$$
### Epsilon-greedy policy
RL에서 선택의 방식은 두 가지가 있다.
- **Exploitation**: 최선의 선택을 한다(greedy).
- **Exploration**: 새로운 선택을 한다.
이두 방식을 모두 사용하기 위해 $`\epsilon`$-greedy policy 방식을 사용한다. $`\epsilon`$ 확률로 새로운 선택을 한다.
$$
\pi'(a|s)= \begin{cases} 1-\epsilon +\frac{\epsilon}{m} & \text{if }a=\argmax _{a'}Q^\pi (s,a') \\ \frac{\epsilon}{m} & \text{otherwise (m-1 actions)}\end{cases}
$$
기존의 DP 방식은 deterministic이였지만 Rl은 stochastic policy 방식이다.
$`\epsilon`$-greedy policy의 value가 이전의 value보다 크기 때문에 이를 policy improvement에 적용할 수 있다.
### Monte Carlo method
최종적으로 MC 방식의 알고리즘을 나타내면 다음과 같다.
![](notion-file-block://2510ad69-a5f8-833c-a4b2-8182329d3e9b/9a889033-b0fa-4c36-8a31-58689b204efb?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
## Temporal Difference learnings(TD)
TD도 tabular 업데이트를 하고 model-free이다. MC와는 다르게 **one-step** 기반의 GPI를 사용한다.
![](notion-file-block://41b0ad69-a5f8-8358-b970-019690507a9e/c202edd3-c94d-45bb-a2a6-4ed3c7d5379a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
TD는 DP의 부트스래핑과 같이 episode의 끝까지 계산할 필요가 없다.
또한 MC의 샘플링과 비슷하게 transition probability를 알 필요가 없다.
3개의 RL PE 식을 비교하면 다음과 같다.
1. Monte Carlo: **on-policy**
$$
Q(S_t,A_t)\leftarrow Q(S_t, A_t)+\alpha [\colorbox{yellow}{$G_t$} -Q(S_t, A_t)]
$$
1. Sarsa: **on-policy**
$$
Q(S_t,A_t)\leftarrow Q(S_t, A_t)+\alpha [\colorbox{yellow}{$R_{t+1}+\gamma Q(S_{t+1}, A_{t+1} )$} -Q(S_t, A_t)]
$$
1. Q-learning: **off-policy**
$$
Q(S_t,A_t)\leftarrow Q(S_t, A_t)+\alpha [\colorbox{yellow}{$R_{t+1}+\gamma \max_a Q(S_{t+1}, a )$} -Q(S_t, A_t)]
$$
Sarsa는 Bellman expectation 공식을 사용하고 Q-learning은 Bellman optimality 공식을 사용한다.
Sarsa와 Q-learning의 알고리즘은 다음과 같다.
![](notion-file-block://7150ad69-a5f8-83d6-93e4-017f64b5fb6b/edd6f954-7cc7-4719-b67f-8575c85ebf8c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
Sarsa는 $`\epsilon`$-greedy policy를 사용하기 때문에 near-optimal policy를 얻고, Q-learning의 경우 optimal policy만 얻는다. 따라서 Sarsa가 더 안전한 방식을 택해서 경우에 따라 성능이 좋다.
![](notion-file-block://c990ad69-a5f8-82c2-95f3-817d6c096270/9d6da13e-0466-4666-9b40-3cb3d41d76a0?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### Double Q-learning
Q-learning은 maximization을 사용하기 때문에 Q가 overestimated되는 문제가 있다. 그래서 두 개의 Q function을 사용하여 maximization이 적용되는 Q function과 추정치를 구하는 Q function이 다르기 때문에 overestimate 문제를 방지할 수 있다.
![](notion-file-block://f310ad69-a5f8-831c-b9c4-01ea1a765f2c/34ed420f-ed52-4b3a-aaa8-0c82bf5bd6df?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)
### TD(n)
**n-step return**: $`G_t^{(n)}=R_{t+1} + \gamma R_{t+2} + \cdots + \gamma ^ {n-1} R_{t+n} + \gamma ^n V(S_{t+n})`$
TD(n)은 n-step TD이다.
$$
V(S_t) \leftarrow V(S_t) + \alpha [G_t ^{(n)} -V(S_t)]
$$
$`\lambda`$**-return**: $`G_t^ \lambda = (1-\lambda ) \sum ^\infty _{n=1} \lambda ^{n-1} G_t^{(n)}`$
TD($`\lambda`$)은 다음과 같다.
$$
V(S_t) \leftarrow V(S_t) + \alpha [G_t ^\lambda -V(S_t)]
$$
TD(0)는 기존의 TD와 같고, TD(1)의 경우 every-visit MC와 같은 역할을 한다.
## On-policy vs Off-policy
**Target policy**: agent가 학습하고자 하는 policy이다.
**Behavior policy**: agent가 action을 고르고 데이터를 만들 때 사용하는 policy이다.
- **On-policy**: target policy = behavior policy** **
	Sarsa: Q(S,A)를 업데이트할 때 behavior policy를 사용하여 target $`R+\gamma Q(S', A')`$을 계산한다.
- **Off-policy**: target policy ≠ behavior policy
	Q-learning: maximization을 통해 target $`R+\gamma \max_a Q(S', a)`$를 업데이트한다. 이후 behavior policy를 통해 다음 action과 state를 결정한다.
### Importance sampling
직접 구하기 어려운 p(x) 확률분포로 기댓값을 계산해야할 때 importance sampling을 사용한다.
간단한 q(x)로부터 sampling을 하고 p(x)와 비슷하게 만든다(q(x) \> 0 if p(x) \> 0).
$$
\mathbb{E}[f]=\int f(x)p(x) dx = \int f(x) \frac{p(x)}{q(x)}q(x) dx = \mathbb{E} \left[f(x) \frac{p(x)}{q(x)} \right]
$$
여기서 $`\frac{p(x)}{q(x)}`$를 **importance weight**라고 한다.
Importance sampling을 통해 on-policy를 off-policy로 바꿀 수 있다.
이를 통해 on-policy MC와 TD를 off-policy로 바꿀 수 있다.
- Off-policy MC: using target returns $`G_t`$ generated from $`\mu`$ to evaluate $`\pi`$
$$
G_t ^{\pi / \mu} = \rho ^T _t G_t = \left(\prod^{T-1} _ {k=t} \frac{\pi(A_k|S_k)}{\mu(A_k |S_k)} \right)G_t
$$
$$
Q(S_t,A_t)\leftarrow Q(S_t, A_t)+\alpha [\colorbox{yellow}{$G_t^{\pi / \mu}$} -Q(S_t, A_t)]
$$
- Off-policy TD: using targets $`R_{t+1}+\gamma Q(S_{t+1}, A_{t+1})`$ generated from $`\mu`$
$$
Q(S_t,A_t)\leftarrow Q(S_t, A_t)+\alpha \left[\colorbox{yellow}{$\frac{\pi(A_k|S_k)}{\mu(A_k|S_k)}$}(R_{t+1}+\gamma Q(S_{t+1}, A_{t+1} )) -Q(S_t, A_t)\right]
$$
TD의 경우 한 번의 step에만 곱해주면 되기 때문에 MC에 비해 더 작은 variance를 가진다.
### Bias vs Variance
**Bias**: 추정치의 평균과의 차이
**Variance**: 얼마나 흩어져 있는지
$`G_t`$는 unbiased estimate of q(S,A)이기 때문에 MC는 unbiased이다.
TD는 estimate $`R+\gamma Q(S,A)`$가 biased이다.
하지만 MC는 $`G_t`$가 많은 random action에 영향을 받기 때문에 variance가 크고 TD는 하나의 step에만 영향을 받아서 variance가 작다. 그래서 MC는 일반적으로 느리게 수렴한다.
<empty-block/>