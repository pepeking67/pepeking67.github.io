

![](notion-file-block://41f0ad69-a5f8-80dd-b740-f0a3e4c5770d/6ee0e6d6-a894-4848-b579-1100e91576ef?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=image.png)

# Introduction

<p>
We are interested in how can we perform efficient inference and learning for probabilistic models with intractable posterior distributions and large datasets. 
</p>

1. We use <b>reparametrization</b> of the variational lower bound, so that it can be simply differentiated and optimized by SGD.
2. Posterior inference can be made by fitting approximate inference model(a.k.a <b>recognition model</b>) using lower bound estimator.

We propose Auto-Encoding variational bayesian(<b>AEVB</b>) with <b>SGVB</b> estimator, which doesn’t need of expensive iterative inference schemes such as MCMC.

# Method

## Problem scenario

Dataset $`X=\{ x^{(i)} \}^N_{i=1}`$ consisting of $`N`$ i.i.d. samples.

<p>
For unobserved continuous random variable $`z`$, 
</p>

1. $`z^{(i)} \sim p_{\theta^*}(z)`$
2. $`x^{(i)} \sim p_{\theta^*}(x|z)`$

We also assume that $`p_{\theta^*}(z)`$ and $`p_{\theta^*}(x|z)`$ come from parametric families of $`p_{\theta}(z)`$ and $`p_{\theta}(x|z)`$, and their PDFs are differentiable.

Note that true paramter $`\theta^*`$ and latent variables $`z^{(i)}`$ are unknown.

<p />

We should solve two assumption cases:

1. <b>Intractability</b>

<p>
$`p_\theta(x)=\int p_\theta(z)p_\theta(x|z)dz`$ is intractable. 
</p>

2. <b>Large dataset</b>

For example, MCMC-based methods are computationally expensive because they require iterative posterior sampling for each datapoint.

<p />

We construct <b>recognition model </b><b>$`q_\phi(z|x)`$</b>: approximation to the intractable true posterior $`p_\theta(z|x)`$.

We train the recognition model parameters $`\phi`$ with the generative model parameters $`\theta`$.

## The variational bound

### Marginal likelihood

The <b>marginal distribution</b> is obtained by integrating out the latent variable $`z`$ from the joint distribution: $`p_\theta(x) = \int p_\theta(x,z),dz = \int p_\theta(x|z)p_\theta(z),dz`$.

When the observed data $`x`$ is fixed and $`p_\theta(x)`$ is treated as a function of $`\theta`$, it is called the <b>marginal likelihood</b>: $`L(\theta;x)=p_\theta(x)`$.

Thus, the same expression can be interpreted as either a marginal distribution over $`x`$ or a marginal likelihood over $`\theta`$, depending on which variable is fixed.

### The variational bound

The marginal likelihood $`\log p_\theta(x^{(1)}, x^{(2)}, \cdots, x^{(N)})=\sum^N_{i=1}\log p_\theta (x^{(i)})`$ can be rewritten as:

$$
\log p_\theta(x^{(i)})=D_{KL}(q_\phi(z|x^{(i)})||p_\theta(z|x^{(i)}))+\mathcal{L}(\theta,\phi;x^{(i)}) \tag{1}
$$

Note that $`D_{KL}(p||q)=\int p(x) \log \frac{p(x)}{q(x)} dx = \mathbb{E}_p[\log \frac{p(x)}{q(x)}]`$.

Since KL divergence is non-negative, $`\mathcal{L}(\theta,\phi ; x)`$ is called the <b>variational lower bound</b> on the marginal likelihood of datapoint $`i`$.

$$
\log p_\theta(x^{(i)}) \geq \mathcal{L}(\theta,\phi;x)=\mathbb{E}_{q_\phi(z|x)}[-\log q_\phi(z|x)+\log p_\theta(x,z)] \tag{2}
$$

<details>
<summary>Proof of (1), (2)</summary>

$`\log p_\theta(x) = \mathbb{E}_{q_\phi(z|x)}[\log p_\theta(x)]`$ since $`x`$ is not related to $`z`$.

$$
\begin{aligned} \mathbb{E}_{q_\phi(z|x)}[\log p_\theta (x)] &= \mathbb{E}_q\log [\frac{p_\theta (z,x)}{p_\theta(z|x)}] \\ &= \mathbb{E}_q[\log \frac{q_\phi(z|x)}{p_\theta(z|x)}\cdot \frac{p_\theta(z,x)}{q_\phi(z|x)}] \\ &= D_{KL}(q_\phi(z|x) || p_\theta(z|x))+\mathbb{E}_q[-\log q_\phi(z|x) + \log p_\theta(z,x)]\end{aligned}
$$

Also lower bound $`\mathcal{L}`$ can be written as:

$$
\mathcal{L}(\theta, \phi ; x^{(i)})=-D_{KL}(q_\phi(z|x^{(i)})||p_\theta(z))+\mathbb{E}_{q_\phi(z|x^{(i)})}[\log p_\theta(x^{(i)}|z)] \tag{3}
$$
</details>

<details>
<summary>Proof of (3)</summary>

$$
\begin{aligned} \mathcal{L}&=\mathbb{E}_q[-\log q_\phi(z|x)+\log p_\theta(z,x)] \\ &= \mathbb{E}_q[-\log(q_\phi(z|x)+\log p_\theta(x|z)+\log p_\theta(z)] \\ &= -D_{KL}(q_\phi(z|x)||p_\theta(z))+\mathbb{E}_q[\log p_\theta(x|z)]  \end{aligned}
$$
</details>

In VAE, the KL divergence term in (3) is called <b>regularization</b>, while the expectation term represents <b>reconstruction error</b>. The regularization measures how close the encoder's approximate posterior is to the prior distribution, while the reconstruction error measures how well the decoder reconstructs the input data.

We cannot calculate $`p_\theta(z|x)`$, so that we train the model by maximizing lower bound $`\mathcal{L}`$.

Thus we want to differentiate and optimize the lower bound $`\mathcal{L}`$. However, the usual Monte Carlo gradient estimator:

<p>
 $`\nabla_\phi \mathbb{E}_{q_\phi(z)}[f(z)] = \mathbb{E}_{q_\phi(z)}\left[f(z)\nabla_\phi \log q_\phi(z)\right] \simeq \frac{1}{L}\sum_{l=1}^{L}f(z^{(l)})\nabla_\phi \log q_\phi(z^{(l)})`$
</p>

has high variance since the estimated gradient can vary significantly depending on the sampled values. So we use <b>reparametrization trick</b>.

## The reparametrization trick

It is often possible to express $`z\sim q_\phi(z|x)`$ as $`z=g_\phi(\epsilon, x)`$, where $`\epsilon`$ is noise with independent marginal $`p(\epsilon)`$ and $`g_\phi(\cdot)`$ is some vector-valued function.

<p />

<p>
Note that $`q_\phi(z|x)\prod_i dz_i = p(\epsilon) \prod_i d\epsilon_i`$, where $`d \bold{z} = \prod_i dz_i`$. 
</p>

Therefore, $`\int q_\phi(z|x)f(z)\,dz= \int p(\epsilon)f(z)\,d\epsilon= \int p(\epsilon)f(g_\phi(\epsilon,x))\,d\epsilon`$.

Then we can construct a differentiable estimator: $`\int q_\phi(z|x)f(z)\,dz\simeq \frac{1}{L}\sum_{l=1}^{L}f\left(g_\phi(x,\epsilon^{(l)})\right)`$, where $`\epsilon^{(l)} \sim p(\epsilon)`$.

Thus this reparametrization trick is ued to rewrrite an expectation w.r.t. $`q_\phi(z|x)`$ s.t. Monte Carlo estimate is differentiable w.r.t. $`\phi`$.

<p />

For example, the univariate Gaussian case: $`z\sim p(z|x)=\mathcal{N}(\mu, \sigma^2)`$. Then the reparametrization is $`z=\mu + \sigma \epsilon`$, where $`\epsilon \sim \mathcal{N}(0,1)`$.

$$
\mathbb{E}_{\mathcal{N}(z;\mu,\sigma^2)}[f(z)]
=
\mathbb{E}_{\mathcal{N}(\epsilon;0,1)}
[f(\mu+\sigma\epsilon)]
\simeq
\frac{1}{L}\sum_{l=1}^{L}
f(\mu+\sigma\epsilon^{(l)})
$$

## The SGVB estimator and AEVB algorithm

Using reparametrization trick, we introduce a practical estimator of the lower bound and its derivatives w.r.t. the parameters $`\theta, \phi`$.

We reparametrize $`\tilde{z}\sim q_\phi(z|x)`$: $`\tilde{z}=g_\phi(\epsilon, x)`$ with $`\epsilon \sim p(\epsilon) `$.

We can from Monte Carlo estimates of expectations of some function $`f(z)`$ w.r.t. $`q_\phi(z|x)`$:

$$
\mathbb{E}_{q_\phi(z|x^{(i)})}[f(z)]=\mathbb{E}_{p(\epsilon)}[f(g_\phi(\epsilon,x^{(i)}))]\simeq\frac{1}{L}\sum^L_{l=1}f(g_\phi(\epsilon^{(l)},x^{(i)})) \text{ where }\epsilon^{(l)}\sim p(\epsilon) \tag{5}
$$

We apply to (2), resulting in <b>Stochastic Gradient Variational Bayes(SGVB)</b> estimator $`\tilde{\mathcal{L}}^A(\theta, \phi;x^{(i)})\simeq \mathcal{L}(\theta, \phi;x^{(i)})`$:

$$
\tilde{\mathcal{L}}^A(\theta, \phi;x^{(i)})=\frac{1}{L}\sum^L_{l=1} \log p_\theta(x^{(i)}, z^{(i,l)})-\log q_\phi(z^{(i,l)}|x^{(i)}) \tag{6}
$$

where $`z^{(i,l)}=g_\phi(\epsilon^{(i,l)},x^{(i)}) \text{ and }\epsilon^{(l)}\sim p(\epsilon)`$.

<p>
 Since KL divergence can be analytically integrated for Gaussian distribution, we only need to estimate reconstruction error $`\mathbb{E}_{q_\phi(z|x^{(i)})}[\log p_\theta (x^{(i)}|z)]`$ by sampling. 
</p>

<details>
<summary>Appendix B: Integration KL divergence analytically</summary>

Note that $`KL(N_0||N_1)=\frac{1}{2}(tr \sum_1^{-1}\sum_0+(\mu_1-\mu_0)^T \sum_1^{-1}(\mu_1 - \mu_0)-k+\ln \frac{\det \sum_1}{\det \sum _0})`$.

$$
\begin{aligned} KL(q_\phi(z|x)||p_\theta(z)) &= \frac{1}{2}(tr(\sigma_i^2I)+\mu_i^T\mu_i-J+\ln \frac{1}{\prod \sigma_{i,j}}) \\ &= \frac{1}{2} (\sum^J_{j=1}\sigma_{i,j}^2+\sum^J_{j=1}\mu^2_{i,j}-J-\sum^J_{j=1}\ln \sigma_{i,j}^2) \\ &=\frac{1}{2}\sum^J_{j=1}(\mu_{i,j}^2+\sigma_{i,j}^2-\ln \sigma_{i,j}^2 -1) \end{aligned}
$$
</details>

Then we can get the second version of SGVB estimator $`\tilde{\mathcal{L}}^B(\theta, \phi;x^{(i)})\simeq \mathcal{L}(\theta, \phi;x^{(i)})`$ corresponding to (3):

$$
\tilde{\mathcal{L}}^B(\theta, \phi;x^{(i)})=-D_{KL}(q_\phi(z|x^{(i)})||p_\theta(z))+\frac{1}{L}\sum^L_{l=1}(\log p_\theta(x^{(i)}|z^{(i,l)})) \tag{7}
$$

where $`z^{(i,l)}=g_\phi(\epsilon^{(i,l)},x^{(i)}) \text{ and } \epsilon^{(l)} \sim p(\epsilon)`$.

For the minibatch $`X^M=\{ x^{(i)} \}^M_{i=1}`$ with dataset $`X`$ with $`N`$ datapoints,

$$
\mathcal{L}(\theta, \phi;X)\simeq \tilde{\mathcal{L}}^M(\theta, \phi;X^M)=\frac{N}{M}\sum^M_{i=1}\tilde{\mathcal{L}}(\theta, \phi;x^{(i)}) \tag{8}
$$

<details>
<summary>Proof of (8)</summary>

$`\mathcal{L}(\theta, \phi ; X)=\sum^N_{i=1}\mathcal{L}(\theta,\phi ; x^{(i)})`$. If $`N`$ is very large, then it is difficult to calculate ELBO. So we use the minibatch and consider their means.

$$
\frac{1}{M}\sum^M_{i=1} \tilde{\mathcal{L}}(\theta, \phi; x^{(i)}) \simeq \frac{1}{N} \sum^N_{i=1} \mathcal{L}(\theta, \phi;x^{(i)})
$$
</details>

In addition, we found that the number of samples $`L`$ per datapoint can be set to <b>1</b> when the minibatch size $`M`$ was large enough.

![](notion-file-block://4200ad69-a5f8-807c-be5b-f31404256031/233e9534-7aaa-47ef-8aa3-647557cdb305?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_142825_Samsung_Notes.jpg)

# Example: Variational Auto-Encoder

Let the prior over latent variables $`z`$: $`p_\theta(z)=\mathcal{N}(z;0,I)`$. In this case, the $`p_\theta(x|z)`$ can be multivariate <b>Gaussian</b> for real-valued data or <b>Bernoulli</b> for binary data. This distribution parameters are computed with MLP.

<details>
<summary>Appendix C: MLP decoder for both cases</summary>

1. Bernoulli MLP as decoder

$$
\log p(x|z)=\sum^D_{i=1} x_i \log y_i + (1-x_i)\cdot \log(1-y_i)
$$

where $`y=f_\sigma(W_2 \tanh(W_1z+b_1)+b_2)`$ for elementwise sigmoid function $`f_\sigma`$.

2. Gaussian MLP as decoder

For diagonal covariance,

$$
\begin{aligned} \log p(x|z)&=\log \mathcal{N}(x;\mu,\sigma^2I) \\ \text{where } \mu&=W_4h+b_4 \\ \log \sigma^2 &=W_5h+b_5 \\ h &= \tanh(W_3z+b_3) \end{aligned}
$$
</details>

In the VAE model, both prior $`p_\theta(z)`$ and encoder $`q_\phi(z|x)`$ are Gaussian. By appendix B, we can express (7) as:

$$
\mathcal{L}(\theta,\phi;x^{(i)})\simeq\frac{1}{2}\sum_{j=1}^{J}\left(1+\log\left((\sigma_j^{(i)})^2\right)-(\mu_j^{(i)})^2-(\sigma_j^{(i)})^2\right)+\frac{1}{L}\sum_{l=1}^{L}\log p_\theta(x^{(i)}|z^{(i,l)}) \tag{10}
$$

<p>
where $`z^{(i,l)}=\mu^{(i)}+\sigma^{(i)}\odot \epsilon^{(i)} \text{ and } \epsilon^{(l)} \sim \mathcal{N}(0,I)`$. 
</p>

$`\log p_\theta(x|z)`$ can be explained by appendix C for Gaussian or Bernoulli case.

# Experiments

![](notion-file-block://4200ad69-a5f8-802c-8478-cf3ea06bac1a/c970416e-5a3c-46b6-87c0-266cc383a66a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_150426_Samsung_Notes.jpg)

![](notion-file-block://4200ad69-a5f8-8002-bfa2-f38f9e75be58/6288591f-d24f-4f50-94f9-819ed479381b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_150439_Samsung_Notes.jpg)

![](notion-file-block://4200ad69-a5f8-8060-a1ad-f4dd02249e76/434e2d92-6ff6-43fd-8b21-b125cfe9db8b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_150453_Samsung_Notes.jpg)

![](notion-file-block://4200ad69-a5f8-8087-b2cc-dcbca9cc4701/cfdbac2f-d45f-44ff-a0a3-ad8355b46c4a?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_150502_Samsung_Notes.jpg)

The visualization shows the images generated by the decoder from different points in the latent space. It demonstrates that nearby latent variables tend to produce similar images.

# Full VB

In the main body of the paper, the derivations treat $`\theta`$ as a fixed parameter. However, VI can also be applied to $`\theta`$.

Let $`p_\alpha(\theta)`$ be some hyperprior. Then the marginal likelihood is written as:

$$
\log p_\alpha(X)=D_{KL}(q_\phi(\theta)||p_\alpha(\theta|X))+\mathcal{L}(\phi;X) \tag{13} 
$$

$$
\text{where } \mathcal{L}(\phi;X)=\int q_\phi(\theta)(\log p_\theta(X)+\log p_\alpha(\theta)-\log q_\phi(\theta)) d\theta \tag{14}
$$

Let $`\tilde{\theta} = h_\phi(\zeta) \quad \text{with} \quad \zeta \sim p(\zeta)`$.

$$
\mathcal{L}(\phi;X)\simeq \frac{1}{L}\sum^L_{l=1}f_\phi(x^{(l)},g_\phi(\epsilon^{(l)},x^{(l)}),h_\phi(\zeta^{(l)})) \tag{22}
$$

<p />

![](notion-file-block://4200ad69-a5f8-80a6-8e1b-e506f24c20e0/403cd50a-673f-4a1a-b725-aea8ec4c766e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=SmartSelect_20261122_153124_Samsung_Notes.jpg)

<p />