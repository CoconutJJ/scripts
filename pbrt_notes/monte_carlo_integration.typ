= Monte Carlo Integration

Let $X$ be a random variable chosen from a distribution with PDF $p(X)$. Then
we have

$
  E[f(X)] = integral_(-infinity)^(infinity) f(x) dot p(x) d x
  = lim_(N arrow infinity) 1/N sum_(i = 0)^(N) f(X)
$

To compute

$
  integral_(-infinity)^(infinity) f(x) d x
$

we need

$
  E[f(X)/p(X)] & = integral_(-infinity)^(infinity) f(x)/p(x) dot p(x) d x \
               & = integral_(-infinity)^(infinity) f(x) d x \
               & = lim_(N arrow infinity) 1/N sum_(i = 0)^(N) f(X)/p(X)
$

Error

$
  V[f(X)/p(X)] & = E[(f(X)/p(X) - E[f(X)/p(X)])^2] \
  & = E[(f(X)/p(X))^2 - 2 dot f(X)/p(X) dot E[f(X)/p(X)] + E^2[f(X)/p(X)]] \
  & = E[(f(X)/p(X))^2] - 2 dot E[f(X)/p(X)] dot E[f(X)/p(X)] + E^2[f(X)/p(X)] \
  & = E[(f(X)/p(X))^2] - E^2[f(X)/p(X)] \
  & = 1/N sum_i f(X_i)^2/p(X_i)^2 - (1/N sum_i f(X_i)/p(X_i))^2 \
$


If $y^2 < x$, then there is $epsilon > 0$ such that $(y + epsilon)^2 < x$

$
  (y + epsilon)^2
  & = y^2 + 2y epsilon + epsilon^2\
  &<= y^2 + 2 abs(y)epsilon + epsilon quad ["suppose " epsilon < 1]\
  & = x
$

$
  epsilon = min(1, (x - y^2)/(2 abs(y) + 1))
$

$
  (y + epsilon)^2 & = y^2 + 2abs(y) epsilon + epsilon^2 \
                  & < y^2 + 2abs(y) epsilon + epsilon \
                  & < y^2 + (2abs(y) + 1) ((x - y^2)/(2abs(y)+ 1)) \
                  & = x
$
