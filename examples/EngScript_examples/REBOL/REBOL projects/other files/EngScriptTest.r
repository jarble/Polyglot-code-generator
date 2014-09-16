[comment This code is written in REBOL 3.]
[comment This code is written in REBOL 3.]
engScript_a [
    b
]
engScript_v [
    d
]
true [
    d
]
[comment "The next line uses the string concatenation operator"]
append engScript_str1 engScript_str2
[comment "The next line uses the array concatenation operator"]
append engScript_arr1 engScript_arr2
engScript_openingTag: func [engScript_theTag [string!]] [
    return append "<" append engScript_theTag ">"
]
engScript_closingTag: func [engScript_theTag [string!]] [
    return append "</" append engScript_theTag ">"
]
engScript_surroundWithTag: func [engScript_theString [string!], engScript_theTag [string!]] [
    return append engScript_openingTag engScript_theTag append engScript_theString engScript_closingTag engScript_theTag
]
engScript_boldText: func [engScript_str1 [string!]] [
    return engScript_surroundWithTag engScript_str1 "b"
]
engScript_italicText: func [engScript_str1 [string!]] [
    return engScript_surroundWithTag engScript_str1 "i"
]
engScript_boldWikiText: func [engScript_str1 [string!]] [
    return append "'''" append engScript_str1 "'''"
]
engScript_italicWikiText: func [engScript_str1 [string!]] [
    return append "''" append engScript_str1 "''"
]
engScript_wikiLink: func [engScript_pageTitle [string!], engScript_linkText [string!]] [
    return append "[[" append engScript_pageTitle append "|" append engScript_linkText "]]"
]
engScript_markdownLink: func [engScript_theURL [string!], engScript_linkText [string!]] [
    return append "[" append engScript_linkText append "](" append engScript_theURL ")"
]
length? "hello"
copy/part skip engScript_a 2 5
append "derp" "herp"
(3 > 4)
(3 < 4)
(3 >= 4)
(3 <= 4)
print engScript_lawz
foreach engScript_a engScript_b [
    derp
]
[comment "Hello World!"]
append "common " " lisp"
engScript_helloWorld: func [engScript_a [integer!], engScript_b [integer!]] [
    case [
    engScript_a [
        return (3 - (((1 * 1) + 2) / 4))
    ]
    engScript_b [
        return 2
    ]
    true [
        return 3
    ]
    ]
]