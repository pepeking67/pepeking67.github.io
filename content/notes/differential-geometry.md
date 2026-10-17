<table_of_contents/>
# Ch. 1 — Curves
## Parametrized differentiable curve
<callout color="gray_bg">
	**Def. parametrized diff'ble curve**
	Diff'ble map $`\alpha`$ from $`I=(a,b)`$ into $`\mathbb R^3`$.
</callout>
**Ex. line**
$$
\alpha(t)=p+tv=(x_0+at,\ y_0+bt,\ z_0+ct).
$$
Point ← 이것도 parametrized diff'ble curve 취급.
$$
\frac{d}{dt}(u\cdot v)=u'\cdot v+u\cdot v'.
$$
**Prop.** $`|\alpha(t)|=\mathrm{const}\iff\alpha(t)\perp\alpha'(t)`$, $`\forall t\in I`$.
<callout color="gray_bg">
	**Def. regular / singular point**
	$`\alpha`$ is **regular** if $`\alpha'(t)\ne0`$, $`\forall t\in I`$.
	$`\alpha'(t_0)=0`$ ⇒ $`t_0`$ is a **singular point** of $`\alpha`$.
</callout>
**Arclength**
$$
s(t)=\int_{t_0}^t|\alpha'(\rho)|\,d\rho,
\qquad\frac{ds}{dt}=|\alpha'(t)|\ne0\quad\text{if regular}.
$$
$`ds/dt`$는 variable 가능.
$$
\left|\frac{d\alpha(s)}{ds}\right|=1.
$$
<callout color="gray_bg">
	**Def. tangent vector / curvature**
	$`\alpha'(t)`$: tangent vector of $`\alpha`$ at $`t`$.
	Curvature of $`\alpha`$ at $`s\in I`$:
	$$
	k(s)=|\alpha''(s)|=\left|\frac{d^2\alpha}{ds^2}\right|.
	$$
</callout>
방향 바꾸면 부호 바뀜 / 곡률은 부호 안 바뀜.
**Ex. circle** $`(r\cos(s/r),r\sin(s/r))`$ ⇒ $`k(s)=1/r`$. 반지름이 작으면 더 변화가 큼.
<callout color="gray_bg">
	**Def. normal vector** ($`k(s)\ne0`$)
	$$
	n(s)=\frac{\alpha''(s)}{|\alpha''(s)|}=\frac{\alpha''(s)}{k(s)},\qquad n(s)\perp\alpha'(s)=t(s).
	$$
	$`t'(s)=k(s)n(s)`$.
</callout>
Plane spanned by $`t,n`$: **osculating plane** of $`\alpha`$ at $`s`$.
**Binormal vector** $`b(s)=t(s)\wedge n(s)`$. $`\{t,n,b\}`$: basis for $`\mathbb R^3`$.
$$
b'(s)=t(s)\wedge n'(s)\perp t(s),b(s)\quad\Rightarrow\quad b'(s)\parallel n(s).
$$
$$
b'(s)=\tau(s)n(s).
$$
$`\tau(s)`$: **torsion** of $`\alpha`$ at $`s`$ (has sign unlike $`k\ge0`$).
**Prop.** $`\alpha`$ is a plane curve $`\iff\tau=0`$.
<callout color="gray_bg">
	**Frenet formulas**
	$$
	\begin{cases}t'=kn,\\ n'=-kt-\tau b,\\ b'=\tau n.\end{cases}
	$$
</callout>
<callout color="gray_bg">
	**Fundamental thm. of local theory of curves**
	$`k,\tau:I\to\mathbb R`$ diff'ble ⇒ ∃ regular $`\alpha`$ s.t. curvature, torsion are $`k,\tau`$.
	If $`\widetilde\alpha`$ has same properties, $`\widetilde\alpha=\rho\alpha+c`$.
	⇒ $`\widetilde\alpha`$ and $`\alpha`$ are equivalent up to rigid motion.
</callout>
![](notion-file-block://63cd679f-6409-4cb1-9fcc-bdc48c26f919/4855b9fd-5c6c-4f1f-b7b9-cb8581f5342b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-1-final.png)
## Local canonical form
Taylor:
$$
\alpha(s)=\alpha(0)+s\alpha'(0)+\frac{s^2}{2}\alpha''(0)+\frac{s^3}{6}\alpha'''(0)+R.
$$
$$
\alpha(s)-\alpha(0)=\left(s-\frac{k^2s^3}{6}\right)t+
\left(\frac{ks^2}{2}+\frac{k's^3}{6}\right)n-\frac{s^3k\tau}{6}b+R.
$$
$$
\begin{cases}
x(s)=s-\dfrac{k^2s^3}{6}+R_x,\\
y(s)=\dfrac{ks^2}{2}+\dfrac{k's^3}{6}+R_y,\\
z(s)=-\dfrac{k\tau s^3}{6}+R_z.
\end{cases}
$$
$`\tau>0`$, $`\tau<0`$: determines direction crossing the osculating plane.
$`tb`$-plane = **rectifying plane**.
<callout color="gray_bg">
	**Thm. (Isoperimetric inequality)**
	$`C\subset\mathbb R^2`$ diff'ble simple closed curve with length $`\ell`$ enclosing area $`A`$.
	$$
	\ell^2\ge4\pi A.
	$$
</callout>
# Ch. 2 — Regular surfaces
<callout color="gray_bg">
	**Def. regular surface**
	$`S\subset\mathbb R^3`$ is a regular surface if $`\forall p\in S`$, ∃ nbhd $`V`$, $`X:U\to V\cap S`$ s.t.
	1. $`X`$ is diff'ble.
	2. $`X`$ is a homeomorphism. ($`X,X^{-1}`$ continuous.)
	3. $`X`$ is regular ($`dX_q`$ is injective).
	$`V`$: coordinate nbhd. $`X`$: coordinate map.
</callout>
Self-intersecting 것은 여기서 불가능.
$$
X_u=\left(\frac{\partial x}{\partial u},\frac{\partial y}{\partial u},\frac{\partial z}{\partial u}\right),\qquad
X_v=\left(\frac{\partial x}{\partial v},\frac{\partial y}{\partial v},\frac{\partial z}{\partial v}\right)
$$
independent.
$$
\frac{\partial(x,y)}{\partial(u,v)}\ne0\quad\text{or}\quad
\frac{\partial(y,z)}{\partial(u,v)}\ne0\quad\text{or}\quad
\frac{\partial(x,z)}{\partial(u,v)}\ne0.
$$
**Ex.** $`F(x,y,z)=z-f(x,y)`$. Graph: level set $`\{F=0\}`$.
<callout color="gray_bg">
	**Def. critical point / critical value / regular value**
	Diff'ble $`F:U\subset\mathbb R^m\to\mathbb R^n`$.
	$`p\in U`$ is a **critical point** of $`F`$ if $`dF_p`$ is not surjective.
	Image of critical point: **critical value** / **regular value** → regular level set.
</callout>
<callout color="gray_bg">
	**Prop.** $`f:U\subset\mathbb R^3\to\mathbb R`$ diff'ble, $`a\in f(U)`$ is a regular value ⇒ $`f^{-1}(a)`$ is a regular surface.
</callout>
**Ex.** $`f(x,y,z)=x^2+y^2+z^2`$.
$$
df=(2x,2y,2z),\quad\text{critical point is }(0,0,0),\quad df_{(0,0,0)}=0.
$$
$$
f^{-1}(r^2)=\{x^2+y^2+z^2=r^2\}=S_r^2\quad(r>0).
$$
**Inverse function thm.** If $`F:U\to\mathbb R^n`$ is diff'ble, $`p\in U`$, $`dF_p:\mathbb R^n\to\mathbb R^n`$ is invertible, then ∃ nbhd $`V\subset U`$ s.t. $`F`$ is a bijection, $`(F|_V)^{-1}:F(V)\to V`$ is also diff'ble.
![](notion-file-block://0584da1d-ca1c-4c74-8087-0a80fd29e411/aadf144a-d92c-4062-8e2c-65f256b92be8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-2.png)
## Stereographic projection
$`N=(0,0,2)`$, $`P=(x,y,z)`$, $`\pi(P)=(u,v,0)`$.
$$
\pi:S^2\setminus\{N\}\to\mathbb R^2,
$$
$$
\pi^{-1}:\mathbb R^2\to S^2\setminus\{N\},\quad
(u,v)\mapsto\left(\frac{4u}{u^2+v^2+4},\frac{4v}{u^2+v^2+4},\frac{2(u^2+v^2)}{u^2+v^2+4}\right).
$$
## Change of parameters
**Prop.** $`S`$: regular surface. $`X:U\subset\mathbb R^2\to S`$, $`Y:V\subset\mathbb R^2\to S`$, $`p\in X(U)\cap Y(V)`$.
$$
h=X^{-1}\circ Y:Y^{-1}(X(U)\cap Y(V))\subset V\to X^{-1}(X(U)\cap Y(V))
$$
is diff'ble with diff'ble inverse (**diffeomorphism**).
## Functions on regular surfaces
<callout color="gray_bg">
	**Def.** $`f:V\subset S\to\mathbb R`$ is differentiable at $`p\in V`$ if ∃ $`X`$, $`p\in X(U)\cap V`$, $`f\circ X:U\to\mathbb R`$ is diff'ble at $`X^{-1}(p)`$.
</callout>
Independent of param.: $`X^{-1}\circ\widetilde X`$ is a diffeomorphism.
$`\varphi:V_1\subset S_1\to S_2`$ is diff'ble at $`p\in V_1`$ if $`X_1:U_1\to V_1`$, $`p\in X_1(U_1)`$, $`X_2:U_2\to S_2`$, $`\varphi(p)\in X_2(U_2)`$,
$$
X_2^{-1}\circ\varphi\circ X_1:U_1\to U_2
$$
is diff'ble at $`X_1^{-1}(p)`$.
If $`\varphi`$ is a diff'ble bijection, $`\varphi^{-1}`$ is diff'ble, then $`\varphi`$ is a **diffeomorphism**.
**Ex. diff'ble map**
1. Param. in itself.
2. Stereographic projection.
3. Projection onto a plane.
4. If $`S`$ symmetric to $`xy`$-plane, reflection map $`(x,y,z)\mapsto(x,y,-z)`$: diffeomorphism.
5. Rotation map.
## Surface of revolution
No self-intersection, no intersection with $`z`$-axis.
$`C:x=f(v),\ z=g(v)`$. $`u`$: rotation angle around $`z`$-axis.
$$
X(u,v)=(f(v)\cos u,\ f(v)\sin u,\ g(v)).
$$
## Tangent plane and differential
<callout color="gray_bg">
	**Def. tangent plane** $`T_pS`$, $`p\in S`$:
	Vector subspace of $`\mathbb R^3`$ given by $`dX_q(\mathbb R^2)`$, $`p=X(q)`$.
</callout>
**Prop.** $`T_pS`$ is the set of all $`\alpha'(0)`$ for all parametrized diff'ble curves $`\alpha:(-\varepsilon,\varepsilon)\to S`$ s.t. $`\alpha(0)=p`$.
$$
\alpha(t)=X(u(t),v(t))\quad\Rightarrow\quad
\alpha'(0)=u'(0)X_u+v'(0)X_v.
$$
<callout color="gray_bg">
	**Def.** $`\varphi:V\subset S_1\to S_2`$ diff'ble map, $`p\in V`$.
	Differential of $`\varphi`$ at $`p`$:
	$$
	d\varphi_p:T_pS_1\to T_{\varphi(p)}S_2,\qquad d\varphi_p(\alpha'(0))=(\varphi\circ\alpha)'(0).
	$$
</callout>
**Prop.** $`d\varphi_p`$ is a linear map. If $`\alpha'(0)=\widetilde\alpha'(0)`$, then $`d\varphi_p(\alpha'(0))=d\varphi_p(\widetilde\alpha'(0))`$.
**Prop. (Inverse function thm. on regular surfaces)** If $`d\varphi_p:T_pS_1\to T_{\varphi(p)}S_2`$ is a linear isomorphism, then $`\varphi`$ is a local diffeomorphism at $`p`$.
## First fundamental form
<callout color="gray_bg">
	$`w\in T_pS`$,
	$$
	I_p(w)=\langle w,w\rangle_p=|w|_p^2
	$$
	is the **first fundamental form** on $`T_pS`$.
	Intrinsic to $`S`$ ↔ determined by $`S`$ not $`\mathbb R^3`$.
</callout>
$`\alpha(t)=X(u(t),v(t))`$, $`\alpha(0)=p`$:
$$
I_p(\alpha'(0))=E(u')^2+2Fu'v'+G(v')^2,
$$
$$
E=\langle X_u,X_u\rangle,\quad F=\langle X_u,X_v\rangle,\quad G=\langle X_v,X_v\rangle.
$$
Param.에 따라 달라짐.
**Ex.**
$$
s(t)=\int_{t_0}^t|\alpha'(t)|\,dt
=\int_{t_0}^t\sqrt{I_{\alpha(t)}(\alpha'(t))}\,dt
=\int_{t_0}^t\sqrt{E(u')^2+2Fu'v'+G(v')^2}\,dt.
$$
**Area** — independent of param.
$$
A(R)=\iint_{X^{-1}(R)=Q}|X_u\wedge X_v|\,du\,dv
=\iint_Q\sqrt{|X_u|^2|X_v|^2-\langle X_u,X_v\rangle^2}\,du\,dv
=\iint_Q\sqrt{EG-F^2}\,du\,dv.
$$
**Gradient**
$$
\langle\nabla f,v\rangle_p=df_p(v),\quad\forall v\in T_pS,\quad
\nabla f=aX_u+bX_v,\quad v=cX_u+dX_v.
$$
$$
\langle aX_u+bX_v,cX_u+dX_v\rangle=cf_u+df_v
\quad\Rightarrow\quad
\begin{pmatrix}E&F\\F&G\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix}
=\begin{pmatrix}f_u\\f_v\end{pmatrix}.
$$
## Orientation
Open sets of $`\mathbb R^2`$ are orientable: can fix an ordered basis at a point and continuously move it around.
$`S`$: regular surface. $`\{X_u,X_v\}`$ is an ordered basis for $`T_pS`$.
다른 $`\{\widetilde X_{\widetilde u},\widetilde X_{\widetilde v}\}`$에 대해
$$
\widetilde X_{\widetilde u}=\frac{\partial u}{\partial\widetilde u}X_u+\frac{\partial v}{\partial\widetilde u}X_v,\qquad
\widetilde X_{\widetilde v}=\frac{\partial u}{\partial\widetilde v}X_u+\frac{\partial v}{\partial\widetilde v}X_v,
$$
$`\widetilde X(\widetilde u,\widetilde v)=X(u(\widetilde u,\widetilde v),v(\widetilde u,\widetilde v))`$.
<callout color="gray_bg">
	**Def.** $`\{X_u,X_v\}`$, $`\{\widetilde X_{\widetilde u},\widetilde X_{\widetilde v}\}`$ determine the **same orientation** if
	$$
	\frac{\partial(u,v)}{\partial(\widetilde u,\widetilde v)}>0
	$$
	on the overlap; otherwise different / opposite orientation.
</callout>
**Ex.** In $`\mathbb R^2`$, $`\{\partial/\partial x,\partial/\partial y\}`$, $`\{\partial/\partial y,\partial/\partial x\}`$:
$$
\frac{\partial(x,y)}{\partial(y,x)}=\det\begin{pmatrix}0&1\\1&0\end{pmatrix}=-1<0
$$
⇒ opposite orientation.
<callout color="gray_bg">
	**Def.** A regular surface is **orientable** if it can be covered with coordinate neighborhoods s.t. on the overlaps we have the same orientation.
	Such a family of coordinate nbhds: **orientation**.
</callout>
한 번, 두 번 돌아옴 → 뫼비우스: orientable ×.
**Ex.** $`S^2`$ is orientable. Any regular surface that can be covered with two coordinate charts s.t. the intersection is connected is orientable.
$$
X,\widetilde X\text{에 대해 같은 orientation}
\iff\frac{\partial(u,v)}{\partial(\widetilde u,\widetilde v)}>0
\iff\widetilde X_{\widetilde u}\wedge\widetilde X_{\widetilde v}
=\frac{\partial(u,v)}{\partial(\widetilde u,\widetilde v)}X_u\wedge X_v
\iff\widetilde N=N.
$$
Same normal vector.
**Prop.** $`S`$ is orientable ⇔ we can associate to each $`p\in S`$ a unit normal vector $`N(p)\in\mathbb R^3`$ (a diff'ble map $`N:S\to\mathbb R^3`$ s.t. $`N(p)\perp T_pS`$, $`|N(p)|=1`$).
**Cor.** Regular level sets of diff'ble function $`f:U\subset\mathbb R^3\to\mathbb R`$ are orientable.
$$
N=\frac{\nabla f}{|\nabla f|}.
$$
Converse: If $`S`$ is an orientable regular surface, can we find a diff'ble $`f:U\subset\mathbb R^3\to\mathbb R`$ s.t. $`S`$ is a regular level set of $`f`$? → yes if compact surfaces.
![](notion-file-block://214b5a09-687a-4ca0-bdeb-64d00c6319bb/97c286eb-9514-4f36-8bd5-a6fe71159479?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-3-final.png)
# Ch. 3 — Gauss map
<callout color="gray_bg">
	**Def.** $`S`$: oriented surface. ∃ diff'ble map $`N:S\to\mathbb R^3`$ mapping into $`S^2=\{x^2+y^2+z^2=1\}`$, $`N(p)\perp T_pS`$.
	$`N`$: **Gauss map** of $`S`$.
</callout>
$$
T_pS\cong T_{N(p)}S^2.
$$
**Prop.** The linear map $`dN_p:T_pS\to T_{N(p)}S^2`$ is self-adjoint:
$$
\langle dN_p(w_1),w_2\rangle=\langle w_1,dN_p(w_2)\rangle,\qquad w_1,w_2\in T_pS.
$$
$$
\langle N_u,X_v\rangle=\langle X_u,N_v\rangle.
$$
<callout color="gray_bg">
	**Def. second fundamental form**
	The quadratic form $`II_p`$ on $`T_pS`$,
	$$
	II_p(v)=-\langle dN_p(v),v\rangle.
	$$
</callout>
<callout color="gray_bg">
	**Def. normal curvature**
	$`C`$: regular curve in $`S`$, passing $`p`$; $`n`$: normal vector of $`C`$ at $`p`$.
	$$
	k_n(p)=\langle kn,N\rangle=k\cos\theta.
	$$
</callout>
$$
\langle N(\alpha(s)),t(s)\rangle=0,\quad\alpha(0)=p
$$
$$
\Rightarrow\langle N'(s)|_{s=0},t(0)\rangle+\langle N(0),kn(0)\rangle=0.
$$
$$
k_n(p)=\langle kn,N\rangle(p)=-\langle N'(0),t(0)\rangle
=-\langle dN_p(\alpha'(0)),\alpha'(0)\rangle=II_p(\alpha'(0)).
$$
$$
\alpha'(t)=u'(t)X_u+v'(t)X_v.
$$
**Self-adjointness / principal curvatures**
$$
dN_p:T_pS\to T_pS\text{ is self-adjoint}
\iff\text{matrix is symmetric}
$$
⇔ ∃ orthonormal basis $`\{e_1,e_2\}`$ of $`T_pS`$ s.t.
$$
dN_p(e_1)=-k_1e_1,\quad dN_p(e_2)=-k_2e_2,\quad k_1\ge k_2.
$$
**Ex.** $`N(p)=p`$: sphere oriented outward.
$$
k_1=k_2=-1\quad\Rightarrow\quad II_p(v)=-|v|^2.
$$
<callout color="gray_bg">
	**Def.** $`k_1,k_2`$: **principal curvatures** at $`p`$ of $`S`$.
	$`e_1,e_2`$: **principal directions**.
</callout>
정확히 무슨 의미? — 미적 복기.
$`\{X_u/\sqrt E,X_v/\sqrt G\}`$.
$`v\in T_pS`$, $`|v|=1`$ ⇒ $`v=\cos\theta\,e_1+\sin\theta\,e_2`$.
$$
II_p(v)=II_p(\cos\theta\,e_1+\sin\theta\,e_2)=k_1\cos^2\theta+k_2\sin^2\theta.
$$
<callout color="gray_bg">
	**Def. Gaussian curvature / mean curvature**
	$$
	K=k_1k_2=\det dN_p,\qquad H=\frac{k_1+k_2}{2}=-\frac{\operatorname{tr}dN_p}{2}.
	$$
</callout>
- Elliptic: $`K>0`$.
- Parabolic: $`K=0,\ H\ne0`$.
- Planar: $`K=0,\ H=0`$.
- Hyperbolic: $`K<0`$.
<callout color="gray_bg">
	**Def.** $`p\in S`$ is **umbilic** if $`k_1=k_2`$ ⇒ elliptic or planar.
</callout>
**Prop.** If $`S`$ is connected and all $`p\in S`$ are umbilic s.t. $`dN_p=\lambda(p)\operatorname{Id}`$, then $`S`$ is contained in either a plane or sphere.
<callout color="gray_bg">
	**Def. asymptotic directions**
	$`v\in T_pS\setminus\{0\}`$ s.t. $`II_p(v)=k_n=0`$.
</callout>
![](notion-file-block://29759cd0-e996-47b9-9a17-85fc1f9daad1/afb1c6ee-58cd-45c1-ba16-ea7bbb96d1d5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-4-final.png)
The **Dupin indicatrix** is $`\{v\in T_pS\mid II_p(v)=\pm1\}`$.
Let $`dN=\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}`$, then
$$
-\begin{pmatrix}e&f\\f&g\end{pmatrix}
=\begin{pmatrix}a_{11}&a_{21}\\a_{12}&a_{22}\end{pmatrix}\begin{pmatrix}E&F\\F&G\end{pmatrix}.
$$
$$
e=\langle N,X_{uu}\rangle,\quad f=\langle N,X_{uv}\rangle,\quad g=\langle N,X_{vv}\rangle.
$$
$$
K=\frac{eg-f^2}{EG-F^2},\qquad H=\frac{eG-2fF+gE}{2(EG-F^2)},\qquad k^2-2Hk+K=0.
$$
**Prop.** If $`p\in S`$ is an elliptic point, then nbhd of $`p`$ lies on one side of $`T_pS`$. Hyperbolic: has points on both sides of $`T_pS`$.
Parallels ($`v=\mathrm{const}`$) and meridians ($`u=\mathrm{const}`$) are **lines of curvature**: curves along which the velocity gives principal directions.
Locally, $`S`$ is given by $`z=h(x,y)`$ near $`p`$ (graph).
Local $`S`$를 plane sections parallel to $`T_pS=\{z=0\}`$로 reconstruct.
$`C_\varepsilon`$ projects down to $`xy`$-plane to $`\{(x,y)\mid h(x,y)=\varepsilon\}`$.
$`K\ne0`$, $`\partial_x=e_1`$, $`\partial_y=e_2`$ 가정 ⇒ $`h_{xx}=k_1`$, $`h_{xy}=0`$, $`h_{yy}=k_2`$.
Taylor:
$$
h(x,y)=\frac12\left(h_{xx}(0,0)x^2+2h_{xy}(0,0)xy+h_{yy}(0,0)y^2\right)+R=\varepsilon
$$
$$
\Rightarrow h(x,y)=\frac12(k_1x^2+k_2y^2)+R=\varepsilon
\Rightarrow k_1x^2+k_2y^2=2(\varepsilon-R)\quad\text{on }C_\varepsilon.
$$
$`\bar x=x/\sqrt{2\varepsilon}`$, $`\bar y=y/\sqrt{2\varepsilon}`$:
$$
k_1\bar x^2+k_2\bar y^2=1-\frac R\varepsilon,\qquad R/\varepsilon\to0\text{ as }(x,y)\to(0,0).
$$
→ Dupin indicatrix at $`p`$.
**Prop.** For connected coordinate nbhd $`V`$ of $`p`$ and open set $`B`$ s.t. $`\overline B\subset V`$, $`K(p)\ne0`$,
$$
|K(p)|=\lim_{\operatorname{area}(B)\to0}\frac{\operatorname{Area}(N(B))}{\operatorname{Area}(B)}.
$$
$$
\operatorname{Area}(B)=\iint_{X^{-1}(B)}|X_u\wedge X_v|\,du\,dv,\qquad
\operatorname{Area}(N(B))=\iint_{X^{-1}(B)}|N_u\wedge N_v|\,du\,dv.
$$
$$
|N_u\wedge N_v|=|K|\,|X_u\wedge X_v|.
$$
## Vector fields
Trajectory (flow line) of $`w`$: $`\alpha(t)=(x(t),y(t))`$ s.t. $`\alpha'(t)=w(\alpha(t))`$.
**Thm.** Diff'ble $`w`$ on $`U`$, $`p\in U`$ ⇒ ∃ diff'ble trajectory $`\alpha`$ s.t. $`\alpha(0)=p`$, $`\alpha:I\to U`$. If another trajectory $`\beta:J\to U`$, $`\beta(0)=p`$, then $`\alpha|_{I\cap J}=\beta|_{I\cap J}`$.
<callout color="gray_bg">
	**Thm. (Flow of a vector field)**
	Diff'ble $`w`$ on $`U\ni p`$ ⇒ ∃ nbhd $`V`$ of $`p`$, $`V\subset U`$, diff'ble $`\alpha:V\times I\to U`$ s.t. $`\forall q\in V`$, $`t\mapsto\alpha(q,t)`$ is a trajectory of $`w`$ passing through $`q`$, s.t.
	$$
	\frac{\partial\alpha}{\partial t}(\alpha(q,t))=w(\alpha(q,t)).
	$$
</callout>
이 $`\alpha`$를 **flow of **$`w`$라 한다. Trajectory는 하나, flow는 전체적인 흐름을 나타냄.
<callout color="gray_bg">
	**Def. field of directions** $`r`$ in $`U`$: assignment each $`p\in U`$ a line $`r(p)`$ passing $`p`$.
	Diff'ble at $`p`$ if ∃ diff'ble $`w`$ on nbhd $`V`$ of $`p`$ s.t. $`w(q)\ne0`$, $`\forall q\in V`$, and $`w(q)`$ generates $`r(q)`$.
	A regular connected curve $`C\subset U`$ is an **integral curve** of $`r`$ if $`\forall q\in C`$, $`r(q)`$ is the tangent line to $`C`$ at $`q`$.
</callout>
$`F=(f_1,f_2)`$, $`V(F)=0`$ ⇒ $`f_i`$: **first integrals**.
$$
\frac{d}{dt}(x,y,z)=V(x,y,z),\qquad V(x,y,z)=(a,b,c)
\quad\Rightarrow\quad a\frac{\partial F}{\partial x}+b\frac{\partial F}{\partial y}+c\frac{\partial F}{\partial z}=0.
$$
# Ch. 3.5 — Ruled and minimal surfaces (Quiz 6)
Regular surface → ruled surface / minimal surface.
## 1. Ruled surface
$`\{\alpha(t),w(t)\}`$: point / vector; directrix / ruling.
<callout color="gray_bg">
	$$
	X(t,v)=\alpha(t)+v\,w(t).
	$$
	**Ruled surface** generated by $`\{\alpha(t),w(t)\}`$.
</callout>
**Ex.** $`X(t,v)=\alpha(t)+v\alpha'(t)`$: **tangent surface**.
$$
\alpha(s)=(\cos s,\sin s,0),\qquad w(s)=\alpha'(s)+(0,0,1)
$$
→ hyperboloid.
Ruled surface ⇒ $`K\le0`$.
<details>
<summary>Proof / line of striction</summary>
	Assume $`|w(t)|=1`$, $`w'(t)\ne0`$: **noncylindrical**. $`w\cdot w'=0`$.
	Line of striction:
	$$
	\beta(t)=\alpha(t)+u(t)w(t),\qquad\langle\beta'(t),w'(t)\rangle=0.
	$$
	$$
										0=\langle\beta',w'\rangle=\langle\alpha',w'\rangle+u'\langle w,w'\rangle+u\langle w',w'\rangle
\Rightarrow u(t)=-\frac{\langle\alpha'(t),w'(t)\rangle}{\langle w'(t),w'(t)\rangle}.
	$$
	$$
	\therefore\beta(t)=\alpha(t)-\frac{\langle\alpha'(t),w'(t)\rangle}{\langle w'(t),w'(t)\rangle}w(t).
	$$
	$$
	X(t,u)=\beta(t)+uw(t),\quad X_t=\beta'+uw',\quad X_u=w,
	$$
	$$
	X_t\wedge X_u=\beta'\wedge w+uw'\wedge w.
	$$
	$`w\perp w'`$, $`\beta'\perp w'`$ ⇒ $`\beta'\wedge w=\lambda(t)w'(t)`$.
	$$
	|X_t\wedge X_u|^2=\lambda^2|w'|^2+u^2|w\wedge w'|^2=(\lambda^2+u^2)|w'|^2.
	$$
	If $`u\ne0`$, this is nonzero. Fail to be regular are all on $`\{u=0\}`$ (⇔ on $`\beta`$).
	At the regular points,
	$$
	X_{tt}=\beta''+uw'',\quad X_{tu}=w',\quad X_{uu}=0,
	$$
	$$
	e=\cdots,\quad f=\frac{\lambda|w'|^2}{|X_t\wedge X_u|},\quad g=0,
	$$
	$$
										K=\frac{eg-f^2}{EG-F^2}
=-\frac{\lambda^2|w'|^4}{(\lambda^2+u^2)^2|w'|^4}
=-\left(\frac{\lambda}{\lambda^2+u^2}\right)^2\le0.
	$$
</details>
![](notion-file-block://0799f044-ca1c-4f66-ac3c-e23865ac1256/0510cb1f-7ab5-4d15-a038-1c2dab05b43b?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-5.png)
## 2. Minimal surface
<callout color="gray_bg">
	An oriented regular surface is **minimal** if $`H\equiv0`$.
</callout>
**First variation formula**
Let $`X:U\to S`$ parametrize $`S`$ locally. Choose $`D\subset U`$ compact.
Normal variation:
$$
\varphi:\overline D\times(-\varepsilon,\varepsilon)\to\mathbb R^3,\qquad
\varphi(u,v,t)=X(u,v)+t\,h(u,v)N(u,v).
$$
$`h:\overline D\to\mathbb R`$. 법선 방향으로 표면을 살짝 변경. $`t`$: 그 정도를 나타내는 변수. 변경시킨 것의 $`t`$에 따른 넓이를 조사해서 그 값이 변하는지 확인.
For each $`t`$, $`X^t(u,v)=\varphi(u,v,t)`$.
$$
(X^t)_u=X_u+thN_u+th_uN,\qquad (X^t)_v=X_v+thN_v+th_vN.
$$
Area of $`X^t(D)`$:
$$
A(t)=\int_D\sqrt{E^tG^t-(F^t)^2}\,du\,dv,\quad E^t=\langle(X^t)_u,(X^t)_u\rangle,\ldots
$$
$$
E^tG^t-(F^t)^2=(EG-F^2)-4th(EG-F^2)H+R,\qquad R=o(t).
$$
$$
A(t)=\int_D\sqrt{1-4thH+\frac R{EG-F^2}}\sqrt{EG-F^2}\,du\,dv.
$$
<callout color="gray_bg">
	**First variation formula**
	$$
	\left.\frac d{dt}\right|_{t=0}A(t)=-\int_D2hH\sqrt{EG-F^2}\,du\,dv.
	$$
</callout>
$`H\equiv0`$ ⇒ $`\left.\dfrac d{dt}\right|_{t=0}A(t)=0`$. Minimal surface는 변형을 줘도 최소, 그 점의 변화율 = 0. Critical point of area.
## Isothermal parametrization
Mean curvature: $`\vec H=H\cdot N`$ ← orientation과 무관.
<callout color="gray_bg">
	Regular parametrization $`X(u,v)`$ is **isothermal** if
	$$
	\langle X_u,X_u\rangle=\langle X_v,X_v\rangle,\qquad\langle X_u,X_v\rangle=0.
	$$
	길이 동일, 직교성.
</callout>
**Prop.** If $`X`$ is isothermal, then
$$
X_{uu}+X_{vv}=2\lambda^2\vec H,\qquad\lambda^2=\langle X_u,X_u\rangle=\langle X_v,X_v\rangle.
$$
**Cor.** An isothermal $`X`$ defines a minimal surface ($`H=0`$)
$$
\iff X\text{ isothermal},\quad X_{uu}+X_{vv}=\Delta X=0
$$
⇔ the coordinate functions of the isothermal $`X`$ are **harmonic**.
Laplacian:
$$
\Delta f=\frac{\partial^2f}{\partial u^2}+\frac{\partial^2f}{\partial v^2},\qquad\Delta f=0.
$$
**Ex. plane**
1. **Helicoid (나선면)**
$$
X(u,v)=(v\cos u,v\sin u,au)\quad\Rightarrow\quad H=0\text{ 확인 가능}.
$$
$`X`$가 $`E\ne G`$로 isothermal이 아니어서 직접 $`H=0`$으로 증명.
Remark. $`E\ne G`$ → not isothermal. Isothermal parametrization 아니어도 minimal surface 증명 가능.
1. **Catenoid**
$$
X(u,v)=(a\cosh v\cos u,a\cosh v\sin u,av).
$$
$`E=G`$ → isothermal. $`E=G`$ → isothermal, $`X_{uu}+X_{vv}=0`$으로 minimal인지 증명.
## 3. Weierstrass representation
Fact: $`f:U\subset\mathbb R^2=\mathbb C\to\mathbb C`$ holomorphic ($`f`$ is complex analytic), $`(u,v)\leftrightarrow u+iv`$.
$`f=f_1+if_2`$, $`f_1,f_2:U\to\mathbb R`$.
Cauchy–Riemann equations:
$$
\begin{cases}(f_1)_u=(f_2)_v,\\(f_1)_v=-(f_2)_u.\end{cases}
$$
Let $`X:U\to\mathbb R^3`$, $`X(u,v)=(x(u,v),y(u,v),z(u,v))`$, $`\zeta=u+iv`$.
Define
$$
\begin{cases}
\varphi_1(\zeta)=\dfrac{\partial x}{\partial u}-i\dfrac{\partial x}{\partial v},\\
\varphi_2(\zeta)=\dfrac{\partial y}{\partial u}-i\dfrac{\partial y}{\partial v},\\
\varphi_3(\zeta)=\dfrac{\partial z}{\partial u}-i\dfrac{\partial z}{\partial v}.
\end{cases}
$$
$$
\varphi_1^2+\varphi_2^2+\varphi_3^2
=(x_u^2+y_u^2+z_u^2)-(x_v^2+y_v^2+z_v^2)-2i(x_ux_v+y_uy_v+z_uz_v)
=E-G-2iF.
$$
$$
\therefore\varphi_1^2+\varphi_2^2+\varphi_3^2=0\iff E=G,\ F=0
\iff X\text{ is an isothermal parametrization}.
$$
If they ($`\varphi_i`$) are holomorphic → minimal surface. $`X_{uu}+X_{vv}=0`$인지 확인 → 그래서 minimal surface.
**Enneper's surface**
$$
\varphi_1(\zeta)=1-\zeta^2,\quad\varphi_2(\zeta)=i(1+\zeta^2),\quad\varphi_3(\zeta)=2\zeta,\qquad\zeta=u+iv.
$$
$$
1-(u+iv)^2=x_u-ix_v,\qquad1-u^2+v^2-2iuv
\quad\Rightarrow\quad x=u-\frac{u^3}{3}+uv^2.
$$
비슷하게 $`y=v-\dfrac{v^3}{3}+vu^2`$, $`z=u^2-v^2`$으로 구할 수 있다.
**Scherk's surface**
$$
\varphi_1(\zeta)=-\frac1{1+\zeta^2},\quad
\varphi_2(\zeta)=-\frac i{1+\zeta^2},\quad
\varphi_3(\zeta)=\frac{4\zeta}{1-\zeta^4}
\quad\Rightarrow\quad z=\log\frac{\cos y}{\cos x}.
$$
Weierstrass representation examples.
**참고 — minimal surface 성질**
Monotonicity formula:
$$
\frac{A(S\cap B_{x_0}(t))}{t^2}-\frac{A(S\cap B_{x_0}(s))}{s^2}\ge0.
$$
**Bernstein's thm.** If the graph of $`f:\mathbb R^2\to\mathbb R`$ is a regular minimal surface, then the graph is a **plane**.
$$
f(u,v)=au+bv+c.
$$
# Ch. 4.2 — Isometries (Quiz 7)
Isometric: 기하학적으로 같다 (길이, 각도 변화 ×).
<callout color="gray_bg">
	**Def. isometry**
	Diff'ble $`\varphi:S\to\overline S`$ is an **isometry** if $`\varphi`$ is a diffeomorphism and
	$$
	\langle w_1,w_2\rangle_p=\langle d\varphi_p(w_1),d\varphi_p(w_2)\rangle_{\varphi(p)},\qquad\forall p\in S,\ \forall w_1,w_2\in T_pS.
	$$
</callout>
$$
I_p(w)=I_{\varphi(p)}(d\varphi_p(w)),\qquad I_p(w)=\langle w,w\rangle_p.
$$
$`\varphi:V\to\overline S`$, $`p\in V`$ ($`V`$: nbhd of $`p`$) is a **local isometry at **$`p`$ if there is a nbhd $`\overline V`$ of $`\varphi(p)`$ in $`\overline S`$ s.t. $`\operatorname{Image}(\varphi)=\overline V`$, $`\varphi:V\to\overline V`$ is an isometry.
$`\forall p\in S`$, ∃ a local isometry at $`p`$ to $`\overline S`$, then $`S`$ is **locally isometric** to $`\overline S`$.
$`S`$ is locally isometric to $`\overline S`$, $`\overline S`$ to $`S`$, then $`S`$ and $`\overline S`$ are locally isometric.
**Ex. plane & cylinder**
$`\{w_1,w_2\}`$ orthonormal,
$$
X(u,v)=p+uw_1+vw_2,\qquad\overline X(u,v)=(\cos u,\sin u,v).
$$
$$
\overline X_u=(-\sin u,\cos u,0),\quad\overline X_v=(0,0,1).
$$
“Plane and cylinder are locally isometric.” Check $`\Phi=X\circ\overline X^{-1}`$ is a local isometry.
$$
(\cos u,\sin u,v)\xmapsto{\Phi}p+uw_1+vw_2,
$$
$$
d\Phi(\overline X_u)=w_1,\quad d\Phi(\overline X_v)=w_2
\Rightarrow\overline E=E=1,\quad\overline G=G=1,\quad\overline F=F=0.
$$
<callout color="gray_bg">
	**Prop.** $`X:U\to S`$, $`\overline X:U\to\overline S`$ s.t. $`E=\overline E`$, $`F=\overline F`$, $`G=\overline G`$. Then $`X\circ\overline X^{-1}:\overline X(U)\to S`$ is a local isometry.
</callout>
<details>
<summary>Proof</summary>
	$`\Phi=X\circ\overline X^{-1}`$, then $`d\Phi(\overline X_u)=X_u`$, $`d\Phi(\overline X_v)=X_v`$.
	$`w=a\overline X_u+b\overline X_v`$에 대해 $`d\Phi_p(w)=aX_u+bX_v`$.
	$$
									I_{\Phi(p)}(d\Phi_p(w))=Ea^2+2Fab+Gb^2
=\overline Ea^2+2\overline Fab+\overline Gb^2=I_p(w).
	$$
</details>
**Ex. catenoid & helicoid**
Catenoid:
$$
X(u,v)=(a\cosh v\cos u,a\cosh v\sin u,av),
$$
$$
E=(a\cosh v)^2,\quad F=0,\quad G=(a\cosh v)^2.
$$
Helicoid:
$$
\overline X(\overline u,\overline v)=(\overline v\cos\overline u,\overline v\sin\overline u,a\overline u),\quad
(\overline u,\overline v)\in\overline U=(0,2\pi)\times(-\infty,\infty).
$$
Change of parameter: $`\overline u=u`$, $`\overline v=a\sinh v`$, $`\partial(\overline u,\overline v)/\partial(u,v)=a\cosh v`$.
$`(u,v)\in U=(0,2\pi)\times(-\infty,\infty)`$: new parametrization of helicoid; $`X`$ maps to catenoid.
$$
\overline X_u=(-a\sinh v\sin u,a\sinh v\cos u,a),\qquad
\overline X_v=(a\cosh v\cos u,a\cosh v\sin u,0).
$$
$$
\overline E=a^2\cosh^2v,\quad\overline F=0,\quad\overline G=a^2\cosh^2v.
$$
Isothermal param. of helicoid ⇒ catenoid, helicoid local isometry.
![](notion-file-block://d63d18f1-8705-4e6b-8caa-ea422a6d962c/0afd81aa-18a7-49d2-8a90-53e8e92b82f8?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-6.png)
## Conformal map
<callout color="gray_bg">
	**Def.** $`\varphi:S\to\overline S`$ is a **conformal map** if it is a diffeomorphism and
	$$
	\langle d\varphi_p(w_1),d\varphi_p(w_2)\rangle_{\varphi(p)}=\lambda^2(p)\langle w_1,w_2\rangle_p,
	$$
	$`\forall p\in S`$, $`w_1,w_2\in T_pS`$, for some $`\lambda^2:S\to\mathbb R`$ a diff'ble nonzero function.
</callout>
$`S`$ and $`\overline S`$ are conformal if there is a conformal map $`S\to\overline S`$.
Diff'ble $`\varphi:V\to\overline S`$, $`p\in V`$, is locally conformal if …
Angle 보존, 길이 보존 ×.
**Prop.** ∃ $`X:U\to S`$, $`\overline X:U\to\overline S`$ s.t. $`\overline E=\lambda^2E`$, $`\overline F=\lambda^2F`$, $`\overline G=\lambda^2G`$ for some $`\lambda^2`$ nonzero on $`U`$. Then $`X\circ\overline X^{-1}:\overline X(U)\to S`$ is a locally conformal map.
Proof: exercise.
<callout color="gray_bg">
	**Thm. Any two regular surfaces are locally conformal.**
</callout>
Need: Any regular surface is locally conformal to a plane.
⇔ ∃ param. on $`S`$ s.t. $`E=\lambda^2`$, $`F=0`$, $`G=\lambda^2`$ ⇔ **isothermal**.
Regular surface가 아니어도 isothermal parametrization을 가지면 임의의 regular surface와 conformal하다!
# Ch. 4.3 — Gauss theorem
“The Gaussian curvature is invariant under local isometries.”
⇒ Gaussian curvature가 다르면 local isometry가 아님.
Recall:
$$
K=k_1k_2=\frac{eg-f^2}{EG-F^2}.
$$
Any two regular surfaces are locally conformal. Need: any regular surface is locally conformal to a plane ⇒ $`E=\lambda^2`$, $`F=0`$, $`G=\lambda^2`$.
## Christoffel symbols
$`X:U\to S`$ positively oriented parametrization. $`\{X_u,X_v,N\}`$ is a basis of $`\mathbb R^3`$.
$$
\begin{aligned}
X_{uu}&=\Gamma^1_{11}X_u+\Gamma^2_{11}X_v+L_1N,\\
X_{uv}&=\Gamma^1_{12}X_u+\Gamma^2_{12}X_v+L_2N,\\
X_{vu}&=\Gamma^1_{21}X_u+\Gamma^2_{21}X_v+L_2N,\\
X_{vv}&=\Gamma^1_{22}X_u+\Gamma^2_{22}X_v+L_3N,\\
N_u&=a_{11}X_u+a_{21}X_v,\\
N_v&=a_{12}X_u+a_{22}X_v.
\end{aligned}
$$
**Def.** $`\Gamma^k_{ij}`$: **Christoffel symbols**. $`X_{uv}=X_{vu}`$ ⇒ $`\Gamma^k_{ij}=\Gamma^k_{ji}`$.
$$
\langle X_{uu},N\rangle=L_1=e,\quad L_2=f,\quad L_3=g,
$$
$$
\begin{pmatrix}a_{11}&a_{21}\\a_{12}&a_{22}\end{pmatrix}
=-\begin{pmatrix}e&f\\f&g\end{pmatrix}\begin{pmatrix}E&F\\F&G\end{pmatrix}^{-1}.
$$
<details>
<summary>Christoffel symbols 계산 / Gauss theorem</summary>
	①
	$$
	\langle X_{uu},X_u\rangle=\frac12E_u=\Gamma^1_{11}E+\Gamma^2_{11}F,
	$$
	$$
	\langle X_{uu},X_v\rangle=F_u-\frac12E_v=\Gamma^1_{11}F+\Gamma^2_{11}G.
	$$
	$`F_u=\dfrac\partial{\partial u}\langle X_u,X_v\rangle=\langle X_{uu},X_v\rangle+\langle X_u,X_{uv}\rangle`$.
	$$
									\begin{pmatrix}E&F\\F&G\end{pmatrix}\begin{pmatrix}\Gamma^1_{11}\\\Gamma^2_{11}\end{pmatrix}
=\begin{pmatrix}\frac12E_u\\F_u-\frac12E_v\end{pmatrix}.
	$$
	$$
									\therefore\begin{pmatrix}\Gamma^1_{11}\\\Gamma^2_{11}\end{pmatrix}
=\begin{pmatrix}E&F\\F&G\end{pmatrix}^{-1}\begin{pmatrix}\frac12E_u\\F_u-\frac12E_v\end{pmatrix}.
	$$
	②, ④ 비슷하게
	$$
									\begin{pmatrix}\Gamma^1_{12}\\\Gamma^2_{12}\end{pmatrix}
=\begin{pmatrix}E&F\\F&G\end{pmatrix}^{-1}\begin{pmatrix}\frac12E_v\\\frac12G_u\end{pmatrix},
\qquad\begin{pmatrix}\Gamma^1_{22}\\\Gamma^2_{22}\end{pmatrix}
=\begin{pmatrix}E&F\\F&G\end{pmatrix}^{-1}\begin{pmatrix}F_v-\frac12G_u\\\frac12G_v\end{pmatrix}.
	$$
	⑤ $`(X_{uu})_v=(X_{vu})_u`$, ⑥ $`(X_{vv})_u=(X_{uv})_v`$, ⑦ $`N_{uv}=N_{vu}`$.
	⑤ ⇒
	$$
									(\Gamma^1_{11}X_u+\Gamma^2_{11}X_v+eN)_v
-(\Gamma^1_{12}X_u+\Gamma^2_{12}X_v+fN)_u=0.
	$$
	$$
									(\Gamma^1_{11})_vX_u+(\Gamma^2_{11})_vX_v+e_vN
+\Gamma^1_{11}X_{uv}+\Gamma^2_{11}X_{vv}+eN_v-\cdots=0.
	$$
	⑤′, ⑥′, ⑦′: $`A_iX_u+B_iX_v+C_iN=0`$, where $`A_i=0`$, $`B_i=0`$, $`C_i=0`$. Basis = linearly independent.
	이를 통해 $`K`$를 $`E,F,G`$로만 나타낼 수 있음.
	⇒ invariant under locally isometry.
</details>
$`H`$는 아님. Rigid motion에서만 불변.
Plane $`K=0,H=0`$ → roll up (isometry) → cylinder $`K=0,H\ne0`$.
# Ch. 4.4 — Parallel transport & geodesics
**Intrinsic geometry** → depending only on $`E,F,G`$ + their derivatives, not needing what exactly the surface is as a subset of $`\mathbb R^3`$.
구 표면을 따른 거리: intrinsic / 공간에서 바로 잇는 거리: extrinsic.
$`S`$: oriented regular surface. $`w`$: differentiable vector field on $`U`$.
## Covariant derivative
<callout color="gray_bg">
	**Def.** Let $`\alpha:(-\varepsilon,\varepsilon)\to U`$, $`\alpha(0)=p`$, $`\alpha'(0)=y\in T_pS`$.
	The **covariant derivative** of $`w`$ relative to $`y`$ at $`p`$ is the normal projection of $`\dfrac{dw}{dt}(0)`$ onto $`T_pS`$:
	$$
	\frac{Dw}{dt}(0),\qquad(\nabla_yw)(p).
	$$
	Depends only on $`y`$, not $`\alpha`$.
</callout>
**Ex. plane** ⇒ $`dw/dt=Dw/dt`$.
## Quiz 8 — Ch. 4.4
$`S`$: oriented regular surface. $`\alpha:I\to U\subset S`$ ($`U`$: open), $`w`$: diff'ble vector field on $`U`$.
Covariant derivative of $`w`$ relative to $`\alpha'(0)`$ at $`p`$.
For $`\alpha(t)=X(u(t),v(t))`$, $`w(t)=a(t)X_u(t)+b(t)X_v(t)`$,
$$
\frac{dw}{dt}=a(X_{uu}u'+X_{uv}v')+b(X_{vu}u'+X_{vv}v')+a'X_u+b'X_v
$$
$$
=\left(a'+\Gamma^1_{11}au'+\Gamma^1_{12}av'+\Gamma^1_{12}bu'+\Gamma^1_{22}bv'\right)X_u
+\left(b'+\Gamma^2_{11}au'+\Gamma^2_{12}av'+\Gamma^2_{12}bu'+\Gamma^2_{22}bv'\right)X_v+[\cdots]N.
$$
$$
\frac{Dw}{dt}
=\left(a'+\Gamma^1_{11}au'+\Gamma^1_{12}av'+\Gamma^1_{12}bu'+\Gamma^1_{22}bv'\right)X_u
+\left(b'+\Gamma^2_{11}au'+\Gamma^2_{12}av'+\Gamma^2_{12}bu'+\Gamma^2_{22}bv'\right)X_v.
$$
<callout color="gray_bg">
	**Def. parametrized curve** $`\alpha:[0,\ell]\to S`$ is the restriction of diff'ble curve $`(-\varepsilon,\ell+\varepsilon)\to S`$.
	$`\alpha`$ is **regular** if $`\alpha'(t)\ne0`$ for any $`t\in[0,\ell]`$.
	Let $`p,q\in S`$. $`\alpha`$ **joins** $`p`$ to $`q`$ if $`\alpha(0)=p`$, $`\alpha(\ell)=q`$.
</callout>
<callout color="gray_bg">
	**Def. vector field **$`w`$** along **$`\alpha`$: assignment $`w(t)\in T_{\alpha(t)}S`$ for each $`t\in I`$.
	$`w`$ is diff'ble at $`t_0\in I`$ if $`w(t)=a(t)X_u(t)+b(t)X_v(t)`$ for some param. at $`\alpha(t_0)`$, $`a(t),b(t)`$ diff'ble.
</callout>
**Ex.** $`w(t)=\alpha'(t)`$.
$$
\frac{dw}{dt}=\alpha''(t)\in T_{\alpha(t)}\mathbb R^3\cong\mathbb R^3,
$$
$$
\frac{Dw}{dt}=\text{projection of }\alpha''(t)\text{ onto }T_{\alpha(t)}S
=\text{acceleration as seen on }S.
$$
<callout color="gray_bg">
	**Def.** Vector field along $`\alpha`$ is **parallel** if $`Dw/dt=0`$, $`\forall t\in I`$.
</callout>
$`Dw/dt=0`$ ⇒ parallel. $`dw/dt`$ is normal to plane $`T_pS`$. Intrinsic 관점.
**Ex. plane** $`Dw/dt=dw/dt=0\iff w`$ is constant.
**Prop.** $`w,v`$: vector fields along $`\alpha:I\to S`$. If $`w,v`$ are parallel, then $`|w(t)|`$, $`|v(t)|`$, $`\angle(w,v)`$ are constant in $`t`$.
$$
\langle v,w'\rangle=0,\quad\langle v',w\rangle=0
\Rightarrow\langle v,w\rangle'=0\Rightarrow\langle v,w\rangle=\mathrm{const}.
$$
**Prop.** $`\alpha:I\to S`$, $`w_0\in T_{\alpha(t_0)}S`$, $`t_0\in I`$. ∃! parallel vector field $`w(t)`$ along $`\alpha(t)`$ s.t. $`w(t_0)=w_0`$.
<callout color="gray_bg">
	**Def.** This vector $`w(t)`$ is called **parallel transport** of $`w_0`$ along $`\alpha`$.
</callout>
Does not depend on parametrization of $`\alpha(I)`$.
$$
\widetilde\alpha=\alpha(t(s)):J\to\alpha(I),\qquad
\frac{dw}{ds}=\frac{dw}{dt}\frac{dt}{ds}\Rightarrow\frac{Dw}{ds}=\frac{Dw}{dt}\frac{dt}{ds}.
$$
![](notion-file-block://1158bb55-7563-476a-80ff-21e7587c2081/60459ed3-4c2f-4dfe-9699-2e6843eeb240?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-7.png)
**Ex. parallel transport of a vector along a line of latitude** $`\alpha:I\to S^2`$, $`w_0=\alpha'(t_0)`$.
$`S^2`$와 cone의 tangent plane 공유 ⇒ cone에서의 parallel transport 고려.
Cone → local isometry → part of a plane, $`\theta=2\pi\sin\psi`$.
For great circle, not a cone, cylinder.
## Geodesics
<callout color="gray_bg">
	**Def.** Nonconstant parametrized curve $`\gamma:I\to S`$ is a **geodesic** at $`t\in I`$ if
	$$
	\frac{D\gamma'}{dt}(t)=0.
	$$
	$`\forall t\in I`$ ⇒ $`\gamma`$ is a geodesic.
</callout>
접선 벡터가 곡면 위에서 자기 자신에 대해 parallel.
**Ex.** Great circles on $`S^2`$ are geodesics.
$`\gamma`$ geodesic ⇒ $`\gamma'`$ parallel ⇒ $`|\gamma'(t)|`$ is constant in $`t`$ ⇒ $`\gamma`$ has **constant speed**.
**Ex. ① plane (**$`xy`$**-plane)**
$$
\gamma(t)=(x(t),y(t)),\qquad0=\frac{D\gamma'}{dt}=\frac{d\gamma'}{dt}=\gamma''
$$
⇔ $`x,y`$ are linear functions of $`t`$ ⇒ $`\gamma`$ parametrizes a straight line.
평면의 geodesic은 straight line.
**② cylinder** $`x^2+y^2=1`$. Local isometry to $`\mathbb R^2`$.
Geodesics on the cylinder are helices, parallel circles, straight vertical lines. 이런 식으로 geodesic을 찾을 수 있음.
Between any two points on the cylinder, ∃ geodesic connecting them.
$`\forall v\in T_p(\text{cylinder})`$, ∃ geodesic shooting off from $`p`$ with initial velocity equal to $`v`$.
**③ spheres**: great circles.
![](notion-file-block://1ed26741-2d4e-40a3-b991-9f2a9d98f369/907c87aa-5df5-4b16-9b8d-1798aa078989?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-8.png)
## Geodesic curvature
$`\alpha:I\to S`$, $`w`$: diff'ble field of **unit vectors** along $`\alpha`$. $`|w(t)|=1`$, $`\forall t\in I`$.
Then $`dw/dt\perp w`$ ⇒ $`Dw/dt\perp N,w`$.
$$
\frac{Dw}{dt}=\lambda(t)(N(\alpha(t))\wedge w(t)),\qquad\lambda:I\to\mathbb R.
$$
$`\lambda(t)`$: **algebraic value** of $`Dw/dt`$ at $`t`$, denoted $`[Dw/dt]`$.
<callout color="gray_bg">
	**Def.** $`\alpha`$ parametrized by arclength $`s`$.
	$$
	\left[\frac{D\alpha'(s)}{ds}\right]=k_g(s)
	$$
	is **geodesic curvature** of $`\alpha`$ at $`\alpha(s)`$.
</callout>
$`\alpha`$ is geodesic $`\iff k_g=0`$ along $`\alpha`$.
Recall $`\alpha''=kn`$.
$$
k_g^2+k_n^2=k^2.
$$
$`D\alpha'/ds=k_g\,N\wedge\alpha'`$.
Change orientation of $`S`$ → $`k_g`$ changes sign.
Change orientation of $`\alpha`$ → $`k_g`$ changes sign.
Given $`\alpha:I\to S`$ (not necessarily param. by arclength), $`v,w`$: two diff'ble vector fields along $`\alpha`$ s.t. $`|v(t)|=|w(t)|=1`$, $`\forall t\in I`$.
$`\varphi(t)`$: angle between $`v(t),w(t)`$.
$`\overline v`$: vector field along $`\alpha`$ s.t. $`\{v,\overline v\}`$ is a positively oriented orthonormal basis along $`\alpha`$.
Then $`v`$ is diff'ble ⇔ $`\overline v`$ is diff'ble.
Let $`w(t)=a(t)v(t)+b(t)\overline v(t)`$, $`a^2+b^2=1`$, $`a,b`$: diff'ble functions of $`t`$.
**Lemma / claim.**
$$
\varphi(t)=\varphi(t_0)+\int_{t_0}^t(ab'-ba')\,dt,
$$
$`\varphi`$ is diff'ble. $`[t_0,t_1]`$의 $`I`$ 안에서 differentiability를 extend할 수 있다.
$`a(t)=\cos\varphi(t)`$, $`b(t)=\sin\varphi(t)`$.
<callout color="gray_bg">
	**Lemma.**
	$$
	\frac{d\varphi}{dt}=\left[\frac{Dw}{dt}\right]-\left[\frac{Dv}{dt}\right].
	$$
</callout>
**Cor.** $`\alpha:I\to S`$ parametrized by arclength, $`v`$ a parallel vector field along $`\alpha`$.
$`\varphi(s)`$: angle from $`v(s)`$ to $`\alpha'(s)`$.
$$
\frac{d\varphi}{ds}=\left[\frac{D\alpha'}{ds}\right]-\underbrace{\left[\frac{Dv}{ds}\right]}_{0}=k_g.
$$
Independent of choice of $`v`$.
## Orthogonal parametrization에서의 parallel transport
**Prop.** $`X(u,v)`$: orthogonal positively oriented parametrization ($`F=0`$) of nbhd of $`S`$.
$`\alpha(t)=X(u(t),v(t))`$; $`w(t)`$: diff'ble field of unit vectors along the curve.
$$
e_1=\frac{X_u}{\sqrt E},\qquad e_2=\frac{X_v}{\sqrt G},\qquad N=e_1\wedge e_2.
$$
$`\{e_1,e_2\}`$: orthonormal basis of $`T_pS`$. $`\varphi`$: angle from $`e_1`$ ($`X_u`$) to $`w`$.
By lemma,
$$
\left[\frac{Dw}{dt}\right]=\left[\frac{De_1}{dt}\right]+\frac{d\varphi}{dt}.
$$
<details>
<summary>계산</summary>
	$$
								\left[\frac{De_1}{dt}\right]=\left\langle\frac{de_1}{dt},N\wedge e_1\right\rangle
=\left\langle\frac{de_1}{dt},e_2\right\rangle
=\langle(e_1)_u,e_2\rangle\frac{du}{dt}+\langle(e_1)_v,e_2\rangle\frac{dv}{dt}.
	$$
	$$
								F=0\Rightarrow\langle X_u,X_v\rangle_u=0=\langle X_{uu},X_v\rangle+\langle X_u,X_{uv}\rangle
\Rightarrow\langle X_{uu},X_v\rangle=-\frac12E_v.
	$$
	$$
								\langle(e_1)_u,e_2\rangle
=\left\langle\left(\frac{X_u}{\sqrt E}\right)_u,\frac{X_v}{\sqrt G}\right\rangle
=\left\langle\frac{X_{uu}}{\sqrt E},\frac{X_v}{\sqrt G}\right\rangle
-\frac12E^{-3/2}E_u\left\langle X_u,\frac{X_v}{\sqrt G}\right\rangle
=-\frac{E_v}{2\sqrt{EG}}.
	$$
	비슷하게 $`\langle(e_1)_v,e_2\rangle=G_u/(2\sqrt{EG})`$.
	$$
	\left[\frac{De_1}{dt}\right]=-\frac{E_v}{2\sqrt{EG}}\frac{du}{dt}+\frac{G_u}{2\sqrt{EG}}\frac{dv}{dt}.
	$$
</details>
<callout color="gray_bg">
	$$
	\left[\frac{Dw}{dt}\right]=-\frac{E_v}{2\sqrt{EG}}\frac{du}{dt}+\frac{G_u}{2\sqrt{EG}}\frac{dv}{dt}+\varphi'.
	$$
</callout>
이를 이용해서 parallel transport의 존재성, 유일성을 orthogonal, positively oriented param.에서 증명할 수 있다.
$$
w\text{ parallel}\iff\left[\frac{Dw}{dt}\right]=0
\iff\varphi'=\frac{E_v}{2\sqrt{EG}}\frac{du}{dt}-\frac{G_u}{2\sqrt{EG}}\frac{dv}{dt}=:B(t)
$$
$$
\iff\varphi(t)=\varphi(t_0)+\int_{t_0}^tB(t)\,dt.
$$
엄밀하게 하려면 $`\alpha(I)`$가 coordinate nbhd에 포함되지 않는다면 $`I`$의 compactness를 통해 $`I_1\sim I_\ell`$ finite subset으로 나누고 각각에 적용.
## Equation of geodesics
$`\gamma:I\to S`$, $`X:U\subset\mathbb R^2\to S`$: param. of a nbhd $`V`$ of $`\gamma(t_0)`$ in $`S`$.
Open $`J\subset I`$, $`t_0\in J`$, $`\gamma(J)\subset V`$.
$$
\gamma'(t)=u'(t)X_u+v'(t)X_v.
$$
$`\gamma`$ is a geodesic $`\iff D\gamma'/dt=0`$:
<callout color="gray_bg">
	$$
								\begin{cases}
u''+\Gamma^1_{11}(u')^2+2\Gamma^1_{12}u'v'+\Gamma^1_{22}(v')^2=0,\\
v''+\Gamma^2_{11}(u')^2+2\Gamma^2_{12}u'v'+\Gamma^2_{22}(v')^2=0.
\end{cases}
	$$
</callout>
$`Dw/dt`$ 식에서 $`a=u'`$, $`b=v'`$.
## Quiz 9 — Ch. 4.4
Equations of geodesics:
$$
\begin{cases}
u''+\Gamma^1_{11}(u')^2+2\Gamma^1_{12}u'v'+\Gamma^1_{22}(v')^2=0,\\
v''+\Gamma^2_{11}(u')^2+2\Gamma^2_{12}u'v'+\Gamma^2_{22}(v')^2=0.
\end{cases}
$$
<callout color="gray_bg">
	**Prop.** Given $`p\in S`$, $`w\in T_pS`$, $`w\ne0`$, ∃ $`\varepsilon>0`$, unique parametrized geodesic $`\gamma:(-\varepsilon,\varepsilon)\to S`$ with $`\gamma(0)=p`$, $`\gamma'(0)=w`$.
</callout>
ODE theory.
Geodesic이 $`S`$ 위에서 정의되기 때문에 존재성의 최대 구간이 무조건 $`(-\infty,\infty)`$는 아니다. $`S`$를 벗어날 수 있음.
![](notion-file-block://5b3f46c4-8360-4c0b-b283-1a35ed4ec28b/b7b8a74a-bd11-482e-a757-5cf198d4ab43?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-9.png)
## Geodesics on a surface of revolution
$$
x=f(v)\cos u,\quad y=f(v)\sin u,\quad z=g(v),\quad
0<u<2\pi,\quad a<v<b,\quad f>0.
$$
$`(f,g)`$: regular. 세로선: meridian / 가로선: parallel.
Remark. Christoffel symbols:
$$
\begin{cases}\Gamma^1_{11}E+\Gamma^2_{11}F=\frac12E_u,\\
\Gamma^1_{11}F+\Gamma^2_{11}G=F_u-\frac12E_v,\end{cases}
$$
$$
\begin{cases}\Gamma^1_{12}E+\Gamma^2_{12}F=\frac12E_v,\\
\Gamma^1_{12}F+\Gamma^2_{12}G=\frac12G_u,\end{cases}
\qquad
\begin{cases}\Gamma^1_{22}E+\Gamma^2_{22}F=F_v-\frac12G_u,\\
\Gamma^1_{22}F+\Gamma^2_{22}G=\frac12G_v.\end{cases}
$$
$$
E=f^2,\quad F=0,\quad G=(f')^2+(g')^2,
$$
$$
E_u=0,\ E_v=2ff',\ F_u=F_v=0,\ G_u=0,\ G_v=2f'f''+2g'g''.
$$
⇒ equations of geodesics:
$$
\begin{cases}
u''+\dfrac{2ff'}{f^2}u'v'=0,\\
v''-\dfrac{ff'}{(f')^2+(g')^2}(u')^2+\dfrac{f'f''+g'g''}{(f')^2+(g')^2}(v')^2=0.
\end{cases}
$$
**① meridians**: $`u=\mathrm{const}`$, $`v=v(s)`$ param. by arclength $`s`$.
$$
v''+\frac{f'f''+g'g''}{(f')^2+(g')^2}(v')^2=0.
$$
First fundamental form:
$$
1=E\left(\frac{du}{ds}\right)^2+2F\frac{du}{ds}\frac{dv}{ds}+G\left(\frac{dv}{ds}\right)^2
=((f')^2+(g')^2)(v')^2.
$$
$$
(v')^2=\frac1{(f')^2+(g')^2}.
$$
Derivate:
$$
2v'v''=-\frac{2(f'f''+g'g'')}{((f')^2+(g')^2)^2}v'
=-\frac{2(f'f''+g'g'')}{(f')^2+(g')^2}(v')^3.
$$
Same: eq. of geodesic을 만족. ∴ **meridians are geodesics**.
**② not all parallels are geodesics**. $`v=\mathrm{const}`$ + equation:
$$
\begin{cases}u''=0\iff u'=\mathrm{const},\\
-\dfrac{ff'}{(f')^2+(g')^2}(u')^2=0.\end{cases}
$$
Def. ⇒ constant curve ×. $`u'\ne0`$ ⇒ $`f'=0`$.
Rotation axis와 tangent line이 평행한 parallel만 geodesic.
**Ex. sphere**: 위도 원은 not geodesic, 적도는 geodesic.
**③ neither meridians nor parallels**
$$
\begin{cases}u''+\dfrac{2f'}f u'v'=0,\quad\text{①}\\
v''-\dfrac{ff'}{(f')^2+(g')^2}(u')^2+\dfrac{f'f''+g'g''}{(f')^2+(g')^2}(v')^2=0.\quad\text{②}\end{cases}
$$
$$
\text{①}\iff f^2u''+2ff'u'v'=(f^2u')'=0\iff f^2u'=c\ne0.
$$
$$
\text{②}\Rightarrow2v'v''((f')^2+(g')^2)+2(v')^3(f'f''+g'g'')=\frac{2f'c^2}{f^3}v'.
$$
Left side $`=[(v')^2((f')^2+(g')^2)]'`$; right side $`=(-c^2/f^2)'=-(f^2(u')^2)'`$.
$$
\iff f^2(u')^2+(v')^2((f')^2+(g')^2)=\mathrm{const}.
$$
$`u'\ne0`$ ⇒ let $`u=u(s)`$, $`s=s(u)`$, $`v=v(s)=v(s(u))`$.
**Remark. inverse function thm.** $`F:\mathbb R^n\to\mathbb R^n`$이 다음 조건을 만족하면 ∃ $`x_0`$에서 국소적으로 $`F^{-1}`$을 가진다: ① $`F`$는 $`x_0`$에서 미분 가능, ② Jacobian $`J_F(x_0)`$ invertible.
② ⇔ $`E(u')^2+G(v')^2=\mathrm{const}`$.
Parametrizing the geodesic by arc length $`s`$:
$$
\langle u'X_u+v'X_v,u'X_u+v'X_v\rangle=1.
$$
$$
f^2\left(\frac{du}{ds}\right)^2+((f')^2+(g')^2)\left(\frac{dv}{du}\right)^2\left(\frac{du}{ds}\right)^2=1.
$$
① ⇒ $`f^2\dfrac{du}{ds}=c`$, $`\dfrac{du}{ds}=c/f^2`$, $`\dfrac{ds}{du}=f^2/c`$.
$$
f^2+((f')^2+(g')^2)\left(\frac{dv}{du}\right)^2=\frac{f^4}{c^2}
$$
$$
\iff\frac{dv}{du}=\pm\sqrt{\frac{f^4/c^2-f^2}{(f')^2+(g')^2}}
=\pm\frac fc\sqrt{\frac{f^2-c^2}{(f')^2+(g')^2}}.
$$
$$
\therefore u=c\int\frac1f\sqrt{\frac{(f')^2+(g')^2}{f^2-c^2}}\,dv+\mathrm{const},\qquad c\ne0.
$$
## Clairaut's relation
$`f^2u'=c`$에 대해서 $`\theta`$를 geodesic과 parallel의 각이라 하면 ($`0\le\theta\le\pi`$)
$$
\cos\theta=\frac{\langle X_u,X_uu'+X_vv'\rangle}{|X_u|\cdot1}=|X_u|\,u'=fu'.
$$
<callout color="gray_bg">
	$$
	f\cos\theta=c.
	$$
	**Clairaut's relation**
</callout>
$`f\uparrow`$, $`\theta\uparrow`$ / $`f\downarrow`$, $`\theta\downarrow`$: $`\cos\theta`$ decreases. 일종의 모멘텀 법칙.
**Ex. cylinder**: $`\theta=\mathrm{const}`$ along any helix!
**Ex. paraboloid**: 꼭짓점과의 거리 (stand up). (원본의 하단 메모는 아래 원본 대조에서 함께 보존.)
# Ch. 4.5 — Gauss–Bonnet
Geometry ⇒ topology. $`S`$: regular surface.
![](notion-file-block://26d92f26-bb3b-4883-8c7d-08e3396c6b02/8ad06c14-6168-4c3b-9366-04e9c13af243?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-10.png)
## Simple closed piecewise regular parametrized curves
<callout color="gray_bg">
	**Def.** $`\alpha:[0,\ell]\to S`$ if $`\alpha(0)=\alpha(\ell)`$, $`\alpha(t_1)\ne\alpha(t_2)`$ unless $`t_1=t_2`$ or $`t_1,t_2\in\{0,\ell\}`$, and ∃ $`t_0=0<t_1<\cdots<t_{k+1}=\ell`$ s.t. $`\alpha`$ is diff'ble and regular in each $`[t_i,t_{i+1}]`$, $`i=0,\ldots,k`$, and continuous on $`[0,\ell]`$.
</callout>
<callout color="gray_bg">
	**Def. simple region** ($`S`$: oriented)
	Connected open set $`R\subset S`$ s.t. $`R`$ is homeomorphic to the disk $`\{(x,y)\in\mathbb R^2\mid x^2+y^2<1\}`$, and $`\partial R`$ (boundary) is the trace of a simple closed piecewise regular parametrized curve $`\alpha:I\to S`$.
</callout>
$`\alpha`$ is **positively oriented** if, as we walk with our head in $`N`$-direction, $`R`$ is on our left. 시계는 positively oriented ×.
## (Local) Gauss–Bonnet
$`X:U\to S`$: isothermal parametrization (locally always exists), $`E=G=\lambda^2`$, $`F=0`$.
$`U`$ is homeomorphic to an open disk and $`X`$ is positively oriented.
$`R\subset X(U)`$: simple region. $`\alpha:I\to S`$ simple closed, piecewise regular, positively oriented, param. by arclength, $`\partial R=\alpha(I)`$.
$`\alpha(s_0),\ldots,\alpha(s_k)`$: **vertices**.
$`0\le s_0<s_1<\cdots<s_k\le\ell`$, $`\alpha|_{(s_i,s_{i+1})}`$ regular and diff'ble ($`s_{k+1}=s_0`$).
$`\theta_i`$: **external angle** at $`\alpha(s_i)`$, from $`\alpha'(s_i-0)`$ to $`\alpha'(s_i+0)`$, given orientation of basis $`\{\alpha'(s_i-0),\alpha'(s_i+0),N\}`$.
If $`\alpha'(s_i-0)=-\alpha'(s_i+0)`$, $`\theta_i=\pi`$ or $`-\pi`$ ⇒ **cusp**.
보통 $`\alpha'(s_i-0)`$에 $`-i`$ 방향인 positively oriented isothermal parametrization at $`\alpha(s_i)`$로 생각하면, 위에서 돌아오면 $`\theta=-\pi`$, 아래에서 돌아오면 $`\theta=+\pi`$. $`N`$ points out of this picture.
<callout color="gray_bg">
	**Thm. (Local Gauss–Bonnet)**
	$`S`$: oriented regular surface. $`\alpha:[0,\ell]\to S`$ parametrized by arclength, simple closed, piecewise regular, positively oriented, bounding a simple region $`R`$, which is in the image of an isothermal parametrization $`X:U\subset\mathbb R^2\to S`$.
	$$
	\sum_{i=0}^k\int_{s_i}^{s_{i+1}}k_g\,ds+\iint_RK\,d\sigma+\sum_{i=0}^k\theta_i=2\pi.
	$$
	$`k_g`$: geodesic curvature inside $`S`$.
</callout>
내용을 간단하게 만들기 위해 (constant quantity) of simple closed curves, using Green's thm.
The total (signed) angle against the $`x`$-axis: **winding number** of a simple closed piecewise regular curve ⇒ always equal to $`2\pi`$.
**Ex. ① **$`\mathbb R^2`$
$$
\theta_1+\theta_2+\theta_3=2\pi,\qquad K=0,\quad k_g=0.
$$
곡면상에서의 곡률.
**② **$`S^2`$ — geodesic triangle, all edges are parts of geodesics = great circles on $`S^2`$.
$`K=1`$, $`k_g=0`$.
$$
\iint_RK\,d\sigma=\iint_Rd\sigma=\operatorname{Area}(R)=\varphi,
$$
$$
\sum\theta_i=\frac\pi2+\frac\pi2+\pi-\varphi=2\pi-\varphi
\quad\Rightarrow\quad2\pi.
$$
$$
\iint_RK\,d\sigma=\sum_{i=1}^3\beta_i-\pi\quad\text{(내각합)}.
$$
<details>
<summary>Local Gauss–Bonnet — proof</summary>
	For a unit length vector field $`w=u'X_u+v'X_v`$ along a regular curve, $`X`$: orthogonal,
	$$
	\left[\frac{Dw}{dt}\right]=-\frac{E_v}{2\sqrt{EG}}u'+\frac{G_u}{2\sqrt{EG}}v'+\frac{d\varphi}{dt},
	$$
	$`\varphi`$: angle from $`X_u`$ to $`w`$.
	For $`w=\alpha'`$ on $`(s_i,s_{i+1})`$,
	$$
	\left[\frac{D\alpha'}{ds}\right]=k_g=\frac1{2\sqrt{EG}}(G_uv'-E_vu')+\frac{d\varphi_i}{ds}.
	$$
	$`\varphi_i`$: $`\varphi`$ on $`(s_i,s_{i+1})`$.
	$$
							\sum_{i=0}^k\int_{s_i}^{s_{i+1}}k_g\,ds
=\underbrace{\sum_{i=0}^k\int_{s_i}^{s_{i+1}}\frac{G_uv'-E_vu'}{2\sqrt{EG}}\,ds}_{\mathrm I}
+\underbrace{\sum_{i=0}^k\int_{s_i}^{s_{i+1}}\frac{d\varphi_i}{ds}\,ds}_{\mathrm {II}}.
	$$
	**Green's thm.** Given a simple planar region $`A`$ with positively oriented piecewise diff'ble boundary curve, and diff'ble vector field $`(P,Q)`$,
	$$
							\int P\,du+Q\,dv
=\sum_{i=0}^k\int_{s_i}^{s_{i+1}}(Pu'+Qv')\,ds
=\iint_A(Q_u-P_v)\,du\,dv.
	$$
	Apply to I:
	$$
							\mathrm I=\sum_{i=0}^k\int_{s_i}^{s_{i+1}}\frac{G_uv'-E_vu'}{2\sqrt{EG}}\,ds
=\iint_{X^{-1}(R)}\left\{\left(\frac{G_u}{2\sqrt{EG}}\right)_u+\left(\frac{E_v}{2\sqrt{EG}}\right)_v\right\}\,du\,dv.
	$$
	Since $`X`$ is isothermal, $`E=G=\lambda^2`$, $`F=0`$,
	$$
							\left(\frac{E_v}{2\sqrt{EG}}\right)_v+\left(\frac{G_u}{2\sqrt{EG}}\right)_u
=\left(\frac{2\lambda\lambda_v}{2\lambda^2}\right)_v+\left(\frac{2\lambda\lambda_u}{2\lambda^2}\right)_u
=\left(\frac{\lambda_v}{\lambda}\right)_v+\left(\frac{\lambda_u}{\lambda}\right)_u
	$$
	$$
							=\frac{\lambda_{vv}}\lambda-\frac{\lambda_v^2}{\lambda^2}+\frac{\lambda_{uu}}\lambda-\frac{\lambda_u^2}{\lambda^2}
=\frac{\Delta\lambda}\lambda-\frac{|\nabla\lambda|^2}{\lambda^2}.
	$$
	$`\nabla\lambda`$: 내적이라 요소별로.
	$$
	\Rightarrow\mathrm I=\iint_{X^{-1}(R)}\left(\frac{\Delta\lambda}\lambda-\frac{|\nabla\lambda|^2}{\lambda^2}\right)\,du\,dv.
	$$
	Look at $`\iint_RK\,d\sigma`$.
	Note:
	$$
	-EK=(\Gamma^2_{11})_v-(\Gamma^2_{12})_u+\Gamma^1_{11}\Gamma^2_{12}+\Gamma^2_{11}\Gamma^2_{22}-\Gamma^1_{12}\Gamma^2_{11}-\Gamma^2_{12}\Gamma^2_{12}.
	$$
	Exercise 4.3.2: for an isothermal $`E=G=\lambda^2`$, $`F=0`$,
	$$
							K=-\frac1{2\lambda^2}\Delta\log(\lambda^2)
=-\frac1{2\lambda^2}\nabla\cdot\nabla\log(\lambda^2)
=-\frac1{2\lambda^2}\nabla\cdot\left(\frac{2\lambda\nabla\lambda}{\lambda^2}\right)
	$$
	$$
							=-\frac1{\lambda^2}\left(\frac{\lambda\Delta\lambda}{\lambda^2}+\frac{|\nabla\lambda|^2}{\lambda^2}-\frac{2|\nabla\lambda|^2}{\lambda^2}\right)
=-\frac1{\lambda^2}\left(\frac{\Delta\lambda}\lambda-\frac{|\nabla\lambda|^2}{\lambda^2}\right).
	$$
	$$
							\therefore-K\lambda^2=\frac{\Delta\lambda}\lambda-\frac{|\nabla\lambda|^2}{\lambda^2}
=\left(\frac{E_v}{2\sqrt{EG}}\right)_v+\left(\frac{G_u}{2\sqrt{EG}}\right)_u.
	$$
	$$
							\sum_{i=0}^k\int_{s_i}^{s_{i+1}}k_g\,ds=\mathrm I+\mathrm {II}
=-\iint_{X^{-1}(R)}K\lambda^2\,du\,dv+\sum_{i=0}^k\int_{s_i}^{s_{i+1}}\varphi_i'\,ds
	$$
	$$
	=-\iint_RK\,d\sigma+\sum_{i=0}^k\bigl(\varphi_i(s_{i+1})-\varphi_i(s_i)\bigr).
	$$
	$`\lambda^2=\sqrt{EG-F^2}`$.
	$$
							\Rightarrow\sum_{i=0}^k\int_{s_i}^{s_{i+1}}k_g\,ds+\iint_RK\,d\sigma
=\sum_{i=0}^k\bigl(\varphi_i(s_{i+1})-\varphi_i(s_i)\bigr).
	$$
	Angle measured from $`X_u`$.
	Note: **Thm. of turning tangents**, Ch. 5-7:
	$$
	\sum_{i=0}^k\bigl(\varphi_i(s_{i+1})-\varphi_i(s_i)\bigr)+\sum_{i=0}^k\theta_i=2\pi.
	$$
</details>
## Global Gauss–Bonnet
Need to define topological invariant **Euler characteristic** $`\chi`$.
3 holes ⇒ $`g=\text{genus}=\#\text{ of holes}`$, $`\chi=2-2g`$.
Given regular surface $`S`$ (not necessarily oriented), ∃ **triangulation** for $`R\subset S`$ compact, connected region s.t. boundary $`\partial R`$ is a finite disjoint union of simple closed piecewise regular curves.
**Fact 1.** We can find $`T_1,\ldots,T_n`$ compact, connected regions with 3 vertices s.t.
$$
\bigcup_{i=1}^nT_i=R,
$$
$`T_i\cap T_j\ne\varnothing`$ only if $`T_i,T_j`$ share a common edge or vertex.
![](notion-file-block://1a6f6da5-6555-4686-8895-5508116a8713/4940a7dd-7810-4b23-ae8e-cf0e17b42920?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-11.png)
**Fact 2.** $`\{T_1,\ldots,T_n\}`$ triangulation of $`R`$.
$$
F-E+V
$$
($`\#`$ of faces − $`\#`$ of edges + $`\#`$ of vertices) is always the same, independent of choice of triangulation.
<callout color="gray_bg">
	**Def. Euler characteristic** of $`R`$:
	$$
	\chi(R)=F-E+V.
	$$
</callout>
**Ex.** One triangle: $`F=1,E=3,V=3`$, $`\chi(R)=1`$. Subdivided triangle: $`F=3,E=6,V=4`$, $`\chi(R)=1`$.
![](notion-file-block://c57666a6-2605-4cb3-8432-1fdb92292a0b/8f089292-74fa-426b-9398-fc779b4eb05c?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-12.png)
**Fact 3.** If $`S`$ is a compact connected regular surface, then $`\chi(S)`$ is even, $`\chi(S)=2-2g`$.
$`\chi`$ (or $`g`$)가 $`S`$의 topological type을 결정한다: if $`\chi(S)=\chi(S_1)`$, then they are diffeomorphic.
**Ex. ① **$`S^2`$: $`F=2,E=3,V=3`$.
$$
F-E+V=2-3+3=2,\qquad\chi(S^2)=2.
$$
**② **$`T^2`$: $`F=2,E=3,V=1`$, $`\chi(T^2)=0`$.
Given $`R\subset S`$ and a triangulation, we can make finer and finer $`\{T_1,\ldots,T_n\}`$ s.t. $`T_i`$ is inside the image of (positively oriented) parametrization $`X_i`$.
⇒ We can integrate a function $`f`$ over each $`T_i`$.
**Fact 4.**
$$
\sum_{i=1}^n\iint_{X_i^{-1}(T_i)}f(u_i,v_i)\sqrt{E_iG_i-F_i^2}\,du_i\,dv_i
$$
is independent of choice of triangulation & parametrization.
<callout color="gray_bg">
	**Thm. (Gauss–Bonnet)**
	$`S`$: compact oriented regular surface.
	Let $`C_1,\ldots,C_n`$ be the connected components of $`\partial R`$, each a closed, simple, piecewise regular curve given positive orientation, param. by arclength.
	Let $`\theta_1,\ldots,\theta_p`$ be all external angles of $`C_1,\ldots,C_n`$. Then
	$$
	\sum_{i=1}^n\int_{C_i}k_g\,ds+\iint_RK\,d\sigma+\sum_{j=1}^p\theta_j=2\pi\chi(R).
	$$
	If $`R=S`$, then
	$$
	\iint_SK\,d\sigma=2\pi\chi(S).
	$$
</callout>
<details>
<summary>Global Gauss–Bonnet — proof</summary>
	$`R`$을 triangle이 isothermal param.의 이미지에 있도록 triangulation한다 (positive orientation).
	Apply local GB to each triangle $`T_j`$:
	$$
	\int_{\partial T_j}k_g\,ds+\iint_{T_j}K\,d\sigma+(\theta_{j1}+\theta_{j2}+\theta_{j3})=2\pi.
	$$
	For all $`T_j`$,
	$$
							\sum_{i=1}^n\int_{C_i}k_g\,ds+\iint_RK\,d\sigma+
\sum_{j=1}^F(\theta_{j1}+\theta_{j2}+\theta_{j3})=2\pi F.
	$$
	Orientation이 반대이기 때문에 shared edges에서 $`k_g`$의 sign이 바뀐다 ⇒ get cancellation.
	Interior angles $`\varphi_{jk}=\pi-\theta_{jk}`$, $`j=1,\ldots,F`$, $`k=1,2,3`$.
	$$
	\sum_{j,k}\varphi_{jk}=3\pi F-\sum_{j,k}\theta_{jk}.
	$$
	Denote: $`E_e/E_i`$: $`\#`$ of external / internal edges; $`V_e/V_i`$: $`\#`$ of external / internal vertices. External: part of $`\partial R`$.
	**Claim 1.** $`E_e=V_e`$.
	**Claim 2.** $`3F=2E_i+E_e`$.
	By induction on $`F`$, $`F=1`$: $`E_i=0`$, $`E_e=3`$. For $`F\ge2`$, $`T_j`$ has an external edge $`e`$.
	Case 1: induction hypothesis for $`F-1`$,
	$$
	3(F-1)=2(E_i-1)+(E_e+1)\Rightarrow3F-3=2E_i+E_e-1.
	$$
	Case 2:
	$$
	3(F-1)=2(E_i-1)+(E_e-1)\Rightarrow3F-3=2E_i+E_e-3.
	$$
	이제 남은 것은
	$$
							\sum_{j=1}^p\theta_j=\sum_{j=1}^F(\theta_{j1}+\theta_{j2}+\theta_{j3})-2\pi\chi(R)
=\sum_{j,k}\theta_{jk}-2\pi(F-E+V).
	$$
	$$
							\sum_{j,k}\varphi_{jk}=3\pi F-\sum_{j,k}\theta_{jk}
\overset{\text{Claim 2}}=\pi(2E_i+E_e)-\sum_{j,k}\theta_{jk}.
	$$
	External $`V_{er}`$: $`\#`$ of external vertices on the regular part of $`\partial R`$; $`V_{ec}`$: $`\#`$ of rest.
	$$
	\sum_{j,k}\varphi_{jk}=2\pi V_i+\pi V_{er}+\pi V_{ec}-\sum_{j=1}^p\theta_j.
	$$
	$$
							\Rightarrow\sum_{j,k}\theta_{jk}
=\sum_{j=1}^p\theta_j+2\pi E-\pi E_e-2\pi V_i-\pi V_{er}-\pi V_{ec}
	$$
	$$
							=\sum_{j=1}^p\theta_j+2\pi E-2\pi(V_i+V_e)
=\sum_{j=1}^p\theta_j+2\pi(E-V).
	$$
</details>
## Corollaries
**Cor. 1**
1. If compact regular surface has $`K>0`$, then it is homeomorphic to $`S^2`$.
2. If compact surface is homeomorphic to $`S^2`$, then no way to deform it differentiably to have $`K<0`$ everywhere.
**Cor. 2** If compact connected regular surface $`S`$ has $`K>0`$ everywhere, then any two closed geodesics intersect.
Intersect × → 두 geodesic은 $`S^2`$ 위 → 이 둘이 topologically 하게 cylinder를 이룸 → GB ⇒ $`\iint K\,d\sigma=0`$ → 모순.
**Jordan curve thm.** Simple closed curve in $`\mathbb R^2`$이 $`\mathbb R^2`$을 topologically disk인 interior region과 noncompact exterior region으로 나눈다.
**Cor. 3** If connected regular surface $`S`$ has $`K\le0`$ everywhere, then two geodesics $`\gamma_1,\gamma_2`$ starting from $`p\in S`$ and $`\gamma_1'(p)\ne\gamma_2'(p)`$ cannot meet again to form a region homeomorphic to a disk.
$`\chi(R)=1`$, $`1-2+2=1`$.
⇒ 안 만나거나 there is some topology between them.
**Cor. 4** Topological cylinder with $`K<0`$ (ex. catenoid) has at most one simple closed geodesic.
**Cor. 5** For $`S\cong S^2`$, $`K>0`$, simple closed geodesic $`\Gamma`$ on $`S`$.
$`\Gamma`$ separates $`S`$ into two regions $`U,V`$.
$$
S^2=N(U)\cup N(V),\qquad\operatorname{Area}(N(U))=\operatorname{Area}(N(V)).
$$
![](notion-file-block://27b78ca6-3178-48ac-97df-f6d2d6228b6a/fce27264-83eb-464b-b241-4aa6380e79a5?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-13.png)
**Cor. 6** For a geodesic triangle,
$$
\sum(\text{interior angles})=3\pi-\sum(\text{exterior angles})
\begin{cases}>\pi&\text{if }K>0,\\=\pi&\text{if }K=0,\\<\pi&\text{if }K<0.\end{cases}
$$
## Singular points and index of a vector field
$`S`$: oriented regular surface, $`v`$: diff'ble vector field on $`S`$.
<callout color="gray_bg">
	**Def.** $`p\in S`$ is a **singular point** of $`v`$ if $`v(p)=0`$.
	**Isolated singular point** if ∃ nbhd of $`p`$ in $`S`$ s.t. $`p`$ is the only singular point.
</callout>
<callout color="gray_bg">
	**Def.** Let $`\alpha:[0,\ell]\to S`$ simple closed piecewise regular curve, positively oriented, $`p`$ in interior region of $`\alpha`$.
	Let $`\varphi`$ be a diff'ble angle function from $`X_u`$ to $`v(t)`$.
	$$
	\varphi(\ell)-\varphi(0)=\int_0^\ell\frac{d\varphi}{dt}\,dt=2\pi I,\qquad I\in\mathbb Z,
	$$
	where $`v(\alpha(0))=v(\alpha(\ell))`$.
	$`I`$: **index of **$`v`$** at **$`p`$.
</callout>
Isolated singular point에서만 index를 다룬다.
![](notion-file-block://7ca379fa-4823-4c3f-935a-e0a83aecc40d/3ba18ffe-99c9-4b33-a44c-fb453859e1a1?space_id=a572f2a2-f7b0-4923-b5c0-74f5db67bcd1&name=dg-diagram-14.png)
**Ex. ①** $`p=(0,0)`$, $`v(x,y)=(-y,x)`$.
$`\alpha`$: unit circle centered at $`p`$, $`\alpha(t)=(\cos t,\sin t)`$, $`0\le t\le2\pi`$.
$$
\varphi(t)=t+\frac\pi2\quad\Rightarrow\quad I=1.
$$
**Remark.** Index is independent of choice of $`\alpha`$ and $`X`$.
**② source** $`p=(0,0)`$, $`v(x,y)=(x,y)`$, $`\alpha(t)=(\cos t,\sin t)`$.
$`\varphi(t)=t`$ ⇒ $`I=1`$.
**Sink** $`v(x,y)=(-x,-y)`$ ⇒ $`I=1`$.
**③ saddle** $`v(x,y)=(x,-y)`$, $`I=-1`$.
If $`S`$ is compact, $`v`$ is a diff'ble vector field on $`S`$ with only isolated singular points ⇒ finitely many singular points $`p_1,\ldots,p_k`$ with index $`I_1,\ldots,I_k`$.
Triangulate $`S=T_1\cup\cdots\cup T_n`$ s.t. each $`T_i`$ is in an isothermal coordinate nbhd, no $`p_1,\ldots,p_k`$ lying on the edges, each $`T_i`$ contains at most one singular point of $`v`$.
Take unit vector $`w_0\in T_{\alpha(0)}S\setminus\{0\}`$. Parallel transport $`w`$ along $`\alpha`$. If $`\psi`$ is angle from $`X_u`$ to $`w`$,
$$
\iint_{T_j}K\,d\sigma=\psi(\ell)-\psi(0),\qquad2\pi I_j=\varphi(\ell)-\varphi(0).
$$
$$
\Rightarrow\iint_{T_j}K\,d\sigma-2\pi I_j
=[\psi(\ell)-\varphi(\ell)]-[\psi(0)-\varphi(0)].
$$
Sum over all $`T_i`$ ⇒ RHS cancel!
$$
\sum_{i=1}^n\iint_{T_i}K\,d\sigma=2\pi\sum_{j=1}^kI_j.
$$
$$
\iint_SK\,d\sigma\overset{\mathrm{GB}}=2\pi\chi(S).
$$
<callout color="gray_bg">
	**Poincaré's theorem**
	$$
	\chi(S)=\sum_{j=1}^kI_j.
	$$
</callout>
**Cor. (Hairy ball thm.)** For $`S^2`$ ($`\chi(S^2)=2`$),
$$
\sum_{j=1}^kI_j=2\ne0.
$$
⇒ Any diff'ble vector field has a singular point.
머리는 빗는 데 소용돌이가 생김 (singular point).
<empty-block/>