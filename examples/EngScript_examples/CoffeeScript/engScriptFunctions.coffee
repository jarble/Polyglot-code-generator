

engScript_b = 4
engScript_firstNCharacters = (engScript_theString, engScript_n) ->
    return engScript_theString.substring(0, engScript_n)
engScript_arrayContainsSplit = (engScript_theLang, engScript_theString) ->
    return engScript_theString.split(",").indexOf(engScript_theLang) !== -1
engScript_langException = (engScript_lang, engScript_theFunction) ->
    return (engScript_theFunction + " is not yet defined for " + engScript_lang)
engScript_print = (engScript_lang, engScript_toPrint) ->
    if engScript_arrayContainsSplit(engScript_lang,"Python")
        return ("print(" + engScript_toPrint + ")")
    else if engScript_arrayContainsSplit(engScript_lang,"JavaScript")
        return ("console.log(" + engScript_toPrint + ")")
    throw engScript_langException(engScript_lang,"print")
engScript_error = (engScript_lang, engScript_toPrint) ->
    if engScript_arrayContainsSplit(engScript_lang,"Python")
        return ("raise Exception(" + engScript_toPrint + ")")
    throw engScript_langException(engScript_lang,"error")
engScript_endCodeBlock = (engScript_lang) ->
    if engScript_arrayContainsSplit(engScript_lang,"CoffeeScript,Cobra,Python,Haskell,F#,Cython,Nimrod")
        return ""
    else if engScript_arrayContainsSplit(engScript_lang,"REBOL")
        return "]"
    else if engScript_arrayContainsSplit(engScript_lang,"JavaScript,Hack,D,Ceylon,ActionScript,Rust,TypeScript,Swift,AutoHotKey,Gosu,AWK,bc,C,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan,Pike")
        return "}"
    else if engScript_arrayContainsSplit(engScript_lang,"Lua,Ruby,MATLAB,Oz,Falcon,Julia")
        return "end"
    else if engScript_arrayContainsSplit(engScript_lang,"Clojure,Emacs Lisp,Common Lisp,Racket,Scheme,LispyScript,Sibilant")
        return ")"
    else if engScript_arrayContainsSplit(engScript_lang,"Delphi,Pascal")
        return "end;"
    else
        throw engScript_langException(engScript_lang,"endCodeBlock")
engScript_startWhile = (engScript_lang, engScript_condition) ->
    throw engScript_langException(engScript_lang,"startWhile")
engScript_joinList = (engScript_theStrings, engScript_theSeparator) ->
    return engScript_theStrings.join(engScript_theSeparator)
engScript_add = (engScript_lang, engScript_numArray) ->
    if engScript_arrayContainsSplit(engScript_lang,"Tcl")
        return ("[expr " + engScript_joinList(engScript_numArray," + ") + "]")
    else if engScript_arrayContainsSplit(engScript_lang,"Bash")
        return ("((" + engScript_joinList(engScript_numArray," + ") + "))")
    else if engScript_arrayContainsSplit(engScript_lang,"Racket,LispyScript,Sibilant,Clojure,Common Lisp,Scheme")
        return ("(+ " + engScript_joinList(engScript_numArray," ") + ")")
    throw engScript_langException(engScript_lang,"add")
engScript_initializeDictionary2 = (engScript_lang, engScript_initialValue) ->
    if engScript_arrayContainsSplit(engScript_lang,"Ruby,Python,Dart,JavaScript,Haxe")
        return ("{" + engScript_joinList(engScript_initialValue,", ") + "}")
    else if engScript_arrayContainsSplit(engScript_lang,"Scala")
        return ("Map(" + engScript_joinList(engScript_initialValue,", ") + ")")
    else if engScript_arrayContainsSplit(engScript_lang,"Groovy")
        return ("[" + engScript_joinList(engScript_initialValue,", ") + "]")
    else if engScript_arrayContainsSplit(engScript_lang,"REBOL")
        return ("to-hash [" + engScript_joinList(engScript_initialValue," ") + "]")
    else if engScript_arrayContainsSplit("Perl,Perl 6")
        return ("(" + engScript_joinList(engScript_initialValue,",") + ")")
    else if engScript_arrayContainsSplit(engScript_lang,"PHP")
        return ("array(" + engScript_joinList(engScript_initialValue,",") + ")")
    else if engScript_arrayContainsSplit(engScript_lang,"Java")
        return ("new HashMap<String, String>();\n" + engScript_joinList(engScript_initialValue,";\n"))
    throw engScript_langException(engScript_lang,"initializeDictionary2")