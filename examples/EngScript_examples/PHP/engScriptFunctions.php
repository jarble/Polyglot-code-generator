

$engScript_b = 4;
function engScript_firstNCharacters($engScript_theString, $engScript_n){
    return substr($engScript_theString,0,$engScript_n);
}
function engScript_arrayContainsSplit($engScript_theLang, $engScript_theString){
    return in_array($engScript_theLang, explode(",", $engScript_theString))
}
function engScript_langException($engScript_lang, $engScript_theFunction){
    return engScript_theFunction . " is not yet defined for " . $engScript_lang;
}
function engScript_print($engScript_lang, $engScript_toPrint){
    if(engScript_arrayContainsSplit($engScript_lang,"Python")){
        return "print(" . $engScript_toPrint . ")";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"JavaScript")){
        return "console.log(" . $engScript_toPrint . ")"
    }
    throw new Exception(engScript_langException($engScript_lang,"print"));
}
function engScript_error($engScript_lang, $engScript_toPrint){
    if(engScript_arrayContainsSplit($engScript_lang,"Python")){
        return "raise Exception(" . $engScript_toPrint . ")";
    }
    throw new Exception(engScript_langException($engScript_lang,"error"));
}
function engScript_endCodeBlock($engScript_lang){
    if(engScript_arrayContainsSplit($engScript_lang,"CoffeeScript,Cobra,Python,Haskell,F#,Cython,Nimrod")){
        return "";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"REBOL")){
        return "]";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"JavaScript,Hack,D,Ceylon,ActionScript,Rust,TypeScript,Swift,AutoHotKey,Gosu,AWK,bc,C,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan,Pike")){
        return "}";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Lua,Ruby,MATLAB,Oz,Falcon,Julia")){
        return "end";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Clojure,Emacs Lisp,Common Lisp,Racket,Scheme,LispyScript,Sibilant")){
        return ")";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Delphi,Pascal")){
        return "end;";
    }
    else {
        throw new Exception(engScript_langException($engScript_lang,"endCodeBlock"));
    }
}
function engScript_startWhile($engScript_lang, $engScript_condition){
    throw new Exception(engScript_langException($engScript_lang,"startWhile"));
}
function engScript_joinList($engScript_theStrings, $engScript_theSeparator){
    return implode($engScript_theSeparator,$engScript_theStrings);
}
function engScript_add($engScript_lang, $engScript_numArray){
    if(engScript_arrayContainsSplit($engScript_lang,"Tcl")){
        return "[expr " . engScript_joinList($engScript_numArray," + ") . "]";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Bash")){
        return "((" . engScript_joinList($engScript_numArray," + ") . "))";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Racket,LispyScript,Sibilant,Clojure,Common Lisp,Scheme")){
        return "(+ " . engScript_joinList($engScript_numArray," ") . ")";
    }
    throw new Exception(engScript_langException($engScript_lang,"add"));
}
function engScript_initializeDictionary2($engScript_lang, $engScript_initialValue){
    if(engScript_arrayContainsSplit($engScript_lang,"Ruby,Python,Dart,JavaScript,Haxe")){
        return "{" . engScript_joinList($engScript_initialValue,", ") . "}";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Scala")){
        return "Map(" . engScript_joinList($engScript_initialValue,", ") . ")";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Groovy")){
        return "[" . engScript_joinList($engScript_initialValue,", ") . "]";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"REBOL")){
        return "to-hash [" . engScript_joinList($engScript_initialValue," ") . "]";
    }
    elseif(engScript_arrayContainsSplit("Perl,Perl 6")){
        return "(" . engScript_joinList($engScript_initialValue,",") . ")";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"PHP")){
        return "array(" . engScript_joinList($engScript_initialValue,",") . ")";
    }
    elseif(engScript_arrayContainsSplit($engScript_lang,"Java")){
        return "new HashMap<String, String>();\n" . engScript_joinList($engScript_initialValue,";\n");
    }
    throw new Exception(engScript_langException($engScript_lang,"initializeDictionary2"));
}