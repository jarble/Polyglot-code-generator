[comment This code is written in REBOL 3.]
[comment This code is written in REBOL 3.]
append engScript_a engScript_b
append engScript_a engScript_b
(4 == 5)
engScript_b: to-hash [[ f o o   1   b a r   2 ]]
engScript_a: "haha"
engScript_b: to-hash [[ f o o   1   b a r   2 ]]
engScript_add: func [engScript_a, engScript_b] [
    return (engScript_a + engScript_b)
]
engScript_multiply: func [engScript_a, engScript_b] [
    return (engScript_a * engScript_b)
]
engScript_subtract: func [engScript_a, engScript_b] [
    return (engScript_a - engScript_b)
]
engScript_squared: func [engScript_a] [
    return (engScript_a * engScript_a)
]