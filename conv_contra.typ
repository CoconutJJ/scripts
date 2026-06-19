= What the hell are covariant and contravariant vectors?

I've been interested in learning about Special Relativity and General Relativity
for a while now. However, I haven't got very far into these topics -- the biggest
reason is because I've been quite lazy. It's a lot more entertaining to watch
#link("https://www.youtube.com/@Mahesh_Shenoy")[FloatHeadPhysics] on YouTube than
it is to open up a physics textbook and try to decipher all the mathematical
formalisms. 

But recently, I picked up this book called General Relativity: The Theoretical
Minimum from my local library. It is written by Leonard Susskind and Andre 
Cabannes. Apart from being a good book to read before I sleep every night, it 
provides a very gentle introduction to General Relativity without too many 
formalisms cluttering the core ideas.

However, I was completely lost when they introduced covariant vectors and 
contravariant vectors. The book says that because we are now using curvilinear
coordinates -- where the basis vectors of a coordinate system are no longer 
orthogonal -- we can only perform a tensor contraction on a repeated index, 
where one is "upstairs" (contravariant) and one is "downstairs" (covariant). 
This is best illustrated with the vector dot product

$
  V dot V = V^i V_i
$

This is the only valid form of a tensor contraction for two vectors. We cannot 
contract two upstairs or two downstairs indicies. For instance, the following 
are invalid

$
  V_i V_i quad V^i V^i
$

It then says that we can lower an index with the metric tensor,

$
  V_i = g_(i j)V^j 
$

where 
$
  g_(i j) = e_i dot e_j
$
where ${e_1, e_2, ..., e_n}$ are the basis vectors of a given coordinate system.

Okay. I already have a few questions about what has been introduced.

+ What is the difference between a contravariant and covariant vector?
    - Which one is the one that I'm used to from linear algebra?
+ Why does the metric tensor have this "magical power" of converting between the
  two?
+ Why do we need to make a distinction between a contravariant and covariant 
  vector?

After filling up a few pages of scrap paper, I think I've finally explained it
to myself in a way that clicks. One of the biggest reasons for my confusion is
because I've become so comfortable with working under a orthonormal basis from
linear algebra that I have forgotten the implicit assumptions I was making.

Truthfully, I also had a pretty terrible linear algebra professor back in first 
year undergrad.

I was always taught that the vector dot product is defined as

$
  V dot W = v_1 w_1 + v_2 w_2 + ... + v_n w_n
$

However, this definition already assumes an orthonormal basis. This becomes clear
when we write out $V$ and $W$ as a linear combination of a given coordinate system's
basis vectors.

$
  V = v_1 e_1 + v_2 e_2 + ... + v_n e_n quad W = w_1 e_1 + w_2 e_2 + ... + w_n e_n 
$

We see that $V dot W$ is actually

$
  V dot W &= (v_1 e_1 + v_2 e_2 + ... + v_n e_n) dot (w_1 e_1 + w_2 e_2 + ... + w_n e_n)\
          &= sum_(i)^(n) sum_(j)^(n) v_i w_j (e_i dot e_j)  
$

Ahh, in an orthonormal basis, $e_i dot e_j = 0$ whenever $i != j$ and $1$ 
otherwise. This is why in an orthonormal basis we can write,

$
  V dot W = v_1 w_1 + v_2 w_2 + ... + v_n w_n
$

because all the other terms are $0$. However, in curvilinear coordinates, we must
account for these other terms.

$
  V dot W &= sum_(i)^(n) sum_(j)^(n) v_i w_j (e_i dot e_j)\
          &= sum_(i) v_i w_i (e_i dot e_i) + sum_(i != j) v_i w_j (e_i dot e_j)
$

Examining the expression further, we also see what appears to be the metric tensor!

$
  V dot W &= sum_(i)^(n) sum_(j)^(n) v_i w_j underbrace((e_i dot e_j), g_(i j))\
          &= sum_(i)^(n) sum_(j)^(n) v_i w_j g_(i j)\
$

From this we can see that a contravariant vector is nothing more than just a collection
of numbers (i.e. $v_i$ or $w_i$). We must contract it with the metric tensor to 
produce a meaningful value. We remove the summation symbols per Einstein Index
notation and rewrite $v_i$ as $V^i$ and $w_i$ as $W^i$. It should be noted that
_currently_ these two notations are equivalent to each other. We are not changing
it's meaning.

$
  v_i = V^i " and " w_i = W^i
$

We are left with the following,

$
  V^i W^j g_(i j) 
$

We also see that the covariant vector is just a shorthand way of writing a 
contravariant vector contracted with the metric tensor!

$
  W_i = W^j g_(i j)
$



