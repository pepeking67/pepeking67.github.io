<table_of_contents color="gray"/>
# Descriptive Statistics
## Population, Sample, and Percentiles
<callout icon="📘" color="blue_bg">
	**Def. (Population, Parameter, Statistic)**
	Population: the entire group under consideration.
	Parameter: a numerical measure depending on all units in the population; a characteristic of the population.
	Statistic: a numerical measure depending only on the sampled units; a characteristic of the sample.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Population Percentiles / Quantiles)**
	The $`100p`$th percentile is the location that indicates the percent of a distribution equal to or below $`100p`$.
	First quartile $`Q_1`$: $`p=0.25`$; median $`Q_2`$: $`p=0.5`$; third quartile $`Q_3`$: $`p=0.75`$.
	Interquartile range (IQR): $`Q_3-Q_1`$.
</callout>
![](notion-file-block://7334628e-bbd3-422c-9917-8502a1374bce/9382bc57-b3a0-4891-a5ee-ddb410d7fd8e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_quartiles_tight.svg)
**The sample median** is more robust to outliers than the sample mean.
If the sample is sorted as $`x_{(1)}\le \cdots\le x_{(n)}`$:
- Odd $`n`$: sample median is the value at position $`(n+1)/2`$.
- Even $`n`$: sample median is the average of values at positions $`n/2`$ and $`n/2+1`$.
<callout icon="📘" color="blue_bg">
	**Def. (Sample **$`100p`$**th Percentile)**
	The sample $`100p`$th percentile $`\tilde{x}`$ of a dataset is a value with at least $`np`$ observations $`\le\tilde{x}`$ and at least $`n(1-p)`$ observations $`\ge\tilde{x}`$.
	If $`np`$ is not an integer, use the next integer greater than $`np`$. If $`np`$ is an integer, use the average of the values in the corresponding two positions.
</callout>
## Shape of a Distribution
![](notion-file-block://00e88abe-6f3f-43d7-8ffe-7b1ad004dee0/b9c64849-d61e-47bb-81cd-b0ccb9156f89?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_distribution_shapes_tight.svg)
- Unimodal, symmetric bell-shaped distribution: mean $`\approx`$ median.
- Unimodal distribution skewed to the left: mean $`<`$ median.
<callout icon="📜" color="yellow_bg">
	**Thm. (Chebyshev's Inequality: Sample Form)**
	For dataset $`x_1,\ldots,x_n`$ with sample mean $`\bar{x}`$ and sample standard deviation $`s`$, let $`S_k=\{i:1\le i\le n,\ |x_i-\bar{x}|<ks\}`$ and $`N(S_k)`$ be the number of elements in $`S_k`$.
	$$
	\frac{N(S_k)}n\ge1-\frac{n-1}{nk^2}>1-\frac1{k^2}.
	$$
	Let $`N(k)`$ be the number of indices satisfying $`1\le i\le n`$ and $`x_i-\bar{x}\ge ks`$.
	$$
	\frac{N(k)}n\le\frac1{1+k^2}.
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Sample Correlation)**
	$$
																									r=\frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}
{(n-1)s_xs_y}
=\frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}
{\sqrt{\sum_{i=1}^n(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^n(y_i-\bar{y})^2}}.
	$$
	Positive correlation if $`r>0`$, negative if $`r<0`$, and $`-1\le r\le1`$.
	Geometric interpretation: $`r=\langle\mathbf{x}',\mathbf{y}'\rangle/(\|\mathbf{x}'\|\|\mathbf{y}'\|)=\cos\theta`$.
	$`r=\pm1`$: linear relation. $`r\approx0`$: weak linear relation; not necessarily independence.
</callout>
# Probability
## Sample Space, Events, and Axioms
<callout icon="📘" color="blue_bg">
	**Def. (Sample Space and Event)**
	The sample space $`S`$ of an experiment is the set of all possible outcomes of the experiment.
	An event $`E\subseteq S`$ occurs if the outcome of the experiment belongs to $`E`$.
</callout>
**The algebra of events**
- Commutative: $`E\cup F=F\cup E`$, $`E\cap F=F\cap E`$.
- Associative: $`(E\cup F)\cup G=E\cup(F\cup G)`$.
- Distributive: $`(E\cup F)\cap G=(E\cap G)\cup(F\cap G)`$.
- De Morgan: $`(E\cup F)^c=E^c\cap F^c`$.
- $`EF:=E\cap F`$.
<callout icon="📘" color="blue_bg">
	**Def. (Axioms of Probability)**
	1. $`0\le P(E)\le1`$.
	2. $`P(S)=1`$.
	3. For any mutually exclusive sequence $`\{E_i\}_{i=1}^\infty`$,
	$$
	P\!\left(\bigcup_{i=1}^{\infty}E_i\right)=\sum_{i=1}^{\infty}P(E_i).
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Basic Probability Properties)**
	$$
	P(E^c)=1-P(E).
	$$
	$$
	P(E\cup F)=P(E)+P(F)-P(E\cap F).
	$$
	If all $`n`$ elementary outcomes are equally likely, $`P(\{s_i\})=1/n`$.
	Combination notation: $`\binom nk={n!}/{(k!(n-k)!)}`$.
</callout>
**Ex.** Probability that $`n`$ people have birthdays on different days (365 equally likely birthdays):
$$
P(\text{all birthdays distinct})=\frac{{}_{365}P_n}{365^n}.
$$
## Conditional Probability and Bayes' Formula
<callout icon="📘" color="blue_bg">
	**Def. (Conditional Probability)**
	The probability of event $`E`$ given that event $`F`$ has occurred:
	$$
	P(E\mid F)=\frac{P(E\cap F)}{P(F)},\qquad P(F)>0.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. (Bayes' Formula)**
	For mutually exclusive and exhaustive events $`F_1,\ldots,F_n`$,
	$$
	P(F_i\mid E)=\frac{P(E\mid F_i)P(F_i)}{\sum_{j=1}^nP(E\mid F_j)P(F_j)}.
	$$
	Also $`P(E\mid F)=P(F\mid E)P(E)/P(F)`$ after rearrangement.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Independent Events)**
	$`E`$ and $`F`$ are independent if $`P(E\cap F)=P(E)P(F)`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Independence)**
	1. If $`E`$ and $`F`$ are independent, so are $`E`$ and $`F^c`$.
	2. If $`E,F,G`$ are independent, $`E`$ is independent of every event formed from $`F`$ and $`G`$ (under mutual independence).
</callout>
<details>
<summary>Proof (1)</summary>
	$$
																									P(E)=P(E\cap F)+P(E\cap F^c)
=P(E)P(F)+P(E\cap F^c).
	$$
	Therefore $`P(E\cap F^c)=P(E)(1-P(F))=P(E)P(F^c)`$.
</details>
**Ex. (Coupons)**
A set of $`k`$ coupons is collected, each of which is independently type $`j`$ with probability $`p_j`$, $`\sum_{j=1}^np_j=1`$. Find the probability that the set contains a type $`j`$ coupon given that it contains type $`i`$, $`i\ne j`$.
**(Sol)** $`A_i`$: the set of $`k`$ coupons contains type $`i`$.
Goal:
$$
P(A_j\mid A_i)=\frac{P(A_i\cap A_j)}{P(A_i)}.
$$
$$
P(A_i)=1-P(A_i^c)
=1-P(\text{no type }i\text{ out of }k\text{ coupons})
=1-(1-p_i)^k.
$$
$$
P(A_i\cap A_j)=1-P(A_i^c\cup A_j^c).
$$
$$
P(A_i^c\cup A_j^c)=P(A_i^c)+P(A_j^c)-P(A_i^c\cap A_j^c).
$$
$$
P(A_i^c\cap A_j^c)=P(\text{no }i,j)=(1-p_i-p_j)^k.
$$
Therefore,
$$
\boxed{P(A_j\mid A_i)
=\frac{1-\left[(1-p_i)^k+(1-p_j)^k-(1-p_i-p_j)^k\right]}{1-(1-p_i)^k}}.
$$
- $`A_i,A_j`$ are not independent. The types of the coupons are independently selected.
# Random Variables and Distributions
## Cumulative Distribution Function
<callout icon="📘" color="blue_bg">
	**Def. (Random Variable)**
	A numerical quantity of interest determined by the outcome of an experiment.
	Ex. $`X`$ = sum of the values on two dice.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Cumulative Distribution Function, CDF)**
	$$
	F(x)=P(X\le x).
	$$
	$$
	P(a<X\le b)=F(b)-F(a).
	$$
</callout>
## Discrete, Continuous, and Joint Random Variables
<callout icon="📘" color="blue_bg">
	**Def. (Discrete Random Variable)**
	The set of values of $`X`$ is countable. Its probability mass function (PMF) is
	$$
	p(x)=P(X=x),\qquad F(x)=\sum_{x_i\le x}p(x_i).
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Continuous Random Variable)**
	There is a nonnegative probability density function (PDF) $`f`$ on $`(-\infty,\infty)`$ such that
	$$
																									P(X\in B)=\int_Bf(t)\,dt,\quad\int_{-\infty}^{\infty}f(t)\,dt=1,
\quad F(x)=\int_{-\infty}^xf(t)\,dt.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Continuous Distribution)**
	$$
	P(a<X\le b)=\int_a^bf(x)\,dx,\quad P(X=a)=\int_a^af(x)\,dx=0.
	$$
	At points where the density is continuous, $`F'(x)=f(x)`$.
	$$
						P\left(a-\frac{\varepsilon}{2}<X\le a+\frac{\varepsilon}{2}\right)
=\int_{a-\varepsilon/2}^{a+\varepsilon/2}f(x)\,dx
\approx f(a)\varepsilon.
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Joint and Marginal Distributions)**
	Joint CDF: $`F(x,y)=P(X\le x,Y\le y)`$.
	Marginal CDFs: $`F_X(x)=F(x,\infty)`$, $`F_Y(y)=F(\infty,y)`$.
	Discrete joint PMF: $`p(x_i,y_j)=P(X=x_i,Y=y_j)`$.
	Continuous joint PDF: $`P((X,Y)\in C)=\iint_Cf(x,y)\,dx\,dy`$.
	$$
																									p_X(x_i)=\sum_jp(x_i,y_j),\qquad
f_X(x)=\int_{-\infty}^\infty f(x,y)\,dy.
	$$
	Similarly for $`Y`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Joint PDF/CDF)**
	$$
	P(X\in A,Y\in B)=\int_A\int_B f(x,y)\,dy\,dx.
	$$
	$$
	F(a,b)=\int_{-\infty}^a\int_{-\infty}^b f(x,y)\,dy\,dx.
	$$
	$$
	f(a,b)=\left.\frac{\partial^2F(x,y)}{\partial x\partial y}\right|_{x=a,y=b}.
	$$
	For small increments, $`P(a<X<a+da,\ b<Y<b+db)\approx f(a,b)\,da\,db`$.
</callout>
**Ex.** With $`f(x,y)=2e^{-x}e^{-2y}`$ for $`x,y>0`$ and zero otherwise, compute $`P(X<Y)`$ by integrating over $`0<x<y<\infty`$.
<callout icon="📘" color="blue_bg">
	**Def. (Independent Random Variables)**
	$`X,Y`$ are independent if
	$$
	P(X\in A,Y\in B)=P(X\in A)P(Y\in B).
	$$
	Equivalently $`F(x,y)=F_X(x)F_Y(y)`$, and for discrete/continuous variables,
	$$
																									p(x,y)=p_X(x)p_Y(y),\qquad
f(x,y)=f_X(x)f_Y(y).
	$$
</callout>
**Ex.** $`X,Y`$ are independent and have the same PDF
$$
f(x)=\begin{cases}e^{-x},&x>0,\\0,&\text{otherwise}.
\end{cases}
$$
Find the PDF of $`X/Y`$.
$$
F_{X/Y}(a)=P\left(\frac XY\le a\right)
=\int_0^{\infty}\int_0^{ay}e^{-x}e^{-y}\,dx\,dy
=1-\frac1{a+1}.
$$
$$
f_{X/Y}(a)=F'_{X/Y}(a)=\frac1{(a+1)^2},\qquad a>0.
$$
# Conditional Distribution and Expectation
<callout icon="📘" color="blue_bg">
	**Def. (Conditional Distribution)**
	For discrete $`X,Y`$:
	$$
	p_{X\mid Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}.
	$$
	For continuous $`X,Y`$:
	$$
	f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}.
	$$
</callout>
**Prop.**
$$
P(a<X<a+dx\mid y<Y<y+dy)\approx f_{X\mid Y}(a\mid y)\,dx.
$$
$$
P(X\in A\mid Y=y)=\int_A f_{X\mid Y}(x\mid y)\,dx,
$$
$$
P(X\in A,Y\in B)=\int_B P(X\in A\mid Y=y)f_Y(y)\,dy.
$$
<callout icon="📘" color="blue_bg">
	**Def. (Expectation / Mean)**
	Discrete: $`E[X]=\sum_xxp(x)`$. Continuous: $`E[X]=\int_{-\infty}^{\infty}x f(x)\,dx`$.
	More generally,
	$$
	E[g(X)]=\sum_xg(x)p(x)\quad\text{or}\quad \int_{-\infty}^{\infty}g(x)f(x)\,dx.
	$$
	$$
	E[aX+b]=aE[X]+b,\qquad E[X+Y]=E[X]+E[Y].
	$$
	$$
	E[g(X,Y)]=\sum_{x,y}g(x,y)p(x,y)\quad\text{or}\quad\iint g(x,y)f(x,y)\,dx\,dy.
	$$
	$`n`$th moment of $`X`$: $`E[X^n]`$ ($`n=1`$: mean; $`n=2`$: variance).
</callout>
**Ex. (Fixed placement).** Let $`X_i=1`$ if the $`i`$th item is placed correctly, and $`0`$ otherwise. Since $`X=\sum_{i=1}^n X_i`$ and $`P(X_i=1)=1/n`$,
$$
E[X]=\sum_i E[X_i]=\sum_i\frac1n=1.
$$
**Ex. (Coupons).** Among 20 types of coupons, 10 coupons are selected independently. Each type has probability $`1/20`$. Let $`X_i`$ indicate whether type $`i`$ appears, and $`X=\sum_{i=1}^{20}X_i`$. Then
$$
P(X_i=1)=1-\left(\frac{19}{20}\right)^{10},
\qquad E[X]=20\left[1-\left(\frac{19}{20}\right)^{10}\right]\approx8.
$$
**The meaning of expectation.** Predict $`X`$ by a fixed value $`c`$. Squared error is $`(X-c)^2`$. The value minimizing mean squared error $`E[(X-c)^2]`$ is $`c=E[X]`$.
## Variance, Covariance, Correlation
<callout icon="📘" color="blue_bg">
	**Def. (Variance)**
	$$
	\operatorname{Var}(X)=E[(X-\mu)^2]=E[X^2]-\mu^2,\qquad\mu=E[X].
	$$
	$$
	\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Covariance and Correlation Coefficient)**
	$$
	\operatorname{Cov}(X,Y)=E[(X-\mu_X)(Y-\mu_Y)]=E[XY]-\mu_X\mu_Y.
	$$
	$$
																									\rho=\operatorname{Corr}(X,Y)
=\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}.
\qquad |\rho|\le1.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Variance of a Sum)**
	$$
																									\operatorname{Var}\left(\sum_{i=1}^{n}X_i\right)
=\sum_{i=1}^{n}\operatorname{Var}(X_i)
+2\sum_{i<j}\operatorname{Cov}(X_i,X_j).
	$$
	$`\operatorname{Cov}(X,Y)=0`$ for independent $`X,Y`$; converse need not hold.
</callout>
**Ex.** $`X=\cos Z,\quad Y=\sin Z,\quad Z\sim U[0,2\pi]`$.
$$
\operatorname{Cov}(X,Y)=0,
$$
but $`X`$ and $`Y`$ are not independent, since $`X^2+Y^2=1`$.
# Moment Generating Function and Inequalities
<callout icon="📘" color="blue_bg">
	**Def. (Moment Generating Function, MGF)**
	$$
																								\phi_X(t)=E[e^{tX}]
=\begin{cases}
\sum_x e^{tx}p(x),&\text{discrete},\\
\int_{-\infty}^{\infty}e^{tx}f(x)\,dx,&\text{continuous}.
\end{cases}
	$$
	The MGF does not always exist for all $`t\in\mathbb{R}`$.
	$$
																								\phi_X^{(k)}(t)=E[X^ke^{tX}],\quad \phi_X'(0)=E[X],\quad
\phi_X^{(k)}(0)=E[X^k].
	$$
	For independent $`X,Y`$: $`\phi_{X+Y}(t)=\phi_X(t)\phi_Y(t)`$.
	The MGF uniquely determines the distribution (when it exists around zero).
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Markov's Inequality)**
	For a nonnegative $`X`$ and $`a>0`$,
	$$
	P(X\ge a)\le\frac{E[X]}a.
	$$
</callout>
<details>
<summary>Proof</summary>
	$$
																								E[X]=\int_0^\infty x f(x)\,dx
\ge\int_a^\infty x f(x)\,dx
\ge a\int_a^\infty f(x)\,dx
=aP(X\ge a).
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Prop. (Chebyshev's Inequality)**
	$$
																								P(|X-\mu|\ge k)\le \frac{\sigma^2}{k^2}
=\frac{\operatorname{Var}(X)}{k^2}.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. (Weak Law of Large Numbers)**
	Let $`X_1,\ldots,X_n`$ be independent and identically distributed random variables with mean $`\mu`$ and variance $`\sigma^2`$. Then for every $`\varepsilon>0`$,
	$$
																								P\left(\left|\frac{X_1+\cdots+X_n}{n}-\mu\right|>\varepsilon\right)\to0
\qquad(n\to\infty).
	$$
	Thus the sample mean converges to the population mean in probability as sample size increases.
</callout>
# Special Random Variables
## Discrete Random Variables
### Bernoulli and Binomial
<callout icon="📘" color="blue_bg">
	**Def. (Bernoulli Random Variable)**
	$$
	P(X=0)=1-p,\quad P(X=1)=p,\qquad X\sim\operatorname{Bernoulli}(p).
	$$
	$$
	E[X]=p,\quad \operatorname{Var}(X)=p(1-p).
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Binomial Random Variable)**
	$`X`$ is the number of successes in $`n`$ independent Bernoulli trials:
	$$
	P(X=i)=\binom ni p^i(1-p)^{n-i},\quad X\sim B(n,p).
	$$
	$$
	X=\sum_{i=1}^n X_i,\quad X_i\sim\operatorname{Bernoulli}(p),
	$$
	$$
	E[X]=np,\quad \operatorname{Var}(X)=np(1-p).
	$$
	$$
	P(X\le i)=\sum_{k=0}^i\binom nk p^k(1-p)^{n-k}.
	$$
	For $`i\ge0`$:
	$$
	P(X=i+1)=\frac{(n-i)p}{(i+1)(1-p)}P(X=i).
	$$
</callout>
**MGF of Bernoulli and Binomial**
$$
\phi_{\mathrm{Bernoulli}}(t)=1-p+pe^t,\qquad
\phi_{\mathrm{Binomial}}(t)=(1-p+pe^t)^n.
$$
**Ex.** If $`X\sim B(n,p)`$, $`Y\sim B(m,p)`$ are independent, then
$$
\phi_{X+Y}(t)=(1-p+pe^t)^{n+m}
\quad\Longrightarrow\quad X+Y\sim B(n+m,p).
$$
By the uniqueness of MGFs, adding independent binomial variables with equal $`p`$ gives another binomial variable.
### Poisson
<callout icon="📘" color="blue_bg">
	**Def. (Poisson Random Variable)**
	$$
																								P(X=i)=e^{-\lambda}\frac{\lambda^i}{i!},\quad
X\sim\operatorname{Poisson}(\lambda),\quad i=0,1,2,\ldots
	$$
	$`\sum_{i=0}^\infty \lambda^i/i!=e^\lambda`$.
	$$
																								\phi_X(t)=e^{\lambda(e^t-1)},
\qquad E[X]=\lambda,\quad\operatorname{Var}(X)=\lambda.
	$$
</callout>
**Ex. (Accidents).** The average number of accidents per week on a particular stretch of highway is 3. What is the probability of at least one accident this week?
$$
P(X\ge1)=1-P(X=0)=1-e^{-3}.
$$
<callout icon="📜" color="yellow_bg">
	**Prop. (Poisson Approximation to the Binomial)**
	If $`X\sim B(n,p)`$, $`n\to\infty`$, $`p\to0`$, and $`np=\lambda`$ is fixed, then
	$$
																								P(X=i)=\binom ni p^i(1-p)^{n-i}
\approx e^{-\lambda}\frac{\lambda^i}{i!}.
	$$
</callout>
<details>
<summary>Derivation</summary>
	Take $`p=\lambda/n`$:
	$$
																								\binom ni\left(\frac{\lambda}{n}\right)^i
\left(1-\frac\lambda n\right)^{n-i}
=\frac{n(n-1)\cdots(n-i+1)}{n^i}
\frac{\lambda^i}{i!}\,
\frac{(1-\lambda/n)^n}{(1-\lambda/n)^i}.
	$$
	As $`n\to\infty`$, the first ratio tends to 1, the numerator power tends to $`e^{-\lambda}`$, and the final denominator tends to 1.
</details>
<callout icon="📜" color="yellow_bg">
	**Prop. (Addition of Independent Poisson Variables)**
	If $`X_i\sim\operatorname{Poisson}(\lambda_i)`$ are independent, then
	$$
	X_1+\cdots+X_n\sim\operatorname{Poisson}(\lambda_1+\cdots+\lambda_n).
	$$
</callout>
**Ex. (Coupon type among Poisson events).** Suppose $`N\sim\operatorname{Poisson}(\lambda)`$ events occur, independently assigned type 1 with probability $`p`$ and type 2 with probability $`1-p`$. Given $`N=n+m`$, the number of type-1 events is $`B(n+m,p)`$. Hence
$$
P(N_1=n,N_2=m)
=e^{-\lambda}\frac{\lambda^{n+m}}{(n+m)!}
\binom{n+m}n p^n(1-p)^m
$$
$$
=\frac{(\lambda p)^n e^{-\lambda p}}{n!}
\frac{[\lambda(1-p)]^m e^{-\lambda(1-p)}}{m!}.
$$
Thus $`N_1\sim\operatorname{Poisson}(\lambda p)`$, $`N_2\sim\operatorname{Poisson}(\lambda(1-p))`$, and they are independent.
<callout icon="📜" color="yellow_bg">
	**Prop. (Splitting a Poisson Distribution)**
	If each event of a Poisson variable with mean $`\lambda`$ is independently classified as one of $`r`$ types with probabilities $`p_1,\ldots,p_r`$, the numbers of each type are independent Poisson random variables with means $`\lambda p_1,\ldots,\lambda p_r`$.
	$$
	\frac{P(X=i+1)}{P(X=i)}=\frac{\lambda}{i+1}.
	$$
</callout>
### Hypergeometric
<callout icon="📘" color="blue_bg">
	**Def. (Hypergeometric Random Variable)**
	Draw $`n`$ balls without replacement from $`N`$ balls, $`M`$ of which are marked.
	$$
	P(X=i)=\frac{\binom Mi\binom{N-M}{n-i}}{\binom Nn}.
	$$
	$$
																								E[X]=\frac{nM}{N},\quad
\operatorname{Var}(X)=n\frac MN\left(1-\frac MN\right)\frac{N-n}{N-1}.
	$$
	Sampling **with** replacement gives a binomial model; sampling **without** replacement gives a hypergeometric model.
</callout>
![](notion-file-block://40b9bf2a-2c14-40ec-be1d-b2555e0db6ea/062aed86-db01-498d-a7bf-780a9bb48b1d?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_hypergeom_urn_tight.svg)
**Ex.** If $`X\sim B(n,p)`$ and $`Y\sim B(m,p)`$ are independent, then
$$
P(X=i\mid X+Y=k)
=\frac{P(X=i)P(Y=k-i)}{P(X+Y=k)}
$$
$$
=\frac{\binom ni\binom m{k-i}}{\binom{n+m}k}.
$$
This has a hypergeometric distribution.
## Continuous Random Variables
### Uniform
<callout icon="📘" color="blue_bg">
	**Def. (Uniform Random Variable)**
	$$
																								f(x)=\begin{cases}
\frac1{\beta-\alpha},&\alpha\le x\le\beta,\\
0,&\text{otherwise}.
\end{cases}
	$$
	$$
																								X\sim U(\alpha,\beta),\quad
P(a<X\le b)=\frac{b-a}{\beta-\alpha},
	$$
	$$
																								E[X]=\frac{\alpha+\beta}{2},\quad
\operatorname{Var}(X)=\frac{(\beta-\alpha)^2}{12}.
	$$
</callout>
### Normal
<callout icon="📘" color="blue_bg">
	**Def. (Normal Random Variable)**
	$$
																								f(x)=\frac1{\sqrt{2\pi}\sigma}\exp\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],
\quad X\sim N(\mu,\sigma^2).
	$$
	$$
																								\phi_X(t)=\exp\left(\mu t+\frac{\sigma^2t^2}{2}\right),
\quad E[X]=\mu,\quad\operatorname{Var}(X)=\sigma^2.
	$$
	If $`X\sim N(\mu,\sigma^2)`$,
	$$
	Z=\frac{X-\mu}{\sigma}\sim N(0,1)
	$$
	(standardization). The density is symmetric around $`\mu`$.
</callout>
**Sum of independent normals.** If $`X_i`$ are normal and independent, then
$$
\sum_{i=1}^nX_i\sim N\left(\sum_{i=1}^n\mu_i,\ \sum_{i=1}^n\sigma_i^2\right).
$$
**Normal critical value.** $`z_\alpha`$ denotes a value satisfying $`P(Z>z_\alpha)=\alpha`$, $`Z\sim N(0,1)`$.
### Exponential
<callout icon="📘" color="blue_bg">
	**Def. (Exponential Random Variable)**
	$$
																								f(x)=\begin{cases}\lambda e^{-\lambda x},&x\ge0,\\0,&x<0,\end{cases}
\quad X\sim\operatorname{Exp}(\lambda).
	$$
	$$
																								F(x)=1-e^{-\lambda x}\quad(x\ge0),
\quad\phi_X(t)=\frac\lambda{\lambda-t}\ (t<\lambda).
	$$
	$$
																								E[X]=\frac1\lambda,\quad
\operatorname{Var}(X)=\frac1{\lambda^2}.
	$$
	Rate $`\lambda=1/\beta`$ corresponds to scale $`\beta`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Memoryless Property)**
	$$
	P(X>s+t\mid X>t)=P(X>s).
	$$
</callout>
<details>
<summary>Proof</summary>
	$$
																								P(X>s+t\mid X>t)
=\frac{P(X>s+t,X>t)}{P(X>t)}
=\frac{e^{-\lambda(s+t)}}{e^{-\lambda t}}=e^{-\lambda s}.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Prop. (Minimum of Exponentials)**
	If $`X_1,\ldots,X_n`$ are independent exponentials with rates $`\lambda_1,\ldots,\lambda_n`$, then
	$$
	\min(X_1,\ldots,X_n)\sim \operatorname{Exp}\left(\sum_{i=1}^n\lambda_i\right).
	$$
</callout>
<details>
<summary>Proof</summary>
	$$
																								P(\min_iX_i>x)=P(X_1>x,\ldots,X_n>x)
=\prod_{i=1}^ne^{-\lambda_i x}
=e^{-(\sum_i\lambda_i)x}.
	$$
</details>
## Poisson Process
<callout icon="📘" color="blue_bg">
	**Def. (Poisson Process: Time-Dependent)**
	$`N(t)`$ counts events in $`[0,t]`$, $`N(0)=0`$, and the rate is $`\lambda`$.
	1. Numbers of events in disjoint time intervals are independent.
	2. Distribution of the number of events in an interval depends only on its length (not its location).
	For small $`h`$:
	$$
																								\lim_{h\to0}\frac{P(N(h)=1)}h=\lambda,
\quad\lim_{h\to0}\frac{P(N(h)\ge2)}h=0.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Poisson Count Distribution)**
	$$
	P(N(t)=k)=e^{-\lambda t}\frac{(\lambda t)^k}{k!},\qquad k=0,1,2,\ldots
	$$
</callout>
**Sketch from notes.** Split $`[0,t]`$ into $`n`$ subintervals. For small length $`t/n`$, a subinterval contains 1 event with approximate probability $`\lambda t/n`$ and 2 or more with negligible probability. Thus $`N(t)`$ is approximately $`B(n,\lambda t/n)`$; as $`n\to\infty`$ this tends to $`\operatorname{Poisson}(\lambda t)`$.
**Ex. (Customers at a checkout counter)**
Customers arrive at a checkout counter according to a Poisson distribution at an average of **seven per hour** ($`\lambda=7`$).
(a) During a given hour, what is the probability that no more than three customers arrive?
(b) During a given hour, what is the probability that at least two customers arrive?
(c) If it takes approximately ten minutes to serve each customer, find the mean and variance of total service time for customers arriving during a 1-hour period (assume sufficient servers). Is it likely the total service time will exceed 2.5 hours?
(d) What is the probability exactly two customers arrive during the continuous two-hour period from 2:00 P.M. to 4:00 P.M.? How about two separate one-hour periods, 1:00–2:00 P.M. and 3:00–4:00 P.M.?
**(a)** $`t=1`$:
$$
P(N(1)\le3)=P(N(1)=0)+\cdots+P(N(1)=3)
$$
$$
=e^{-7}+e^{-7}\cdot7+e^{-7}\frac{7^2}{2}+e^{-7}\frac{7^3}{6}.
$$
**(b)**
$$
P(N(1)\ge2)=1-P(N(1)<2)=1-P(N(1)=1)-P(N(1)=0)
=1-8e^{-7}.
$$
**(c)** $`Y`$: total service time; $`X`$: number of customers, $`Y=10X`$.
$$
E[Y]=70\text{ minutes},\quad\operatorname{Var}(Y)=700\text{ minutes}^2.
$$
2.5 hours $`=150`$ minutes. So
$$
P(Y>150)=P(10X>150)=P(X>15)
$$
$$
=1-P(X\le15)=1-\sum_{i=0}^{15}e^{-7}\frac{7^i}{i!}
\approx0.0024.
$$
Thus not likely to occur.
**(d) (1)** For a continuous 2-hour period:
$$
P(N(2)=2)=e^{-14}\frac{14^2}{2}.
$$
**(d) (2)** For two separated 1-hour periods, consider three cases:
- Case 1: first hour 2 customers; second hour 0 customers.
- Case 2: first hour 1 customer; second hour 1 customer.
- Case 3: first hour 0 customers; second hour 2 customers.
$$
P(N_1+N_2=2)=P(N_1=2,N_2=0)+P(N_1=1,N_2=1)+P(N_1=0,N_2=2)
$$
$$
=e^{-14}\left(\frac{7^2}{2}+7^2+\frac{7^2}{2}\right)=e^{-14}\frac{14^2}{2}.
$$
## Gamma and Distributions Arising from the Normal
### Gamma
<callout icon="📘" color="blue_bg">
	**Def. (Gamma Random Variable: Shape and Rate)**
	For $`\alpha,\lambda>0`$,
	$$
																								f(x)=\begin{cases}
\frac{\lambda e^{-\lambda x}(\lambda x)^{\alpha-1}}{\Gamma(\alpha)},&x\ge0,\\
0,&\text{otherwise}.
\end{cases}
	$$
	$$
																								\Gamma(\alpha)=\int_0^\infty e^{-u}u^{\alpha-1}\,du,\quad
\Gamma(n)=(n-1)!.
	$$
	$$
																								\phi_X(t)=\left(\frac{\lambda}{\lambda-t}\right)^\alpha,
\quad E[X]=\frac\alpha\lambda,\quad
\operatorname{Var}(X)=\frac\alpha{\lambda^2}.
	$$
	$`X\sim\operatorname{Gamma}(\alpha,\lambda)`$.
</callout>
**Independent gamma sums.** If $`X_i\sim\operatorname{Gamma}(\alpha_i,\lambda)`$ are independent, then
$$
X_1+\cdots+X_n\sim \operatorname{Gamma}\left(\sum_i\alpha_i,\lambda\right).
$$
**Cor.** For independent $`X_i\sim\operatorname{Exp}(\lambda)`$,
$$
\sum_{i=1}^nX_i\sim\operatorname{Gamma}(n,\lambda).
$$
### Chi-Square
<callout icon="📘" color="blue_bg">
	**Def. (Chi-Square Distribution)**
	If $`Z_1,\ldots,Z_n`$ are independent standard normal variables, then
	$$
	X=\sum_{i=1}^nZ_i^2\sim\chi^2_n,
	$$
	where $`n`$ is the number of degrees of freedom.
	$$
																								\phi_{Z^2}(t)=(1-2t)^{-1/2},\quad
\phi_{\chi^2_n}(t)=(1-2t)^{-n/2}.
	$$
	Thus $`\chi^2_n\sim\operatorname{Gamma}(n/2,1/2)`$ and
	$$
	E[X]=n,\qquad\operatorname{Var}(X)=2n.
	$$
	$$
	f(x)=\frac{x^{n/2-1}e^{-x/2}}{2^{n/2}\Gamma(n/2)},\quad x>0.
	$$
</callout>
**Ex.** For independent $`X_1,X_2\sim N(0,2^2)`$:
$$
\left(\frac{X_1}{2}\right)^2+\left(\frac{X_2}{2}\right)^2\sim\chi^2_2.
$$
To find $`P(X_1^2+X_2^2>9)`$, rewrite as $`P(\chi^2_2>9/4)`$.
### Student t
<callout icon="📘" color="blue_bg">
	**Def. (Student's t Distribution)**
	If $`Z\sim N(0,1)`$, $`V\sim\chi^2_n`$ are independent, then
	$$
	T_n=\frac{Z}{\sqrt{V/n}}\sim t_n.
	$$
	$`E[T_n]=0`$ (when $`n>1`$), $`\operatorname{Var}(T_n)=n/(n-2)`$ for $`n>2`$.
	For large $`n`$, $`t_n`$ approaches $`N(0,1)`$.
	$$
																								P(T_n>t_{\alpha,n})=\alpha,\qquad
t_{1-\alpha,n}=-t_{\alpha,n}.
	$$
</callout>
### F
<callout icon="📘" color="blue_bg">
	**Def. (F Distribution)**
	If $`U\sim\chi^2_n`$, $`V\sim\chi^2_m`$ are independent, then
	$$
	F_{n,m}=\frac{U/n}{V/m}\sim F_{n,m}.
	$$
	$$
	P(F_{n,m}>F_{\alpha,n,m})=\alpha.
	$$
	Reciprocal identity: $`F_{\alpha,m,n}=1/F_{1-\alpha,n,m}`$.
</callout>
![](notion-file-block://01831e50-c662-4ccc-8ca0-cf28d392b7a0/4549fd85-dc63-4dbd-a2a7-e362b6b1d43c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_t_distribution_tight.svg)
**Ex.** For independent $`X_i\sim N(\mu,\sigma^2)`$, the standardized variables $`(X_1-X_2)/(\sqrt2\sigma)`$ and $`(X_1+X_2-2\mu)/(\sqrt2\sigma)`$ are normal; their squares lead to independent chi-square variables, and their ratio has an F distribution.
# Distributions of Sampling Statistics
<callout icon="📘" color="blue_bg">
	**Def. (Random Sample)**
	If $`X_1,\ldots,X_n`$ are independent random variables having a common distribution $`F`$, they constitute a random sample from $`F`$.
	Parameter inference: obtain information about an unknown population parameter (e.g., $`\mu,\sigma^2,p`$).
	Nonparametric inference: inference not specified in terms of a particular parametric family.
	An estimator is a function $`\hat\theta=\theta(X_1,\ldots,X_n)`$ of the sample; therefore it is also a random variable and has its own sampling distribution.
</callout>
![](notion-file-block://df9c793c-f96a-41e8-a8c6-13e8932195b1/04d01078-30a4-457f-b778-f9e69436975e?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_sampling_diagram_tight.svg)
## Sample Mean and the Central Limit Theorem
<callout icon="📘" color="blue_bg">
	**Def. (Sample Mean)**
	For population mean $`\mu`$ and variance $`\sigma^2`$, let
	$$
	\overline X=\frac{X_1+\cdots+X_n}{n}.
	$$
	Then
	$$
	E[\overline X]=\mu,\qquad \operatorname{Var}(\overline X)=\frac{\sigma^2}{n}.
	$$
	If $`X_i\sim N(\mu,\sigma^2)`$, then $`\overline X\sim N(\mu,\sigma^2/n)`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. (Central Limit Theorem)**
	Let $`X_1,X_2,\ldots`$ be i.i.d. random variables with mean $`\mu`$ and variance $`\sigma^2`$. For large $`n`$,
	$$
																							P\left(\frac{X_1+\cdots+X_n-n\mu}{\sigma\sqrt n}\le x\right)
\to P(Z\le x),\qquad Z\sim N(0,1).
	$$
	Consequently,
	$$
	\overline X\ \overset{\rm approx}{\sim}\ N\left(\mu,\frac{\sigma^2}n\right).
	$$
</callout>
## Normal Approximation to Binomial and Continuity Correction
<callout icon="📜" color="yellow_bg">
	**Prop. (Normal Approximation to Binomial)**
	When $`X\sim B(n,p)`$ and $`np`$ and $`n(1-p)`$ are sufficiently large (notes: about 5 or more),
	$$
	X\ \overset{\rm approx}{\sim}\ N(np,np(1-p)).
	$$
	Use a continuity correction when approximating discrete binomial probabilities by a continuous normal distribution.
	$$
	P(11\le X\le14)\approx P(10.5\le Y\le14.5)
	$$
	for the corresponding normal variable $`Y`$.
</callout>
## Sample Variance
<callout icon="📘" color="blue_bg">
	**Def. (Sample Variance)**
	$$
	S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline X)^2.
	$$
	$$
																							(n-1)S^2=\sum_i(X_i-\overline X)^2
=\sum_iX_i^2-n\overline X^2.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Unbiased Sample Variance)**
	$$
	E[S^2]=\sigma^2.
	$$
</callout>
<details>
<summary>Proof</summary>
	$$
	E[(n-1)S^2]=E\left[\sum_iX_i^2-n\overline X^2\right]
	$$
	$$
																							=\sum_i(\sigma^2+\mu^2)-n\left(\frac{\sigma^2}{n}+\mu^2\right)
=(n-1)\sigma^2.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. (Sample Distribution from a Normal Population)**
	For $`X_1,\ldots,X_n\sim N(\mu,\sigma^2)`$ independent,
	$$
																							\overline X\sim N\left(\mu,\frac{\sigma^2}n\right),
\qquad
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
	$$
	Moreover, $`\overline X`$ and $`S^2`$ are independent.
</callout>
<details>
<summary>Proof sketch</summary>
	By expanding the squared deviations,
	$$
																							\sum_{i=1}^n(X_i-\mu)^2
=\sum_{i=1}^n(X_i-\overline X)^2+n(\overline X-\mu)^2.
	$$
	After dividing by $`\sigma^2`$, the left side has $`\chi_n^2`$ and the second right-hand term has $`\chi_1^2`$. This leaves $`\chi^2_{n-1}`$ for the residual sum of squares.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor. (Sample t Statistic)**
	If $`X_i`$ is a random sample from $`N(\mu,\sigma^2)`$, then
	$$
	\frac{\overline X-\mu}{S/\sqrt n}\sim t_{n-1}.
	$$
</callout>
# Parameter Estimation
<callout icon="📘" color="blue_bg">
	**Def. (Point and Interval Estimates)**
	A point estimate assigns one value to an unknown parameter.
	An interval estimate gives a range expected to contain the unknown parameter.
</callout>
## Likelihood and Maximum Likelihood Estimation
<callout icon="📘" color="blue_bg">
	**Def. (Likelihood Function)**
	Given observations $`x_1,\ldots,x_n`$ from $`f(x\mid\theta)`$, the joint density or probability mass considered as a function of $`\theta`$ is the likelihood:
	$$
	L(\theta\mid x_1,\ldots,x_n)=\prod_{i=1}^n f(x_i\mid\theta).
	$$
	It measures how likely the observed data are for each parameter value (with the data fixed).
	Log-likelihood:
	$$
																							\ell(\theta)=\log L(\theta\mid x_1,\ldots,x_n)
=\sum_{i=1}^n\log f(x_i\mid\theta).
	$$
	Choose $`\hat\theta`$ maximizing $`L`$ or $`\ell`$; usually solve $`\partial\ell/\partial\theta=0`$ and check the maximum.
</callout>
![](notion-file-block://e79872da-a2ee-4d8c-a532-31a7e433d501/9abfbc16-a05e-4a06-95bb-8a3a04e8cbe7?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_likelihood_curves_tight.svg)
**Ex. (Why the likelihood measures the "likelihood" of θ)**
$`X_i\overset{\text{i.i.d.}}{\sim}N(\mu,\sigma^2)`$, $`\sigma^2`$: known $`\Rightarrow \theta=\mu`$.
Goal: estimate $`\mu`$ given $`(x_1,\ldots,x_n)`$.
$`\mu_1`$ is more likely than $`\mu_2`$: more data points are at the center.
How can we quantify this?
$`f(x_i\mid\mu_1)`$: height of $`x_i`$ for $`\mu_1`$.
$`f(x_i\mid\mu_2)`$: height of $`x_i`$ for $`\mu_2`$.
$$
\prod_{i=1}^n f(x_i\mid\mu_1)>\prod_{i=1}^n f(x_i\mid\mu_2).
$$
How to get a solution?
$$
\frac{\partial\ell}{\partial\theta}=0,\qquad\frac{\partial^2\ell}{\partial\theta^2}<0
\quad(\text{maximum}).
$$
<callout icon="📜" color="yellow_bg">
	**Prop. (MLE for Bernoulli / Binomial)**
	For $`X_1,\ldots,X_n\sim\operatorname{Bernoulli}(p)`$,
	$$
																							L(p)=\prod_i p^{x_i}(1-p)^{1-x_i},
\quad
\ell(p)=\sum_i[x_i\log p+(1-x_i)\log(1-p)].
	$$
	$$
																							\frac{\partial\ell}{\partial p}=\frac{\sum_i x_i}{p}
-\frac{n-\sum_i x_i}{1-p}=0
\ \Longrightarrow\ 
\hat p=\frac{\sum_i x_i}{n}=\overline X.
	$$
	$$
	E[\hat p]=p,\qquad\operatorname{Var}(\hat p)=\frac{p(1-p)}n.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (MLE for Poisson)**
	For i.i.d. $`X_i\sim\operatorname{Poisson}(\lambda)`$,
	$$
	L(\lambda)=\prod_{i=1}^n\frac{e^{-\lambda}\lambda^{x_i}}{x_i!},
	$$
	$$
	\ell(\lambda)=-n\lambda+\log\lambda\sum_i x_i-\sum_i\log(x_i!).
	$$
	$$
																							\ell'(\lambda)=-n+\frac{\sum_i x_i}{\lambda}=0
\ \Longrightarrow\ \hat\lambda=\overline X.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (MLE for Normal)**
	For i.i.d. $`X_i\sim N(\mu,\sigma^2)`$,
	$$
					L(\mu,\sigma^2)=\prod_i\frac1{\sqrt{2\pi\sigma^2}}
\exp\left(-\frac{(x_i-\mu)^2}{2\sigma^2}\right).
	$$
	$$
					\ell(\mu,\sigma^2)=-\frac n2\log(2\pi\sigma^2)
-\frac1{2\sigma^2}\sum_i(x_i-\mu)^2.
	$$
	$$
					\frac{\partial\ell}{\partial\mu}=\frac{\sum_i(x_i-\mu)}{\sigma^2}=0
\quad\Longrightarrow\quad\hat\mu=\overline X.
	$$
	$$
					\frac{\partial\ell}{\partial\sigma^2}=-\frac n{2\sigma^2}
+\frac{\sum_i(x_i-\mu)^2}{2\sigma^4}=0.
	$$
	$$
					\Longrightarrow\quad\hat\sigma^2
=\frac1n\sum_i(x_i-\hat\mu)^2
=\frac1n\sum_i(x_i-\overline X)^2.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (MLE for Uniform **$`U(0,\theta)`$**)**
	For i.i.d. $`X_i\sim U(0,\theta)`$,
	$$
	L(\theta)=\begin{cases}\theta^{-n},&0\le\max_i x_i\le\theta,\\0,&\text{otherwise}.\end{cases}
	$$
	Therefore $`\hat\theta=\max_i X_i`$.
</callout>
## Evaluating a Point Estimator
<callout icon="📘" color="blue_bg">
	**Def. (Mean Squared Error and Bias)**
	For an estimator $`d(X)`$ of $`\theta`$,
	$$
	r(d,\theta)=E[(d(X)-\theta)^2].
	$$
	Bias:
	$$
	b_d(\theta)=E[d(X)]-\theta.
	$$
	If $`b_d(\theta)=0`$ for every $`\theta`$, $`d`$ is unbiased.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Bias–Variance Decomposition)**
	$$
	r(d,\theta)=\operatorname{Var}(d)+[b_d(\theta)]^2.
	$$
	For an unbiased estimator, $`r(d,\theta)=\operatorname{Var}(d)`$.
</callout>
<details>
<summary>Proof</summary>
	$$
	r(d,\theta)=E[(d-E[d]+E[d]-\theta)^2]
	$$
	$$
																							=E[(d-E[d])^2]+(E[d]-\theta)^2
=\operatorname{Var}(d)+b_d(\theta)^2.
	$$
</details>
## Bayes Estimator
<callout icon="📘" color="blue_bg">
	**Def. (Bayes Estimator)**
	Let $`p(\theta)`$ be the prior distribution and $`f(x\mid\theta)`$ the likelihood. Then
	$$
																							f(\theta\mid x_1,\ldots,x_n)
=\frac{f(x_1,\ldots,x_n\mid\theta)p(\theta)}
{\int f(x_1,\ldots,x_n\mid\theta)p(\theta)\,d\theta}.
	$$
	Under squared error loss, the Bayes estimator is the posterior mean:
	$$
																							E[\theta\mid X_1=x_1,\ldots,X_n=x_n]
=\int\theta f(\theta\mid x_1,\ldots,x_n)\,d\theta.
	$$
</callout>
# Interval Estimates
## Confidence Interval for a Normal Mean: Known Variance
For $`X_1,\ldots,X_n`$ from a normal distribution with unknown $`\mu`$ and known $`\sigma^2`$,
$$
Z=\frac{\overline X-\mu}{\sigma/\sqrt n}\sim N(0,1).
$$
At $`95\%`$ confidence,
$$
P\left(-1.96<\frac{\overline X-\mu}{\sigma/\sqrt n}<1.96\right)=0.95.
$$
<callout icon="📘" color="blue_bg">
	**Def. (Two-Sided Confidence Interval)**
	At $`100(1-\alpha)\%`$ confidence,
	$$
																							\boxed{\left(\overline X-z_{\alpha/2}\frac{\sigma}{\sqrt n},\
\overline X+z_{\alpha/2}\frac{\sigma}{\sqrt n}\right)}.
	$$
	Example: $`\alpha=0.05`$, $`z_{\alpha/2}=1.96`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (One-Sided Confidence Intervals)**
	Upper:
	$$
	\left(-\infty,\ \overline X+z_\alpha\frac{\sigma}{\sqrt n}\right).
	$$
	Lower:
	$$
	\left(\overline X-z_\alpha\frac{\sigma}{\sqrt n},\ +\infty\right).
	$$
</callout>
## Confidence Interval for a Normal Mean: Unknown Variance
<callout icon="📜" color="yellow_bg">
	**Thm. (Studentized Mean)**
	For a normal sample with unknown $`\mu,\sigma^2`$,
	$$
	T=\frac{\overline X-\mu}{S/\sqrt n}\sim t_{n-1}.
	$$
	$$
	P\left(-t_{\alpha/2,n-1}\le T\le t_{\alpha/2,n-1}\right)=1-\alpha.
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Confidence Interval for **$`\mu`$**: Unknown Variance)**
	$$
																							\boxed{\left(\overline X-t_{\alpha/2,n-1}\frac{S}{\sqrt n},\
\overline X+t_{\alpha/2,n-1}\frac{S}{\sqrt n}\right)}.
	$$
</callout>
## Prediction Interval
For a new independent observation $`X_{n+1}`$ from the same normal population, it is reasonable to use the current sample mean $`\overline X`$ as a predicted value. Because $`X_{n+1}`$ and $`\overline X`$ are independent,
$$
X_{n+1}-\overline X\sim N\left(0,\sigma^2\left(1+\frac1n\right)\right),
\quad
\frac{X_{n+1}-\overline X}{S\sqrt{1+1/n}}\sim t_{n-1}.
$$
<callout icon="📘" color="blue_bg">
	**Def. (Prediction Interval)**
	At $`100(1-\alpha)\%`$:
	$$
																							\boxed{\left(\overline X-t_{\alpha/2,n-1}S\sqrt{1+\frac1n},\
\overline X+t_{\alpha/2,n-1}S\sqrt{1+\frac1n}\right)}.
	$$
</callout>
## Confidence Interval for a Normal Variance
For a normal sample,
$$
\frac{(n-1)S^2}{\sigma^2}\sim\chi^2_{n-1}.
$$
With upper-tail convention $`P(\chi^2_\nu>\chi^2_{\alpha,\nu})=\alpha`$, a two-sided confidence interval for $`\sigma^2`$ is
<callout icon="📘" color="blue_bg">
	**Def. (Confidence Interval for **$`\sigma^2`$**)**
	$$
																							\boxed{\left(
\frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}},
\frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}}
\right)}.
	$$
</callout>
## Difference in Two Means
Let $`X_1,\ldots,X_n`$ be sampled from $`N(\mu_1,\sigma_1^2)`$, and $`Y_1,\ldots,Y_m`$ independently from $`N(\mu_2,\sigma_2^2)`$.
**Known variances**
$$
\overline X-\overline Y
\sim N\left(\mu_1-\mu_2,\frac{\sigma_1^2}{n}+\frac{\sigma_2^2}{m}\right).
$$
<callout icon="📘" color="blue_bg">
	**Def. (CI for Difference of Means, Known Variances)**
	$$
																							\boxed{\left(
\overline X-\overline Y-z_{\alpha/2}\sqrt{\frac{\sigma_1^2}n+\frac{\sigma_2^2}m},\
\overline X-\overline Y+z_{\alpha/2}\sqrt{\frac{\sigma_1^2}n+\frac{\sigma_2^2}m}
\right)}.
	$$
</callout>
**Unknown but equal variances** ($`\sigma_1^2=\sigma_2^2=\sigma^2`$):
$$
S_p^2=\frac{(n-1)S_1^2+(m-1)S_2^2}{n+m-2},
\qquad
\frac{(n+m-2)S_p^2}{\sigma^2}\sim\chi^2_{n+m-2}.
$$
$$
\frac{\overline X-\overline Y-(\mu_1-\mu_2)}
{S_p\sqrt{1/n+1/m}}\sim t_{n+m-2}.
$$
<callout icon="📘" color="blue_bg">
	**Def. (CI for Difference of Means, Pooled Variance)**
	$$
																							\boxed{\left(
\overline X-\overline Y-t_{\alpha/2,n+m-2}S_p\sqrt{\frac1n+\frac1m},\
\overline X-\overline Y+t_{\alpha/2,n+m-2}S_p\sqrt{\frac1n+\frac1m}
\right)}.
	$$
</callout>
## Approximate Confidence Interval for a Bernoulli Mean
If $`X_i\sim\operatorname{Bernoulli}(p)`$ and $`\hat p=\overline X`$,
$$
\frac{\overline X-p}{\sqrt{p(1-p)/n}}\overset{\rm approx}{\sim} N(0,1).
$$
Substitute $`\hat p`$ for unknown $`p`$ in the standard error:
<callout icon="📘" color="blue_bg">
	**Def. (Approximate CI for **$`p`$**)**
	$$
																							\boxed{\left(
\hat p-z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}n},\
\hat p+z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}n}
\right)}.
	$$
</callout>
## Sample Size Determination
If desired interval length is no more than $`b`$ for a Bernoulli proportion, the approximate interval length is
$$
2z_{\alpha/2}\sqrt{\frac{p(1-p)}n}\le b.
$$
Unknown $`p`$: use a preliminary sample to estimate $`p`$ (or $`p=1/2`$ for a conservative choice). Then
$$
n\ge \frac{4z_{\alpha/2}^2p(1-p)}{b^2}.
$$
If a preliminary sample gives $`\hat p`$, substitute $`\hat p(1-\hat p)`$; maximize at $`p=1/2`$.
# Hypothesis Testing
## Null Hypothesis, Alternative, and Errors
<callout icon="📘" color="blue_bg">
	**Def. (Statistical Hypotheses)**
	The **null hypothesis** $`H_0`$ is what is to be tested, usually the negation of the assertion or effect under examination.
	The **alternative hypothesis** $`H_1`$ is the competing assertion.
	A statistical test is a procedure for choosing whether to reject $`H_0`$.
	Hypotheses are expressed using **population parameters**, not sample statistics (which are observed quantities).
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Critical / Rejection Region)**
	A critical (rejection) region $`C`$ is a set of observations or test statistic values for which $`H_0`$ is rejected.
	Failure to reject $`H_0`$ does **not** mean $`H_0`$ is true; only that the data did not provide sufficient evidence against it.
</callout>
<table fit-page-width="true" header-row="true">
<tr>
<td>Decision / Actual</td>
<td>$`H_0`$ true</td>
<td>$`H_1`$ true</td>
</tr>
<tr>
<td>Reject $`H_0`$</td>
<td>Type I error ($`\alpha`$)</td>
<td>Correct rejection</td>
</tr>
<tr>
<td>Fail to reject $`H_0`$</td>
<td>Correct decision</td>
<td>Type II error ($`\beta`$)</td>
</tr>
</table>
<callout icon="📘" color="blue_bg">
	**Def. (Type I / II Error, Power, Significance)**
	Type I error $`(\alpha)`$: rejecting $`H_0`$ when it is true.
	Type II error $`(\beta)`$: failing to reject $`H_0`$ when it is false.
	Power: $`P(\text{reject }H_0\mid H_1\text{ true})=1-\beta`$.
	Significance level $`\alpha`$: under $`H_0`$, $`P(\text{reject }H_0)\le\alpha`$.
</callout>
![](notion-file-block://e537ed0d-9f1d-4c7f-963b-c3fa2205f674/60571a44-9962-4ea5-9a9a-b2ce67eb4793?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_critical_region_tight.svg)
**General steps of a test:**
1. State $`H_0,H_1`$ (population parameters).
2. Set significance level $`\alpha`$.
3. Fix test statistic (point estimator / test statistic).
4. Determine the critical region $`C`$ and collect data.
5. Evaluate the test statistic.
6. Decide to reject or fail to reject $`H_0`$ at $`\alpha`$.
7. Interpret the decision.
## Tests for a Normal Mean, Known Variance
For a normal random sample $`X_1,\ldots,X_n\sim N(\mu,\sigma^2)`$, $`\sigma`$ known,
$$
Z=\frac{\overline X-\mu_0}{\sigma/\sqrt n}
\sim N(0,1)\quad\text{under }H_0:\mu=\mu_0.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (One-Sided Z Test)**
	For $`H_0:\mu\le\mu_0`$ versus $`H_1:\mu>\mu_0`$:
	$$
																						\text{Reject }H_0\quad\text{if}\quad
\frac{\overline X-\mu_0}{\sigma/\sqrt n}>z_\alpha.
	$$
	For $`H_0:\mu\ge\mu_0`$ versus $`H_1:\mu<\mu_0`$:
	$$
	\text{Reject }H_0\quad\text{if}\quad Z<-z_\alpha.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. (Two-Sided Z Test)**
	For $`H_0:\mu=\mu_0`$ versus $`H_1:\mu\ne\mu_0`$,
	$$
	\text{Reject }H_0\quad\text{if}\quad |Z|>z_{\alpha/2}.
	$$
	Otherwise fail to reject $`H_0`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (p-value)**
	The p-value is the **smallest significance level** at which the given data lead to rejection of $`H_0`$.
	If p-value $`<\alpha`$, reject $`H_0`$.
	If p-value $`\ge\alpha`$, fail to reject $`H_0`$.
	For right-tailed $`Z=z`$: $`p=P(Z\ge z)`$.
	For two-sided $`Z=z`$: $`p=P(|Z|\ge|z|)`$.
</callout>
**Ex. (Two-sided Z test).** Test $`H_0:\mu=8`$ versus $`H_1:\mu\ne8`$, with $`\alpha=0.05`$. Using the observed standardized value $`z=1.68`$,
$$
|1.68|<1.96\quad\Longrightarrow\quad\text{fail to reject }H_0.
$$
Two-sided p-value $`P(|Z|\ge1.68)\approx0.093`$.
**Relation to CIs.** Failing to reject $`H_0:\mu=\mu_0`$ at significance $`\alpha`$ is equivalent to $`\mu_0`$ lying in the corresponding $`100(1-\alpha)\%`$ confidence interval.
## Power and Sample Size
![](notion-file-block://1306db2e-baa1-4d00-9354-aaaabf4fdb96/87c89f30-b851-4042-9ab4-05db6270c666?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_power_tight.svg)
For one-sided $`H_0:\mu=\mu_0`$, $`H_1:\mu>\mu_0`$ with a true mean $`\mu_1>\mu_0`$:
$$
\operatorname{Power}(\mu_1)
=P_{\mu_1}\left(\frac{\overline X-\mu_0}{\sigma/\sqrt n}>z_\alpha\right).
$$
Since $`(\overline X-\mu_1)/(\sigma/\sqrt n)\sim N(0,1)`$,
$$
\operatorname{Power}(\mu_1)
=1-\Phi\left(z_\alpha-\frac{\mu_1-\mu_0}{\sigma/\sqrt n}\right)
=1-\beta.
$$
<callout icon="📜" color="yellow_bg">
	**Prop. (Sample Size for One-Sided Power)**
	For desired power $`1-\beta`$ at alternative $`\mu_1>\mu_0`$,
	$$
	\boxed{n\approx\frac{(z_\alpha+z_\beta)^2\sigma^2}{(\mu_1-\mu_0)^2}}.
	$$
	Choose the next higher integer.
</callout>
**Two-sided power** for $`H_1:\mu=\mu_1`$:
$$
\beta(\mu_1)=P_{\mu_1}\left(
-z_{\alpha/2}\le\frac{\overline X-\mu_0}{\sigma/\sqrt n}\le z_{\alpha/2}
\right).
$$
Set $`\delta=(\mu_1-\mu_0)/(\sigma/\sqrt n)`$:
$$
\beta(\mu_1)=\Phi(z_{\alpha/2}-\delta)
-\Phi(-z_{\alpha/2}-\delta),\quad
\operatorname{Power}=1-\beta(\mu_1).
$$
**Ex. (One-sided test and power)**
$`H_0:\mu=3`$, $`H_1:\mu>3`$.
$$
z=\frac{3.4-3}{2.4/\sqrt{75}}=1.44,\qquad
\text{p-value}=P(Z>1.44)=0.07>0.01.
$$
Therefore, fail to reject $`H_0`$ at $`\alpha=0.01`$.
$$
\operatorname{Power}(3.2)
=P_{\mu=3.2}\left(\frac{\bar X-3}{2.4/\sqrt{75}}\ge2.33\right)
=P\left(\frac{\bar X-3.2}{2.4/\sqrt{75}}\ge1.61\right)=0.0537.
$$
**Two-Sided Power**
$$
\beta(\mu_1)=P_{\mu_1}(\text{fail to reject }H_0)
=P_{\mu_1}\left(\left|\frac{\bar X-\mu_0}{\sigma/\sqrt n}\right|\le z_{\alpha/2}\right)
$$
$$
=P_{\mu_1}\left(-z_{\alpha/2}\le
\frac{\bar X-\mu_0}{\sigma/\sqrt n}\le z_{\alpha/2}\right)
$$
$$
=P_{\mu_1}\left(
-z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}
\le\frac{\bar X-\mu_1}{\sigma/\sqrt n}
\le z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}
\right).
$$
$$
\boxed{
\beta(\mu_1)=\Phi\left(z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}\right)
-\Phi\left(-z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}\right)
}.
$$
**Sample Size Determination**
If $`\mu_1>\mu_0`$, then $`\Phi(-z_{\alpha/2}+(\mu_0-\mu_1)/(\sigma/\sqrt n))\approx0`$.
$$
\beta\approx\Phi\left(z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}\right),
\quad
z_{\alpha/2}+\frac{\mu_0-\mu_1}{\sigma/\sqrt n}\approx-z_\beta.
$$
$$
\boxed{n\approx\frac{(z_{\alpha/2}+z_\beta)^2\sigma^2}{(\mu_1-\mu_0)^2}}.
$$
## Unknown Variance: One-Sample t Test
For $`X_i\sim N(\mu,\sigma^2)`$ with unknown variance,
$$
T=\frac{\overline X-\mu_0}{S/\sqrt n}\sim t_{n-1}
\quad\text{under }H_0.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (One-Sample t Test)**
	For $`H_0:\mu=\mu_0`$ against $`H_1:\mu\ne\mu_0`$,
	$$
	\text{Reject }H_0\iff |T|>t_{\alpha/2,n-1}.
	$$
	One-sided tests use $`T>t_{\alpha,n-1}`$ or $`T<-t_{\alpha,n-1}`$ according to $`H_1`$.
</callout>
## Testing Equality of Two Normal Population Means
### Known Variances
With independent normal samples and known $`\sigma_1^2,\sigma_2^2`$:
$$
H_0:\mu_1=\mu_2,\qquad H_1:\mu_1\ne\mu_2,
$$
$$
Z=\frac{\overline X-\overline Y}{\sqrt{\sigma_1^2/n+\sigma_2^2/m}}
\sim N(0,1)\quad(H_0).
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (Two-Sample Z Test)**
	Two-sided: fail to reject $`H_0`$ if $`|Z|\le z_{\alpha/2}`$; reject otherwise.
	For one-sided $`H_1:\mu_1>\mu_2`$, reject if $`Z>z_\alpha`$.
</callout>
### Unknown but Equal Variances
If the unknown population variances are equal,
$$
S_p^2=\frac{(n-1)S_1^2+(m-1)S_2^2}{n+m-2},
\qquad
T=\frac{\overline X-\overline Y}{S_p\sqrt{1/n+1/m}}
\sim t_{n+m-2}\quad(H_0).
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (Pooled Two-Sample t Test)**
	For two-sided $`H_0:\mu_1=\mu_2`$, reject if $`|T|>t_{\alpha/2,n+m-2}`$.
</callout>
### Unknown and Unequal Variances (Large Samples)
$$
T=\frac{\overline X-\overline Y}{\sqrt{S_1^2/n+S_2^2/m}},
$$
When both sample sizes are large, use the approximate normal distribution.
## Paired t Test
For pairs $`(X_i,Y_i)`$, the two measurements within a pair are dependent. Set $`W_i=X_i-Y_i`$.
<callout icon="📜" color="yellow_bg">
	**Thm. (Paired t Test)**
	To test $`H_0:\mu_W=0`$ versus $`H_1:\mu_W\ne0`$, use
	$$
	T=\frac{\overline W}{S_W/\sqrt n}.
	$$
	If normality of the paired differences is assumed, under $`H_0`$ this has a $`t_{n-1}`$ distribution.
	Reject the two-sided null when $`|T|>t_{\alpha/2,n-1}`$.
</callout>
## Testing a Normal Variance
For a normal sample $`X_i\sim N(\mu,\sigma^2)`$ with unknown $`\mu,\sigma^2`$, test
$$
H_0:\sigma^2=\sigma_0^2,\quad H_1:\sigma^2\ne\sigma_0^2.
$$
Under $`H_0`$,
$$
Q=\frac{(n-1)S^2}{\sigma_0^2}\sim\chi^2_{n-1}.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (Chi-Square Test for a Variance)**
	Fail to reject the two-sided null when
	$$
	\chi^2_{1-\alpha/2,n-1}\le Q\le\chi^2_{\alpha/2,n-1}.
	$$
	Otherwise reject $`H_0`$.
</callout>
## Testing Equality of Two Variances
For independent normal samples with variances $`\sigma_1^2,\sigma_2^2`$:
$$
H_0:\sigma_1^2=\sigma_2^2,\qquad H_1:\sigma_1^2\ne\sigma_2^2.
$$
$$
F=\frac{S_1^2}{S_2^2}\sim F_{n-1,m-1}\quad(H_0).
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (F Test for Variance Equality)**
	For two-sided testing, fail to reject $`H_0`$ when
	$$
	F_{1-\alpha/2,n-1,m-1}\le F\le F_{\alpha/2,n-1,m-1}.
	$$
	Reject otherwise.
</callout>
## Tests for a Bernoulli Proportion
If $`X=\sum_{i=1}^n X_i\sim B(n,p)`$,
$$
H_0:p\le p_0,\qquad H_1:p>p_0,
$$
the exact binomial test rejects for large $`X`$: $`C=\{X>k\}`$, chosen to control $`P_{p_0}(X>k)\le\alpha`$.
The p-value is $`P_{p_0}(X\ge x_{\rm obs})`$.
For large $`np_0,n(1-p_0)`$:
$$
Z=\frac{X-np_0}{\sqrt{np_0(1-p_0)}}\overset{\rm approx}{\sim}N(0,1)\quad(H_0).
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (Normal Approximation for a Proportion Test)**
	For $`H_1:p>p_0`$, reject if $`Z>z_\alpha`$.
	For $`H_1:p\ne p_0`$, reject if $`|Z|>z_{\alpha/2}`$.
</callout>
## Testing Equality of Two Proportions
Let $`X\sim B(n,p_1)`$ and $`Y\sim B(m,p_2)`$ independent. Estimate
$$
\hat p_1=\frac Xn,\qquad\hat p_2=\frac Ym.
$$
For approximate confidence intervals use
$$
\hat p_1-\hat p_2\pm z_{\alpha/2}
\sqrt{\frac{\hat p_1(1-\hat p_1)}n+\frac{\hat p_2(1-\hat p_2)}m}.
$$
Under $`H_0:p_1=p_2=p`$, use pooled
$$
\hat p=\frac{X+Y}{n+m}.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (Two-Proportion Z Test)**
	$$
																						Z=\frac{\hat p_1-\hat p_2}
{\sqrt{\hat p(1-\hat p)(1/n+1/m)}}\overset{\rm approx}{\sim}N(0,1).
	$$
	Two-sided $`H_1:p_1\ne p_2`$: reject if $`|Z|>z_{\alpha/2}`$.
</callout>
# Regression
## Simple Linear Regression and Correlation
<callout icon="📘" color="blue_bg">
	**Def. (Simple Linear Regression Model)**
	We want to determine a relationship between a response $`Y`$ and an explanatory variable $`x`$:
	$$
	Y=\beta_0+\beta_1x+\varepsilon,\qquad \varepsilon\sim N(0,\sigma^2).
	$$
	Response $`Y`$ is the dependent variable; the explanatory variable $`x`$ is treated as given (independent variable), and $`\varepsilon`$ is random error.
	The regression coefficients $`\beta_0,\beta_1`$ are unknown parameters.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Corrected Sums)**
	$$
																					S_{XY}=\sum_{i=1}^n(x_i-\overline x)(y_i-\overline y)
=\sum_i x_iy_i-n\overline x\,\overline y.
	$$
	$$
	S_{XX}=\sum_{i=1}^n(x_i-\overline x)^2=\sum_i x_i^2-n\overline x^2,
	$$
	$$
	S_{YY}=\sum_{i=1}^n(y_i-\overline y)^2=\sum_i y_i^2-n\overline y^2.
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Sample Correlation Coefficient)**
	$$
	r=\frac{S_{XY}}{\sqrt{S_{XX}S_{YY}}}.
	$$
	For independent bivariate normal pairs, a test of zero population correlation
	$`H_0:\rho=0`$ uses
	$$
	T=\frac{\sqrt{n-2}\,r}{\sqrt{1-r^2}}\sim t_{n-2}.
	$$
</callout>
## Least Squares Estimators
<callout icon="📘" color="blue_bg">
	**Def. (Residual Sum of Squares)**
	For a line $`y=A+Bx`$ fitted to the data, minimize
	$$
	SS=\sum_{i=1}^n(y_i-A-Bx_i)^2.
	$$
	$`A`$ estimates $`\beta_0`$ and $`B`$ estimates $`\beta_1`$.
</callout>
<details>
<summary>Derivation of Least Squares Estimates</summary>
	Set partial derivatives equal to zero:
	$$
																					\frac{\partial SS}{\partial A}
=-2\sum_i(y_i-A-Bx_i)=0,
	$$
	$$
																					\frac{\partial SS}{\partial B}
=-2\sum_i x_i(y_i-A-Bx_i)=0.
	$$
	Normal equations:
	$$
																					\begin{cases}
nA+B\sum_i x_i=\sum_i y_i,\\
A\sum_i x_i+B\sum_i x_i^2=\sum_i x_iy_i.
\end{cases}
	$$
	Thus
	$$
																					\boxed{B=\frac{\sum_i x_iy_i-n\overline x\,\overline y}{\sum_i x_i^2-n\overline x^2}
=\frac{S_{XY}}{S_{XX}},
\qquad A=\overline y-B\overline x}.
	$$
	Estimated response: $`\hat Y=A+Bx`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Prop. (Sampling Distributions of Least Squares Estimators)**
	Assume fixed $`x_i`$, independent normal errors with mean zero and variance $`\sigma^2`$.
	$$
																					B=\beta_1+\frac{\sum_i(x_i-\overline x)\varepsilon_i}{S_{XX}},
\quad E[B]=\beta_1,\quad \operatorname{Var}(B)=\frac{\sigma^2}{S_{XX}}.
	$$
	$$
	\boxed{B\sim N\left(\beta_1,\frac{\sigma^2}{S_{XX}}\right)}.
	$$
	Also
	$$
	A=\overline Y-B\overline x,\quad E[A]=\beta_0,
	$$
	$$
																					\operatorname{Var}(A)=\sigma^2\left(\frac1n+\frac{\overline x^2}{S_{XX}}\right),
\quad
\boxed{A\sim N\left(\beta_0,\sigma^2\left(\frac1n+\frac{\overline x^2}{S_{XX}}\right)\right)}.
	$$
</callout>
## Residual Variance and Inference on Regression Parameters
<callout icon="📘" color="blue_bg">
	**Def. (Residual Sum of Squares / Residual Mean Square)**
	$$
	SSR=\sum_{i=1}^n(Y_i-A-Bx_i)^2.
	$$
	Under normal errors,
	$$
																					\frac{SSR}{\sigma^2}\sim\chi^2_{n-2},\quad
E\left[\frac{SSR}{n-2}\right]=\sigma^2.
	$$
	Therefore $`S_{Y\mid X}^2=SSR/(n-2)`$ is an unbiased estimator of $`\sigma^2`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Regression Estimators and Residuals)**
	$`A`$ and $`B`$ are unbiased. Under the normal linear model, $`(A,B)`$ is independent of $`SSR`$, and
	$$
	\frac{SSR}{\sigma^2}\sim\chi^2_{n-2}.
	$$
</callout>
**Residual sum of squares and regression parameter calculations**
$$
SSR=\sum_{i=1}^n(Y_i-A-Bx_i)^2=\sum_{i=1}^n\hat e_i^2.
$$
$$
\frac{SSR}{\sigma^2}\sim\chi^2_{n-2},\qquad
E\left[\frac{SSR}{\sigma^2}\right]=n-2,
\quad E\left[\frac{SSR}{n-2}\right]=\sigma^2.
$$
Therefore $`SSR/(n-2)`$ is an unbiased estimator of $`\sigma^2`$.
Recall $`B=S_{XY}/S_{XX}\sim N(\beta_1,\sigma^2/S_{XX})`$ and $`A=\bar Y-B\bar x`$.
$$
\boxed{SSR=\frac{S_{XX}S_{YY}-S_{XY}^2}{S_{XX}}}.
$$
$$
A\sim N\left(\beta_0,\frac{\sigma^2\sum_i x_i^2}{nS_{XX}}\right).
$$
### Hypothesis Test for Slope
$$
H_0:\beta_1=0\qquad\text{vs.}\qquad H_1:\beta_1\ne0.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (t Test for Slope)**
	Under $`H_0`$,
	$$
	T=\frac{B}{\sqrt{SSR/[(n-2)S_{XX}]}}\sim t_{n-2}.
	$$
	Two-sided: reject $`H_0`$ if $`|T|>t_{\alpha/2,n-2}`$.
	The p-value is $`2P(T_{n-2}>|t_{\rm obs}|)`$.
</callout>
*Note (from notes).* In simple regression, the test for $`\beta_1=0`$ is related to the zero-correlation test
$$
T=\frac{\sqrt{n-2}\,r}{\sqrt{1-r^2}},
$$
where $`r`$ is the sample correlation coefficient.
**Derivation of slope significance and the correlation test**
Under $`H_0:\beta_1=0`$:
$$
\frac{B-\beta_1}{\sqrt{\sigma^2/S_{XX}}}\sim N(0,1),
\qquad \frac{SSR}{\sigma^2}\sim\chi^2_{n-2}.
$$
$$
\sqrt{\frac{(n-2)S_{XX}}{SSR}}B\sim t_{n-2}.
$$
*Sample mean/correlation relation:* $`H_0:\rho=0\iff H_0:\beta_1=0`$; the t value is the same.
$$
t=\frac{B}{\sqrt{[SSR/(n-2)]/S_{XX}}}
=\frac{S_{XY}}{\sqrt{S_{XX}}}
\frac{\sqrt{n-2}}{\sqrt{S_{YY}-S_{XY}^2/S_{XX}}}
$$
$$
=\frac{S_{XY}}{\sqrt{S_{XX}S_{YY}}}
\frac{\sqrt{n-2}}{\sqrt{1-S_{XY}^2/(S_{XX}S_{YY})}}
=r\frac{\sqrt{n-2}}{\sqrt{1-r^2}}.
$$
### Confidence Interval for the Slope
<callout icon="📘" color="blue_bg">
	**Def. (CI for **$`\beta_1`$**)**
	$$
																					\boxed{\left(
B-t_{\alpha/2,n-2}\sqrt{\frac{SSR}{(n-2)S_{XX}}},\
B+t_{\alpha/2,n-2}\sqrt{\frac{SSR}{(n-2)S_{XX}}}
\right)}.
	$$
</callout>
### Confidence Interval for the Intercept
<callout icon="📘" color="blue_bg">
	**Def. (CI for **$`\beta_0`$**)**
	$$
																					\boxed{\left(
A-t_{\alpha/2,n-2}\sqrt{\frac{SSR}{n-2}\left(\frac1n+\frac{\overline x^2}{S_{XX}}\right)},\
A+t_{\alpha/2,n-2}\sqrt{\frac{SSR}{n-2}\left(\frac1n+\frac{\overline x^2}{S_{XX}}\right)}
\right)}.
	$$
</callout>
## Mean Response and Prediction at a New x
For a given $`x_0`$, the mean response is
$$
E[Y\mid x_0]=\beta_0+\beta_1 x_0.
$$
We want to estimate the mean response $`\beta_0+\beta_1x_0`$ for input $`x_0`$.
$$
E[A+Bx_0]=\beta_0+\beta_1x_0
\quad\text{(unbiased estimator)}.
$$
$$
A+Bx_0=\bar Y-B\bar x+Bx_0
=\frac1n\sum_{i=1}^nY_i
-(\bar x-x_0)\frac{\sum_{i=1}^n(x_i-\bar x)Y_i}{S_{XX}}
$$
$$
=\sum_{i=1}^nY_i\left(\frac1n
-\frac{(x_i-\bar x)(\bar x-x_0)}{S_{XX}}\right).
$$
$$
\operatorname{Var}(A+Bx_0)
=\sum_{i=1}^n\left(\frac1n
-\frac{(x_i-\bar x)(\bar x-x_0)}{S_{XX}}\right)^2
\operatorname{Var}(Y_i)
$$
$$
=\sigma^2\left(\frac1n+\frac{(\bar x-x_0)^2}{S_{XX}}\right).
$$
Thus
$$
\boxed{A+Bx_0\sim
N\left(\beta_0+\beta_1x_0,\
\sigma^2\left(\frac1n+\frac{(\bar x-x_0)^2}{S_{XX}}\right)\right)}.
$$
$$
\frac{A+Bx_0-(\beta_0+\beta_1x_0)}
{\sqrt{\sigma^2(1/n+(\bar x-x_0)^2/S_{XX})}}
\frac1{\sqrt{SSR/[\sigma^2(n-2)]}}
\sim t_{n-2}.
$$
<callout icon="📘" color="blue_bg">
	**Def. (CI for Mean Response)**
	$$
																					\boxed{\left(
A+Bx_0\pm t_{\alpha/2,n-2}
\sqrt{\frac{SSR}{n-2}\left(\frac1n+\frac{(x_0-\overline x)^2}{S_{XX}}\right)}
\right)}.
	$$
</callout>
**Prediction of a future response.** For $`Y_0=\beta_0+\beta_1x_0+\varepsilon_0`$, with $`\varepsilon_0`$ independent of the sample,
$$
Y_0-A-Bx_0\sim N\left(0,\
\sigma^2\left[1+\frac1n+\frac{(x_0-\overline x)^2}{S_{XX}}\right]\right).
$$
<callout icon="📘" color="blue_bg">
	**Def. (Prediction Interval for a Future Response)**
	$$
																					\boxed{\left(
A+Bx_0\pm t_{\alpha/2,n-2}
\sqrt{\frac{SSR}{n-2}\left(1+\frac1n+\frac{(x_0-\overline x)^2}{S_{XX}}\right)}
\right)}.
	$$
</callout>
## Coefficient of Determination
<callout icon="📘" color="blue_bg">
	**Def. (Coefficient of Determination, **$`R^2`$**)**
	Total variation in the response:
	$$
	S_{YY}=\sum_i(Y_i-\overline Y)^2.
	$$
	$$
											S_{YY}=\sum_{i=1}^n(Y_i-\bar Y)^2
=\underbrace{\sum_i(\hat Y_i-\bar Y)^2}_{\text{variation explained by the model}}
+\underbrace{\sum_i(Y_i-\hat Y_i)^2}_{SSR:\text{ variation due to error}}.
	$$
	$`S_{YY}-SSR`$ is the amount of variation in the responses explained by the different input values.
		$$
		R^2=\frac{S_{YY}-SSR}{S_{YY}}=1-\frac{SSR}{S_{YY}}.
		$$
		For simple linear regression,
		$$
		R^2=r^2,\qquad r=\frac{S_{XY}}{\sqrt{S_{XX}S_{YY}}}.
		$$
</callout>
# Analysis of Variance (ANOVA)
## One-Way ANOVA
For $`m`$ independent groups, ask:
$$
H_0:\mu_1=\cdots=\mu_m,
\qquad
H_1:\text{at least two population means differ}.
$$
Let $`X_{ij}=\mu_i+\varepsilon_{ij}`$, independent errors $`\varepsilon_{ij}\sim N(0,\sigma^2)`$.
![](notion-file-block://f38146b1-c5fd-4319-b5f5-538a9a9f40b5/0f8a01f2-1ed8-4962-8b9c-473a60a41efb?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=source_anova_groups_tight.svg)
<callout icon="📘" color="blue_bg">
	**Def. (Total, Between, and Within Sum of Squares)**
	For $`m`$ groups each having $`n`$ observations,
	$$
																					\sum_{i=1}^m\sum_{j=1}^n(X_{ij}-\overline X_{\cdot\cdot})^2
=SS_B+SS_W.
	$$
	$$
																					SS_B=n\sum_{i=1}^m(\overline X_{i\cdot}-\overline X_{\cdot\cdot})^2
\quad\text{(between-group variation)},
	$$
	$$
																					SS_W=\sum_{i=1}^m\sum_{j=1}^n(X_{ij}-\overline X_{i\cdot})^2
\quad\text{(within-group variation)}.
	$$
	Overall mean: $`\overline X_{\cdot\cdot}=(mn)^{-1}\sum_{ij}X_{ij}`$.
</callout>
**Distribution of within-group variation**
$$
\sum_{i=1}^m\sum_{j=1}^n
\frac{(X_{ij}-E[X_{ij}])^2}{\sigma^2}
=\sum_{i=1}^m\sum_{j=1}^n
\frac{(X_{ij}-\mu_i)^2}{\sigma^2}
\sim\chi^2_{mn}.
$$
For one group,
$$
\frac{\sum_{j=1}^n(X_{ij}-\bar X_{i\cdot})^2}{\sigma^2}
\sim\chi^2_{n-1},
$$
as with $`(n-1)S^2/\sigma^2`$.
Thus
$$
\frac{SS_W}{\sigma^2}
=\frac{\sum_{i=1}^m\sum_{j=1}^n(X_{ij}-\bar X_{i\cdot})^2}{\sigma^2}
\sim\chi^2_{m(n-1)}.
$$
$$
\frac{E[SS_W]}{\sigma^2}=m(n-1),
\qquad\boxed{E\left[\frac{SS_W}{m(n-1)}\right]=\sigma^2}.
$$
This is an estimator of $`\sigma^2`$ **regardless of whether **$`H_0`$** is true or not**.
**When **$`H_0`$** is true:** $`\mu_1=\cdots=\mu_m=\mu`$.
$$
\frac{\bar X_{i\cdot}-\mu}{\sigma/\sqrt n}\sim N(0,1),
\qquad
\sum_{i=1}^m\frac{n(\bar X_{i\cdot}-\mu)^2}{\sigma^2}\sim\chi^2_m.
$$
When $`H_0`$ is true, estimator of $`\mu`$ is $`\bar X_{\cdot\cdot}`$.
$$
\frac{SS_B}{\sigma^2}
=\frac{n\sum_{i=1}^m(\bar X_{i\cdot}-\bar X_{\cdot\cdot})^2}{\sigma^2}
\sim\chi^2_{m-1}.
$$
Therefore $`E[SS_B/(m-1)]=\sigma^2`$ is a second estimator of $`\sigma^2`$.
Also,
$$
SS_W=\sum_i\sum_j(X_{ij}-\bar X_{i\cdot})^2
=\sum_i(n-1)S_i^2,
$$
where $`S_i^2`$ is the sample variance of the $`i`$th group.
When $`H_0`$ is true,
$$
\frac{SS_B}{\sigma^2}\sim\chi^2_{m-1},\quad
E\left[\frac{SS_B}{m-1}\right]=\sigma^2.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (One-Way ANOVA F Test)**
	$$
																					F=\frac{SS_B/(m-1)}{SS_W/[m(n-1)]}
\sim F_{m-1,m(n-1)}\qquad(H_0).
	$$
	Reject $`H_0`$ for sufficiently large $`F`$:
	$$
	F>F_{\alpha,m-1,m(n-1)}.
	$$
</callout>
## Multiple Comparisons of Sample Means
When $`H_0`$ of equal means is rejected, we are interested in a comparison of different sample means $`\mu_1,\ldots,\mu_m`$.
There are $`\binom m2`$ simultaneous tests: $`H_0:\mu_1=\mu_2`$, …, $`H_0:\mu_{m-1}=\mu_m`$.
**Ex.** $`m=3`$: test $`H_0:\mu_1=\mu_2`$, $`H_0:\mu_2=\mu_3`$, $`H_0:\mu_1=\mu_3`$.
Assume that we conduct **two independent tests**.
$`\alpha_e`$: overall type I error.
$`\alpha_{I_i}`$: individual type I error of test $`i`$.
$$
\alpha_e=P(\text{falsely reject test 1 or 2})
=1-P(\text{correctly not reject both tests})
$$
$$
=1-P(\text{correctly not reject test 1})P(\text{correctly not reject test 2})
$$
$$
=1-[1-P(\alpha_{I_1})][1-P(\alpha_{I_2})].
$$
Let $`\alpha_{I_1}=\alpha_{I_2}=0.05`$, then $`\alpha_e\approx0.0975`$.
3 tests: $`\alpha_e\approx0.143`$. 4 tests: the overall error increases further.
## ANOVA with Unequal Sample Sizes
Let group $`i`$ contain $`n_i`$ observations, $`i=1,\ldots,m`$, and total $`N=\sum_i n_i`$.
<callout icon="📘" color="blue_bg">
	**Def. (ANOVA Sums of Squares: Unequal Sizes)**
	$$
	SS_W=\sum_{i=1}^m\sum_{j=1}^{n_i}(X_{ij}-\overline X_{i\cdot})^2,
	$$
	$$
																					\overline X_{\cdot\cdot}=\frac1N\sum_i n_i\overline X_{i\cdot},
\qquad
SS_B=\sum_{i=1}^m n_i(\overline X_{i\cdot}-\overline X_{\cdot\cdot})^2.
	$$
</callout>
For equal population variances,
$$
\frac{SS_W}{\sigma^2}\sim\chi^2_{N-m},
\qquad
\frac{SS_B}{\sigma^2}\sim\chi^2_{m-1}\quad\text{under }H_0.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. (ANOVA F Test: Unequal Sample Sizes)**
	$$
																					F=\frac{SS_B/(m-1)}{SS_W/(N-m)}
\sim F_{m-1,N-m}\quad(H_0).
	$$
</callout>
**Relation among tests**
<table fit-page-width="true" header-row="true">
<tr>
<td>Question</td>
<td>Type / Procedure</td>
</tr>
<tr>
<td>Continuous response, categorical group</td>
<td>ANOVA, regression</td>
</tr>
<tr>
<td>Two group means</td>
<td>Two-sample t test</td>
</tr>
<tr>
<td>Difference or relation between quantitative variables</td>
<td>Regression / correlation</td>
</tr>
</table>
# Chi-Square Tests for Categorical Data
## Goodness-of-Fit Test
<callout icon="📘" color="blue_bg">
	**Def. (Goodness-of-Fit Test)**
	Test whether an assumed probability mechanism or model is appropriate for observed categorical data.
	For random sample $`Y_1,\ldots,Y_n`$ taking values $`1,\ldots,k`$:
	$$
	H_0:P(Y_i=j)=p_j,\quad j=1,\ldots,k,
	$$
	$$
	H_1:P(Y_i=j)\ne p_j\quad\text{for some }j.
	$$
	Observed frequency $`X_j`$ is the number of $`Y_i`$ equal to $`j`$; expected frequency under $`H_0`$ is $`np_j`$.
	$$
	T=\sum_{j=1}^k\frac{(X_j-np_j)^2}{np_j}.
	$$
	Under $`H_0`$, $`T\overset{\rm approx}{\sim}\chi^2_{k-1}`$ for sufficiently large expected cell counts.
</callout>
<callout icon="📜" color="yellow_bg">
	**Prop. (Two-Category Chi-Square Statistic)**
	For $`k=2`$, $`X_1+X_2=n`$ and $`p_1+p_2=1`$,
	$$
																					T=\frac{(X_1-np_1)^2}{np_1}+
\frac{(X_2-np_2)^2}{np_2}
	$$
	$$
																					=(X_1-np_1)^2\left(\frac1{np_1}+\frac1{n(1-p_1)}\right)
=\frac{(X_1-np_1)^2}{np_1(1-p_1)}.
	$$
	Thus $`T=Z^2`$, where $`Z`$ is the approximate normal statistic for a single population proportion.
</callout>
## Tests of Independence in Contingency Tables
Suppose each unit is classified by two categorical characteristics $`X`$ and $`Y`$.
Let $`X`$ have categories $`1,\ldots,r`$ and $`Y`$ categories $`1,\ldots,c`$.
<callout icon="📘" color="blue_bg">
	**Def. (Independence in a Contingency Table)**
	$$
																					p_{ij}=P(X=i,Y=j),\quad
p_{i\cdot}=P(X=i),\quad p_{\cdot j}=P(Y=j).
	$$
	Under the independence null:
	$$
	H_0:p_{ij}=p_{i\cdot}p_{\cdot j}\quad\text{for every }i,j.
	$$
	$`H_1`$: at least one pair is associated (not independent).
</callout>
**Counts and expected frequencies.** $`N_{ij}`$ is the number in cell $`(i,j)`$, and
$$
\hat p_{i\cdot}=\frac{N_{i\cdot}}N,\quad
\hat p_{\cdot j}=\frac{N_{\cdot j}}N,
\quad E_{ij}=N\hat p_{i\cdot}\hat p_{\cdot j}
=\frac{N_{i\cdot}N_{\cdot j}}N.
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>$`X\backslash Y`$</td>
<td>1</td>
<td>2</td>
<td>…</td>
<td>Total</td>
</tr>
<tr>
<td>1</td>
<td>$`N_{11}`$</td>
<td>$`N_{12}`$</td>
<td>…</td>
<td>$`N_{1\cdot}`$</td>
</tr>
<tr>
<td>2</td>
<td>$`N_{21}`$</td>
<td>$`N_{22}`$</td>
<td>…</td>
<td>$`N_{2\cdot}`$</td>
</tr>
<tr>
<td>Total</td>
<td>$`N_{\cdot1}`$</td>
<td>$`N_{\cdot2}`$</td>
<td>…</td>
<td>$`N`$</td>
</tr>
</table>
<callout icon="📜" color="yellow_bg">
	**Thm. (Chi-Square Test of Independence)**
	$$
																					T=\sum_{i=1}^r\sum_{j=1}^c
\frac{(N_{ij}-E_{ij})^2}{E_{ij}}
\overset{\rm approx}{\sim}\chi^2_{(r-1)(c-1)}
\quad(H_0).
	$$
	Reject independence for sufficiently large $`T`$.
	For a $`2\times2`$ table, the chi-square test corresponds asymptotically to a two-sample population proportion test.
</callout>