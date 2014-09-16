"""
testMacro is the only method from this file you should ever use from other files.
Test files in EngScript.py instead of testing them here.

This is a comment.
"""

from statementArr import statementArr
#from crossLanguageParser import evaluateMacro
#from crossLanguageParser import addParentheses
'''sys.path.append("/polyglotFunctions/generatedFunctions/Python/")'''

#from polyglotFunctions.generatedFunctions.PythonFunctions.Compiler import *
            


import traceback
import os
import glob
import logging

#!/usr/bin/python3.3


'''print(sys.version);'''
import inspect
import re

def getResultForLanguages(langsAndResults):
    for idx, val in enumerate(langsAndResults):
        if((idx == 0) or (idx + 1) % 2 == 0):
            if(lang in val):
                return langsAndResults[idx + 1]

def semicolon(lang, theStatement): #also known as statement
    if type(theStatement) == list:
        return seriesOfStatements(lang=lang,body=theStatement)
    if(lang in "JavaScript,OCaml,Java,Dart,PHP,C#,C++,Haxe,AWK,bc,Haskell,Perl,Go,Nemerle,Vala".split(",")):
        if(theStatement[-1:] != ";"):
            #print(theStatement)
            return theStatement + ";"
        else:
            return theStatement
    elif(lang in "Ruby,REBOL,Python,Bash,Visual Basic,Visual Basic .NET,Hack,Lua,Racket,Common Lisp".split(",")):
        return theStatement
    elif(lang in ["crosslanguage"]):
        return "("+theStatement+" ;)"
    elif(lang in ["Erlang"]):
        if(theStatement[-1:] != ","):
            return theStatement + ","
        else:
            return theStatement
    notYetDefinedError(lang, inspect.stack()[0][3])

def listComprehension(lang, x, y, z):
    if lang == "Python":
        return "[" + getVariableName(lang, x) + " for " + getVariableName(lang, y) + " in " + getVariableName(lang, z) + "]"
    notYetDefinedError(lang, inspect.stack()[0][3])

def seriesOfStatements(lang, body):
    for idx, val in enumerate(body):
        body[idx] = semicolon(lang, val);
        if(lang == "Erlang" and idx == len(body) - 1):
            body[idx] = body[idx][0:(len(body[idx])-1)]
    return concatenateAllElements(body)

def Eval(lang, toEval):
    if(lang in ["Python", "JavaScript"]):
        return "eval(" + toEval + ")"
    notYetDefinedError(functionName = inspect.stack()[0][3])

def this(lang, variableName):
    if(lang == "Python"):
        return "self."+variableName
    if(lang in ["Java", "C#"]):
        return "this."+variableName
    if(lang in ["crosslanguage"]):
        return "this."+variableName
    notYetDefinedError(functionName = inspect.stack()[0][3])
    
def notYetDefinedError(lang, functionName):
    toReturn = functionName + " is not yet defined for " + str(lang)
    raise Exception(toReturn);

def endCodeBlock(lang):
        if lang in "AWK,bc,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan".split(","):
            return "}"
        elif lang in "CoffeeScript,Python,Haskell,F#".split(","):
            return ""
        elif lang in "Racket,Common Lisp,Emacs Lisp,crosslanguage".split(","):
            return ")"
        elif lang in "REBOL".split(","):
            return "]"
        elif lang in "Lua,Ruby,MATLAB,Oz,Falcon".split(","):
            return "end"
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3])

def callFunctionWithNamedArgs(lang, functionName, argumentNames, theArgs, fromClass):
    notYetDefinedError(functionName = inspect.stack()[0][3])

def crossLanguageStatement(functionName, params):
    toReturn = "("+functionName + " "
    i=0
    while(i < len(params)):
        if((type(params[i]) is list or (params[i] is None))):
            params[i] = str(params[i])
        toReturn += params[i]
        if(i < (len(params)-1)):
            toReturn += " "
        i += 1
    return toReturn
    notYetDefinedError(functionName = inspect.stack()[0][3])

def startWhile(lang, condition):
        print("The condition is " + str(condition))
        if lang in "Python".split(","):
            return "while " + condition + ":"    
        if lang in "CoffeeScript,crosslanguage".split(","):
            return "while " + condition
        elif lang in "REBOL".split(","):
            return "while [" + condition + "] ["
        elif lang in "Lua,Ruby,OCaml,F#".split(","):
            return "while " + condition + " do"
        elif lang in "Fortran".split(","):
            return "do while (" + condition + ")"
        elif lang in "Gambas".split(","):
            return "WHILE " + condition
        elif lang in "Bash".split(","):
            return "while [ " + condition + " ]; do"
        elif lang in "Dart,Groovy,Scala,Java,JavaScript,PHP,C#,Perl,C++,Haxe,R,AWK,Vala".split(","):
            return "while(" + condition + "){"
        elif lang in "Tcl,bc".split(","):
            return "while{" + condition + "}{"
        elif lang in "Go".split(","):
            return "for " + condition + " {"
        elif lang in "Octave".split(","):
            return "while (" + condition + ")"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "While " + condition
        raise Exception("startWhile is not yet defined for " + lang)

def endWhile(lang):
        if lang in "CoffeeScript,Groovy,Scala,Dart,bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,Haxe,JavaScript,C#,Perl,crosslanguage,Ruby,C++,Lua,PHP,Go,MATLAB".split(","):
            return endCodeBlock(lang)
        elif lang in "Bash,OCaml".split(","):
            return "done"
        elif lang in "Fortran".split(","):
            return "enddo"
        elif lang in "Ada".split(","):
            return "end loop;"
        elif lang in "Octave".split(","):
            return "endwhile"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End While"
        elif lang in "Gambas".split(","):
            return "WEND"
        raise Exception("endWhile is not yet defined for " + lang)

def startFor(initializer, condition, increment):
    if(lang in ["Java", "JavaScript", "PHP", "C#", "Perl", "C++", "AWK"]):
        return "for(" + semicolon(initializer) +" "+ semicolon(condition) +" "+ increment + "){";
    if(lang in ["Python"]):
        return [initializer,startWhile(condition=condition)]
    if(lang in ["crosslanguage"]):
        return "(for" +" "+ initializer +" "+ condition +" "+ increment + ")"
    if(lang in ["Go"]):
        return "for "+initializer+"; "+condition+"; "+increment+" {"
    notYetDefinedError(functionName = inspect.stack()[0][3])



def callFunction(lang, function, fromClass, parameters):
    if type(parameters) == str:
        parameters = [parameters]
    parameters = [getVariableName(lang, foo) for foo in parameters]
    function = removeInitialDollarSign(function)
    newArr = [function] + parameters
    if(lang in "Haskell,REBOL,Common Lisp,Racket,Scheme,crosslanguage,Hack".split(",")):
        return "(" + " ".join(newArr) + ")"
    elif(lang in ["Oz"]):
        return "{" + " ".join(newArr) + "}"
    elif(lang in ["Tcl"]):
        return "[" + " ".join(newArr) + "]"
    elif(lang in ["Bash"]):
        return "$(" + " ".join(newArr) + ")"
    elif(lang in "Go,Ruby,Vala,Java,OCaml,Erlang,Python,C#,Lua,Haxe,JavaScript,Dart,bc,Visual Basic,Visual Basic .NET,PHP,Perl".split(",")):
        aString=""
        if(len(parameters) == 0):
            aString = function + "()"
        else:
            i=0
            while(i < len(parameters)):
                if(type(parameters[i]) == "str"):
                    parameters[i] = initializeVar()
                aString += str(parameters[i]);
                if(i != len(parameters) -1):
                    if lang == "crosslanguage":
                        aString += " "
                    else:
                        aString += ","
                i += 1
        if(fromClass == None):
            return function + "(" + aString + ")"
        else:
            return fromClass + "." + function + "(" + aString + ")"
    notYetDefinedError(lang, inspect.stack()[0][3])
    
def accessArray(lang, arrayName, indexList):
    i = 0
    for current in indexList:
        indexList[i] = str(current)
        i += 1
    arrayName = getVariableName(lang, arrayName)
    if(lang in ["crosslanguage"]):
        return "accessArray(" + ", " + lang + ", " + arrayName + ", " + indexList
    
    if(lang in ["Haskell"]):
        newIndexList = [arrayName] + indexList
        return "!!".join(newIndexList)
    
    if(lang in ["Python", "Java", "JavaScript", "Ruby", "Go", "C++", "PHP", "Haxe"]):
        i = 0;
        toReturn = arrayName + "[";
        while(i < len(indexList)):
            toReturn += str(indexList[i]);
            if(i < len(indexList)-1):
                toReturn += "][";
            i += 1;
        toReturn += "]";
        return toReturn;
    if(lang in ["REBOL"]):
        i = 0;
        toReturn = arrayName + "/";
        while(i < len(indexList)):
            toReturn += str(indexList[i]);
            if(i < len(indexList)-1):
                toReturn += "/";
            i += 1;
    elif(lang in ["Lua"]):
        i = 0;
        toReturn = arrayName + "[";
        while(i < len(indexList)):
            toReturn += str(indexList[i]);
            if(i < len(indexList)-1):
                toReturn += "+1][";
            i += 1;
        toReturn += "]";
    elif(lang in ["C#"]):
        i = 0;
        toReturn = arrayName + "[";
        while(i < len(indexList)):
            toReturn += str(indexList[i]);
            if(i < len(indexList)-1):
                toReturn += ",";
            i += 1;
        toReturn += "]";
    return toReturn;
    notYetDefinedError(functionName = inspect.stack()[0][3])

def charAt(lang, aString, index):
        aString = getVariableName(lang, aString)
        index = getVariableName(lang, index)
        if lang in "Python,JavaScript,Ruby,C#,PHP,REBOL".split(","):
            return accessArray(lang=lang, arrayName=aString, indexList = [index])
        elif lang in "Java,Haxe".split(","):
            return aString + ".charAt(" + index + ")"
        elif lang in "Tcl".split(","):
            return "[string index " + aString + " " + index + "]"
        elif lang in "crosslanguage".split(","):
            return "(charAt " + aString + " " + index + ")"
        elif lang in "Haskell".split(","):
            return aString + " !! " + index
        elif lang in "Go".split(","):
            return "string([]rune(" + aString + ")[" + index + "])"
        elif lang in "Lua".split(","):
            return "string.sub(" + aString + "," + index + " + 1," + index + " + 1)"
        elif lang in "Perl".split(","):
            return "substr("+aString+", "+index+"-1, 1)"   
        raise Exception("charAt is not yet defined for " + lang)

def index(theObject, theType, indexList):
    if(getCorrespondingType(theType) == getCorrespondingType("string")):
        return charAt(theObject, indexList[0])
    else:
        return accessArray(arrayName=theObject, indexList = indexList)

def getStringFromIndentation(indent):
    i = 0;
    theString = "";
    while(i < indent):
        theString += "    ";
        i += 1;
    return theString;

def Error(message):
        if lang in "Python".split(","):
            return "raise Exception(" + message + ")"
        elif lang in "Java,PHP,C#".split(","):
            return "throw new Exception(" + message + ");"
        elif lang in "JavaScript,Haxe".split(","):
            return "throw " + message
        elif lang in "Haskell,Scheme,crosslanguage".split(","):
            return "(error " + message + ")"
        elif lang in "Haskell,Scheme".split(","):
            return "(error " + message + ")"
        elif lang in "crosslanguage".split(","):
            return "error(" + message + ")"
        raise Exception("Error is not yet defined for " + lang)

def getComment(comment):
        if lang in "Bash,AWK,Ruby,Perl,R,Tcl,bc,Python".split(","):
            return "# " + comment
        elif lang in "Gambas,Visual Basic,Visual Basic .NET".split(","):
            return "'" + comment
        elif lang in "REBOL".split(","):
            return "[comment " + comment + "]"
        elif lang in "Fortran".split(","):
            return "! " + comment
        elif lang in "OCaml".split(","):
            return "(*" + comment + "*)"
        elif lang in "Java,Vala,C#,JavaScript,Haxe,Scala,Go,C,C++,PHP,F#,Nemerle,crosslanguage".split(","):
            return "//" + comment
        elif lang in "MATLAB,Octave,Erlang,Prolog".split(","):
            return "%" + comment
        elif lang in "Lua,Haskell,Ada".split(","):
            return "-- " + comment
        elif lang in "Racket,Common Lisp,Clojure".split(","):
            return ";" + comment
        elif lang in "Emacs Lisp".split(","):
            return """ + comment + """
        raise Exception("getComment is not yet defined for " + str(lang))

def getFunctionParameterList(lang, parameterNames, parameterTypes):
    '''
    Get the parameter list for a function definition
    '''
    if(lang in "Bash"):
        i = 0
        for current in parameterNames:
            parameterNames[i] = "    " + (parameterNames[i])[1:len(parameterNames[i])] + "=" + "$" + str(i+1)
            i += 1
        return parameterNames
    
    
    if(lang in "Perl"):
        i = 0
        for current in parameterNames:
            parameterNames[i] = "    " + parameterNames[i] + " = " + "$_[" + str(i) + "];"
            i += 1
        return parameterNames
    
    elif(lang in "Haskell,Racket,OCaml,Tcl,Common Lisp,REBOL".split(",")):
        i = 0;
        toReturn = "";
        while(i < len(parameterNames)):
            toReturn += parameterNames[i];
            if(i < len(parameterNames) -1):
                toReturn += " ";
            i += 1;
        return toReturn;
    elif(lang in "Python,Dart,JavaScript,Erlang,PHP,Lua,Ruby,R,bc".split(",")):
        i = 0;
        toReturn = "";
        while(i < len(parameterNames)):
            toReturn += parameterNames[i];
            if(i < len(parameterNames) -1):
                toReturn += ", ";
            i += 1;
        return toReturn;
    elif(lang in "Java,C#,Go,Haxe,Nemerle,TypeScript,C++,C,Vala,Visual Basic,Visual Basic .NET,crosslanguage".split(",")):
        for current in parameterTypes:
            current = getCorrespondingType(lang=lang, dimension=None, theType=current)
        i = 0;
        toReturn = "";
        while(i < len(parameterNames)):
            if(lang in ["Go"]):
                toReturn += parameterNames[i] +" "+ parameterTypes[i];
            elif(lang in "Haxe,Nemerle".split(",")):
                toReturn += parameterNames[i] +" : "+ parameterTypes[i];
            elif(lang in "Visual Basic,Visual Basic .NET".split(",")):
                toReturn += parameterNames[i] +" as "+ parameterTypes[i];
            elif(lang in "TypeScript,C#,Java,C++,Vala,C,crosslanguage".split(",")):
                toReturn += parameterTypes[i] +" "+ parameterNames[i];
            if(i < len(parameterNames) -1):
                if(lang == "crosslanguage"):
                    toReturn += " "
                else:
                    toReturn += ", ";
            i += 1;
        return toReturn;
    notYetDefinedError(lang, inspect.stack()[0][3])

getParameterList = getFunctionParameterList

def methodRequiresParameterTypes(lang):
    '''
        Return true if the start of the method requires parameter types, and otherwise return false.
    '''
    if(lang in "Haskell,Dart,OCaml,REBOL,Erlang,Python,Lua,JavaScript,PHP,Bash,Ruby,Perl,Racket,Common Lisp,Tcl,R,bc".split(",")):
        return False;
    if(lang in "Java,C#,Haxe,Nemerle,Go,C++,Visual Basic,Visual Basic .NET,crosslanguage,Vala".split(",")):
        return True;
    notYetDefinedError(lang, inspect.stack()[0][3])

def startMethod(lang, name, returnType, parameterNames, parameterTypes, isStatic, requiresTheFunctions=False, isDefined=False):
    name = removeInitialDollarSign(name)
    functionName = name
    
    if(lang in ["PHP"]):
        for idx, val in enumerate(parameterNames):
            parameterNames[idx] = addInitialDollarSign(val);
    
    staticString = ""
    if(isStatic == True):
        if(lang in ["Python"]):
            staticString = "@staticmethod"
        elif(lang in ["C#", "Java", "Haxe"]):
            staticString = "static "
    else:
        if(lang in ["Python"]):
            parameterNames = ["self"] + parameterNames
    
    if(isDefined == False):
        isDefined = "false"
    if(isDefined == True):
        isDefined = "true"
    if(requiresTheFunctions == False):
        requiresTheFunctions = "false"
    if(methodRequiresParameterTypes(lang) == True):
        i = 0
        while(i < len(parameterTypes)):
            parameterTypes[i] = getCorrespondingType(lang = lang, dimension=None, theType=parameterTypes[i])
            i = i + 1
    theParameterList = getParameterList(lang=lang, parameterNames=parameterNames, parameterTypes=parameterTypes);
    if(lang in ["Dart"]):
        toReturn = name + "(" + theParameterList + "){"
    if(lang in ["Python"]):
        toReturn = [staticString] + ["def " + name + "(" + theParameterList + "):"];
    if(lang in ["Visual Basic", "Visual Basic .NET"]):
        toReturn = "Function "+name+"("+theParameterList+") As "+returnType
    if(lang in ["Erlang"]):
        toReturn = name+"("+theParameterList+") ->"
    if(lang in ["R"]):
        toReturn = name + " <- function(" + theParameterList + "){"
    if(lang in ["REBOL"]):
        toReturn = name + ": func [" + theParameterList + "] ["
    if(lang in ["Tcl"]):
        toReturn = "proc " + name + " { " + theParameterList + " } {"
    if(lang in ["bc"]):
        toReturn = "define " + name + "(" + theParameterList + ") {"
    if(lang in ["Ruby"]):
        toReturn = "def " + name + " " + theParameterList
    if(lang in ["Go"]):
        toReturn = "func " + name + "(" + theParameterList + ") "+returnType+"{";
    if(lang in ["Java", "C#"]):
        toReturn = "public "+ staticString + returnType + " " + name + "(" + theParameterList + "){";
    if(lang in ["Haxe"]):
        toReturn = staticString + "function " + name + "(" + theParameterList + ") : "+returnType+" {";
    if(lang in ["Nemerle"]):
        toReturn = name + "(" + theParameterList + ") : "+returnType+" {";
    if(lang in ["JavaScript", "PHP", "AWK"]):
        toReturn = "function " + name + "(" + theParameterList + "){";
    if(lang in ["Lua"]):
        toReturn = "function " + name + "(" + theParameterList + ")";
    if(lang in ["C++","Vala"]):
        toReturn = returnType + " " + name + "(" + theParameterList + "){";
    if(lang in ["crosslanguage"]):
        toReturn = "(def " + returnType + " " + name + " (" + theParameterList +")"
    if(lang in ["Haskell"]):
        return name + " " + theParameterList + " ="
    if(lang in ["OCaml"]):
        return name + " " + theParameterList + " ="
    if(lang in ["Haskell"]):
        return "let " + name + " " + theParameterList + " ="
    if(lang in ["Racket", "Common Lisp"]):
        return '"(define ("' + name + " " + theParameterList + ")"
    if(lang in ["Emacs Lisp"]):
        return '"(defun "' + name + " (" + theParameterList + ")"
    if(lang in ["Bash"]):
        return ["function "+functionName+" {"] + theParameterList
    if(lang in ["Perl"]):
        return ["sub "+functionName+" {"] + theParameterList
    
    '''if toReturn is defined:'''    
    if('toReturn' in locals()):
        return toReturn
    notYetDefinedError(lang, inspect.stack()[0][3])

def getCorrespondingTypeWithoutBrackets(lang, theType):
        if theType in ["None", None]:
            return None
        if theType in "True,true".split(","):
            if lang in "Java,Dart,JavaScript,Ruby,Erlang,C#,Haxe,Go,OCaml,Lua,Scala,PHP,crosslanguage,REBOL".split(","):
                return "true"
            elif lang in "Python,Haskell,Visual Basic .NET".split(","):
                return "True"
            elif lang in "Perl".split(","):
                return "1"
            elif lang in "Racket".split(","):
                return "#t"
            elif lang in "Common Lisp".split(","):
                return "t"
        if theType in "False,false".split(","):
            if lang in "Java,Dart,JavaScript,Ruby,Erlang,C#,Haxe,Go,OCaml,Lua,Scala,PHP,crosslanguage,REBOL".split(","):
                return "false"
            elif lang in "Python,Haskell,Visual Basic .NET".split(","):
                return "False"
            elif lang in "Perl".split(","):
                return "0"
            elif lang in "Racket".split(","):
                return "#f"
            elif lang in "Common Lisp".split(","):
                return "nil"
        if theType in "Int,int,Integer".split(","):
            if lang in "OCaml,Dart,Groovy,Scala,Python,Java,C#,C,C++,Vala,Nemerle,crosslanguage".split(","):
                return "int"
            elif lang in "PHP".split(","):
                return "integer"
            elif lang in "Visual Basic .NET".split(","):
                return "Integer"
            elif lang in "Haxe".split(","):
                return "Int"
            elif lang in "JavaScript,CoffeeScript,Lua,Perl".split(","):
                return "number"
            elif lang in "Haskell".split(","):
                return "Num"
            elif lang in "Ruby".split(","):
                return "fixnum"
            #elif lang in "Perl".split(","):
            #    return "scalar"
        elif theType in "boolean,Boolean,bool".split(","):
            if lang in "Python,Java,PHP,Perl".split(","):
                return "boolean"
            if lang in "C++,crosslanguage,Go".split(","):
                return "bool"
            if lang in "Haxe".split(","):
                return "Bool"
        elif theType in "String,str,string".split(","):
            if lang in "Python,crosslanguage".split(","):
                return "str"
            elif lang in "C#,Perl,Lua,JavaScript,Go,PHP,C++,Nemerle,Erlang".split(","):
                return "string"
            elif lang in "Java,Ruby,Haxe,Haskell,Visual Basic,Visual Basic .NET".split(","):
                return "String"
        elif theType in "Void,void".split(","):
            if lang in "Python,Java,C#,Vala,crosslanguage".split(","):
                return "void"
            elif lang in "Haxe".split(","):
                return "void"
        raise Exception("getCorrespondingTypeWithoutBrackets is not yet defined for " + str(lang) + " and the type " + theType)

def getCorrespondingType(lang, theType, dimension=None):
    if type in ["None", None]:
        return None
    #print(theType)
    if("[]" in theType):
        if(lang in ["JavaScript"]):
            return "Array";
        if(lang in ["Python"]):
            return "list";
        '''
        otherwise, do this:
        '''
        theType2 = theType[0:theType.index("[")]
        brackets = theType[len(theType2):len(theType)]
        return getCorrespondingType(lang=lang, theType=theType2, dimension=False)+brackets
    return getCorrespondingTypeWithoutBrackets(lang, theType)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def removeInitialDollarSign(theVar):
    if(theVar[0] == "$"):
        return theVar[1:len(theVar)]
    else:
        return theVar
        
def addInitialDollarSign(theVar):
    if(theVar[0] != "$"):
        return "$" + theVar
    else:
        return theVar

def isIdentifier(theExpression):
    if(theExpression.startswith('"') or theExpression.startswith("'")):
        return False
    if("(" in theExpression or "[" in theExpression or "!" in theExpression or "{" in theExpression or '"' in theExpression):
        if(is_number(theExpression) == False):
            return False
    else:
        return True

def getVariableName(lang, theVar):
    if type(theVar) == list:
        #raise Exception("theVar is a list. Figure out what to do now.")
        return getArrayInitializer(lang, theVar)
    
    for current in [",", "[", "]", "}", "{"]:
        if current in theVar:
            return theVar
    
    if(theVar == True):
        theVar = "True"
    if(theVar == False):
        theVar = "False"
    
    theVar = str(theVar)
    if(is_number(theVar)):
        return theVar
    theVar = removeInitialDollarSign(theVar)
    
    if(theVar in ["False", "True", "false", "true"]):
        return getCorrespondingType(lang, theVar)
    elif(lang in ["PHP", "Perl", "Bash"]):
        if(isIdentifier(theVar)):
            return addInitialDollarSign(theVar);
        else:
            return theVar;
    elif(lang in ["Erlang"]):
        if(isIdentifier(theVar)):
            theVar = theVar[0].upper() + theVar[1:len(theVar)]
            return theVar
        else:
            return theVar
    else:
        return theVar;

def getClassBeginning(lang, className):
        if lang in "Python".split(","):
            return "class " + className + ":"
        if lang in "crosslanguage".split(","):
            return "(class " + className
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "Public Class " + className
        elif lang in "Ruby".split(","):
            return "class " + className
        elif lang in "Java,C#".split(","):
            return "public class " + className + "{"
        elif lang in "Go,Haxe,C++,PHP".split(","):
            return "class " + className + "{"
        elif lang in "JavaScript".split(","):
            return "function " + className + "(){"
        elif lang in "Perl,REBOL,Erlang,Lua,Bash,Racket,Common Lisp,Tcl,bc,AWK,Haskell".split(","):
            return ""
        notYetDefinedError(lang, inspect.stack()[0][3]);

def getClassEnding(lang):
        if lang in "PHP,Python,Ruby,Java,Nemerle,C#,crosslanguage,Go,Groovy,Haxe,JavaScript,Vala".split(","):
            return endCodeBlock(lang)
        elif lang in "C++".split(","):
            return "};"
        elif lang in "Perl,OCaml,Erlang,REBOL,Lua,Bash,Haskell,bc,AWK".split(","):
            return ""
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End Class"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def add(lang, numArray):
    for idx, val in enumerate(numArray):
        numArray[idx] = getVariableName(lang, str(val))
    if(lang in "Java,Groovy,Scala,OCaml,Erlang,Gambas,Hack,C++,MATLAB,REBOL,Lua,Go,AWK,Haskell,Perl,Python,JavaScript,C#,PHP,Ruby,R,Haxe,Visual Basic,Visual Basic .NET,Vala,bc,crosslanguage".split(",")):
        return  "(" + " + ".join(numArray) + ")"
    if(lang in ["Bash"]):
        return  "((" + " + ".join(numArray) + "))"
    if(lang in ["Racket", "Common Lisp"]):
        return  "(+ " + " ".join(numArray) + ")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

#raise to power
def raiseToExponent(lang, num1, num2):
    if lang in "Python".split(","):
        return  num1 + "**" + num2
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def mod(lang, numArray):
    for idx, val in enumerate(numArray):
        numArray[idx] = getVariableName(lang, str(val))
    if lang in "Haxe,Lua,Java,JavaScript,Python,C,C++,C#,Ruby".split(","):
        return  "(" + " % ".join(numArray) + ")"
    elif lang in "Haskell":
        return  "(" + " mod ".join(numArray) + ")"
        
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    
def multiply(lang, numArray):
    for idx, val in enumerate(numArray):
        numArray[idx] = str(val)
    if lang in "Haxe,Perl,Ruby,Lua,Haskell,Hack,Java,OCaml,REBOL,Python,JavaScript,C#,Visual Basic,Visual Basic .NET,Dart".split(","):
        return  "(" + " * ".join(numArray) + ")"
    if(lang in ["Bash"]):
        return  "((" + " * ".join(numArray) + "))"
    if(lang in ["Racket", "Common Lisp"]):
        return  "(* " + " ".join(numArray) + ")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def subtract(lang, numArray):
    for idx, val in enumerate(numArray):
        numArray[idx] = str(val)
    if(lang in "Java,Perl,Hack,OCaml,Python,REBOL,JavaScript,C#,PHP,Visual Basic,Visual Basic .NET,Ruby,Haxe,Lua".split(",")):
        return  "(" + " - ".join(numArray) + ")"
    if(lang in ["Racket", "Common Lisp"]):
        return  "(-" + " ".join(numArray) + ")"
    notYetDefinedError(lang, inspect.stack()[0][3]);

def divide(lang, numArray):
    if(lang in ["Java", "Lua", "Haskell", "OCaml", "Python", "JavaScript", "C#", "PHP"]):
        return  "/".join(numArray)
    if(lang in ["Racket"]):
        return  "(/" + " ".join(numArray) + ")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

mul = multiply
sub=subtract
Add = add


def concatenateStrings(lang, stringArray):
    i = 0
    for current in stringArray:
        stringArray[i] = getVariableName(lang, current)
        i += 1
    
    if(lang in ["Java", "Python", "JavaScript", "C#", "Haxe", "Ruby"]):
        return  " + ".join(stringArray)
    elif(lang in ["Visual Basic .NET"]):
        return  " & ".join(stringArray)
    elif(lang in ["Lua"]):
        return  " .. ".join(stringArray)
    elif(lang in ["REBOL"]):
        return  "(append " + stringArray[0] + " " + " ".join(stringArray[1 : len(stringArray)])+")"
    elif(lang in ["Bash"]):
        return  "".join(stringArray)
    elif(lang in ["Haskell"]):
        return  " ++ ".join(stringArray)
    elif(lang in ["OCaml"]):
        return  " ^ ".join(stringArray)
    elif(lang in ["PHP"]):
        return " . ".join(stringArray)
    elif(lang in ["crosslanguage"]):
        return "("+ " . ".join(stringArray)+")"
    elif(lang in ["Octave"]):
        return "strcat(" + ", ".join(stringArray) + ")"
    elif(lang in ["Erlang"]):
        return "string:concat(" + ", ".join(stringArray) + ")"
    elif(lang in ["Perl"]):
        return "(join " + ", ".join(['""'] + stringArray) + ")"
    elif(lang in ["Go"]):
        return "strings.Join([]string{" + ", ".join(stringArray) + "}, \" \")"
    elif(lang in ["Racket"]):
        return "(string-append " + " ".join(stringArray) + ")"
    elif(lang in ["Common Lisp"]):
        return "(concatenate" + " ".join(stringArray) + ")"
    notYetDefinedError(lang, inspect.stack()[0][3]);

def concatenateArrays(lang, arrayOfArrays):
    '''Concatenate two arrays, without flattening any of them.'''
    
    if lang in ["Python", "Haskell", "Ruby"]:
        return concatenateStrings(lang, arrayOfArrays)
    if lang in ["crosslanguage"]:
        return getFunctionCall(lang = lang, function="concatenateArrays", parameters=arrayOfArrays, fromClass=None)
    if lang in ["Lua"]:
        '''
        http://stackoverflow.com/questions/1410862/concatenation-of-tables-in-lua
        '''
    if lang in ["PHP"]:
        '''
        http://php.net/manual/en/function.array-merge.php
        '''
        return "array_merge(" + ", ".join(arrayOfArrays) + ")"
    if lang in ["Java"]:
        '''
        http://stackoverflow.com/questions/80476/how-to-concatenate-two-arrays-in-java
        '''
    if lang in ["JavaScript"]:
        firstElement = arrayOfArrays[0]
        arrayOfArrays = arrayOfArrays[1:len(arrayOfArrays)]
        return firstElement + ".concat(" + ", ".join(arrayOfArrays) + ")"
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def getJavaInitializer(lang, theArray, opening, closing):
    if(isinstance(theArray,list)):
        toReturn = opening;
        i=0
        while(i < len(theArray)):
            toReturn += getJavaInitializer(lang, theArray[i], opening, closing);
            if((i < len(theArray)-1) and (lang != "REBOL")):
                toReturn += ",";
            i = i + 1
        toReturn += closing;
        return toReturn;
    else:
        return str(theArray);

def getArrayInitializer(lang, arrayObject):
    if lang in ["Java", "C#", "Go", "Lua", "C++", "Visual Basic .NET"]:
        '''
        port getJavaInitializer from javascriptVersion
        '''
        return getJavaInitializer(lang=lang,opening="{", closing="}", theArray = arrayObject)
    if lang in ["Python", "JavaScript", "Haxe", "Haskell", "Ruby", "REBOL"]:
        return getJavaInitializer(lang=lang, opening="[", closing="]", theArray = arrayObject)
    elif lang in ["PHP"]:
        return getJavaInitializer(lang=lang, opening="array(", closing=")", theArray = arrayObject)
    elif lang in ["Perl"]:
        return getJavaInitializer(lang=lang, opening="(", closing=")", theArray = arrayObject)
    elif lang in ["crosslanguage"]:
        return crossLanguageStatement("getArrayInitializer", [arrayObject])
    notYetDefinedError(lang, inspect.stack()[0][3]);

initializerList = getArrayInitializer

def startConstructor(lang, className, parameterNames, parameterTypes):
    parameterList = getParameterList(parameterNames=parameterNames, parameterTypes=parameterTypes);
    if lang in ["Java", "C#"]:
        return "public " + className+"("+parameterList+"){"
    if lang == "Python":
        return "def __init__("+"self, "+parameterList+"):"
    if lang == "JavaScript":
        return ["var args = arguments;", "__construct = function(that){"]
    if lang == "PHP":
        return "public function __construct("+parameterList+")"
    if lang == "Haxe":
        return "public function new() {"
    notYetDefinedError(functionName = inspect.stack()[0][3]);
    
def endConstructor():
    if lang == "JavaScript":
        return "}(this)"
    elif lang in ["Java", "Vala", "C#", "Python", "PHP", "crosslanguage"]:
        return endCodeBlock();
    notYetDefinedError(functionName = inspect.stack()[0][3]);
    

def constructor(className, parameterNames, parameterTypes, body):
    i = 0
    toAdd = []
    if lang == "JavaScript":
        for current in parameterNames:
            toAdd += ["var " + current + " = args[" + str(i) + "];"]
            i += 1
    body = concatenateAllElements(body)
    body = toAdd + body
        
    i = 0
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startConstructor(className, parameterNames, parameterTypes)] +body+ [endConstructor()]
    return body

def startCase(lang, condition):
    if lang == "Scala":
        return "case " + condition + " =>"
    if lang in ["Erlang"]:
        return startIf(condition)
    if lang in "Dart,JavaScript,C#,Java,Groovy,C++,PHP,C,Go,Haxe,AWK,Vala".split(","):
        return "case "+condition+":"
    if lang in ["REBOL"]:
        return condition+" ["
    if lang in ["Fortran"]:
        return "case ("+condition+")"
    if lang in ["crosslanguage"] :
        return "(case "+condition
    if lang in ["Visual Basic","Visual Basic .NET"]:
        return "Case "+condition
    if lang in ["Ruby"]:
        return "when "+condition
    if lang in ["Haskell"]:
        return condition + " ->"
    if lang in ["Bash"]:
        return condition + ")"
    if lang in ["Tcl"]:
        return condition + "{"
    if lang in ["OCaml"]:
        return "| "+condition+" ->";
    notYetDefinedError(lang = lang, functionName = inspect.stack()[0][3]);
    
def endCase(lang):
    #This should not enable fall-through.
    if lang in ["PHP", "Java", "AWK", "Vala", "Dart"]:
        return "break;"
    if lang in ["crosslanguage", "REBOL"]:
        return endCodeBlock();
    if lang in "JavaScript,Groovy,Scala,OCaml,Ada,C#,Ruby,C++,PHP,C,Go,Haskell,Haxe,Visual Basic,Visual Basic .NET,Fortran".split(","):
        return ""
    if lang in ["Erlang"]:
        return ";"
    if lang in ["Bash"]:
        return ";;"
    if lang in ["Tcl"]:
        return "}"
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def case(lang, condition, body):
    body = concatenateAllElements(body)
        
    i = 0
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startCase(lang, condition)] +body+ [endCase(lang)]
    return body

def startDefault(lang):
    if lang in "JavaScript,Groovy,Dart,Java,C#,C++,Haxe,PHP,AWK,Vala,Go".split(","):
        return "default:"
    if lang in ["Fortran"]:
        return "case default"
    if(lang in ["crosslanguage"]):
        return "(default"
    elif lang in ["Scala"]:
        return "_ =>"
    elif lang in ["Haskell", "Erlang"]:
        return "_ ->"
    elif lang in "OCaml":
        return "| _ ->"
    if lang in ["Visual Basic", "Visual Basic .NET"]:
        return "Case Else"
    if lang in ["Bash"]:
        return "*)"
    if lang in ["Ruby"]:
        return "else"
    if lang in ["Tcl"]:
        return "default"
    if lang in ["REBOL"]:
        return "] ["
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    
def endDefault(lang):
    if lang in "Dart,Groovy,Scala,JavaScript,OCaml,REBOL,Erlang,Java,Vala,C#,C++,Haxe,Haskell,PHP,Go,Visual Basic,Visual Basic .NET,Ruby,Fortran,AWK".split(","):
        return ""
    if lang in ["Bash"]:
        return ";;"
    if lang in ["crosslanguage"]:
        return endCodeBlock()
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def default(lang, body):
    body = concatenateAllElements(body)
        
    i = 0
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startDefault(lang)] +body+ [endDefault(lang)]
    return body

def startSwitch(lang, variableToCheck):
    variableToCheck = getVariableName(lang, variableToCheck);
    if lang in ["Scala"]:
        return variableToCheck + " match {"
    if lang in "JavaScript,Groovy,Dart,AWK,C#,Java,C++,PHP,C,Go,Haxe,Vala".split(","):
        return "switch("+variableToCheck+"){"
    if lang in ["crosslanguage"]:
        return "(switch "+variableToCheck
    if lang in ["Nemerle"]:
        return "switch("+variableToCheck+"){"
    if lang in ["REBOL"]:
        return "switch/default "+variableToCheck+" ["
    if lang in ["F#"]:
        return "match ("+variableToCheck+") with"
    if lang in ["Haskell", "Erlang"]:
        return "case " +variableToCheck+ " of"
    if lang in ["Ruby"]:
        return "case " +variableToCheck
    if lang in ["Bash"]:
        return "case " +variableToCheck+ " in"
    if lang in ["Visual Basic", "Visual Basic .NET"]:
        return "Select Case " + variableToCheck
    if lang in ["OCaml"]:
        return "match "+variableToCheck+" with"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def endSwitch(lang):
    if lang in "Dart,Groovy,Scala,JavaScript,REBOL,crosslanguage,Nemerle,AWK,Ruby,Vala,Haskell,C#,Java,C++,PHP,C,Go,Haskell,Haxe,Ruby,Tcl".split(","):
        return endCodeBlock(lang)
    elif lang in ["Visual Basic","Visual Basic .NET"]:
        return "End Select"
    elif lang in ["Bash"]:
        return "esac"
    elif lang in ["Ada"]:
        return "end case;"
    elif lang in ["Erlang"]:
        return "end"
    elif lang in ["OCaml"]:
        return ""
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def Switch(lang, condition, body):
    body = concatenateAllElements(body)
        
    i = 0
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startSwitch(lang, condition)] +body+ [endSwitch(lang)]
    return body

def initializeEmptyArray(lang, variableType, variableName, arrayStarter, arrayDimensions):
    try:
        if(lang in ["Python"]):
            return "numpy.empty(" + call(function = "", parameters = arrayDimensions, fromClass=None)+")"
        if(lang in ["Java"]):
            return variableType + arrayStarter + " " + variableName + " = new " + getArrayAccessor(arrayName=variableType, indexList = arrayDimensions)
        if(lang in ["JavaScript"]):
            return "var " + variableName+" = "+callFunction(function="createArray", parameters=arrayDimensions, fromClass=None)
        if(lang in ["C#"]):
            return variableType +"["+arrayStarter+"] " + variableName + " = new " + getArrayAccessor(arrayName=variableType, indexList = arrayDimensions)
        if(lang in ["crosslanguage"]):
            return crossLanguageStatement("initializeEmptyArray", [variableType, variableName, arrayStarter, arrayDimensions])
    except Exception:
        raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + " and the dimensions " + str(arrayDimensions))
    finally:
        return "None"
    
def initializeArrayWithValue(lang, variableType, arrayStarter, variableName, initialValue, arrayDimensions):
    if(lang in ["crosslanguage"]):
        return crossLanguageStatement("initializeArrayWithValue", [variableType, arrayStarter, variableName, initialValue, arrayDimensions])
    if(lang in ["Java"]):
        return variableType + arrayStarter + " " + variableName + " = "+ initialValue
    if(lang in ["Python", "Lua", "Ruby"]):
        return variableName + " = "+ initialValue
    if(lang in ["PHP"]):
        return variableName + " = "+ initialValue
    if(lang in ["Haskell"]):
        return "let " + variableName + " = "+ initialValue
    if(lang in ["JavaScript", "Haxe"]):
        return "var " + variableName + " = "+ initialValue
    if(lang in ["C#"]):
        return variableType+"["+arrayStarter+"] "+variableName+" = new " + accessArray(arrayName=variableType, indexList=arrayDimensions) + initialValue
    if(lang in ["C++"]):
        return variableType+" "+variableName+arrayStarter+" = " + initialValue
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + ", the dimensions " + str(arrayDimensions) + ", and the initial value " + str(initialValue))


def initializationRequiresType(lang):
    '''
    Return true if a variable initialization must include the type of the variable, and return false otherwise.
    '''
    if(lang in "C++,Java,C#,C,Visual Basic,Visual Basic .NET,Vala,crosslanguage".split(",")):
        return True
    elif(lang in "Python,Dart,REBOL,Erlang,Haxe,Lua,JavaScript,Ruby,Bash,PHP,Haskell,Racket,Tcl,R,bc,Perl".split(",")):
        return False
    notYetDefinedError(lang, inspect.stack()[0][3]);

def initializeScalar(lang, variableType, variableName, initialValue):
    #See also: setvar
    variableName = getVariableName(lang, variableName)
    '''initialValue is not None here'''
    if lang in ["Python", "REBOL", "PHP"]:
        return setVar(lang=lang, valueToGet = initialValue, valueToChange = variableName)
    elif(lang in ["Lua", "Ruby", "bc"]):
        return variableName + " = " + initialValue
    elif(lang in ["Perl", "AWK"]):
        return variableName + " = " + initialValue
    elif(lang in ["Erlang"]):
        return variableName + " = " + initialValue
    elif(lang in ["Tcl"]):
        return "set " + variableName + " " + initialValue
    elif(lang in ["Bash"]):
        return "local "+variableName[1:len(variableName)]+"="+initialValue
    elif(lang in ["Go"]):
        return variableName + " := " + initialValue
    elif(lang in ["Java", "C#", "C++"]):
        return getCorrespondingType(lang=lang, dimension=None, theType=variableType) +" "+ variableName + " = " + initialValue
    elif(lang in ["crosslanguage"]):
        return "(initialize " + variableType +" "+ variableName +" "+ initialValue+")"
    elif(lang in ["JavaScript", "Haxe", "Dart"]):
        return "var " + variableName + " = " + initialValue
    elif(lang in ["Haskell"]):
        return "let " + variableName + " = " + initialValue
    elif(lang in ["Visual Basic","Visual Basic .NET"]):
        return "Dim "+variableName+" As "+variableType+" = "+initialValue
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + " and the initial value " + str(initialValue))

def initializeVar(lang, variableName, variableType, initialValue, arrayDimensions):
    if(arrayDimensions == "None"):
        arrayDimensions = None
    
    if(initializationRequiresType(lang) == True):
        variableType = getCorrespondingType(lang=lang, theType=variableType)
    
    variableName = getVariableName(lang, variableName)
    
    if(arrayDimensions == 0):
        arrayDimensions = None;
    arrayStarter = ""
    if(type(arrayDimensions) is list):
        if(lang == "C++"):
            i = 0
            for current in arrayDimensions:
                arrayDimensions[i] = str(current)
                i += 1
            arrayStarter = "[" + "][".join(arrayDimensions) + "]";
        else:
            for i in arrayDimensions :
                if(lang == "Java"):
                    arrayStarter += "[]"
                if(lang == "C#"):
                    arrayStarter += ","
        if(lang == "C#"):
            arrayStarter = arrayStarter[1:len(arrayStarter)]
    if(type(initialValue) is list):
        initialValue = initializerList(initialValue)
    if(type(initialValue) is int):
        initialValue = str(initialValue)
    '''
    to do: if initialValue is a list, then convert it to a string using initializerList
    '''
    
    
    '''if the type isn't an array:'''
    if(arrayDimensions==None):
        return initializeScalar(lang=lang, variableType=variableType, variableName=variableName, initialValue=initialValue)
        '''If the initial value is not defined:'''
    elif((type(arrayDimensions) is list) & (initialValue is None)):
        return initializeEmptyArray(arrayDimensions=arrayDimensions, variableType=variableType, variableName=variableName, arrayStarter = arrayStarter)
        '''If the initial value is defined:'''
    elif((type(arrayDimensions) is list) and type(initialValue) is str):
        return initializeArrayWithValue(initialValue=initialValue, arrayStarter=arrayStarter, variableName=variableName, variableType=variableType, arrayDimensions=arrayDimensions)
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + ", the dimensions " + str(arrayDimensions) + ", and the initial value " + str(initialValue))

def typeConversion(lang, objectToConvert, convertFrom, convertTo):
    objectToConvert = getVariableName(objectToConvert)
    convertFrom = getCorrespondingType(theType = convertFrom)
    convertTo = getCorrespondingType(theType = convertTo)
    if(convertFrom == convertTo):
        return objectToConvert;
    if(lang in "crosslanguage"):
        return "(convert " + objectToConvert +" from "+ convertFrom +" to "+ convertTo + ")"
    if(lang in ["JavaScript"]):
        if(convertTo in ["string"]):
            return objectToConvert + ".toString()"
    if(lang in ["Python"]):
        if(convertTo in ["str"]):
            return "str("+str(objectToConvert) + ")"
        if(convertTo in ["int"]):
            return "int("+str(objectToConvert) + ")"
    if(lang in ["Java"]):
        if(convertTo in "String"):
            return objectToConvert + ".toString()"
        if(convertTo == "int"):
            if(convertFrom == "String"):
                return "Integer.parseInt("+objectToConvert+")"
    if(lang in ["C#"]):
        if(convertTo == "int"):
            if(convertFrom == "string"):
                return "Convert.ToInt32("+objectToConvert+")"
        if(convertTo == "string"):
            if(convertFrom == "int"):
                return objectToConvert+".ToString()"
    if(lang in ["Haskell"]):
        if(convertTo == getCorrespondingType("string")):
            if(convertFrom == getCorrespondingType("int")):
                return "show("+objectToConvert+")"
    if(lang in ["PHP"]):
        if(convertTo == getCorrespondingType("string")):
            if(convertFrom == getCorrespondingType("int")):
                return "(int)"+objectToConvert
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " from the type " + convertFrom + " to the type " + convertTo);

def toString(lang, objectToConvert, convertFrom):
    return typeConversion(objectToConvert=objectToConvert, convertFrom=convertFrom, convertTo="String")

def subString(lang, aString, start, end):
        if lang in "JavaScript,Java".split(","):
            return aString + ".substring(" + start + ", " + end + ")"
        elif lang in "crosslanguage".split(","):
            return "(substring " + aString + " " + start + " " + end + ")"
        elif lang in "C#,Visual Basic .NET".split(","):
            return aString + ".Substring(" + start + ", " + end + ")"
        elif lang in "Lua".split(","):
            return "string.sub(" + aString + ", " + start + ", " + end + ")"
        elif lang in "Tcl".split(","):
            return "[string range " + aString + " " + start + ' ' + end + "]"
        elif lang in "Ruby".split(","):
            return aString + "[" + start + ".." + end + "]"
        elif lang in "Python,Go".split(","):
            return aString + "[" + start + ":" + end + "]"
        elif lang in "PHP,AWK,Perl".split(","):
            return "substr(" + aString + "," + start + "," + end + ")"
        elif lang in "R".split(","):
            return "substr(" + aString + "," + start + "," + end + ")"
        elif lang in "Haxe".split(","):
            return aString + ".substr(" + start + "," + end + ")"
        # Despite having the same syntax, the substring function works differently in Racket and Emacs Lisp.
        elif lang in "Emacs Lisp".split(","):
            return "(substring " + aString + " " + start + " " + end + ")"
        elif lang in "Racket".split(","):
            return "(substring " + aString + " " + start + " " + end + ")"
        elif lang in "Erlang".split(","):
            return "string:sub_string("+aString+", "+start+", "+end+")"
        notYetDefinedError(lang, inspect.stack()[0][3])
    
'''
def subString(string, start, end):
    if(lang in ["JavaScript", "Java"]):
        return string + ".substring("+start+", " + end + ")";
    if(lang in ["Python", "Go"]):
        return string + "["+ start +":"+ end +"]";

    
    notYetDefinedError(functionName = inspect.stack()[0][3]);
'''

def newObject(lang, className, objectName, parameterList):
    '''
    Create a new instance of an object.
    Refer to the implementation of callFunction when implementing this.
    '''
    
    functionCall = callFunction(function=className, fromClass=None, parameters=parameterList)
    
    if(lang in ["Java", "C#"]):
        return className + " " + objectName + " = new " + functionCall
    if(lang in ["JavaScript"]):
        return "var " + objectName + " = new " + functionCall
    if(lang in ["Python"]):
        return objectName + " = " + functionCall
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def privateMember(lang, variableName, variableType, initialValue, arrayDimensions):
    '''
        This method declares an instance variable in each language.
    '''
    theVar = initializeVar(variableName, variableType, initialValue, arrayDimensions)
    if(lang in ["JavaScript"]):
        return theVar
    if(lang in ["Java", "C#"]):
        return "private " + theVar
    if(lang in ["Python"]):
        return "self."+theVar

def endFor(lang, increment):
    increment = getVariableName(increment)
    if lang in "Python".split(","):
        return increment
    elif lang in "Java,JavaScript,C#,crosslanguage,Ruby,Go,C++,Perl,PHP".split(","):
        return endCodeBlock()
    notYetDefinedError(functionName = inspect.stack()[0][3]);
    
def indexOf(lang, string, substring):
    string = getVariableName(string)
    substring = getVariableName(string)
    '''
    Should return the index if present, and -1 otherwise.
    '''
    if(lang in ["JavaScript","Java"]):
        return string + ".indexOf("+substring+")";
    if(lang in ["Ruby"]):
        return string + ".index("+substring+")";
    if(lang in ["C#"]):
        return string + ".IndexOf("+substring+")";
    if(lang in ["Python"]):
        return string + ".find("+substring+")";
    if(lang in ["Go"]):
        return "strings.Index("+string+", "+substring+")"
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def startElse(lang):
        if lang in "Python".split(","):
            return "else:"
        elif lang in "Scala,Groovy,Java,Dart,AWK,JavaScript,Haxe,PHP,C#,Go,Perl,C++,C,Tcl,R,Vala,bc".split(","):
            return "else {"
        elif lang in "Ada,Bash,Ruby,CoffeeScript,Lua,Haskell,MATLAB,Octave,Gambas,OCaml,Fortran,F#,Oz,Nemerle".split(","):
            return "else"
        elif lang in "Racket,crosslanguage".split(","):
            return "(else"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "Else"
        elif lang in "Erlang".split(","):
            return "; true ->"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def startElseIf(lang, condition):
        condition = getVariableName(lang, condition)
        if lang in "Scala,Groovy,Java,Dart,Vala,JavaScript,C#,C++,Haxe".split(","):
            return "else if(" + condition + "){"
        elif lang in "Go".split(","):
            return "else if " + condition + " {"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "ElseIf " + condition + " Then"
        elif lang in "Racket".split(","):
            return "(" + condition
        elif lang in "PHP".split(","):
            return "elseif(" + condition + "){"
        elif lang in "crosslanguage".split(","):
            return "elif " + condition
        elif lang in "MATLAB".split(","):
            return "elseif " + condition
        elif lang in "Python".split(","):
            return "elif " + condition + ":"
        elif lang in "F#".split(","):
            return "elif " + condition + " then"
        elif lang in "Perl".split(","):
            return "elsif(" + condition + "){"
        elif lang in "Ruby".split(","):
            return "elsif " + condition
        elif lang in "Lua".split(","):
            return "elseif " + condition + " then"
        elif lang in "Bash".split(","):
            return "elif [ " + condition + " ] then"
        elif lang in "Haskell,OCaml".split(","):
            return "else if " + condition + " then"
        elif lang in "CoffeeScript".split(","):
            return "else if " + condition
        elif lang in "Erlang".split(","):
            return "; " + condition + " ->"
        
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def endElse(lang):
    if lang in "CoffeeScript,Groovy,Scala,Tcl,Dart,R,Vala,Python,F#,Java,JavaScript,Haxe,PHP,C#,crosslanguage,Perl,C++,Go,Haskell,Racket".split(","):
        return endCodeBlock(lang)
    elif lang in "Ada,Bash,Lua,Ruby,Visual Basic,Visual Basic .NET,Octave,MATLAB,Gambas,Fortran,Erlang".split(","):
        return ""
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def endElseIf(lang):
        if lang in "Scala,Groovy,CoffeeScript,Tcl,Vala,AWK,R,Python,F#,Java,Dart,JavaScript,Haxe,PHP,C#,crosslanguage,Perl,C++,Go,Racket".split(","):
            return endCodeBlock(lang)
        elif lang in "Ada,Bash,Lua,Ruby,Haskell,Visual Basic,Visual Basic .NET,MATLAB,Octave,Gambas,Fortran,OCaml,Erlang".split(","):
            return ""
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def elseIf(lang, condition, body):
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startElseIf(lang=lang, condition=condition)] +body+ [endElseIf(lang)]
    return body
    
def declareConstant(lang, variableType, arrayDimensions, variableName, initialValue):
    variableDeclaration = initializeVar(variableType=variableType, initialValue=initialValue, arrayDimensions=arrayDimensions, variableName=variableName)
    if(lang in ["Python"]):
        return variableDeclaration
    if(lang in ["Java"]):
        return "final " + variableDeclaration
    if(lang in ["JavaScript"]):
        return variableDeclaration
    if(lang in ["C#"]):
        return "Const " + variableDeclaration
    if(lang in ["Go"]):
        return "Const " + variableDeclaration
    if(lang in ["crosslanguage"]):
        return crossLanguageStatement()
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def printSomething(lang):
    theIndentation = 0;
    print(getClassBeginning(className="Main"));
    theIndentation = theIndentation + 1;
    
    print(startMethod(isDefined = False, requiresTheFunctions=False, name = "testFunction", returnType="int", parameterNames=["thing1", "thing2"], parameterTypes=["int", "int"]));
    
    '''print(getComment(lang="Python", comment="Hi!", indent=theIndentation));'''
    
    theIndentation = theIndentation - 1;
    print(getClassEnding());

def testStatementsInLanguage(arr):
    print("Testing statements in each language using " + inspect.stack()[0][3])
    i = 0;
    while(i < len(arr)):
        if(arr[i] != arr[i+1]):
            print("In the function testStatementsInLanguage, the output should be " + str(arr[i+1]) + " instead of " + str(arr[i]));
        else:
            print(arr[i])
        i += 2;
        
'''Test each statement in Python.'''

def concatenateAllElements(arr):
    if type(arr) == str:
        arr = [arr]
    i = 0
    while(i < len(arr)):
        if(type(arr[i]) == str):
            arr[i] = [arr[i]]
        i += 1
    
    import itertools;
    arr = list(itertools.chain(*arr))
    newArr = []
    i=0
    while(i < len(arr)):
        if(type(arr[i]) == str and (arr[i].strip() != "")):
            newArr += [arr[i]]
        if(type(arr[i]) == list):
            newArr += arr[i]
        i = i + 1
    return newArr;

def include(fileName):
    if lang in "Java,Python,Haxe,Scala".split(","):
        return "import " + fileName
    elif lang in "Go".split(","):
        return "import " + fileName
    elif lang in "C#".split(","):
        return "using " + fileName
    elif lang in "Ruby".split(","):
        return "require '" + fileName + "'"
    elif lang in "crosslanguage".split(","):
        return "(include " + fileName + ")"
    notYetDefinedError(functionName = inspect.stack()[0][3])

'''
def include(fileName):
    '/''
    include is the file or class name, without the file extension.
    '/''
    if(lang in "VBScript"):
        return 'includeFile "'+fileName+'.vbi"'
    notYetDefinedError(functionName = inspect.stack()[0][3])
'''

def getClass(lang, className, body):
    i = 0
    body = concatenateAllElements(body)
    if(type(body) == str):
        body = [body]
    while(i < len(body)):
        if(getClassBeginning(lang, className) != ""):
            body[i] = "    " + body[i]
        i = i + 1
    body = [getClassBeginning(lang=lang, className = className)] +body+ [getClassEnding(lang)]
    toReturn = ""
    i = 0
    while(i < len(body)):
        toReturn += body[i]+"\n";
        i = i + 1
    return toReturn



def methodRequiresReturnType(lang):
    '''
    Return true if the method requires a return type, and return false otherwise.
    '''
    if(lang in "Haskell,Dart,OCaml,REBOL,Erlang,AWK,Python,JavaScript,Bash,PHP,Lua,Ruby,Perl,Racket,Common Lisp,R,Tcl,bc".split(",")):
        return False
    if(lang in "Java,C++,C#,Go,Haxe,Visual Basic,Visual Basic .NET,crosslanguage,Vala".split(",")):
        return True
    notYetDefinedError(lang, inspect.stack()[0][3])

def endMethod(lang, methodName):
        if lang in "bc,Dart,Tcl,Clojure,Nemerle,MATLAB,Vala,REBOL,Common Lisp,Emacs Lisp,AWK,R,C++,F#,PHP,Lua,Python,Java,JavaScript,C#,Haxe,Perl,crosslanguage,Ruby,Go,Racket".split(","):
            return endCodeBlock(lang)
        elif lang in "Haskell,OCaml".split(","):
            return ""
        elif lang in "Erlang".split(","):
            return "."
        elif lang in "Ada".split(","):
            return "end " + methodName + ";"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End Sub"
        elif lang in "Gambas".split(","):
            return "END"
        elif lang in "Bash".split(","):
            return "}"
        elif lang in "Octave".split(","):
            return "endfunction"
        elif lang in "Fortran".split(","):
            return "end function " + methodName
        elif lang in "OCaml".split(","):
            return ";;"
        notYetDefinedError(lang, inspect.stack()[0][3]);

def getFunction(lang, functionName, isStatic, parameterNames, parameterTypes, returnType, body, requiresTheFunctions="", isDefined="", description=""):
    print("Parameter names: ", parameterNames)
    print("Parameter types: ", parameterTypes)
    if type(parameterNames) == str:
        parameterNames = [parameterNames]
    if type(parameterTypes) == str:
        parameterTypes = [parameterTypes]
    
    if(isStatic == "static"):
        isStatic = True
    
    i = 0
    print(parameterNames)
    print(parameterNames)
    for current in parameterNames :
        parameterNames[i] = getVariableName(lang, current)
        i += 1
        
    if(methodRequiresReturnType(lang) == True):
        returnType = getCorrespondingType(lang=lang, dimension=None, theType=returnType)
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startMethod(lang=lang, isStatic=isStatic, requiresTheFunctions=requiresTheFunctions, isDefined=isDefined, returnType = returnType, name = functionName, parameterNames = parameterNames, parameterTypes = parameterTypes)] +body+ [endMethod(lang=lang, methodName=functionName)]
    return body
    
def includeForLang(langToInclude, body):
    if(langToInclude == lang):
        '''body = concatenateAllElements(body)'''
        return body
    else:
        return "";
    
def forLoop(body, initializer, condition, increment):
    i = 0
    if(type(body) == str):
        body = body[0]
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startFor(initializer=initializer, condition=condition, increment=increment)] +body+ [endFor(increment=increment)]
    return body

def startConditionalBlock(lang):
    if(lang in "CoffeeScript,Groovy,Scala,Dart,Tcl,OCaml,bc,AWK,R,Octave,Ada,Gambas,Python,Java,JavaScript,C++,Bash,Haxe,Perl,Ruby,C#,Lua,PHP,Go,Haskell,F#,MATLAB,Visual Basic,Visual Basic .NET,Fortran,Vala".split(",")):
        return "";
    if(lang in ["Scheme", "Racket"]):
        return "(cond"
    if(lang in ["crosslanguage"]):
        return "cond"
    if(lang in ["Erlang"]):
        return "if"
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3])

def endConditionalBlock(lang):
    if(lang in "CoffeeScript,Scala,Groovy,Tcl,OCaml,bc,R,Python,Java,Dart,C++,JavaScript,Haxe,Perl,C#,PHP,Go,Haskell,F#,AWK,Vala".split(",")):
        return "";
    elif(lang in ["Bash"]):
        return "fi"
    elif(lang in ["Octave"]):
        return "fi"
    elif(lang in ["Lua", "Ruby", "MATLAB", "Erlang"]):
        return "end"
    elif(lang in ["Scheme", "Racket", "crosslanguage"]):
        return ")"
    elif(lang in ["Visual Basic", "Visual Basic .NET"]):
        return "End If"
    elif(lang in ["Gambas"]):
        return "ENDIF";
    elif(lang in ["Fortran"]):
        return "end if"
    elif(lang in ["Ada"]):
        return "end if;"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def conditionalBlock(lang, body):
    body = concatenateAllElements(body)
    body = [startConditionalBlock(lang)] +body+ [endConditionalBlock(lang)]
    return body

def startMain():
        if lang in "Java,Groovy".split(","):
            return "public static void main(String[] args){"
        elif lang in "MATLAB".split(","):
            return "function main"
        elif lang in "Erlang".split(","):
            return "main() ->"
        elif lang in "crosslanguage".split(","):
            return "(main"
        elif lang in "Visual Basic".split(","):
            return "Sub Main()"
        elif lang in "Visual Basic .NET".split(","):
            return "Public Shared Sub Main()"
        elif lang in "Gambas".split(","):
            return "PUBLIC SUB Main()"
        elif lang in "C++".split(","):
            return "int main( int argc, const char* argv[] ){"
        elif lang in "Python,OCaml,REBOL,bc,Tcl,JavaScript,Perl,PHP,Lua,Ruby,Racket".split(","):
            return ""
        elif lang in "Bash".split(","):
            return "function main {"
        elif lang in "Haskell".split(","):
            return "main = do"
        elif lang in "Go".split(","):
            return "func main(){"
        elif lang in "C#".split(","):
            return "static int Main(string[] args){"
        elif lang in "Haxe".split(","):
            return "static function main() {"
        elif lang in "Vala".split(","):
            return "void main() {"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def endMain():
        if lang in "Java,Vala,Nemerle,crosslanguage,C#,Haxe,Go,Scala,Perl".split(","):
            return endCodeBlock()
        elif lang in "C++".split(","):
            return "return 0; }"
        elif lang in "Erlang".split(","):
            return "."
        elif lang in "PHP,REBOL,JavaScript,Python,Lua,Ruby,Haskell,Racket,Tcl,bc".split(","):
            return ""
        elif lang in "Bash".split(","):
            return "}\nmain"
        elif lang in "MATLAB".split(","):
            return "end"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End Sub"
        elif lang in "Gambas".split(","):
            return "END"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def main(body):
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        if(startMain() != ""):
            body[i] = "    " + body[i]
        i = i + 1
    body = [startMain()] +body+ [endMain()]
    return body
    
def whileLoop(lang, body, condition):
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startWhile(lang=lang,condition=condition)] +body+ [endWhile(lang)]
    return body
    
def startIf(lang, condition):
        condition = getVariableName(lang, condition)
        if lang in "Python".split(","):
            return "if " + condition + ":"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "If " + condition
        elif lang in "Erlang".split(","):
            return condition + " ->"
        elif lang in "REBOL".split(","):
            return "if [" + condition + "] ["
        elif lang in "Octave,CoffeeScript".split(","):
            return "if " + condition
        elif lang in "crosslanguage".split(","):
            return "(if " + condition
        elif lang in "Racket".split(","):
            return "(" + condition
        elif lang in "Java,Groovy,Scala,Dart,JavaScript,C#,C,C++,Perl,Haxe,PHP,R,AWK,Vala,bc,Squirrel".split(","):
            return "if(" + condition + "){"
        elif lang in "Tcl".split(","):
            return "if{" + condition + "}{"
        elif lang in "Go".split(","):
            return "if " + condition + " {"
        elif lang in "Bash".split(","):
            return "if [ " + condition + " ] then"
        elif lang in "Fortran".split(","):
            return "if (" + condition + ") then"
        elif lang in "Gambas".split(","):
            return "IF " + condition + " THEN"
        elif lang in "Haskell,OCaml,Lua,Ruby,F#".split(","):
            return "if " + condition + " then"
        notYetDefinedError(lang= lang, functionName = inspect.stack()[0][3]);

def endIf(lang):
        if lang in "Scala,Groovy,CoffeeScript,bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,Dart,JavaScript,C#,crosslanguage,C++,Perl,PHP,Go,Haxe,Haskell,Racket".split(","):
            return endCodeBlock(lang)
        elif lang in "Ada,Erlang,Bash,Lua,Ruby,Octave,MATLAB,Gambas,Visual Basic,Visual Basic .NET,Fortran,OCaml".split(","):
            return ""
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def ifStatement(lang, condition, body):
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startIf(lang=lang, condition=condition)] +body+ [endIf(lang)]
    return body

def getFileExtension():
        if lang in "Lua".split(","):
            return "lua"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "vb"
        elif lang in "crosslanguage".split(","):
            return "txt"
        elif lang in "bc".split(","):
            return "bc"
        elif lang in "OCaml".split(","):
            return "ml"
        elif lang in "Vala".split(","):
            return "vala"
        elif lang in "AWK".split(","):
            return "AWK"
        elif lang in "R,REBOL".split(","):
            return "r"
        elif lang in "Erlang".split(","):
            return "erl"
        elif lang in "Fortran".split(","):
            return "for"
        elif lang in "Tcl".split(","):
            return "tcl"
        elif lang in "Racket".split(","):
            return "rkt"
        elif lang in "MATLAB,Octave".split(","):
            return "m"
        elif lang in "Ada".split(","):
            return "ads"
        elif lang in "Bash".split(","):
            return "sh"
        elif lang in "Haskell".split(","):
            return "hs"
        elif lang in "C++".split(","):
            return "cpp"
        elif lang in "Python".split(","):
            return "py"
        elif lang in "Perl".split(","):
            return "pl"
        elif lang in "Java".split(","):
            return "java"
        elif lang in "JavaScript".split(","):
            return "js"
        elif lang in "Haxe".split(","):
            return "hx"
        elif lang in "Ruby".split(","):
            return "rb"
        elif lang in "C#".split(","):
            return "cs"
        elif lang in "Go".split(","):
            return "go"
        elif lang in "PHP".split(","):
            return "php"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def elseStatement(lang, body):
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startElse(lang)] +body+ [endElse(lang)]
    return body

def getRegexMatches(string, regex):
    '''Return a string array of each regex match in the array.'''

def regexMatchesString(aString, regex):
        if lang in "Python".split(","):
            return "re.compile(" + regex + ").match(" + aString + ")"
        if lang in "Java,Scala".split(","):
            return aString + ".matches(" + regex + ")"
        if lang in "C#".split(","):
            return regex + ".isMatch(" + aString + ")"
        if lang in "JavaScript".split(","):
            return "regex.test(" + aString + ")"
        notYetDefinedError(functionName = inspect.stack()[0][3]);


def puts(toPrint):
        toPrint = getVariableName(toPrint)
        if lang in "Python,Perl,PHP,AWK".split(","):
            return "print(" + toPrint + ");"
        elif lang in "bc".split(","):
            return "print " + toPrint
        elif(lang in ["OCaml"]):
            return getFunctionCall(function="print_string", parameters=["toPrint"], fromClass=None)
        
        elif lang in "Erlang".split(","):
            return "io:fwrite(" + toPrint + ")"
            
        elif lang in "Octave".split(","):
            return "printf(" + toPrint + ");"
        elif lang in "MATLAB".split(","):
            return "disp(" + toPrint + ")"
        elif lang in "Gambas".split(","):
            return "PRINT " + toPrint
        elif lang in "Racket".split(","):
            return "(display " + toPrint + ")"
        elif lang in "Common Lisp".split(","):
            return "(print " + toPrint + ")"
        elif lang in "Haskell".split(","):
            return "putStr(" + toPrint + ")"
        elif lang in "Bash".split(","):
            return "(echo " + toPrint + ");"
        elif lang in "REBOL".split(","):
            return "(print " + toPrint + ")"
        elif lang in "C++".split(","):
            return "cout << " + toPrint
        elif lang in "JavaScript".split(","):
            return "console.log(" + toPrint + ")"
        elif lang in "Java,Groovy".split(","):
            return "System.out.println(" + toPrint + ");"
        elif lang in "C#".split(","):
            return "Console.WriteLine(" + toPrint + ");"
        elif lang in "Visual Basic".split(","):
            return "Console.WriteLine(" + toPrint + ")"
        elif lang in "Visual Basic .NET".split(","):
            return "System.Console.WriteLine(" + toPrint + ")"
        elif lang in "Ruby".split(","):
            return "puts(" + toPrint + ")"
        elif lang in "crosslanguage".split(","):
            return "(puts " + toPrint + ")"
        elif lang in "Tcl".split(","):
            return "puts " + toPrint
        elif lang in "Haxe".split(","):
            return "trace(" + toPrint + ");"
        elif lang in "Go".split(","):
            return "fmt.Println(" + toPrint + ");"
        elif lang in "Scala,Vala".split(","):
            return "println(" + toPrint + ");"
        elif lang in "Lua".split(","):
            return "io.write(" + toPrint + ")"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def split(string, separator):
        string = getVariableName(string)
        separator = getVariableName(separator)
        if lang in "JavaScript,Java,Python,Haxe".split(","):
            return string + ".split(" + separator + ")"
        elif lang in "Go".split(","):
            return "strings.Split(" + string + ", " + separator + ")"
        elif lang in "PHP".split(","):
            return "explode(" + separator + ", " + string + ")"
        elif lang in "C#".split(","):
            return string + ".Split(new string[] {" + separator + "}, StringSplitOptions.None)"
        elif lang in "Tcl".split(","):
            return "[split " + string + " " + separator + "]"
        elif lang in "crosslanguage".split(","):
            return "(split " + string + " " + separator + ")"
        notYetDefinedError(functionName = inspect.stack()[0][3]);


'''
def split(string, separator):
    if(lang in ["crosslanguage"]):
        return crossLanguageStatement("split", [string, separator])
    return notYetDefinedError(functionName = inspect.stack()[0][3])
'''

'''
def setVar(valueToGet, valueToChange):
    return Compiler.setVar(lang, valueToGet, valueToChange)
'''

def setVar(lang, valueToGet, valueToChange):
    valueToGet = getVariableName(lang, valueToGet)
    valueToChange = getVariableName(lang, valueToChange)
    if(type(valueToGet) is list):
        valueToGet = getArrayInitializer(valueToGet)
    
    if(lang in "JavaScript,Dart,Java,OCaml,Haxe,C#,MATLAB,C++,PHP,Perl,Python,Lua,Ruby,Gambas,Octave,Visual Basic,Visual Basic .NET,bc".split(",")):
        return valueToChange + " = " + valueToGet
    elif(lang in ["REBOL"]):
        return valueToChange + ": " + valueToGet
    elif(lang in ["Tcl"]):
        return "set " + valueToChange + " " + valueToGet
    elif(lang in ["R"]):
        return valueToChange + " <- " + valueToGet    
    elif(lang in ["Haskell", "Bash"]):
        return "let " + valueToChange + " = " + valueToGet
    elif(lang in ["Go"]):
        return valueToChange + " = " + valueToGet
    elif(lang in ["crosslanguage"]):
        return "(set " + valueToChange + " " + valueToGet + ")"
    return notYetDefinedError(lang = lang, functionName = inspect.stack()[0][3])


def arrayContains(lang, valueToCheck, array):
        valueToCheck = getVariableName(valueToCheck)
        array = getVariableName(array)
        if lang in "Python".split(","):
            return valueToCheck + " in " + array
        elif lang in "crosslanguage".split(","):
            return "(arrayContains " + array + " " + valueToCheck
        elif lang in "JavaScript".split(","):
            return array + ".indexOf(" + valueToCheck + ") !== -1"
        elif lang in "Ruby".split(","):
            return array + ".include?(" + valueToCheck + ")"
        elif lang in "Haxe".split(","):
            return "Lambda.has(" + array + ", " + valueToCheck + ")"
        elif lang in "PHP".split(","):
            return "in_array(" + valueToCheck + ", " + array + ")"
        elif lang in "C#".split(","):
            return array + ".Contains(" + valueToCheck + ")"
        elif lang in "Java".split(","):
            return "Arrays.asList(" + array + ").contains(" + valueToCheck + ")"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

'''
def arrayContains(valueToCheck, array):
    if(type(array) is list):
        array = initializerList(array)
    if(lang in ["Python"]):
        return valueToCheck + " in " + array
    if(lang in ["JavaScript"]):
        return array +".indexOf("+valueToCheck+") !== -1"
    if(lang in ["C#"]):
        return array +".Contains("+valueToCheck+")"
    if(lang == "Java"):
        return "Arrays.asList("+array+").contains("+valueToCheck+")"
    return notYetDefinedError(functionName = inspect.stack()[0][3])
'''

def arrayLength(lang, array):
    array = getVariableName(array)
    if lang in "Python,Go".split(","):
        return "len(" + array + ")"
    elif lang in "Java,JavaScript,Ruby,Haxe".split(","):
        return array + ".length"
    elif lang in "C#".split(","):
        return array + ".Length"
    elif lang in "Emacs Lisp,Scheme,Racket,Haskell".split(","):
        return "(length " + array + ")"
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def stringLength(lang, aString):
        aString = getVariableName(aString)
        if lang in "C#,JavaScript,Python,Go,Ruby,Haxe,Haskell".split(","):
            # Do this when the string length function is the same as the array length function.
            return arrayLength(aString)
        elif lang in "Tcl".split(","):
            return "[string length " + aString + "]"
        elif lang in "Erlang".split(","):
            return "len(" + aString + ")"
        elif lang in "crosslanguage".split(","):
            return "stringLength(" + aString + ")"
        elif lang in "Lua".split(","):
            return "string.len(" + aString + ")"
        elif lang in "AWK".split(","):
            return "length(" + aString + ")"
        elif lang in "R".split(","):
            return "nchar(" + aString + ")"
        elif lang in "Racket".split(","):
            return "(" + aString-length  + aString + ")"
        elif lang in "PHP".split(","):
            return "strlen(" + aString + ")"
        elif lang in "Java".split(","):
            return aString + ".length()"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "Len(" + "theString" + ")"
        elif lang in "Perl".split(","):
            return "length( " + aString + ")"
        elif lang in "OCaml".split(","):
            return getFunctionCall(function="length", parameters=[aString], fromClass=None)
        notYetDefinedError(functionName = inspect.stack()[0][3]);
    
def length(lang, variable, theType):
    variable = getVariableName(variable)
    '''
    Type is either string or array.
    '''
    if(getCorrespondingType(theType) == getCorrespondingType("string")):
        return stringLength(variable)
    else:
        return arrayLength(variable)

def join(lang, array, separator):
    '''join a string array using a separator.'''

def args(lang):
        if lang in "Python".split(","):
            return "sys.argv"
        elif lang in "Java,crosslanguage".split(","):
            return "args"
        elif lang in "C#".split(","):
            return "Environment.GetCommandLineArgs()"
        elif lang in "JavaScript".split(","):
            return "process.argv"
        elif lang in "Ruby".split(","):
            return "ARGV"
        elif lang in "Go".split(","):
            return "os.Args"
        elif lang in "PHP".split(","):
            return "$argv"
        notYetDefinedError(functionName = inspect.stack()[0][3]);

def startForEach(lang, array, variableName, typeInArray):
        array = getVariableName(lang, array)
        variableName = getVariableName(lang, variableName)
        if lang in "Python".split(","):
            return "for " + variableName + " in " + array + ":"
        if lang in "AWK".split(","):
            return "for(" + variableName + " in " + array + "){"
        if lang in "crosslanguage".split(","):
            return "foreach(" + typeInArray + " " + variableName + " in " + array + ")"
        elif lang in "F#".split(","):
            return "for " + variableName + " in " + array + " do"
        elif lang in "Tcl".split(","):
            return "foreach " + variableName + " " + array + " {"
        elif lang in "Bash".split(","):
            return "for i in ${" + variableName + "[@]}; do"
        elif lang in "Lua".split(","):
            return "for _," + variableName + " in " + array + " do"
        elif lang in "C++".split(","):
            return "for(" + typeInArray + " & " + variableName + " : " + array + "){"
        elif lang in "Ruby".split(","):
            return array + ".each do |" + variableName + "|"
        elif lang in "Go".split(","):
            return "for " + variableName + " := range " + array + "{"
        elif lang in "Haxe".split(","):
            return "for(" + variableName + " in " + array + "){"
        elif lang in "PHP".split(","):
            return "foreach (" + array + " as " + variableName + "){"
        elif lang in "JavaScript".split(","):
            return array + ".forEach(function(" + variableName + "){"
        elif lang in "C#,Vala".split(","):
            return "foreach (" + typeInArray + " " + variableName + " in " + array + "){"
        elif lang in "Java".split(","):
            return "for(" + typeInArray + " " + variableName + " : " + array + "){"
        elif lang in "Scala".split(","):
            return "for(" + variableName +  " -> " + array + "){"
        elif lang in "Groovy".split(","):
            return "for(" + variableName +  " in " + array + "){"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "For Each " + variableName + " As " + typeInArray  + " In " + array
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);


def endForEach(lang):
    if lang in "Tcl,Scala,F#,C++,AWK,REBOL,Groovy,Python,Java,C#,Haxe,Go,PHP,Ruby,Lua,Go,Vala,crosslanguage".split(","):
        return endCodeBlock(lang)
    elif lang in "JavaScript".split(","):
        return "});"
    elif lang in "Ada".split(","):
        return "});"
    elif lang in "Visual Basic,Visual Basic .NET".split(","):
        return "Next"
    elif lang in "Gambas".split(","):
        return "NEXT"
    elif lang in "Bash".split(","):
        return "done"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def forEach(lang, array, variableName, typeInArray, body):
    typeInArray = getCorrespondingType(lang, typeInArray)
    i = 0
    body = concatenateAllElements(body)
    while(i < len(body)):
        body[i] = "    " + body[i]
        i = i + 1
    body = [startForEach(lang=lang, array=array, variableName=variableName, typeInArray=typeInArray)] +body+ [endForEach(lang)]
    return body
    return notYetDefinedError(functionName = inspect.stack()[0][3])

def typeOf(lang, theObject):
    if lang in "Python".split(","):
        return "type(" + theObject + ")"
    elif lang in "JavaScript".split(","):
        return "typeof(" + theObject + ")"
    elif lang in "crosslanguage".split(","):
        return "(typeof " + theObject + ")"
    elif lang in "Go".split(","):
        return "reflect.TypeOf(" + theObject + ").Name()"
    elif lang in "Java".split(","):
        return theObject + ".getClass().getName()"
    elif lang in "Haxe".split(","):
        return "Type.typeof(" + theObject + ")"
    elif lang in "Ruby".split(","):
        return "class(" + theObject + ")"
    elif lang in "C#".split(","):
        return theObject + ".getType()"
    elif lang in "Perl".split(","):
        return "ref(" + theObject + ")"
    elif lang in "PHP".split(","):
        return "getType(" + theObject + ")"
    return notYetDefinedError(functionName = inspect.stack()[0][3])

'''
def typeof(theObject):
    '/''must return a string in each language.''/'
    if(lang in ["Python"]):
        return "type(" + theObject + ")"
    if(lang in ["JavaScript"]):
        return "typeof " + theObject
    if(lang in ["C#"]):
        return theObject+".GetType()"
    if(lang in ["Ruby"]):
        return theObject+".class.name"
    if(lang in ["Go"]):
        return "reflect.TypeOf("+theObject+").Name()"
    if(lang in ["Java"]):
        return theObject+".getClass().getName()"
    if(lang in ["crosslanguage"]):
        return crossLanguageStatement(functionName = "typeof", params=[theObject])
    return notYetDefinedError(functionName = inspect.stack()[0][3])
'''

def instanceOf(lang, theValue, theType):
    theValue = getVariableName(theValue)
    if(lang in ["Java", "JavaScript"]):
        return theValue + " instanceof " + theType
    if(lang in ["Python"]):
        return "isinstance("+theValue+", "+theType+")"
    if(lang in ["C#"]):    
        return theValue+".GetType() == typeof("+theType+")"
    if(lang in ["crosslanguage"]):
        return crossLanguageStatement("instanceOf", [theValue, theType])
    return notYetDefinedError(functionName = inspect.stack()[0][3])
    
def getReturnStatement(lang, toReturn):
    toReturn = getVariableName(lang, toReturn)
    if(lang in "Java,Groovy,Scala,CoffeeScript,Dart,C#,JavaScript,Go,Haxe,PHP,C++,Perl,Vala,Lua,Python,REBOL,Ruby,Tcl,AWK,bc".split(",")):
        return "return " + toReturn
    elif(lang in ["R"]):
        return "return(" + toReturn + ")"
    elif(lang in ["crosslanguage"]):
        return "(return " + toReturn + ")"
    elif(lang in ["Racket"]):
        return toReturn
    elif(lang in ["Haskell"]):
        return toReturn
    elif(lang in ["Erlang", "OCaml"]):
        return toReturn
    elif(lang in ["Bash"]):
        return ["(echo " + toReturn+")"] + ["return 0;"]
    elif(lang in ["Gambas"]):
        return "RETURN " + toReturn
    elif(lang in ["Visual Basic", "Visual Basic .NET"]):
        return "Return " + toReturn
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def Int(lang, objectToConvert, convertFrom):
    objectToConvert = getVariableName(objectToConvert)
    return convert(objectToConvert=objectToConvert, convertTo="int", convertFrom=convertFrom)
    
def String(lang, objectToConvert, convertFrom):
    objectToConvert = getVariableName(objectToConvert)
    return convert(objectToConvert=objectToConvert, convertTo="String", convertFrom=convertFrom)

def stringContains(lang, inString, checkFor):
    inString = getVariableName(inString)
    checkFor = getVariableName(checkFor)
    if lang == "JavaScript":
        return "("+indexOf(string=inString, substring=checkFor)+"!= -1)"
    return notYetDefinedError(functionName = inspect.stack()[0][3])

def contains(lang, inObject, checkFor, containerType):
    if(getCorrespondingType(containerType) == getCorrespondingType("string")):
        return stringContains(checkFor=checkFor, inString=inObject)
    else:
        return arrayContains(valueToCheck=checkFor, array = inObject)
    raise Exception("contains is not yet defined for the type " + str(type(inObject)))

def Or(lang, listOfThings):
    '''
    Both of these things are boolean.
    '''
    if(lang in ["JavaScript", "Java", "Haskell", "Haxe"]):
        return "(" + " || ".join(listOfThings) + ")"
    if(lang in ["Python", "Lua", "PHP", "crosslanguage"]):
        return "(" + " or ".join(listOfThings) + ")"
    elif(lang in ["Common Lisp", "Racket"]):
        return "(and " + " ".join(listOfThings) + ")"
    return notYetDefinedError(functionName = inspect.stack()[0][3])
        
def And(lang, listOfThings):
    '''
    Both of these things are boolean.
    '''
    if(lang in "JavaScript,OCaml,AWK,Java,Haskell,Haxe,Bash,Haxe,Go,Perl,Ruby".split(",")):
        return "(" + " && ".join(listOfThings) + ")"
    elif(lang in ["Python", "Lua", "PHP", "Erlang", "crosslanguage", "REBOL"]):
        return "(" + " and ".join(listOfThings) + ")"
    elif(lang in ["Visual Basic", "Visual Basic .NET"]):
        return "(" + " And ".join(listOfThings) + ")"
    elif(lang in ["Common Lisp", "Racket"]):
        return "(and " + " ".join(listOfThings) + ")"
    return notYetDefinedError(lang, inspect.stack()[0][3])

def Not(lang, theVar):
    theVar = getVariableName(lang, theVar)
    if(lang in "Python,Lua,Racket,Common Lisp,crosslanguage,REBOL,Haskell".split(",")):
        return "(not "+theVar + ")"
    elif(lang in ["Visual Basic", "Visual Basic .NET"]):
        return "(Not "+theVar + ")"
    elif(lang in "Perl,JavaScript,Dart,Java,Go,Ruby,PHP,Haxe,C#".split(",")):
        return "(!"+theVar + ")"
    return notYetDefinedError(lang, inspect.stack()[0][3])

def seriesOfAnds(lang, theThings, theFunction):
    toReturn = []
    for i in range(0, len(theThings)-1):
        toReturn += [theFunction(lang, [theThings[i], theThings[i+1]])]
    return And(lang, toReturn)

def greaterThan(lang, theThings):
    if len(theThings) != 2:
        #raise Exception("greaterThan is not defined when (len(theTheThings) == "+str(len(theThings))+")")
        return seriesOfAnds(lang, theThings, greaterThan)
    elif len(theThings) == 2:
        thing1 = getVariableName(lang,theThings[0])
        thing2 = getVariableName(lang,theThings[1])
        if(lang in ["JavaScript", "REBOL", "Erlang", "OCaml", "crosslanguage", "C#", "Nemerle", "AWK", "Java", "Lua", "Perl", "Haxe", "Python", "PHP", "Haskell", "Go", "Ruby", "R", "bc", "Visual Basic", "Visual Basic .NET"]):
            return "("+thing1 + " > " + thing2+")"
        if(lang in ["Racket", "Common Lisp", "Emacs Lisp"]):
            return "(> "+thing1 + " " + thing2+")"
    #print theThings
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def greaterThanOrEqual(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang, theThings[i])
    if len(theThings) == 2:
        if(lang in "Python,Java,OCaml,REBOL,Erlang,C#,Nemerle,Ruby,PHP,Lua,Visual Basic .NET,Haskell,Haxe,Perl,JavaScript,R,AWK,crosslanguage,Go"):
            #raise Exception("(" + theThings[0] + " >= " + theThings[1]+")")
            return "(" + theThings[0] + " >= " + theThings[1]+")"
    else:
        raise Exception("greaterThanOrEqual is not defined when len(theThings) != 2")
        return seriesOfAnds(lang, theThings, greaterThanOrEqual)
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def lessThan(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang,theThings[i])
    if len(theThings) == 2:
        thing1 = theThings[0]
        thing2 = theThings[1]
        if(lang in ["JavaScript", "OCaml", "Nemerle", "C#", "Erlang", "Perl", "AWK", "Lua", "Java", "Haxe", "Python", "PHP", "Go", "Ruby", "Vala", "R", "bc", "Visual Basic", "Visual Basic .NET", "Haskell", "crosslanguage", "REBOL"]):
            return "("+thing1 + " < " + thing2+")"
        elif(lang in ["Racket", "Common Lisp", "Emacs Lisp"]):
            return "(< "+thing1 + " " + thing2+")"
    else:
        return seriesOfAnds(lang, theThings, lessThan)
    
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def lessThanOrEqual(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang, theThings[i])
    if(lang in "Python,REBOL,OCaml,Go,Java,Ruby,C#,Nemerle,PHP,Erlang,Lua,Visual Basic .NET,Haskell,Haxe,Perl,JavaScript,R,crosslanguage".split(",")):
        return "("+theThings[0] + " <= " + theThings[1] +")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def compare(lang, theThings, theType):
    #raise Exception(theThings)
    #print theThings
    if(type(theThings) != list):
        raise Exception("The type of theThings must be a list!")
    if len(theThings) == 1:
        if type(theThings[0] == list):
            theThings = theThings[0]
        else:
            raise Exception("The length of theThings is " + str(theThings) + ". The length of theThings must be greater than 1.")
    for i in range(0, len(theThings)):
        #print(theThings)
        theThings[i] = getVariableName(lang, theThings[i])
    thing1 = theThings[0]
    thing2 = theThings[1]
    if len(theThings) == 2:
        theType=getCorrespondingType(lang,theType)
        if(lang in ["crosslanguage"]):
            return crossLanguageStatement("compare", [thing1, thing2, theType])
        if(lang == "Dart"):
            if(theType == "int"):
                return "("+thing1 + " == " + thing2+")"
        if(lang == "Scala"):
            if(theType == "int"):
                return "("+thing1 + " == " + thing2+")"
        if(lang == "JavaScript"):
            if(theType == "string"):
                return "("+thing1 + " === " + thing2+")"
            if((theType == getCorrespondingType(lang, "string")) or (theType == getCorrespondingType(lang, "int"))):
                return "("+thing1 + " === " + thing2+")"
        if(lang == "Python"):
            if(theType == "str" or theType == "int"):
                return "("+thing1 + " == " + thing2+")"
        if(lang == "Java"):
            #print("Wooow!")
            if(theType == "String"):
                return thing1 + ".equals(" + thing2 + ")"
            elif(theType == "int"):
                return "(" + thing1 + " == " + thing2 + ")"    
        if(lang == "C#"):
            if(theType == "string"):
                return thing1+".Equals("+thing2+", StringComparison.Ordinal)"
            elif(theType == "int"):
                return "(" + thing1 + " == " + thing2 + ")"    
        if(lang == "Ruby"):
            if(theType in ["fixnum", "String"]):
                return "(" + thing1 + " == " + thing2 + ")"    
        if(lang == "PHP"):
            if(theType == getCorrespondingType("string")):
                return thing1 + " === " + thing2
            if(theType == getCorrespondingType("int")):
                return thing1 + " === " + thing2
        if(lang == "Haxe"):
            if(theType == getCorrespondingType(lang, "string") or theType == getCorrespondingType(lang, "Int")):
                return thing1 + " == " + thing2
        if(lang == "Haskell"):
            if(theType == getCorrespondingType(lang, "string") or theType == getCorrespondingType(lang, "int")):
                return "(" + thing1 + " == " + thing2 + ")"
        if(lang == "CoffeeScript"):
            if theType == "number":
                return "(" + thing1 + " == " + thing2+")"
        if(lang == "Groovy"):
            if theType == "int":
                return "(" + thing1 + " == " + thing2+")"
        if lang == "Lua":
            if theType in ["number", "string"]:
                return "(" + thing1 + " == " + thing2+")"
        if lang == "Perl":
            if theType == "number":
                return "(" + thing1 + " == " + thing2+")"
            if theType == "string":
                return "(" + thing1 + " eq " + thing2+")"
    else:
        toReturn = []
        for i in range(0, len(theThings)-1):
            toReturn += [compare(lang, [theThings[i], theThings[i+1]], theType)]
        return And(lang, toReturn)

    raise Exception("compare is not yet defined for the type " + theType + " and the language " + lang + " and the list " + str(theThings))
    
'''Some function aliases'''
array=initializerList
instanceof = instanceOf
comment = getComment
function = getFunction
method = function
If = ifStatement
While = whileLoop
For = forLoop
Else = elseStatement
procedure = function
languageSpecific = includeForLang
println = puts
System_out_println = puts
document_write = puts
trace = puts
string_split = split
printf = puts
initializeArray=array
arr=array
getArray=accessArray
getVar=setVar
const = declareConstant
constant = const
static=const
proc=procedure
func=function
enhancedForLoop=forEach
getArrayAccessor=accessArray
arrayIndex=accessArray
getArrayIndex=accessArray
getFunctionCall=callFunction
Class = getClass
convert = typeConversion
Return = getReturnStatement
Str= String
typeof = typeOf
makeVariable = initializeVar
createVariable = makeVariable
declareVariable = makeVariable
invokeFunction = getFunctionCall
equals=compare
call=callFunction
invoke=invokeFunction
getVariableDeclaration = makeVariable
defineVariable=getVariableDeclaration
array=initializerList
arr=array
foreach = forEach
commandLineArguments = args
arguments = args
size=length
Type = typeof
Set = setVar
matchesString = regexMatchesString
matchesRegex = matchesString
stringMatchesRegex = regexMatchesString
position = index
Def = func
makevar = makeVariable
Main = main
Slice = subString
substring = Slice
Import = include
includeExternalFile = include
using = include
require = using
merge = join
switch=Switch
ElseIf = elseIf
Elif = ElseIf
statement = semicolon
Mod = mod


def includeInEachFile(lang):
    #Inclue this in each file for each language.
    if(lang in ["Python"]):
        return ['''#This is a test of includeInEachFile for Python.''']
    elif(lang in ["REBOL"]):
        return [getComment("This code is written in REBOL 3.")]
    elif(lang in ["C#"]):
        return [
        '''using System;''',
        '''using System.Linq;'''
        ]
    elif(lang in ["Java"]):
        return ['''import java.util.ArrayList;''',
        '''import java.util.Arrays;'''
        ]
    elif(lang in ["Erlang"]):
        return [getComment("All variables and parameter names in Erlang must start with capital letters. Function names should be lower-case.")
        ]
    elif(lang in "crosslanguage"):
        return ["//How to parse Lisp files in Python: ",
                "// http://stackoverflow.com/questions/14058985/parsing-a-lisp-file-with-python",
                "//The compiler should automatically insert parentheses whenever indentation is made here.",
                "//If a symbol (but not an enclosed parentheses) directly precedes an opening parentheses, then it should be automatically moved inside those parentheses."
                "//After these changes are made, it can be parsed like normal Lisp code."
            ]
    else:
        return [""];
    return notYetDefinedError(functionName = inspect.stack()[0][3])

def module(lang, body):
    if(type(body) == str):
        body = [body]
    body = concatenateAllElements(includeInEachFile(lang) + body)
    toReturn = ""
    i = 0
    while(i < len(body)):
        toReturn += body[i]+"\n";
        i = i + 1
    return toReturn


def removeWhitespace(theFile):
    ''''''
    theFile = theFile.split("\n")
    i = 0
    while(i < len(theFile)):
        if(theFile[i].strip() == ""):
            theFile.pop(i)
        else:
            i += 1
    return "\n".join(theFile)

def getMacroOutput(data):
    '''Example input:
    (module foo
        bar
    )
    
    Example output:
    module(foo,
    [bar]
    )
    '''
    #data is a string
    print(data)
    #parseArray = polishNotation2.stringToSyntaxTree(data)
    
    raise Exception('getMacroOutput has not yet been implemented')

def getFileIgnoringExceptions(theLangs, fileNames=None):
    global lang
    if(type(theLangs) == str):
        theLangs = [theLangs]
    if(fileNames == None):
        fileNames = glob.glob("*.dat")
        for n,i in enumerate(fileNames):
            fileNames[n] = fileNames[n][:-3]    
    for fileName in fileNames:
        with open (fileName + "dat", "r") as myfile:
            data=myfile.read()
        print("Evaluating " + fileName + "dat")
        print("Text to translate:\n" + data)
        #print("With added parentheses:\n" + addParentheses(data))
        toEvaluate = getMacroOutput(data)

        
        
        print("Generated text to be evaluated:" + toEvaluate);        
        text_file = open("generatedCrossLanguageCode/" + fileName + "txt", "w")
        text_file.write(toEvaluate)
        text_file.close()
        for current in theLangs:
            try:                
                lang = current;
                theFile = eval(toEvaluate);
                theFile = removeWhitespace(theFile);
                theDir = "generatedFunctions/"+lang+"Functions/"
                if not os.path.exists(theDir):
                    os.makedirs(theDir)
                text_file = open(theDir + fileName + "."+getFileExtension(), "w")
                text_file.write(theFile)
                text_file.close()
            except Exception as e:
                thingToAdd = traceback.format_exc()
                print(thingToAdd)
        

#os.chdir("polyglotFunctions")


'''

getFileIgnoringExceptions(["Gambas", "MATLAB", "Octave", "Visual Basic", "Racket", "C#", "JavaScript", "Java", "Python", "C++", "Perl", "Bash", "Lua","Ruby", "Bash", "PHP","Go","Haxe","Haskell"], ["HelloWorld", "TypeofExample", "HaskellExample"])
'''

'''
getFileIgnoringExceptions(["Lua", "JavaScript", "Python", "Java", "Ruby", "C#", "Go", "Haxe", "VBScript", "Scala"])
'''

def testEverything():
    global lang;    
    
    #langArr = ["Python", "JavaScript", "Java", "PHP"]
    
    
    #langArr = ["Python", "Common Lisp", "Visual Basic .NET", "REBOL"]
    
    langArr = ["JavaScript"]
    
    entireLangArr = ["Python", "Falcon", "Clojure", "Nemerle", "Vala", "AWK", "REBOL", "OCaml", "Gambas", "MATLAB", "Octave", "Visual Basic", "Visual Basic .NET", "Racket", "Common Lisp", "Emacs Lisp", "C#", "JavaScript", "Java", "C++", "Perl", "Lua","Ruby", "Bash", "PHP","Go","Haxe","Haskell","F#","Erlang","Ada","bc","crosslanguage"]
    
    getFileIgnoringExceptions(entireLangArr)

    print("\n\n\n\nChecking the list of statements in each language: ")
    
    listOfErrors = "";
    for current in entireLangArr:
        lang = current
        for statement in statementArr:
            try:
                eval(statement)
            except Exception as e:
                listOfErrors += str(e)+"\n"
    with open("List of errors.txt", "w") as text_file:
        text_file.write(listOfErrors)
    
    print("\n\n\n\nNumber of defined functions in each language: ")
    
    langArr = entireLangArr
    for current in langArr:
        currentNumDefined = 0
        lang = current
        for statement in statementArr:
            try:
                eval(statement)
                currentNumDefined += 1
            except Exception as e:
                ''
        print("    " + current + ": " + str(currentNumDefined))
    print("Check list of errors.txt for a list of all errors that need to be fixed.")
    print("Check generatedCrossLanguageCode to fix errors in the generated crosslanguage code.")
    print("Check generatedFunctions for the generated output in each language.")

testEverything()