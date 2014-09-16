

(engScript_a
    b
)
(engScript_v
    d
)
(t
    d
)
;"The next line uses the string concatenation operator"
(concatenate 'string engScript_str1 engScript_str2)
;"The next line uses the array concatenation operator"
(append engScript_arr1 engScript_arr2)
(defun engScript_openingTag (engScript_theTag)
    (concatenate 'string "<" engScript_theTag ">")
)
(defun engScript_closingTag (engScript_theTag)
    (concatenate 'string "</" engScript_theTag ">")
)
(defun engScript_surroundWithTag (engScript_theString engScript_theTag)
    (concatenate 'string (engScript_openingTag engScript_theTag) engScript_theString (engScript_closingTag engScript_theTag))
)
(defun engScript_boldText (engScript_str1)
    (engScript_surroundWithTag engScript_str1 "b")
)
(defun engScript_italicText (engScript_str1)
    (engScript_surroundWithTag engScript_str1 "i")
)
(defun engScript_boldWikiText (engScript_str1)
    (concatenate 'string "'''" engScript_str1 "'''")
)
(defun engScript_italicWikiText (engScript_str1)
    (concatenate 'string "''" engScript_str1 "''")
)
(defun engScript_wikiLink (engScript_pageTitle engScript_linkText)
    (concatenate 'string "[[" engScript_pageTitle "|" engScript_linkText "]]")
)
(defun engScript_markdownLink (engScript_theURL engScript_linkText)
    (concatenate 'string "[" engScript_linkText "](" engScript_theURL ")")
)
(length "hello")
(subseq engScript_a 2 5)
(concatenate 'string "derp" "herp")
(> 3 4)
(< 3 4)
(>= 3 4)
(<= 3 4)
(write engScript_lawz)
(loop for engScript_a in engScript_b do
    derp
)
;"Hello World!"
(concatenate 'string "common " " lisp")
(defun engScript_helloWorld (engScript_a engScript_b)
    (cond
    (engScript_a
        (- 3 (/ (+ (* 1 1) 2) 4))
    )
    (engScript_b
        2
    )
    (t
        3
    )
    )
)