#let pd(top, bottom) = $partial_(#bottom) #top$

= Gnomonic Projection

In _#link("https://pbr-book.org/4ed/contents")[Physically Based Rendering: From
  Theory to Implementation]_, Section 4.3.2, the author states that:

Differential area $d A$ on a surface is related to differential solid angle as
viewed from a point $p$ by

$
  d omega = (d A cos theta) / r^2
$

It is not obvious why we have a $(cos theta) / r^2$ correction factor. I was
uncomfortable with just accepting the equation as is and decided to investigate.

#figure[
  #image("gnomonic.svg")

]

We show that the differential area of a surface patch ($d A$),  projected onto
the unit hemisphere, is given by

$
  d Omega = (cos theta) / abs(R)^2 d A
$

where $R$ is the distance from the center of the hemisphere to the differential
surface patch (inverse gnomonic projection) and $theta$ is the angle between the
surface normal and the vector from the surface to the center of the hemisphere.

Before showing this result more rigourously, there is some geometric intuition
behind this formula by approximating it as an orthographic projection onto the
unit hemisphere's tangent plane: Consider a square subset of a plane, with width
$w$, tilted along the $x$ or $y$ axis and angle, $theta$, it makes with the
$x,y$--plane (for simplicity, suppose this is the tangent plane). The
orthographic projection of this tilted plane down onto the $x,y$--plane has area
$w dot w cos theta$. We see that this projected area is scaled by $cos theta$.

Let S be a surface parameterized by $S(u,v) -> RR^3$ and $P in RR^3$
be a point. Then the inverse gnomonically projected area on the unit hemisphere
centered at $P$ is given by the following parameterization

$
  T = (S(u,v) - P)/norm(S(u,v) - P)
$

The differential area of the hemisphere patch is given by

$
  d A & = norm(pd(T, u) times pd(T, v)) d u d v \
$


To make this expression easier to manipulate, we use tensor index notation.
Equivalently,


$
  T_(i) & = (S_i - P_i)/norm(S_j - P_j) \
$

Let $r_i = S_i - P_i$
$
  T_i & = (r_i)/sqrt(r_j dot r_j) \
$

Numerator
#columns(2)[
  $
    pd("", u) r_i & = pd(S_i, u) - pd(P_i, u) \
                            & = pd(S_i, u) \
  $
  #colbreak()
  $
    pd("", v) r_i & = pd(S_i, v) - pd(P_i, v) \
                            & = pd(S_i, v) \
  $
]

Denominator
#columns(2)[
  $
    pd("", u) sqrt(r_j r_j) & = 1 / (2 sqrt(r_j r_j)) dot 2 pd(r_k, u)r_k \
                                      & = r_k / sqrt(r_j r_j) dot pd(r_k, u) \
  $
  #colbreak()
  $
    pd("", v) sqrt(r_j r_j) & = 1 / (2 sqrt(r_j r_j)) dot 2 pd(r_k, v)r_k \
                                      & = r_k / sqrt(r_j r_j) dot pd(r_k, v) \
  $
]

Apply quotient rule: $(f/g)' = (-f g' + f' g)/g^2$. The symbols u and v do not 
appear in the numerator or denominator expressions above except for those in the 
$partial$ operator itself. Thus, the partial derivative computations with 
respect to u and v are the same except for replacing u with v or vica versa.

#columns(2)[
  $
    pd(T_i, u) &= (- r_i dot pd("", u) sqrt(r_j r_j) + pd(r_i, u) dot sqrt(r_j r_j))/(r_l r_l)\
    &= (- r_i dot r_k / sqrt(r_j r_j) dot pd(r_k, u) + pd(r_i, u) dot sqrt(r_j r_j))/(r_l r_l)\
    &= (- r_i dot r_k / norm(r) dot pd(r_k, u) + pd(r_i, u) dot norm(r))/norm(r)^2\
    &= (- r_i dot r_k dot pd(r_k, u) + pd(r_i, u) dot norm(r)^2)/norm(r)^3\
    &= (I / norm(r) - (r r^T) / norm(r)^3) dot pd(S, u)\
    &= 1 / norm(r) (I - (r r^T) / norm(r)^2) dot pd(S, u)
  $
  #colbreak()
  $
    pd(T_i, v) &= (- r_i dot pd("", v) sqrt(r_j r_j) + pd(r_i, v) dot sqrt(r_j r_j))/(r_l r_l)\
    &= (- r_i dot r_k / sqrt(r_j r_j) dot pd(r_k, v) + pd(r_i, v) dot sqrt(r_j r_j))/(r_l r_l)\
    &= (- r_i dot r_k / norm(r) dot pd(r_k, v) + pd(r_i, v) dot norm(r))/norm(r)^2\
    &= (- r_i dot r_k dot pd(r_k, v) + pd(r_i, v) dot norm(r)^2)/norm(r)^3\
    &= (I / norm(r) - (r r^T) / norm(r)^3) dot pd(S, v)\
    &= 1 / norm(r) (I - (r r^T) / norm(r)^2) dot pd(S, v)
  $
]


$epsilon_(i j k)$ is the Levi Civita Symbol.

$
  pd(T, u) times pd(T, v) &= epsilon_(i j k) pd(T_j, u) pd(T_k, v)\
  &= 1/norm(r)^2 dot epsilon_(i j k) (delta_(j l) - (r_j r_l) / norm(r)^2 ) dot pd(S_l, u) dot (delta_(k m) - (r_k r_m) / norm(r)^2 ) dot pd(S_m, v)\
  &= 1/norm(r)^2 dot epsilon_(i j k) (delta_(j l) - (r_j r_l) / norm(r)^2 ) dot (delta_(k m) - (r_k r_m) / norm(r)^2) dot pd(S_m, v) dot pd(S_l, u)\
  &= 1/norm(r)^2 dot epsilon_(i j k) ((r_j r_l r_k r_m) / norm(r)^4 - (r_k r_m) / norm(r)^2 delta_(j l) - (r_j r_l) / norm(r)^2 delta_(k m) + delta_(j l) delta_(k m)) dot pd(S_m, v) dot pd(S_l, u)\
  &= 1/norm(r)^2 dot (underbrace(epsilon_(i j k) (r_j r_l r_k r_m) / norm(r)^4, epsilon_(i j k) r_j r_k = 0) - epsilon_(i j k)(r_k r_m) / norm(r)^2 delta_(j l) - epsilon_(i j k)(r_j r_l) / norm(r)^2 delta_(k m) + epsilon_(i j k)delta_(j l) delta_(k m)) dot pd(S_m, v) dot pd(S_l, u)\
  &= 1/norm(r)^2 dot (-epsilon_(i j k) (r_k r_m) / norm(r)^2 delta_(j l) - epsilon_(i j k)(r_j r_l) / norm(r)^2 delta_(k m) + epsilon_(i j k)delta_(j l) delta_(k m)) dot pd(S_m, v) dot pd(S_l, u)\
  &= 1/norm(r)^2 dot (- epsilon_(i j k) (r_k r_m) / norm(r)^2 delta_(j l) dot pd(S_m, v) dot pd(S_l, u) - epsilon_(i j k)(r_j r_l) / norm(r)^2 delta_(k m) dot pd(S_m, v) dot pd(S_l, u)+ epsilon_(i j k)delta_(j l) delta_(k m)dot pd(S_m, v) dot pd(S_l, u)) \
  &= 1/norm(r)^2 dot (- epsilon_(i j k) (r_k r_m) / norm(r)^2 dot pd(S_m, v) dot pd(S_j, u) - epsilon_(i j k)(r_j r_l) / norm(r)^2 dot pd(S_k, v) dot pd(S_l, u)+ epsilon_(i j k) dot pd(S_k, v) dot pd(S_j, u))\
  // &= 1/norm(r)^2 dot (- (#partial_deriv(S, u) times r)(r dot
  // #partial_deriv(S, v))/norm(r)^2 - (r times #partial_deriv(S, v))(r dot
  // #partial_deriv(S, u))/norm(r)^2 + (#partial_deriv(S, u) times
  // #partial_deriv(S, v))) \
$

To simplify things, let

$
  A_(j k) = (r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u)
$

Then we have,

$
  & = 1/norm(r)^2 dot (- epsilon_(i j k) A_(j k) + epsilon_(i j k) dot pd(S_k, v) dot pd(S_j, u)) \
  & = -1/norm(r)^2 epsilon_(i j k) (A_(j k) - pd(S_k, v) pd(S_j, u)) \
$


$
  norm(pd(T, u) times pd(T, v))
  &= sqrt(1/norm(r)^2 epsilon_(i j k) (A_(j k) - pd(S_k, v) pd(S_j, u)) 1/norm(r)^2 epsilon_(i n o) (A_(n o) - pd(S_o, v) pd(S_n, u)))\
  &= sqrt(1/norm(r)^4 epsilon_(i j k) epsilon_(i n o) (A_(j k) - pd(S_k, v) pd(S_j, u)) (A_(n o) - pd(S_o, v) pd(S_n, u)))\
  &= sqrt(1/norm(r)^4 (delta_(j n) delta_(k o) - delta_(j o) delta_(k n)) (A_(j k) - pd(S_k, v) pd(S_j, u)) (A_(n o) - pd(S_o, v) pd(S_n, u)))\
  &= sqrt(1/norm(r)^4 (delta_(j n) delta_(k o) A_(j k) - delta_(j o) delta_(k n) A_(j k) - delta_(j n) delta_(k o) pd(S_k, v) pd(S_j, u) + delta_(j o) delta_(k n) pd(S_k, v) pd(S_j, u))(A_(n o) - pd(S_o, v) pd(S_n, u)))\
  &= sqrt(1/norm(r)^4 (A_(n o) - A_(o n) - pd(S_o, v) pd(S_n, u) + pd(S_n, v) pd(S_o, u))(A_(n o) - pd(S_o, v) pd(S_n, u)))\
  &= 1/norm(r)^2sqrt(
    A_(n o)A_(n o) - 2A_(n o) pd(S_o, v) pd(S_n, u) -A_(o n) A_(n o) + A_(o n)pd(S_o, v) pd(S_n, u) +\
    norm(pd(S, v))^2 norm(pd(S, u))^2 + A_(n o) pd(S_n, v) pd(S_o, u)- (pd(S, v) dot pd(S, u))^2
  )
$

We expand and evaluate each term seperately
$
  A_(j k)A_(j k) &=
  ((r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v)
    + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u)) ((r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v)
    + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u))\
  &= ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u)
    + (r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u)
    + (r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))\
  ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u))((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u))
  &= ((r dot pd(S, v))(r dot pd(S, v)))/norm(r)^2 underbrace((r_k r_k)/norm(r)^2, =1) pd(S_j, u)pd(S_j, u)\
  &= ((r dot pd(S, v))(r dot pd(S, v)))/norm(r)^2 pd(S, u) dot pd(S, u)\
  ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u))((r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  &= ((r dot pd(S, v))(r dot pd(S, u)))/norm(r)^2 (r_k r_j)/norm(r)^2 pd(S_j, u)pd(S_k, v)\
  &= ((r dot pd(S, v))(r dot pd(S, u)))^2/norm(r)^4\
  ((r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))((r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  &=((r dot pd(S, u))(r dot pd(S, u)))/norm(r)^2 underbrace((r_j r_j)/norm(r)^2, =1) pd(S_k, v)pd(S_k, v)\
  &= ((r dot pd(S, u))(r dot pd(S, u)))/norm(r)^2 pd(S, v) dot pd(S, v) \
$

#align(center)[
  #box(stroke: 1pt, inset: 0.5em)[
    $
      A_(j k)A_(j k) &= ((r dot pd(S, v))(r dot pd(S, v)))/norm(r)^2 pd(S, u) dot pd(S, u)
      + 2 dot ((r dot pd(S, v))(r dot pd(S, u)))^2/norm(r)^4
      + ((r dot pd(S, u))(r dot pd(S, u)))/norm(r)^2 pd(S, v) dot pd(S, v)
    $
  ]
]

$
  A_(j k) A_(k j)
  &= ((r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u))
  ((r_j r_m) / norm(r)^2 pd(S_k, u) pd(S_m, v)
    + (r_k r_l) / norm(r)^2 pd(S_j, v) pd(S_l, u))\
  &= ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u)
    + (r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  ((r dot pd(S, v))/norm(r)^2 r_j pd(S_k, u)
    + (r dot pd(S, u)) / norm(r)^2 r_k pd(S_j, v))\
  ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u))
  ((r dot pd(S, v))/norm(r)^2 r_j pd(S_k, u))
  &= ((r dot pd(S, v))(r dot pd(S, u)))^2 / norm(r)^4\
  ((r dot pd(S, v))/norm(r)^2 r_k pd(S_j, u))((r dot pd(S, u)) / norm(r)^2 r_k pd(S_j, v))
  &= ((r dot pd(S, v))(r dot pd(S, u)))/norm(r)^2 pd(S, u) dot pd(S, v)\
  ((r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  ((r dot pd(S, v))/norm(r)^2 r_j pd(S_k, u))
  &= ((r dot pd(S, u))(r dot pd(S, v))) / norm(r)^2 pd(S, v) dot pd(S, u)\
  ((r dot pd(S, u)) / norm(r)^2 r_j pd(S_k, v))
  ((r dot pd(S, u)) / norm(r)^2 r_k pd(S_j, v))
  &=((r dot pd(S, v))(r dot pd(S, u)))^2 / norm(r)^4\
$

#align(center)[
  #box(stroke: 1pt, inset: 0.5em)[
    $
      A_(j k) A_(k j) = 2((r dot pd(S, v))(r dot pd(S, u)))^2 / norm(r)^4 + 2 ((r dot pd(S, u))(r dot pd(S, v))) / norm(r)^2 pd(S, v) dot pd(S, u)
    $
  ]
]

$
  A_(j k)pd(S_k, v) pd(S_j, u)
  &= ((r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u))pd(S_k, v) pd(S_j, u)\
  &= (r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) pd(S_k, v) pd(S_j, u) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u) pd(S_k, v) pd(S_j, u)\
  &= (r dot pd(S, v))^2 / norm(r)^2 norm(pd(S, u))^2
  + (r dot pd(S, u))^2 / norm(r)^2 norm(pd(S, v))^2
$

#align(center)[
  #box(stroke: 1pt, inset: 0.5em)[
    $
      A_(j k)pd(S_k, v) pd(S_j, u) = (r dot pd(S, v))^2 / norm(r)^2 norm(pd(S, u))^2
      + (r dot pd(S, u))^2 / norm(r)^2 norm(pd(S, v))^2
    $
  ]
]


$
  A_(k j) pd(S_k, v) pd(S_j, u)
  &= ((r_j r_m) / norm(r)^2 pd(S_k, u) pd(S_m, v)
    + (r_k r_l) / norm(r)^2 pd(S_j, v) pd(S_l, u))pd(S_k, v) pd(S_j, u)\
  &= (r_j r_m) / norm(r)^2 pd(S_k, u) pd(S_m, v) pd(S_k, v) pd(S_j, u)
  + (r_k r_l) / norm(r)^2 pd(S_j, v) pd(S_l, u) pd(S_k, v) pd(S_j, u)\
  &= ((r dot pd(S, u))(r dot pd(S, v))) / norm(r)^2 pd(S, u) dot pd(S, v) + ((r dot pd(S, v))(r dot pd(S, u))) / norm(r)^2 pd(S, u) dot pd(S, v)\
  &= 2((r dot pd(S, v))(r dot pd(S, u))) / norm(r)^2 pd(S, u) dot pd(S, v)\
$

#align(center)[
  #box(stroke: 1pt, inset: 0.5em)[
    $
      A_(k j) pd(S_k, v) pd(S_j, u) = 2((r dot pd(S, v))(r dot pd(S, u))) / norm(r)^2 pd(S, u) dot pd(S, v)
    $
  ]
]

$
  A_(j k) pd(S_j, v) pd(S_k, u)
  &= ((r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u)) pd(S_j, v) pd(S_k, u)\
  &= (r_k r_m) / norm(r)^2 pd(S_j, u) pd(S_m, v) pd(S_j, v) pd(S_k, u) + (r_j r_l) / norm(r)^2 pd(S_k, v) pd(S_l, u) pd(S_j, v) pd(S_k, u)
$


$
  A_(j k)A_(j k) - A_(j k) A_(k j)
  &= ((r dot pd(S, v))(r dot pd(S, v)))/norm(r)^2 pd(S, u) dot pd(S, u)
  + 2 dot ((r dot pd(S, v))(r dot pd(S, u)))^2/norm(r)^4
  + ((r dot pd(S, u))(r dot pd(S, u)))/norm(r)^2 pd(S, v) dot pd(S, v)\
  &- 2((r dot pd(S, v))(r dot pd(S, u)))^2 / norm(r)^4 - 2 ((r dot pd(S, u))(r dot pd(S, v))) / norm(r)^2 pd(S, v) dot pd(S, u)\
  &= ((r dot pd(S, v))(r dot pd(S, v)))/norm(r)^2 pd(S, u) dot pd(S, u)
  + ((r dot pd(S, u))(r dot pd(S, u)))/norm(r)^2 pd(S, v) dot pd(S, v) - 2 ((r dot pd(S, u))(r dot pd(S, v))) / norm(r)^2 pd(S, v) dot pd(S, u)\
$



// $
//   & omega = A / r^2 \
//   & d omega = (d A)/r^2 \
// $

// $
//   x = rho sin phi cos theta\
//   y = rho sin phi sin theta\
//   z = rho cos phi\
//   T(rho, theta, phi) = vec(rho sin phi cos theta, rho sin phi sin theta, rho cos phi)\
//   T_(theta) = vec(-rho sin phi sin theta, rho sin phi cos theta, 0), quad T_(phi) = vec(rho cos phi cos theta, rho cos phi sin theta, -rho sin phi)\
//   |T_(theta) times T_(phi)| &= det mat(i, j, k; -, T_(theta), -; -, T_(rho), -)\
//   &=
//   norm(
//     det mat(
//       i, j, k;
//       -rho sin phi sin theta, rho sin phi cos theta, 0;
//       rho cos phi cos theta, rho cos phi sin theta, -rho sin phi
//     )
//   )\
//   &= i dot -rho^2 sin^2 phi cos theta \
//   &+ (-j) dot rho^2 sin^2 phi sin theta \
//   &+ k dot (-rho^2 sin phi cos phi sin^2theta - rho^2 sin phi cos phi cos^2 theta)\
//   &= norm(vec(- rho^2 sin^2 phi cos theta, - rho^2 sin^2 phi sin theta, - rho^2 sin phi cos phi))\
//   &= norm(vec(- rho^2 sin^2 phi cos theta, - rho^2 sin^2 phi sin theta, - rho^2 sin phi cos phi))\
// $


