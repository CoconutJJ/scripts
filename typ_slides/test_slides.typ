#import "slides_template.typ": *

#show: conf


#title-slide("Test Slides", "Test", "Test")

#body-frame("Hello")[
  + #only(1)[Hello how are you?]
  + #reveal(1)[What is your name?]

  #slide-footnote("Hello")
]


