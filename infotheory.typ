#import "typ_slides/slides_template.typ": *
#show: doc => conf(doc, handout: true)

#title-slide(
  "Asymmetric Numeral System (ANS) Compression",
  "",
  "By: David Yue | david.yue@utah.edu",
  handout: false,
)

#body-frame("A Bit of Information")[
  Hello
]

#body-frame("Asymmetric Numeral System (ANS) Compression")[
  rANS is a compression algorithm that compresses data into a single arbitrary
  bit width integer. Given a set of symbols $Sigma = {s_1, s_2, s_3, dots, s_N}$ and
  a string $Sigma^*$ composed of symbols in $Sigma$ where each symbol $s_i$ has
  a frequency of $F_i$. The ANS compression algorithm is given as follows:


  $
    X_i = floor(X_(i - 1) / F_i) dot (sum_j^N F_j) + mod(X_(i - 1), F_i) + sum_j^(i-1)F_j
  $

  The initial state is $X_0 = 0$. The compressed data is $X_(N + 1)$.
]

#body-frame("Source Coding Theorem", subtitle: "Motivation")[
  Given a string $Sigma^*$, the minimum number of bits required to encode $Sigma^*$
  is given by

  $
    underbrace((sum_(j=1)^N F_j), "total string length") underbrace((sum_(i=1)^(N) p_i dot log_2(1/p_i)), "shannon entropy")
  $

  where
  $
    p_i = F_i / (sum_(i=1)^N F_j)
  $

]

#body-frame("Idea", subtitle: "Motivation")[
  #set text(size: 23pt)
  We can encode each symbol as the digits of a integer. For instance, if we
  wish to encode the string "abacac".

  To encode a symbol $s_i$ with probability $p_i$, we use $log_2(1/p_i)$ bits
  #columns(2)[
    $
      X_(i+1) & = X_i dot 1/p_i + C_i \
              & = X_i ((sum_(i=1)^N F_j) / F_i) + C_i \
              & = X_i / F_i (sum_(i=1)^N F_j) + C_i \
              & = (floor(X_i/F_i) + mod(X_i, F_i) / F_i)(sum_(i=1)^N F_j) + C_i \
    $
    $
      & = floor(X_i/F_i) (sum_(i=1)^N F_j) + mod(X_i, F_i) (sum_(i=1)^N F_j)/F_i + C_i \
      & = floor(X_i/F_i) (sum_(i=1)^N F_j) + mod(X_i, F_i) 1/p_i + C_i \
      & arrow.l.r^"bijective" floor(X_i/F_i) (sum_(i=1)^N F_j) + mod(X_i, F_i) + C_i
    $
  ]
]


