

(define (engScript_openingTag engScript_theTag)
    (string-append "<" engScript_theTag ">")
)
(define (engScript_closingTag engScript_theTag)
    (string-append "</" engScript_theTag ">")
)
(define (engScript_surroundWithTag engScript_theString engScript_theTag)
    (string-append (engScript_openingTag engScript_theTag) engScript_theString (engScript_closingTag engScript_theTag))
)
(define (engScript_boldText engScript_str1)
    (engScript_surroundWithTag engScript_str1 "b")
)
(string-length "hello")
(substring a 2 5)
(case engScript_a
    [(a)
        blah
    ]
    [else
        heh
    ]
)
(string-append "derp" "herp")
(> 3 4)
(< 3 4)
(>= 3 4)
(<= 3 4)
(display engScript_lawz)
(for ([engScript_a engScript_b])
    derp
)
;"Hello World!"
(string-append "common " " lisp")
(define (engScript_helloWorld engScript_a engScript_b)
    (cond
    (engScript_a
        (- 3 (/ (+ (* 1 1) 2) 4))
    )
    (engScript_b
        2
    )
    (else
        3
    )
    )
)