#This is a test of includeInEachFile for Python.
#This is a test of includeInEachFile for Python.
engScript_b = 4
def engScript_firstNCharacters(engScript_theString, engScript_n):
    return engScript_theString[0:engScript_n]
def engScript_arrayContainsSplit(engScript_theLang, engScript_theString):
    return engScript_theLang in engScript_theString.split(",")
def engScript_langException(engScript_lang, engScript_theFunction):
    return (engScript_theFunction + " is not yet defined for " + engScript_lang)
def engScript_print(engScript_lang, engScript_toPrint):
    if engScript_arrayContainsSplit(engScript_lang,"Python"):
        return ("print(" + engScript_toPrint + ")")
    elif engScript_arrayContainsSplit(engScript_lang,"JavaScript"):
        return ("console.log(" + engScript_toPrint + ")")
    raise Exception(engScript_langException(engScript_lang,"print"))
def engScript_error(engScript_lang, engScript_toPrint):
    if engScript_arrayContainsSplit(engScript_lang,"Python"):
        return ("raise Exception(" + engScript_toPrint + ")")
    raise Exception(engScript_langException(engScript_lang,"error"))
def engScript_endCodeBlock(engScript_lang):
    if engScript_arrayContainsSplit(engScript_lang,"CoffeeScript,Cobra,Python,Haskell,F#,Cython,Nimrod"):
        return ""
    elif engScript_arrayContainsSplit(engScript_lang,"REBOL"):
        return "]"
    elif engScript_arrayContainsSplit(engScript_lang,"JavaScript,Hack,D,Ceylon,ActionScript,Rust,TypeScript,Swift,AutoHotKey,Gosu,AWK,bc,C,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan,Pike"):
        return "}"
    elif engScript_arrayContainsSplit(engScript_lang,"Lua,Ruby,MATLAB,Oz,Falcon,Julia"):
        return "end"
    elif engScript_arrayContainsSplit(engScript_lang,"Clojure,Emacs Lisp,Common Lisp,Racket,Scheme,LispyScript,Sibilant"):
        return ")"
    elif engScript_arrayContainsSplit(engScript_lang,"Delphi,Pascal"):
        return "end;"
    else:
        raise Exception(engScript_langException(engScript_lang,"endCodeBlock"))
def engScript_startWhile(engScript_lang, engScript_condition):
    raise Exception(engScript_langException(engScript_lang,"startWhile"))
def engScript_joinList(engScript_theStrings, engScript_theSeparator):
    return engScript_theSeparator.join(engScript_theStrings)
def engScript_add(engScript_lang, engScript_numArray):
    if engScript_arrayContainsSplit(engScript_lang,"Tcl"):
        return ("[expr " + engScript_joinList(engScript_numArray," + ") + "]")
    elif engScript_arrayContainsSplit(engScript_lang,"Bash"):
        return ("((" + engScript_joinList(engScript_numArray," + ") + "))")
    elif engScript_arrayContainsSplit(engScript_lang,"Racket,LispyScript,Sibilant,Clojure,Common Lisp,Scheme"):
        return ("(+ " + engScript_joinList(engScript_numArray," ") + ")")
    raise Exception(engScript_langException(engScript_lang,"add"))
def engScript_initializeDictionary2(engScript_lang, engScript_initialValue):
    if engScript_arrayContainsSplit(engScript_lang,"Ruby,Python,Dart,JavaScript,Haxe"):
        return ("{" + engScript_joinList(engScript_initialValue,", ") + "}")
    elif engScript_arrayContainsSplit(engScript_lang,"Scala"):
        return ("Map(" + engScript_joinList(engScript_initialValue,", ") + ")")
    elif engScript_arrayContainsSplit(engScript_lang,"Groovy"):
        return ("[" + engScript_joinList(engScript_initialValue,", ") + "]")
    elif engScript_arrayContainsSplit(engScript_lang,"REBOL"):
        return ("to-hash [" + engScript_joinList(engScript_initialValue," ") + "]")
    elif engScript_arrayContainsSplit("Perl,Perl 6"):
        return ("(" + engScript_joinList(engScript_initialValue,",") + ")")
    elif engScript_arrayContainsSplit(engScript_lang,"PHP"):
        return ("array(" + engScript_joinList(engScript_initialValue,",") + ")")
    elif engScript_arrayContainsSplit(engScript_lang,"Java"):
        return ("new HashMap<String, String>();\n" + engScript_joinList(engScript_initialValue,";\n"))
    raise Exception(engScript_langException(engScript_lang,"initializeDictionary2"))