

# Introduction

![](notion-file-block://4200ad69-a5f8-80c9-94e3-f2ecf4e6eaf3/2dd78686-30ce-4deb-9e14-ad35820c6250?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

A <b>diffusion model</b> is a parametrized Markov chain trained using variational inference. It is learned to <b>reverse a diffusion process</b> which is a Markov chain that adds <b>noise</b>(forward process). In the forward process, if we add Gaussian noise, then the reverse process(sampling chain) can be expressed by Gaussian distribution too. As a result, for sampling chain $`x_T \rightarrow x_{T-1} \rightarrow \cdots \rightarrow x_0`$, $`p(x_{t-1}|x_t)`$ can be trained as a Gaussian.

The theoretical basis for this comes from research on Langevin dynamics, which suggests that when sufficiently small amounts of Gaussian noise are added during the forward process, the reverse process can also be approximated by Gaussian distributions.

<p>
DDPM doesn’t have competitive log likelihoods, which shows how well the model learns the true distribution, despite its high sample quality. 
</p>

# Background

<p>
Diffusion models are latent variable models: $`p_\theta(x_0)\coloneqq \int p_\theta(x_{0:T})dx_{1:T}`$, where $`x_1, \cdots, x_T`$ of $`x_0\sim q(x_0)`$. 
</p>

<p>
The joint distribution $`p_\theta(x_{0:T})`$ is called <b>reverse process</b>. 
</p>

Starting at $`p(x_T) = \mathcal{N}(x_T;0,I)`$:

$$
p_\theta(x_{0:T}) \coloneqq p(x_T) \prod ^T _{t=1}p_\theta(x_{t-1}|x_t), \text{ where } p_\theta(x_{t-1}|x_t) \coloneqq \mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)) \tag{1}
$$

The approximate posterior $`q(x_{1:T}|x_0)`$ is called <b>forward process</b>(diffusion process), which adds Gaussian noise to the data according to a variance schedule $`\beta_1, \cdots , \beta_T`$.

$$
q(x_{1:T}|x_0)\coloneqq \prod^T_{t=1} q(x_t|x_{t-1}),\text{ where } q(x_t|x_{t-1}) \coloneqq \mathcal{N}(x_t;\sqrt{1-\beta_t}x_{t-1}, \beta_tI) \tag{2}
$$

<b>The reverse process learns the transition distributions between latent variables leading to the target data </b><b>$`x_0`$</b><b>. Since the target distribution </b><b>$`p_\theta(x_0)`$</b><b> can be obtained by marginalizing the joint distribution over the latent variables, we train the reverse process to model these transitions. During training, the forward process is used as a reference distribution to guide the learning of the reverse process.</b>

We train the model to optimize the variational bound on negative log likelihood:

$$
\mathbb{E}[-\log p_\theta(x_0)] \leq \mathbb{E}_q[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}]=\mathbb{E}_q[-\log p(x_T)-\sum_{t \geq 1} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}] = L \tag{3}
$$

<details>
<summary>Proof of (3)</summary>

Note that Jensen’s inequality: If f is convex, then $`f(\mathbb{E}[X]) \leq \mathbb{E}[f(X)]`$.

$$
\begin{aligned} p_\theta(x_0) &= \int \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\cdot q(x_{1:T}|x_0)dx_{1:T} \\ &= \mathbb{E}_{q(x_{1:T}|x_0)}[\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}] \end{aligned}
$$

By Jensen’s inequality, since $`\log`$ is concave, $`\log p_\theta(x_0) \geq \mathbb{E}_q[\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}]`$.
</details>

The forward process variances $`\beta_t`$ can be learned by reparametrization or constant as hyperparameters.

At forward process, we can express $`x_t`$ in closed form: using $`\alpha_t = 1-\beta_t`$ and $`\bar{\alpha}_t = \prod_{s=1} \alpha_s`$.

$$
q(x_t|x_0)=\mathcal{N}(x_t;\sqrt{\bar{\alpha}_t}x_0, (1-\bar{\alpha}_t)I) \tag{4}
$$

<details>
<summary>Proof of (4)</summary>

Apply $`x_t = \sqrt{\alpha_t}x_{t-1}+\sqrt{\beta_t}\epsilon_t`$, where $`\epsilon_t\sim \mathcal{N}(0,I)`$ to (2).

$$
\begin{aligned} x_1 &= \sqrt{\alpha_1}x_0+\sqrt{\beta_1}\epsilon_1 \\ x_2 &= \sqrt{\alpha_2}x_1+\sqrt{\beta_2}\epsilon_2 \\ x_2 &= \sqrt{\alpha_2}(\sqrt{\alpha_1}x_0+\sqrt{\beta_1}\epsilon_1)+\sqrt{\beta_2}\epsilon_2 \\ &= \sqrt{\alpha_1\alpha_2} x_0 + \sqrt{\alpha_2\beta_1}\epsilon_1+\sqrt{\beta_2}\epsilon_2\end{aligned}
$$

<p>
Thus $`\sqrt{\alpha_2\beta_1}\epsilon_1+\sqrt{\beta_2}\epsilon_2 \sim \mathcal{N}(0,(\alpha_2\beta_1+\beta_2)I)`$ and $`\beta_t = 1-\alpha_t`$, so $`\alpha_2\beta_1+\beta_2 = 1-\alpha_1 \alpha_2`$. 
</p>

Therefore, $`x_2=\sqrt{\alpha_1\alpha_2}x_0+\sqrt{1-\alpha_1\alpha_2}\epsilon`$.

By mathematical induction, we can get (4).
</details>

Variance reduction of $`L`$ (3) by:

$$
\mathbb{E}_q\left[\underbrace{D_{\mathrm{KL}}\left(q(x_T\mid x_0)\|p(x_T)\right)}_{L_T}+\sum_{t>1}\underbrace{D_{\mathrm{KL}}\left(q(x_{t-1}\mid x_t,x_0)\|p_\theta(x_{t-1}\mid x_t)\right)}_{L_{t-1}}-\underbrace{\log p_\theta(x_0\mid x_1)}_{L_0}\right] \tag{5}
$$

<details>
<summary>Appendix A: Proof of (5)</summary>

$$
\begin{aligned} L &= \mathbb{E}_q[-\log \frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}] \\ &=\mathbb{E}_q[-\log p(x_T)-\sum_{t \geq 1} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}] \\ &= \mathbb{E}_q[-\log p(x_T)-\sum_{t > 1} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_t|x_{t-1})}-\log \frac{p_\theta(x_0|x_1)}{q(x_1|x_0)}] \\ &= \mathbb{E}_q[-\log p(x_T)-\sum_{t > 1} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_{t-1}|x_t, x_0)}\cdot\frac{q(x_{t-1}|x_0)}{q(x_t|x_0)}-\log \frac{p_\theta(x_0|x_1)}{q(x_1|x_0)}]  \\ &= \mathbb{E}_q[-\log \frac{p(x_T)}{q(x_T|x_0)}-\sum_{t > 1} \log \frac{p_\theta(x_{t-1}|x_t)}{q(x_{t-1}|x_t, x_0)}-\log p_\theta(x_0|x_1)] \end{aligned}
$$

Note that marginalization depends only on the function variables in expectation: $`\mathbb{E}_{q(x_{0:T})}[f(x_0)]=\mathbb{E}_{q(x_0)}[f(x_0)]`$, since other variables are integrated to 1.

$$
L=\mathbb{E}_q\left[D_{\mathrm{KL}}\left(q(x_T\mid x_0)\|p(x_T)\right)+\sum_{t>1}D_{\mathrm{KL}}\left(q(x_{t-1}\mid x_t,x_0)\|p_\theta(x_{t-1}\mid x_t)\right)-\log p_\theta(x_0\mid x_1)\right]
$$
</details>

Since $`q(x_{t-1})=\int q(x_{t-1}|x_0)q(x_0)dx_0`$ and $`q(x_0)`$ is true data distribution, $`q(x_{t-1}|x_t)=\frac{q(x_t|x_{t-1})q(x_{t-1})}{q(x_t)}`$ is intractable.

However, when conditioned on $`x_0`$, $`q(x_{t-1}|x_t, x_0)`$ becomes tractable.

$$
q(x_{t-1}|x_t,x_0)=\mathcal{N}(x_{t-1};\tilde{\mu}_t(x_t,x_0), \tilde{\beta}_tI) \tag{6}
$$

$$
\text{where }\tilde{\mu}_t(x_t, x_0)=\frac{\sqrt{\bar{\alpha}_{t-1}}\beta_t}{1-\bar{\alpha}_t}x_0+\frac{\sqrt{\alpha_t}(1-\bar{\alpha}_{t-1})}{1-\bar{\alpha}_t}x_t \text{ and }\tilde{\beta}_t=\frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t \tag{7}
$$

Thus we can calculate (5) and all KL divergences in (5) are comparisons between Gaussians, so that they can be calculated by Rao-Backwellized fashion with closed form like VAE.

# Diffusion models and denoising autoencoders

## Forward process

<p>
The forward process variances $`\beta_t`$ are learnable by reparametrization, but in practice, we fix them to <b>constants</b>. 
</p>

So $`q`$ has no learnable parameters, $`L_T`$ is a constant. Thus we ignore $`L_T`$ during training.

## Reverse process

For $`p_\theta(x_{t-1}|x_t) \coloneqq \mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t))`$, we set $`\Sigma_\theta(x_t,t)=\sigma_t^2I`$ to untrained constants. Experimentally, both $`\sigma_t^2=\beta_t`$ and $`\sigma_t^2=\tilde{\beta}_t`$ had similar results.

Since KL divergence in $`L_{t-1}`$ compares between two Gaussians, we can calculate analytically:

<p> </p>

$$
L_{t-1}=\mathbb{E}_q[\frac{1}{2 \sigma_t^2}||\tilde{\mu}_t(x_t,x_0)-\mu_\theta(x_t,t)||^2]+C \tag{8}
$$

So we can see that the simple parametrization of $`\mu_\theta`$ is a model that predicts the forward process posterior mean $`\tilde{\mu}_t`$.

We can expand (8) by reparametrizing (4) as $`x_t(x_0, \epsilon)=\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha_t}}\epsilon`$ for $`\epsilon \sim \mathcal{N}(0,I)`$. Apply for (7):

$$
L_{t-1}-C=\mathbb{E}_{x_0,\epsilon}\left[\frac{1}{2\sigma_t^2}\left\|\tilde{\mu}_t\left(x_t(x_0,\epsilon),\frac{1}{\sqrt{\bar{\alpha}_t}}\left(x_t(x_0,\epsilon)-\sqrt{1-\bar{\alpha}_t}\epsilon\right)\right)-\mu_\theta(x_t(x_0,\epsilon),t)\right\|^2\right] \tag{9}
$$

$$
=\mathbb{E}_{x_0,\epsilon}\left[\frac{1}{2\sigma_t^2}\left\|\frac{1}{\sqrt{\alpha_t}}\left(x_t(x_0,\epsilon)-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon\right)-\mu_\theta(x_t(x_0,\epsilon),t)\right\|^2\right] \tag{10}
$$

We make $`\epsilon`$ NN model:

$$
\mu_\theta(x_t,t)=\tilde{\mu}_t\left(x_t,\frac{1}{\sqrt{\bar{\alpha}_t}}\left(x_t-\sqrt{1-\bar{\alpha}_t}\epsilon_\theta(x_t)\right)\right)=\frac{1}{\sqrt{\alpha_t}}\left(x_t-\frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t,t)\right) \tag{11}
$$

So applying those $`\mu_\theta`$ and $`\Sigma_\theta`$ to $`p_\theta(x_{t-1}|x_t) \coloneqq \mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t))`$, then we can sample $`x_{t-1}\sim p_\theta(x_{t-1}|x_t)`$ as:

$$
x_{t-1}=\frac{1}{\sqrt{\alpha_t}}(x_t-\frac{\beta_t}{\sqrt{1-\bar{\alpha_t}}}\epsilon_\theta(x_t,t))+\sigma z, \text{ where }z\sim\mathcal{N}(0,I)
$$

Finally, with (11), we can simplify (10):

$$
\mathbb{E}_{x_0,\epsilon}\left[\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar{\alpha}_t)}\left\|\epsilon-\epsilon_\theta\left(\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,t\right)\right\|^2\right] \tag{12}
$$

In summary, we can train the reverse process $`\mu_\theta`$ to predict $`\tilde{\mu}_t`$, and further to predict $`\epsilon`$.

![](notion-file-block://4210ad69-a5f8-80e2-93f9-cbe06dbb87e4/69c8f7e6-02a6-4fb3-a1a4-502257d7bda3?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Data scaling, reverse process decoder, and $`L_0`$

Since the image data consists of $`\{ 0, 1, \cdots , 255 \}`$, we should scale the inputs to $`[-1,1]`$.

Then this ensures that reverse process <b>starts from the standard normal prior</b> $`p(x_T)`$.

Because image pixel is discrete(0\~255), to obtain discrete log likelihoods, we set the last term of the reverse process as:

$$
\begin{aligned}p_\theta(x_0\mid x_1) &= \prod_{i=1}^{D}\int_{\delta_-(x_0^i)}^{\delta_+(x_0^i)}\mathcal{N}(x;\mu_\theta^i(x_1,1),\sigma_1^2)\,dx \\[6pt]\delta_+(x) &= \begin{cases}\infty & \text{if }x=1\\ x+\frac{1}{255} & \text{if }x<1\end{cases}\qquad\delta_-(x) = \begin{cases}-\infty & \text{if }x=-1\\ x-\frac{1}{255} & \text{if }x>-1\end{cases}\end{aligned}\tag{13}
$$

In <b>VAE</b>, discretization is achieved by directly modeling the decoder distribution as a <b>Bernoulli </b>distribution. In contrast, DDPM uses Gaussian distributions for computational convenience and because the reverse process can be approximated by Gaussian transitions when sufficiently small amounts of Gaussian noise are added during the forward process. Therefore, DDPM performs discretization by integrating the Gaussian probability density over intervals corresponding to discrete pixel values.

## Simplified training objective

The variational bound consisting of (12) and (13) is already differentiable w.r.t. $`\theta`$.

However, for better sample quality and simpler implement, we simply the variational bound:

$$
L_{\mathrm{simple}}(\theta):=\mathbb{E}_{t,x_0,\epsilon}\left[\left\|\epsilon-\epsilon_\theta\left(\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,t\right)\right\|^2\right]\tag{14}
$$

where $`t`$ is uniform between $`1`$ and $`T`$.

<p>
From (12), $`L_{t-1}`$ has weight $`\frac{\beta_t^2}{2\sigma_t^2\alpha_t(1-\bar{\alpha}_t)}`$ depending time $`t`$. 
</p>

We let $`t`$ as uniform distribution to make consistent weights. Also, for $`t=1`$ case $`L_0`$ in the discrete decoder (13) is approximated by MSE together.

<p>
Since the original variational bound assigns relatively large weights to small $`t`$, where the noise level is low, the simplified objective assigns equal weights across all timesteps to place more emphasis on denoising tasks at larger $`t`$. 
</p>

![](notion-file-block://4210ad69-a5f8-80db-bc74-d47bfe47e3d4/39d4c775-5af3-483a-94b9-67c6958bece6?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

# Experiments

For reverse process, we use a <b>U-Net</b> backbone. Parameters are shared across time, so we use the transformer sinusoidal positional encoding.

## Sample quality

![](notion-file-block://4210ad69-a5f8-805e-a38b-ea9db7220253/af78e99b-bfda-426f-8c40-90541017d7ea?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

## Reverse process parametrization and training objective ablation

In Table 2, we find that (14) can be trained by MSE loss function, since <b>mean</b> has very small difference but $`\epsilon`$ has small variance so that we can calculate MSE effectively.

## Progressive coding

![](notion-file-block://4210ad69-a5f8-80fa-aef9-e38b1da7e6e4/5696b3ec-eedc-4b36-a151-65e77b66f058?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

KL divergence can be interpreted as the amount of information the receiver needs to reconstruct the original sample given what they already know.

The sender transmits $`x_T, \cdots, x_0`$ in sequence, and the receiver reconstructs the sample using the received information. The amount of information required at each step can be measured by KL divergence.

The receiver can calculate the partial information $`x_t`$ at any time $`t`$:

$$
x_0 \approx \hat{x}_0 = (x_t-\sqrt{1-\bar{\alpha}_t}\epsilon_\theta(x_t))/\sqrt{\bar{\alpha}_t} \tag{15}
$$

Thus we can interpret DDPM as a process of <b>progressively recovering information</b>.

![](notion-file-block://4210ad69-a5f8-8077-8b20-d5c3b9e7b5c7/455e14b3-50a1-4e1b-992e-409a4e7af80c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

We can see that the distortion rate decreases steeply in the early steps. This suggests that DDPM <b>first reconstructs the overall structure of an image and then progressively recovers finer details</b>.

This result can also be observed in the following figure.

![](notion-file-block://4210ad69-a5f8-80be-9a31-d580a23683b4/bbbc9816-41fa-48b7-8ee4-02c82c0ad8e6?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

<p />