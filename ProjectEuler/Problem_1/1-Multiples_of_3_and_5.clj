#lang racket
(def total 0)
(range 1000 
    (if (or (= 0 (mod i 3))(= 0 (mod i 5)))
        (set! total (+ total i))
        (+ total 0)))
(write total)