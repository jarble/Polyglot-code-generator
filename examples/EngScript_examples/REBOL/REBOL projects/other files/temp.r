Rebol [] load "listComprehension.r"

engScript_openingTag: func [engScript_theTag] [
    return append "<" append engScript_theTag ">"
]
engScript_closingTag: func [engScript_theTag] [
    return append "</" append engScript_theTag ">"
]
engScript_surroundWithTag: func [engScript_theString engScript_theTag] [
    return append engScript_openingTag engScript_theTag append engScript_theString engScript_closingTag engScript_theTag
]
engScript_boldText: func [engScript_str1] [
    return engScript_surroundWithTag engScript_str1 "b"
]

print engScript_boldText "hello"

switch/default 10 [
    10 [
        print 2
    ]
    ] [
        print 7
]

[Title: "Example script"]

"Press CTRL+D to save this file."

{To do:
Write a function that generate other functions, like this:

"Here's a useful macro."
    "Make sure that only one case is true."
    "example input: [case 1 [return 1] case 2 [return 2]]"

caseWithOneTrue: func [theBlock] [
    
]
}

"For loop example"
repeat i 10 [
    print i
    print "Hi!"
]

sum: func [arg1 arg2] [arg1 + arg2]

macroExample: func [x y toPrint] [
    if [x = y] [ print  toPrint]
]

addMacro: func [x1 y1] [
    do [x1: x1 + y1]
]

x: 1
y: 2
print "addMacro"
addMacro x y
print x

macroExample 10 (11 - 1) "Good!"

semicolon: func [lang text] [
	case [
		
		]
    ]

print "Lulz"
print "Hello"

foo: ask "Your name, please? "


theVar: 60

case [
    theVar > 60 [
        print "Greater than 60!"
    ]

    theVar == 3 [
        print "It's 3!"
    ]

    theVar < 3 [
        print "It's less than 3!"
    ]

    true [
        print "It's something else!"
    ]
]


print "Does this work?"
print find "hello" "he"

ask "Type any key to quit."
