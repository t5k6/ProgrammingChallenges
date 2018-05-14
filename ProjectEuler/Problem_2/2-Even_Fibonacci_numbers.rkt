#lang racket
(define total 0)
(for/list ([i 1000])
    (if (or (= 0 (modulo i 3))(= 0 (modulo i 5)))
        (set! total (+ total i))
        (+ total 0)))
(write total)

