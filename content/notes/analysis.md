<table_of_contents color="gray"/>
# Chapter 2. Basic Topology
<callout icon="📜" color="yellow_bg">
	**Thm. 2.12.**
	Countable union of countable sets is countable.
</callout>
<details>
<summary>Proof</summary>
	Enumerate the elements diagonally, e.g. $`x_{11},x_{12},x_{13},\ldots`$, $`x_{21},x_{22},x_{23},\ldots`$, …
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.13.**
	Set of finite tuples whose elements are in a countable set is countable: $`(a_1,\ldots,a_n)`$.
</callout>
<details>
<summary>Proof</summary>
	Induction. Let $`B_n`$ be the set of n-tuples. The $`(n+1)`$-tuples are obtained from $`B_n\times B_1`$; apply Thm. 2.12.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	The set of all rational numbers is countable.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.14.**
	Let $`A`$ be the set of all sequences whose elements are 0 or 1. Then $`A`$ is uncountable.
</callout>
<details>
<summary>Proof</summary>
	Let $`E=\{s_1,s_2,\ldots\}`$ be a countable subset of $`A`$. Construct $`s`$ such that its n-th digit differs from the n-th digit of $`s_n`$. Then $`s\notin E`$; every countable subset of $`A`$ is proper.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Convex).**
	$`E\subset\mathbb{R}^k`$ is convex if, for $`x,y\in E`$ and $`0\le\lambda\le1`$,
	$$
	\lambda x+(1-\lambda)y\in E.
	$$
</callout>
<callout icon="📘" color="blue_bg">
	**Definitions.**
	- **Limit point:** $`p`$ is a limit point of $`E`$ if $`N_r^*(p)\cap E\ne\varnothing`$ for every $`r>0`$.
	- **Closed:** every limit point of $`E`$ belongs to $`E`$.
	- **Interior point:** some neighborhood $`N_r(p)`$ is contained in $`E`$.
	- **Open:** every point is an interior point.
	- **Perfect:** closed, and every point is a limit point.
	- **Dense:** every point is a limit point or a point of $`E`$ (with respect to the ambient space).
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.20.**
	A neighborhood of a limit point contains infinitely many points of the set.
</callout>
<details>
<summary>Proof</summary>
	If it contained only finitely many other points $`q_m`$, choose a smaller radius using $`\min d(p,q_m)`$, a contradiction.
</details>
**Ex.** $`\mathbb{Z}`$ is closed, not open.
<callout icon="📘" color="blue_bg">
	**Def. (Closure).**
	$`E'`$: set of all limit points of $`E`$ in $`X`$. The closure is $`\overline E=E\cup E'`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.27.**
	- (a) $`\overline E`$ is closed. If $`p\notin\overline E`$, a neighborhood of $`p`$ does not meet $`E`$, so $`(\overline E)^c`$ is open.
	- (b) $`E=\overline E\iff E`$ is closed.
	- (c) $`\overline E\subset F`$ for every closed set $`F`$ containing $`E`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.28.**
	If $`E`$ is bounded above and $`y=\sup E`$, then $`y\in\overline E`$ (and $`y\in E`$ if $`E`$ is closed).
</callout>
<details>
<summary>Proof</summary>
	For each $`h>0`$ there is $`x\in E`$ with $`y-h<x\le y`$, otherwise $`y-h`$ is an upper bound. Thus $`y`$ lies in the closure.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.30.**
	Let $`Y\subset X`$ and $`E\subset Y`$. Then $`E`$ is open relative to $`Y`$ iff $`E=Y\cap G`$ for some open $`G`$ in $`X`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.33.**
	Let $`K\subset Y\subset X`$. Then $`K`$ is compact relative to $`X`$ iff it is compact relative to $`Y`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.34.**
	Compact subsets of metric spaces are closed.
</callout>
<details>
<summary>Proof</summary>
	Fix $`p\in X\setminus K`$. For $`q\in K`$, take neighborhoods $`V_q,W_q`$ of $`p,q`$ of radius $`d(p,q)/2`$. Compactness gives a finite subcover of $`K`$ by the $`W_q`$. The intersection of the corresponding $`V_q`$ is a neighborhood of $`p`$ disjoint from $`K`$. Hence $`K^c`$ is open.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.35.**
	Closed subsets of compact sets are compact.
</callout>
<details>
<summary>Proof</summary>
	If $`F\subset K`$ is closed and $`\{V_\alpha\}`$ covers $`F`$, then $`F^c\cup\{V_\alpha\}`$ is an open cover of $`K`$. A finite subcover of $`K`$ yields a finite cover of $`F`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.36.**
	If every finite subcollection of compact sets $`\{K_\alpha\}`$ has nonempty intersection, then $`\bigcap_\alpha K_\alpha\ne\varnothing`$.
</callout>
<details>
<summary>Proof</summary>
	Fix $`K_1`$, and set $`G_\alpha=K_\alpha^c`$. If the intersection were empty, the $`G_\alpha`$ would give an open cover of $`K_1`$. A finite subcover contradicts the finite intersection property.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	If $`K_1\supset K_2\supset\cdots`$ is a sequence of nonempty compact sets, then $`\bigcap_nK_n\ne\varnothing`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.37.**
	If $`E`$ is an infinite subset of a compact set $`K`$, then $`E`$ has a limit point in $`K`$.
</callout>
<details>
<summary>Proof</summary>
	Otherwise each $`q\in K`$ would have a neighborhood containing at most one point of $`E`$, and no finite subcollection could cover $`E`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.38.**
	If $`\{I_n\}`$ is a sequence of nested intervals in $`\mathbb{R}^1`$ with $`I_n\supset I_{n+1}`$, then $`\bigcap_nI_n`$ is nonempty. \[In the source proof, the intervals are bounded closed intervals $`[a_n,b_n]`$.\]
</callout>
<details>
<summary>Proof</summary>
	Put $`x=\sup_n a_n`$. Since $`a_n\le a_{n+m}\le b_{n+m}\le b_n`$ for each $`m`$, we have $`x\in I_n`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.40.**
	Every $`k`$-cell is compact.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.41.**
	For $`E\subset\mathbb{R}^k`$, the following are equivalent:
	- (a) $`E`$ is closed and bounded.
	- (b) $`E`$ is compact.
	- (c) Every infinite subset of $`E`$ has a limit point in $`E`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.42 (Weierstrass).**
	Every bounded infinite subset of $`\mathbb{R}^k`$ has a limit point in $`\mathbb{R}^k`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.43.**
	A perfect set $`P`$ in $`\mathbb{R}^k`$ is uncountable.
</callout>
<details>
<summary>Proof</summary>
	Suppose $`P=\{x_1,x_2,\ldots\}`$. Construct neighborhoods $`V_n`$ such that $`\overline{V}_{n+1}\subset V_n`$, $`x_n\notin\overline{V}_{n+1}`$, and $`V_{n+1}\cap P\ne\varnothing`$. Set $`K_n=\overline V_n\cap P`$. Each $`K_n`$ is nonempty compact, so $`\bigcap_nK_n\ne\varnothing`$, while no $`x_n`$ belongs to the intersection: contradiction.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	The set of all real numbers is uncountable.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Separated).**
	Sets $`A,B`$ are separated if $`A\cap\overline B=\varnothing`$ and $`\overline A\cap B=\varnothing`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Connected).**
	$`E`$ is connected if it cannot be written as a union of two nonempty separated sets.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 2.47.**
	A subset $`E`$ of the real line is connected iff whenever $`x,y\in E`$ and $`x<z<y`$, then $`z\in E`$.
</callout>
# Chapter 3. Numerical Sequences and Series
<callout icon="📘" color="blue_bg">
	**Def. (Convergence).**
	In metric space $`X`$, $`\{p_n\}`$ converges if there exists $`p\in X`$ such that for every $`\varepsilon>0`$ there is $`N`$ for which $`n\ge N`$ implies $`d(p_n,p)<\varepsilon`$.
	$$
	p_n\to p,\qquad \lim_{n\to\infty}p_n=p.
	$$
</callout>
**Range** of $`\{p_n\}`$: the set of all points $`p_n`$.
<callout icon="📜" color="yellow_bg">
	**Thm. 3.2.**
	- (a) $`p_n\to p`$ iff every neighborhood of $`p`$ contains all but finitely many $`p_n`$.
	- (b) If $`p_n\to p`$ and $`p_n\to p'`$, then $`p=p'`$ (since $`d(p,p')=0`$).
	- (c) Every convergent sequence is bounded.
	- (d) If $`E\subset X`$ and $`p`$ is a limit point of $`E`$, then some sequence $`\{p_n\}`$ in $`E`$ converges to $`p`$.
</callout>
<details>
<summary>Proof (d)</summary>
	Construct $`p_n\in E`$ such that $`d(p_n,p)<1/n`$. Given $`\varepsilon>0`$, choose $`N`$ with $`1/N<\varepsilon`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Subsequential limit).**
	If the subsequence $`\{p_{n_i}\}`$ converges, its limit is called a subsequential limit of $`\{p_n\}`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.6.**
	- (a) A sequence in a compact metric space $`X`$ has a subsequence converging to a point of $`X`$.
	- (b) Every bounded sequence in $`\mathbb{R}^k`$ contains a convergent subsequence.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.7.**
	The subsequential limits of $`\{p_n\}`$ in metric space $`X`$ form a closed subset of $`X`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Cauchy sequence).**
	$`\{p_n\}`$ is Cauchy if for every $`\varepsilon>0`$, there exists $`N`$ such that $`d(p_n,p_m)<\varepsilon`$ whenever $`n,m\ge N`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.10.**
	- (a) $`\operatorname{diam}E=\operatorname{diam}\overline E`$.
	- (b) If $`K_n\supset K_{n+1}`$ are compact and $`\lim_{n\to\infty}\operatorname{diam}K_n=0`$, then $`\bigcap_nK_n`$ consists of one point.
</callout>
<details>
<summary>Proof (a)</summary>
	$`\operatorname{diam}E\le\operatorname{diam}\overline E`$ is trivial. For $`p,q\in\overline E`$, choose $`p',q'\in E`$ within $`\varepsilon`$ of $`p,q`$. Then $`\operatorname{diam}\overline E\le2\varepsilon+\operatorname{diam}E`$.
</details>
<details>
<summary>Proof (b)</summary>
	If the intersection had more than one point, its diameter would be positive, a contradiction.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.11.**
	- (a) Every convergent sequence is Cauchy.
	- (b) Every Cauchy sequence in a compact metric space converges to some point of the space.
	- (c) In $`\mathbb{R}^k`$, every Cauchy sequence converges.
</callout>
*Note.* The definition of convergence includes the limit point $`p`$; the definition of Cauchy does not.
<details>
<summary>Proof (b)</summary>
	Put $`E_N=\{p_N,p_{N+1},\ldots\}`$. Then
	$$
		\lim_{N\to\infty}\operatorname{diam}\overline E_N=0,\qquad
\overline E_N\supset\overline E_{N+1}.
	$$
	Each $`\overline E_N`$ is compact (closed subset of a compact set). By Thm. 3.10(b), there is a unique $`p\in X`$ contained in all $`\overline E_N`$. For every $`\varepsilon>0`$, choose $`N_0`$ so that $`\operatorname{diam}\overline E_N<\varepsilon`$ for $`N\ge N_0`$. Since $`p,p_n\in\overline E_N`$ for $`n\ge N`$, $`d(p,p_n)<\varepsilon`$ and $`p_n\to p`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Complete).**
	A metric space in which every Cauchy sequence converges.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.14.**
	A monotone sequence $`\{s_n\}`$ converges iff it is bounded.
</callout>
<details>
<summary>Proof (⇐)</summary>
	Let $`s=\sup\{s_n\}`$ for an increasing sequence. Given $`\varepsilon>0`$, find $`s_N`$ with $`s-\varepsilon<s_N\le s`$. By monotonicity, for $`n\ge N`$,
	$$
	s-\varepsilon<s_n\le s.
	$$
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Divergence to +∞).**
	If for every $`M`$ there is $`N`$ such that $`n\ge N`$ implies $`s_n\ge M`$, then $`s_n\to+\infty`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Upper and lower limits).**
	$$
		s^*=\limsup_{n\to\infty}s_n,\qquad
s_*=\liminf_{n\to\infty}s_n.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.17.**
	Let $`E`$ be the set of all subsequential limits of $`\{s_n\}`$, allowing $`\pm\infty`$.
	- (a) $`s^*\in E`$.
	- (b) If $`x>s^*`$, then for some $`N`$, $`n\ge N`$ implies $`s_n<x`$.
</callout>
<details>
<summary>Proof (a)</summary>
	If $`s^*=+\infty`$, the set of subsequential limits is unbounded above. If $`s^*`$ is real, the set $`E`$ is bounded and closed (by Thm. 3.7).
</details>
**Ex.** 
$$
\lim_{n\to\infty}s_n=s
\iff
\limsup_{n\to\infty}s_n=\liminf_{n\to\infty}s_n=s.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. 3.20.**
	- (a) $`\displaystyle\lim_{n\to\infty}\sqrt[n]{n}=1`$.
	- (b) $`\displaystyle\lim_{n\to\infty}\frac{n^\alpha}{(1+p)^n}=0`$ for real $`\alpha`$ and $`p>0`$.
</callout>
<details>
<summary>Proof (a)</summary>
	Set $`x_n=\sqrt[n]{n}-1`$. From $`n=(1+x_n)^n\ge\frac{n(n-1)}2x_n^2`$,
	$$
	0\le x_n\le\sqrt{\frac{2}{n-1}}.
	$$
</details>
<details>
<summary>Proof (b)</summary>
	Choose an integer $`k>\alpha`$, $`k>0`$. For $`n>2k`$,
	$$
		(1+p)^n>\binom nk p^k
=\frac{n(n-1)\cdots(n-k+1)}{k!}p^k
>\frac{n^kp^k}{2^kk!}.
	$$
	Hence $`0<\frac{n^\alpha}{(1+p)^n}<\frac{2^kk!}{p^k}n^{\alpha-k}\to0`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Series).**
	$`\displaystyle\sum_{n=1}^{\infty}a_n=s`$: $`s`$ is the sum of the series.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.22 (Cauchy criterion).**
	A series $`\sum a_n`$ converges iff for every $`\varepsilon>0`$ there exists $`N`$ such that whenever $`m\ge n\ge N`$,
	$$
	\left|\sum_{k=n}^{m}a_k\right|\le\varepsilon.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.23.**
	If $`\sum a_n`$ converges, then $`\lim_{n\to\infty}a_n=0`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.24 (Monotone convergence).**
	A series of nonnegative terms converges iff its partial sums form a bounded sequence.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.25 (Comparison test).**
	- (a) If $`|a_n|\le c_n`$ for $`n\ge N_0`$ and $`\sum c_n`$ converges, then $`\sum a_n`$ converges.
	- (b) If $`a_n\ge d_n\ge0`$ for $`n\ge N_0`$ and $`\sum d_n`$ diverges, then $`\sum a_n`$ diverges.
</callout>
<details>
<summary>Proof (a)</summary>
	By the Cauchy criterion,
	$$
		\left|\sum_{k=n}^m a_k\right|
\le\sum_{k=n}^m|a_k|
\le\sum_{k=n}^m c_k\le\varepsilon.
	$$
</details>
<details>
<summary>Proof (b)</summary>
	By Thm. 3.24.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.27 (Cauchy condensation test).**
	If $`a_1\ge a_2\ge\cdots\ge0`$, then
	$$
		\sum_{n=1}^{\infty}a_n\text{ converges}
\iff
\sum_{k=0}^{\infty}2^ka_{2^k}\text{ converges}.
	$$
</callout>
<details>
<summary>Proof</summary>
	Put $`s_n=a_1+\cdots+a_n`$ and $`t_k=a_1+2a_2+\cdots+2^ka_{2^k}`$. For $`n<2^k`$, $`s_n\le t_k`$; for $`n>2^k`$, $`2s_n\ge t_k`$. Thus these two sequences are both bounded or both unbounded. Apply Thm. 3.24.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.28.**
	$$
	\sum\frac{1}{n^p}\text{ converges if }p>1.
	$$
</callout>
<details>
<summary>Proof</summary>
	By the condensation test, consider
	$$
		\sum_{k=0}^{\infty}2^k\frac1{2^{kp}}
=\sum_{k=0}^{\infty}2^{(1-p)k}.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.29.**
	$$
		\sum_{n=2}^{\infty}\frac1{n(\log n)^p}
\text{ converges if }p>1.
	$$
</callout>
<details>
<summary>Proof</summary>
	Consider $`\displaystyle\sum2^k\frac1{2^k(\log 2^k)^p}`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def.**
	$$
	e=\sum_{n=0}^{\infty}\frac{1}{n!}.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.31.**
	$$
	\lim_{n\to\infty}\left(1+\frac1n\right)^n=e.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.32.**
	$`e`$ is irrational.
</callout>
<details>
<summary>Proof</summary>
	Write $`s_n=\sum_{k=0}^n1/k!`$. Then
	$$
		0<e-s_n=\frac1{(n+1)!}+\cdots
<\frac1{(n+1)!}\left(1+\frac1{n+1}+\frac1{(n+1)^2}+\cdots\right)
=\frac1{n!\,n}.
	$$
	Suppose $`e=p/q`$. For sufficiently large $`n`$,
	$$
	0<q!(e-s_n)<1.
	$$
	But both $`q!s_n`$ and $`q!e`$ are integers (taking $`n=q`$), a contradiction.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.33 (Root test).**
	Given $`\sum a_n`$, put
	$$
	\alpha=\limsup_{n\to\infty}\sqrt[n]{|a_n|}.
	$$
	- (a) If $`\alpha<1`$, the series converges.
	- (b) If $`\alpha>1`$, the series diverges.
	- (c) If $`\alpha=1`$, no information; for example, $`\sum 1/n`$ and $`\sum1/n^2`$.
</callout>
<details>
<summary>Proof (a)</summary>
	Choose $`\alpha<\beta<1`$ and $`N`$ with $`\sqrt[n]{|a_n|}<\beta`$ for $`n\ge N`$; hence $`|a_n|<\beta^n`$.
</details>
<details>
<summary>Proof (b)</summary>
	Choose a subsequence $`\{n_k\}`$ with $`\sqrt[n_k]{|a_{n_k}|}\to\alpha>1`$. Then $`|a_{n_k}|>1`$ eventually, so $`a_n\not\to0`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.34 (Ratio test).**
	- (a) $`\sum a_n`$ converges if $`\displaystyle\limsup_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|<1`$.
	- (b) It diverges if $`\left|\frac{a_{n+1}}{a_n}\right|\ge1`$ for all $`n\ge n_0`$.
</callout>
<details>
<summary>Proof (a)</summary>
	For some $`\beta<1`$ and sufficiently large $`N`$,
	$$
		|a_{n+1}|<\beta|a_n|,\quad
|a_{n+2}|<\beta^2|a_n|,\quad
|a_{n+k}|<|a_n|\beta^k.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.37.**
	For any positive sequence $`\{c_n\}`$,
	$$
		\liminf_{n\to\infty}\frac{c_{n+1}}{c_n}
\le\liminf_{n\to\infty}\sqrt[n]{c_n},
\qquad
\limsup_{n\to\infty}\sqrt[n]{c_n}
\le\limsup_{n\to\infty}\frac{c_{n+1}}{c_n}.
	$$
</callout>
<details>
<summary>Proof</summary>
	Let $`\alpha=\limsup c_{n+1}/c_n`$. For $`\beta>\alpha`$, there exists $`N`$ such that $`c_{n+1}/c_n\le\beta`$ for all $`n\ge N`$. Iterating,
	$$
		c_n\le c_N\beta^{n-N},
\qquad
\sqrt[n]{c_n}\le\sqrt[n]{c_N\beta^{-N}}\cdot\beta.
	$$
	Hence $`\limsup\sqrt[n]{c_n}\le\beta`$, then let $`\beta\downarrow\alpha`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Power series).**
	$`\displaystyle\sum_{n=0}^{\infty}c_nz^n`$ is a power series; convergence is considered in the circle.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.39.**
	Let
	$$
		\alpha=\limsup_{n\to\infty}\sqrt[n]{|c_n|},
\qquad R=\frac1\alpha.
	$$
	Then $`\sum c_nz^n`$ converges if $`|z|<R`$ and diverges if $`|z|>R`$.
</callout>
<details>
<summary>Proof</summary>
	Use the root test.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.41 (Partial summation formula).**
	Let $`A_n=\sum_{k=0}^na_k`$ and $`A_{-1}=0`$. Then
	$$
		\sum_{n=p}^q a_nb_n
=\sum_{n=p}^{q-1}A_n(b_n-b_{n+1})
+A_qb_q-A_{p-1}b_p.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.42.**
	If (a) $`\{A_n\}`$ is bounded; (b) $`b_0\ge b_1\ge\cdots`$; and (c) $`b_n\to0`$, then $`\sum a_nb_n`$ converges.
</callout>
<details>
<summary>Proof</summary>
	For $`|A_n|\le M`$ and sufficiently large $`p`$ with $`b_p\le\varepsilon/(2M)`$, the partial summation formula gives
	$$
		\left|\sum_{n=p}^q a_nb_n\right|
\le M\left(\sum_{n=p}^{q-1}(b_n-b_{n+1})+b_q+b_p\right)
=2Mb_p\le\varepsilon.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.43 (Alternating series).**
	Suppose $`|c_1|\ge|c_2|\ge\cdots`$, $`c_{2m-1}\ge0`$, $`c_{2m}\le0`$, and $`c_n\to0`$. Then $`\sum c_n`$ converges.
</callout>
*Relation in notes:* $`a_n=(-1)^{n+1}`$, $`b_n=|c_n|`$.
<callout icon="📜" color="yellow_bg">
	**Thm. 3.44.**
	Suppose $`R=1`$, $`c_0\ge c_1\ge\cdots`$, and $`c_n\to0`$. Then $`\sum c_nz^n`$ converges at every point on $`|z|=1`$ except $`z=1`$.
</callout>
*Relation in notes:* $`a_n=z^n`$, $`b_n=c_n`$.
<callout icon="📘" color="blue_bg">
	**Def. (Absolute convergence).**
	$`\sum a_n`$ converges absolutely if $`\sum|a_n|`$ converges.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.45.**
	If $`\sum a_n`$ converges absolutely, then $`\sum a_n`$ converges.
</callout>
<details>
<summary>Proof</summary>
	By Cauchy,
	$$
		\left|\sum_{k=n}^m a_k\right|
\le\sum_{k=n}^m|a_k|.
	$$
</details>
**Ex.** $`\sum(-1)^n/n`$ converges but not absolutely: it converges nonabsolutely.
<callout icon="📘" color="blue_bg">
	**Def. (Product of series).**
	The Cauchy product of $`\sum a_n`$ and $`\sum b_n`$ has coefficients
	$$
	c_n=\sum_{k=0}^n a_kb_{n-k}.
	$$
</callout>
*Note.* A product of two convergent series may diverge.
<callout icon="📜" color="yellow_bg">
	**Thm. 3.50.**
	If (1) $`\sum a_n`$ converges absolutely, (2) $`\sum a_n=A`$ and $`\sum b_n=B`$, (3) $`c_n=\sum_{k=0}^na_kb_{n-k}`$, then $`\sum c_n=AB`$.
</callout>
<details>
<summary>Proof</summary>
	Put $`B_n=\sum_{k=0}^n b_k`$, $`\beta_n=B_n-B`$. For partial sums $`C_n=\sum_{k=0}^n c_k`$,
	$$
		C_n=a_0B_n+a_1B_{n-1}+\cdots+a_nB_0
=A_nB+\underbrace{a_0\beta_n+\cdots+a_n\beta_0}_{\gamma_n}.
	$$
	Let $`\alpha=\sum|a_n|`$. As $`\beta_n\to0`$, choose $`N`$ so $`|\beta_n|\le\varepsilon`$ for $`n\ge N`$. Then
	$$
		|\gamma_n|
\le|\beta_0a_n+\cdots+\beta_Na_{n-N}|+
\varepsilon\alpha.
	$$
	Thus $`\limsup_{n\to\infty}|\gamma_n|\le\varepsilon\alpha`$, yielding $`C_n\to AB`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.51.**
	If $`\sum a_n=A`$, $`\sum b_n=B`$, and their Cauchy product $`\sum c_n=C`$ also converges, then $`C=AB`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Rearrangement).**
	Let $`\{k_n\}`$ be a bijection of the positive integers and $`a'_n=a_{k_n}`$. Then $`\sum a'_n`$ is a rearrangement of $`\sum a_n`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.54.**
	If $`\sum a_n`$ converges nonabsolutely and $`-\infty\le\alpha\le\beta\le\infty`$, there is a rearrangement $`\sum a'_n`$ such that
	$$
		\liminf_{n\to\infty}s'_n=\alpha,\qquad
\limsup_{n\to\infty}s'_n=\beta.
	$$
</callout>
<details>
<summary>Proof</summary>
	Set
	$$
		p_n=\frac{|a_n|+a_n}{2},\qquad
q_n=\frac{|a_n|-a_n}{2},
\qquad a_n=p_n-q_n,\quad |a_n|=p_n+q_n.
	$$
	Both the positive-term and negative-term parts have divergent sums. List the positive terms as $`P_1,P_2,\ldots`$ and the absolute values of the negative terms as $`Q_1,Q_2,\ldots`$. Choose $`\{\alpha_n\},\{\beta_n\}`$ with $`\alpha_n\to\alpha`$, $`\beta_n\to\beta`$ and $`\alpha_n<\beta_n`$. Build partial sums by successively adding positive terms until a target $`\beta_n`$ is exceeded, then subtracting negative terms until a target $`\alpha_n`$ is passed. The overshoots tend to zero since $`a_n\to0`$, giving the required liminf and limsup.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 3.55.**
	If $`\sum a_n`$ converges absolutely, every rearrangement $`\sum a'_n`$ converges to the same sum.
</callout>
<details>
<summary>Proof</summary>
	Using the Cauchy criterion, show that the original and rearranged partial sums satisfy $`|s_n-s'_m|\le\varepsilon`$ once both include all the initial terms and the absolute tail sum is small.
</details>
# Chapter 4. Continuity
<callout icon="📘" color="blue_bg">
	**Def. (Limit).**
	Let $`f:E\subset X\to Y`$ and let $`p`$ be a limit point of $`E`$. Then $`\lim_{x\to p}f(x)=q`$ if $`q\in Y`$ and for every $`\varepsilon>0`$ there exists $`\delta>0`$ such that
	$$
		d_Y(f(x),q)<\varepsilon
\quad\text{whenever}\quad
0<d_X(x,p)<\delta,\ x\in E.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.2.**
	$$
		\lim_{x\to p}f(x)=q
\iff
\lim_{n\to\infty}f(p_n)=q
	$$
	for every sequence $`\{p_n\}`$ in $`E`$ with $`p_n\ne p`$ and $`p_n\to p`$.
</callout>
<details>
<summary>Proof (⇐)</summary>
	The note uses a sequence of radii $`\delta_n=1/n`$ to argue by contradiction.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	If $`f`$ has a limit at $`p`$, this limit is unique.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Continuous).**
	$`f`$ is continuous at $`p`$ if for every $`\varepsilon>0`$ there is $`\delta>0`$ such that
	$$
		d_Y(f(x),f(p))<\varepsilon
\quad\text{for all }x\text{ with }d_X(x,p)<\delta.
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.6.**
	Suppose $`p`$ is a limit point of $`E`$. Then $`f`$ is continuous at $`p`$ iff
	$$
	\lim_{x\to p}f(x)=f(p).
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.8.**
	The mapping $`f:X\to Y`$ is continuous iff $`f^{-1}(V)`$ is open in $`X`$ for every open $`V`$ in $`Y`$.
</callout>
<details>
<summary>Proof (⇒)</summary>
	If $`V`$ is open in $`Y`$ and $`p\in X`$ satisfies $`f(p)\in V`$, some $`\varepsilon>0`$ has $`B_\varepsilon(f(p))\subset V`$. By continuity, there is $`\delta>0`$ so $`d_X(x,p)<\delta`$ implies $`d_Y(f(x),f(p))<\varepsilon`$. Thus $`p`$ is interior to $`f^{-1}(V)`$.
</details>
<details>
<summary>Proof (⇐)</summary>
	Given $`p\in X`$ and $`\varepsilon>0`$, set $`V=B_\varepsilon(f(p))`$. Since $`V`$ is open, so is $`f^{-1}(V)`$. Therefore some $`\delta>0`$ has $`B_\delta(p)\subset f^{-1}(V)`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	$`f`$ is continuous iff $`f^{-1}(C)`$ is closed for every closed $`C`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (Bounded function).**
	There exists $`M`$ such that $`|f(x)|\le M`$ for all $`x`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.14.**
	If $`f:X\to Y`$ is a continuous mapping and $`X`$ is compact, then $`f(X)`$ is compact.
</callout>
<details>
<summary>Proof</summary>
	If $`\{V_\alpha\}`$ is an open cover of $`f(X)`$, then $`\{f^{-1}(V_\alpha)\}`$ is an open cover of $`X`$ by Thm. 4.8. Compactness gives a finite subcover. Therefore the corresponding $`V_{\alpha_1},\ldots,V_{\alpha_n}`$ cover $`f(X)`$.
</details>
*Note.* $`f^{-1}(f(E))\supset E`$.
<callout icon="📜" color="yellow_bg">
	**Thm. 4.16.**
	Suppose $`f`$ is a continuous real function on a compact metric space $`X`$. Let
	$$
	M=\sup_{p\in X}f(p),\qquad m=\inf_{p\in X}f(p).
	$$
	Then some $`p,q`$ satisfy $`f(p)=M`$ and $`f(q)=m`$: $`f`$ has a maximum and a minimum.
</callout>
<details>
<summary>Proof</summary>
	By Thm. 4.14, $`f(X)`$ is compact, hence closed and bounded in $`\mathbb{R}`$. By Thm. 2.28, $`f(X)`$ contains $`M,m`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.17.**
	If $`f`$ is a continuous one-to-one mapping of compact $`X`$ onto $`Y`$, then $`f^{-1}`$ is continuous.
</callout>
<details>
<summary>Proof</summary>
	By Thm. 4.8, it suffices to show $`f(V)`$ is open in $`Y`$ for every open $`V`$ of $`X`$. The set $`V^c`$ is closed, thus compact. So $`f(V^c)`$ is compact and closed. Because $`f`$ is bijective, $`f(V)=(f(V^c))^c`$, hence $`f(V)`$ is open.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Uniformly continuous).**
	$`f:X\to Y`$ is uniformly continuous if for every $`\varepsilon>0`$ there exists $`\delta>0`$ such that for all $`p,q\in X`$,
	$$
		d_X(p,q)<\delta\quad\Longrightarrow\quad
d_Y(f(p),f(q))<\varepsilon.
	$$
</callout>
*Note.* Uniform continuity is a property of the function on a set, whereas continuity can be defined at a single point.
<callout icon="📜" color="yellow_bg">
	**Thm. 4.19.**
	If $`f:X\to Y`$ is continuous and $`X`$ is compact, then $`f`$ is uniformly continuous on $`X`$ (the two continuity concepts agree on compact sets).
</callout>
<details>
<summary>Proof</summary>
	Fix $`\varepsilon>0`$. For each $`p\in X`$, continuity yields $`\varphi(p)>0`$ so that $`d_X(p,q)<\varphi(p)`$ implies $`d_Y(f(p),f(q))<\varepsilon/2`$. Let
	$$
	J(p)=\{q\in X:d_X(p,q)<\tfrac12\varphi(p)\}.
	$$
	By compactness, $`X`$ is covered by finitely many $`J(p_1),\ldots,J(p_n)`$. Put
	$$
	\delta=\tfrac12\min\{\varphi(p_1),\ldots,\varphi(p_n)\}.
	$$
	If $`d_X(p,q)<\delta`$, choose $`m`$ with $`p\in J(p_m)`$. Then
	$$
		d_X(q,p_m)\le d_X(p,q)+d_X(p,p_m)
<\delta+\tfrac12\varphi(p_m)\le\varphi(p_m).
	$$
	Hence
	$$
		d_Y(f(p),f(q))
\le d_Y(f(p),f(p_m))+d_Y(f(q),f(p_m))<\varepsilon.
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.22.**
	If $`f`$ is continuous and $`E`$ is connected, then $`f(E)`$ is connected.
</callout>
<details>
<summary>Proof</summary>
	Suppose $`f(E)=A\cup B`$ with $`A,B`$ separated. Put $`G=E\cap f^{-1}(A)`$ and $`H=E\cap f^{-1}(B)`$. Then $`E=G\cup H`$. By continuity and separation, $`\overline G\cap H=\varnothing`$ and $`G\cap\overline H=\varnothing`$, contradicting connectedness.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.23 (Intermediate Value Theorem).**
	If $`f`$ is a continuous real function on $`[a,b]`$, $`f(a)<f(b)`$, and $`f(a)<c<f(b)`$, then there exists $`x\in(a,b)`$ with $`f(x)=c`$.
</callout>
<details>
<summary>Proof</summary>
	$`[a,b]`$ is connected, so $`f([a,b])`$ is connected. Apply Thm. 2.47.
</details>
<callout icon="📘" color="blue_bg">
	**Discontinuity.**
	- **First kind:** discontinuous, but the one-sided limits $`f(x+)`$ and $`f(x-)`$ exist.
	- **Second kind:** otherwise.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.29.**
	If $`f`$ is monotonically increasing on $`(a,b)`$, then $`f(x+)`$ and $`f(x-)`$ exist at every point $`x\in(a,b)`$.
</callout>
<details>
<summary>Proof</summary>
	$`\{f(t):a<t<x\}`$ is bounded above by $`f(x)`$. Put its least upper bound $`A`$. For every $`\varepsilon>0`$ choose $`\delta>0`$ such that $`a<x-\delta<x`$ and $`A-\varepsilon<f(x-\delta)\le A`$. Since $`f`$ is monotonic,
	$$
		A-\varepsilon<f(t)\le A
\quad(x-\delta<t<x),
	$$
	so $`f(x-)=A`$. The other side is similar.
</details>
<callout icon="📜" color="yellow_bg">
	**Cor.**
	Monotone functions have no discontinuities of the second kind.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.30.**
	If $`f`$ is monotone on $`(a,b)`$, then the set of points where $`f`$ is discontinuous is at most countable.
</callout>
<details>
<summary>Proof</summary>
	Associate to each discontinuity $`x`$ a rational $`r(x)`$ satisfying
	$$
	f(x-)<r(x)<f(x+).
	$$
	For $`x_1<x_2`$, $`f(x_1+)\le f(x_2-)`$. Hence $`r(x_1)\ne r(x_2)`$: an injection into $`\mathbb{Q}`$.
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Neighborhoods of ±∞).**
	$`(c,+\infty)`$ is a neighborhood of $`+\infty`$, and $`(-\infty,c)`$ is a neighborhood of $`-\infty`$.
</callout>
<callout icon="📘" color="blue_bg">
	**Def. (General limit by neighborhoods).**
	$`f(t)\to A`$ as $`t\to x`$ if for every neighborhood $`U`$ of $`A`$ there exists a neighborhood $`V`$ of $`x`$ such that $`V\cap E\ne\varnothing`$ and $`f(t)\in U`$ for all $`t\in V\cap E`$, $`t\ne x`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 4.34.**
	If $`f(t)\to A`$ and $`g(t)\to B`$ as $`t\to x`$, then:
	- (a) If $`f(t)\to A'`$, then $`A'=A`$.
	- (b) $`(f+g)(t)\to A+B`$.
	- (c) $`(fg)(t)\to AB`$.
	- (d) $`(f/g)(t)\to A/B`$ (where defined and $`B\ne0`$).
</callout>
# Chapter 5. Differentiation
<callout icon="📘" color="blue_bg">
	**Def. (Derivative).**
	Define
	$$
		\phi(t)=\frac{f(t)-f(x)}{t-x},
\qquad
f'(x)=\lim_{t\to x}\phi(t).
	$$
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.2.**
	If $`f`$ is differentiable at $`x`$, then $`f`$ is continuous at $`x`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.3 (Quotient rule).**
	$$
	\left(\frac fg\right)'=\frac{gf'-g'f}{g^2}.
	$$
</callout>
<details>
<summary>Proof</summary>
	Let $`h=f/g`$. Then
	$$
		\frac{h(t)-h(x)}{t-x}
=\frac{1}{g(t)g(x)}
\left[g(x)\frac{f(t)-f(x)}{t-x}
-f(x)\frac{g(t)-g(x)}{t-x}\right].
	$$
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.5 (Chain rule).**
	Suppose $`f`$ is continuous on $`[a,b]`$ and differentiable at $`x\in[a,b]`$, and $`g`$ is differentiable at $`f(x)`$. Then $`h(t)=g(f(t))`$ is differentiable at $`x`$, with
	$$
	h'(x)=g'(f(x))f'(x).
	$$
</callout>
<details>
<summary>Proof</summary>
	Let $`y=f(x)`$. Write
	$$
	f(t)-f(x)=(t-x)[f'(x)+u(t)],
	$$
	$$
	g(s)-g(y)=(s-y)[g'(y)+v(s)]
	$$
	where $`u(t)\to0`$ as $`t\to x`$ and $`v(s)\to0`$ as $`s\to y`$. Put $`s=f(t)`$. Then
	$$
		h(t)-h(x)
=g(f(t))-g(f(x))
=[f(t)-f(x)][g'(y)+v(s)]
	$$
	$$
	=(t-x)[f'(x)+u(t)][g'(y)+v(s)].
	$$
	Hence
	$$
		\frac{h(t)-h(x)}{t-x}
=[g'(y)+v(s)][f'(x)+u(t)].
	$$
</details>
<callout icon="📘" color="blue_bg">
	**Def. (Local maximum).**
	$`f`$ has a local maximum at $`p`$ if there exists $`\delta>0`$ such that $`f(q)\le f(p)`$ whenever $`d(p,q)<\delta`$.
</callout>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.8.**
	If $`f`$ has a local maximum at $`x\in(a,b)`$ and $`f'(x)`$ exists, then $`f'(x)=0`$.
</callout>
<details>
<summary>Proof</summary>
	If $`x-\delta<t<x`$, then $`\frac{f(t)-f(x)}{t-x}\ge0`$, hence $`f'(x)\ge0`$. If $`x<t<x+\delta`$, the quotient is $`\le0`$, hence $`f'(x)\le0`$.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.9 (Mean Value Theorem).**
	If $`f,g`$ are continuous real functions on $`[a,b]`$ and differentiable on $`(a,b)`$, then for some $`x\in(a,b)`$,
	$$
	[f(b)-f(a)]g'(x)=[g(b)-g(a)]f'(x).
	$$
</callout>
<details>
<summary>Proof</summary>
	Define
	$$
	h(t)=[f(b)-f(a)]g(t)-[g(b)-g(a)]f(t).
	$$
	Since $`h(a)=h(b)`$, if $`h(t)>h(a)`$ for some $`t`$, it attains an interior maximum by Thm. 4.16; by Thm. 5.8, $`h'(x)=0`$. The other case follows similarly.
</details>
*Note.* If $`g(x)=x`$, then
$$
f(b)-f(a)=(b-a)f'(x).
$$
Using this fact, the sign of $`f'(x)`$ determines whether $`f`$ is monotonically increasing or decreasing.
<callout icon="📜" color="yellow_bg">
	**Thm. 5.12 (Intermediate value property of derivatives).**
	If $`f`$ is a real differentiable function on $`[a,b]`$ and $`f'(a)<\lambda<f'(b)`$, then some $`x\in(a,b)`$ satisfies $`f'(x)=\lambda`$.
</callout>
<details>
<summary>Proof</summary>
	Let $`g(t)=f(t)-\lambda t`$. Then $`g'(a)<0`$, so $`g(t)<g(a)`$ for some $`t\in(a,b)`$. Similarly $`g'(b)>0`$, so $`g(t)<g(b)`$ for some $`t\in(a,b)`$. Thus $`g`$ attains its minimum at some $`a<x<b`$. Hence $`g'(x)=0`$, i.e. $`f'(x)=\lambda`$.
</details>
*Note.* Not every derivative is continuous, but a derivative assumes intermediate values.
<callout icon="📜" color="yellow_bg">
	**Cor.**
	If $`f`$ is differentiable on $`[a,b]`$, its derivative cannot have simple discontinuities on $`[a,b]`$.
</callout>
**Ex.** The step function
$$
g(x)=
\begin{cases}
0,&x<0,\\
1,&x\ge0
\end{cases}
$$
cannot be the derivative of any function.
<callout icon="📜" color="yellow_bg">
	**Thm. 5.13 (L'Hospital's Rule).**
	Let $`f,g`$ be real and differentiable on $`(a,b)`$, with $`g'(x)\ne0`$, where $`-\infty\le a<b\le\infty`$. Suppose
	$$
	\frac{f'(x)}{g'(x)}\to A\quad(x\to a).
	$$
	If $`f(x),g(x)\to0`$ as $`x\to a`$, or if $`g(x)\to+\infty`$ as $`x\to a`$, then
	$$
	\frac{f(x)}{g(x)}\to A\quad(x\to a).
	$$
</callout>
<details>
<summary>Proof (upper-bound argument, $`A`$ finite)</summary>
	Choose $`A<r<q`$. Since $`f'/g'\to A`$, there exists $`c\in(a,b)`$ such that $`a<x<c`$ implies $`f'(x)/g'(x)<r`$. If $`a<x<y<c`$, the generalized mean value theorem gives some $`t\in(x,y)`$ with
	$$
		\frac{f(x)-f(y)}{g(x)-g(y)}
=\frac{f'(t)}{g'(t)}<r.
	$$
	If $`f(x),g(x)\to0`$, take $`y\to a`$ to obtain $`f(x)/g(x)\le r<q`$.
	If $`g(x)\to+\infty`$, choose $`c`$ with $`g(x)>g(y)`$ and $`g(x)>0`$ when $`a<x<c`$. Rearranging gives
	$$
		\frac{f(x)}{g(x)}
<r-r\frac{g(y)}{g(x)}+\frac{f(y)}{g(x)},
	$$
	so $`\limsup_{x\to a}f(x)/g(x)\le r<q`$.
</details>
<details>
<summary>Proof (lower-bound argument)</summary>
	For $`-\infty<A\le+\infty`$, similarly choose $`p<A`$ to obtain the matching lower bound. Together these yield the limit.
</details>
<callout icon="📜" color="yellow_bg">
	**Thm. 5.15 (Taylor's theorem).**
	Suppose $`f^{(n-1)}`$ is continuous on $`[a,b]`$ and $`f^{(n)}(t)`$ exists for $`t\in(a,b)`$. Let $`\alpha,\beta`$ be distinct points of $`[a,b]`$. Put
	$$
	P(t)=\sum_{k=0}^{n-1}\frac{f^{(k)}(\alpha)}{k!}(t-\alpha)^k.
	$$
	Then for some $`x`$ between $`\alpha`$ and $`\beta`$,
	$$
	f(\beta)=P(\beta)+\frac{f^{(n)}(x)}{n!}(\beta-\alpha)^n.
	$$
</callout>
*Note.* $`f`$ can be approximated by a polynomial of degree $`n-1`$.
<details>
<summary>Proof</summary>
	Define $`M`$ by $`f(\beta)=P(\beta)+M(\beta-\alpha)^n`$, and put
	$$
	g(t)=f(t)-P(t)-M(t-\alpha)^n.
	$$
	Since $`P`$ has degree $`n-1`$,
	$$
	g^{(n)}(t)=f^{(n)}(t)-n!M.
	$$
	Also $`g(\alpha)=g'(\alpha)=\cdots=g^{(n-1)}(\alpha)=0`$ and $`g(\beta)=0`$. By the mean value theorem (repeatedly), there are points $`x_1,x_2,\ldots,x_n`$ between $`\alpha`$ and $`\beta`$ such that $`g'(x_1)=0`$, $`g''(x_2)=0`$, …, $`g^{(n)}(x_n)=0`$. Thus $`M=f^{(n)}(x_n)/n!`$.
</details>
*Note.* In general, the Mean Value Theorem and L'Hospital's rule fail for vector-valued functions. However, the following consequence of MVT remains true:
$$
|f(b)-f(a)|\le(b-a)\sup_{a<x<b}|f'(x)|.
$$
<callout icon="📜" color="yellow_bg">
	**Thm. 5.19.**
	Suppose $`f`$ is a continuous mapping of $`[a,b]`$ into $`\mathbb{R}^k`$, differentiable on $`(a,b)`$. Then some $`x\in(a,b)`$ satisfies
	$$
	|f(b)-f(a)|\le(b-a)|f'(x)|.
	$$
</callout>
<details>
<summary>Proof</summary>
	Let $`z=f(b)-f(a)`$, and define the real-valued function $`\varphi(t)=z\cdot f(t)`$. By MVT,
	$$
		\varphi(b)-\varphi(a)
=(b-a)\varphi'(x)
=(b-a)z\cdot f'(x).
	$$
	But $`\varphi(b)-\varphi(a)=z\cdot(f(b)-f(a))=|z|^2`$. By Schwarz's inequality,
	$$
		|z|^2=(b-a)\big|z\cdot f'(x)\big|
\le(b-a)|z|\,|f'(x)|.
	$$
	Therefore $`|z|\le(b-a)|f'(x)|`$.
</details>