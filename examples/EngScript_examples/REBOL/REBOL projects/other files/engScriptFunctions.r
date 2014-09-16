[comment This code is written in REBOL 3.]
[comment This code is written in REBOL 3.]
[comment "These functions are intended to be used in the EngScript compiler"]
engScript_firstNCharacters: func [engScript_theString [string!], engScript_n [integer!]] [
    return copy/part skip engScript_theString 0 engScript_n
]
engScript_arrayContainsSplit: func [engScript_theLang [string!], engScript_theString [string!]] [
    return not none? find split engScript_theString "," engScript_theLang
]
engScript_langException: func [engScript_lang [string!], engScript_theFunction [string!]] [
    return append engScript_theFunction append " is not yet defined for " engScript_lang
]
engScript_print: func [engScript_lang [string!], engScript_toPrint [string!]] [
    case [
    engScript_arrayContainsSplit engScript_lang "Python" [
        return append "print(" append engScript_toPrint ")"
    ]
    engScript_arrayContainsSplit engScript_lang "JavaScript" [
        return append "console.log(" append engScript_toPrint ")"
    ]
    ]
    make error! engScript_langException engScript_lang "print"
]
engScript_error: func [engScript_lang [string!], engScript_toPrint [string!]] [
    case [
    engScript_arrayContainsSplit engScript_lang "Python" [
        return append "raise Exception(" append engScript_toPrint ")"
    ]
    ]
    make error! engScript_langException engScript_lang "error"
]
engScript_endCodeBlock: func [engScript_lang [string!]] [
    case [
    engScript_arrayContainsSplit engScript_lang "CoffeeScript,Cobra,Python,Haskell,F#" [
        return ""
    ]
    engScript_arrayContainsSplit engScript_lang "REBOL" [
        return "]"
    ]
    engScript_arrayContainsSplit engScript_lang "JavaScript,Hack,D,Ceylon,ActionScript,Rust,TypeScript,Swift,AutoHotKey,Gosu,AWK,bc,C,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan,Pike" [
        return "}"
    ]
    engScript_arrayContainsSplit engScript_lang "Lua,Ruby,MATLAB,Oz,Falcon,Julia" [
        return "end"
    ]
    engScript_arrayContainsSplit engScript_lang "Clojure,Emacs Lisp,Common Lisp,Racket,Scheme" [
        return ")"
    ]
    engScript_arrayContainsSplit engScript_lang "Delphi,Pascal" [
        return "end;"
    ]
    true [
        make error! engScript_langException engScript_lang "endCodeBlock"
    ]
    ]
]