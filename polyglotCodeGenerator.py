#import examples.EngScript_examples.Python.engScriptFunctions #This contains some generated functions in Python
import numpy
import re
#import getFileIgnoringExceptions

class EngScriptException(Exception):
    pass

def arrayContainsSplit(lang, theStrings):
    '''Both parameters are strings. The matching is not case-sensitive.'''
    return (lang.lower() in theStrings.lower().split(","))


acs = arrayContainsSplit #shorthand

def stringInterpolation(theString, varNames, theVars):
        varNames = varNames.split(",")
        theRegex = "("+"|".join(varNames)+")"
        theArr = re.split(theRegex, theString)
        for i in range(0, len(varNames)):
            for j in range(0, len(theArr)):
                if theArr[j] == varNames[i]:
                    theArr[j] = theVars[i]
        theString = "".join(theArr)
        return theString

"""
testMacro is the only method from this file you should ever use from other files.
Test files in EngScript.py instead of testing them here.

This is a comment.
"""

#from statementArr import statementArr
#from crossLanguageParser import evaluateMacro
#from crossLanguageParser import addParentheses
'''sys.path.append("/polyglotFunctions/generatedFunctions/Python/")'''

#from polyglotFunctions.generatedFunctions.PythonFunctions.Compiler import *

def returnIfContaining(theLang, theList):
    i = 0
    while i < len(theList):
        if theLang in theList[i].split(","):
            return theList[i+1]
        i = i + 2
    #raise Exception(theLang + " not in the list")

#print returnIfContaining("Perlga", ["Python,Java", "*", "Lua,Perl", "aa"])

def indent(theString):
    theStrings = theString.split("\n")
    theStrings = ["    " + x for x in theStrings]
    return "\n".join(theStrings)
            
#printTrueStatements(["1 == 2", "2 + 2 == 5", "9*9 == 81", "(4/2) == 2"])


#!/usr/bin/python3.3


'''print(sys.version);'''
import inspect

def getResultForLanguages(lang, langsAndResults):
    for idx, val in enumerate(langsAndResults):
        if(idx == 0) or (idx + 1) % 2 == 0:
            if lang in val:
                return langsAndResults[idx + 1]

def splitContains(lang, theString):
    return (lang in theString.split(","))

def semicolon(lang, theStatement): #also known as statement
    if theStatement == "":
        return ""
    if type(theStatement) == list:
        return seriesOfStatements(lang=lang,body=theStatement)
    if acs(lang, "C,OpenOffice Basic,ALGOL 68,D,Ceylon,Rust,TypeScript,Octave,AutoHotKey,Pascal,Delphi,JavaScript,Pike,Objective-C,OCaml,Java,Scala,Dart,PHP,C#,C++,Haxe,AWK,bc,Haskell,Perl,Go,Nemerle,Vala"):
        if theStatement[-1:] != ";":
            #print(theStatement)
            return theStatement + ";"
        else:
            return theStatement
    elif acs(lang, "Python,PowerShell,Hy,Puppet,Fortran,LispyScript,Sibilant,Nimrod,Oz,Gambas,Cython,CoffeeScript,Swift,Clojure,Prolog,Gosu,Groovy,Polish notation,Reverse Polish notation,Ruby,ML,AutoIt,Tcl,F#,REBOL,Red,R,Python,Cobra,Bash,Visual Basic,Visual Basic .NET,Hack,Lua,Racket,Common Lisp,Julia"):
        return theStatement
    elif acs(lang, "crosslanguage"):
        return "("+theStatement+" ;)"
    elif acs(lang, "Erlang"):
        if(theStatement[-1:] != ","):
            return theStatement + ","
        else:
            return theStatement
    notYetDefinedError(lang, inspect.stack()[0][3])

def listComprehension2(lang, result, variable, array, condition):
    #y is the condition
    #z is the array
    result = getVariableName(lang, result)
    variable = getVariableName(lang, variable)
    array = getVariableName(lang, array)
    condition = getVariableName(lang, condition)
    toReturn=""
    #raise Exception(x + "," + y +","+ z)
    
    if lang == "Python":
        #x for y in z
        toReturn = "[@result for @variable in @array if @condition]"
    elif lang == "JavaScript":
        toReturn = "[@result for (@variable of @array) if @condition]"
    elif lang == "CoffeeScript":
        toReturn = "(@result for @variable in @array when @condition)"
    elif lang == "Haxe":
        toReturn = "[for(@variable in @array) if(@condition) @result]"
    elif lang == "C#":
        toReturn = "(from @variable in @array where @condition select @result)"
    elif lang == "Haskell":
        toReturn= "[ @result | @variable <- @array, @condition ]"
    elif lang == "Erlang":
        toReturn= "[ @result || @variable <- @array, @condition ]"
    elif lang == "Ruby":
        toReturn= "@array.select{|@variable| @condition }.collect{|@variable| @result}"
    elif lang == "Scala":
        toReturn= "(for (@variable <- @array if @condition) yield @result)"
    elif lang in ["Groovy"]:
        toReturn= "@array.grep { @variable -> @condition }.collect { @variable -> @result }"
    elif lang in ["Dart"]:
        toReturn = '@array.where((@variable) => @condition).map((@variable) => @result)'
    #use stringInterpolation here
    if toReturn == "":
        notYetDefinedError(lang, inspect.stack()[0][3])
    else:
        return stringInterpolation(toReturn, "@variable,@condition,@array,@result", [variable,condition,array,result])

def listComprehension(lang, x, y, z):
    if lang == "Python":
        #x for y in z
        return listComprehension2(lang,y,y,z,x)
    if lang == "JavaScript":
        return listComprehension2(lang,y,y,z,x)
    else:
        return listComprehension2(lang,y,y,z,x)
    notYetDefinedError(lang, inspect.stack()[0][3])

def seriesOfStatements(lang, body):
    for idx, val in enumerate(body):
        body[idx] = semicolon(lang, val);
        if lang == "Erlang" and idx == len(body) - 1:
            body[idx] = body[idx][0:(len(body[idx])-1)]
    return concatenateAllElements(body)

def Eval(lang, toEval):
    if lang in ["Python", "JavaScript"]:
        return "eval(" + toEval + ")"
    notYetDefinedError(functionName = inspect.stack()[0][3])

def this(lang, variableName):
    if lang == "Python":
        return "self."+variableName
    if lang in ["Java", "C#"]:
        return "this."+variableName
    if lang in ["crosslanguage"]:
        return "this."+variableName
    notYetDefinedError(functionName = inspect.stack()[0][3])

def googleSearchTerm(functionName):
    if functionName == "concatenateStrings":
        return "concatenate+strings"
    elif functionName == "semicolon":
        return "semicolon"
    elif functionName == "raiseToExponent":
        return "exponent"
    elif functionName == "getComment":
        return "comment"
    elif functionName == "puts":
        return "print+statement"
    elif functionName == "charAt":
        return "string+index"
    elif functionName in ["startWhile", "endWhile"]:
        return "while+loop"
    elif functionName in ["startForLoop", "startForInRange", "endForLoop", "endFor", "startFor", "endForInRange"]:
        return "for+loop"
    elif functionName == "args":
        return "command+line+arguments"
    elif functionName == "accessArray":
        return "array+index"
    elif functionName == "randomIntInRange":
        return "random+integer+in+range"
    elif functionName in ["add", "subtract", "divide", "multiply"]:
        return "arithmetic+operators"
    elif functionName in ["greaterThan", "Not", "greaterThanOrEqual", "lessThanOrEqual", "lessThan", "Or", "And"]:
        return "logical+operators"
    elif functionName in ["startCase", "endCase", "startSwitch", "endSwitch", "startDefault", "endDefault"]:
        return "switch"
    elif functionName == "getFileExtension":
        return "file+extension"
    elif functionName == "arrayLength":
        return "array+length"
    elif functionName == "stringLength":
        return "string+length"
    elif functionName == "getReturnStatement":
        return "return+statement"
    elif functionName in ["endMacroDefinition", "getMacroParameters", "startMacroDefinition"]:
        return "macro"
    elif functionName in ["methodRequiresReturnType", "methodRequiresParameterTypes", "startMethod", "endMethod"]:
        return "functions"
    elif functionName == "globalReplace":
        return "global+replace"
    elif functionName == "regexMatchesString":
        return "regex+match"
    elif functionName in ["startForEach", "endForEach"]:
        return "foreach"
    elif functionName in ["stringContains"]:
        return "string+contains"
    else:
        raise Exception("googleSearchTerm is not yet defined for " + functionName)

def googleSearchQuery(lang, functionName):
    toReturn = "https://www.google.com/?gws_rd=ssl#q="+lang+"+"+googleSearchTerm(functionName)
    from subprocess import call
    #print("Opening with googleSearchQuery")
    #call(["google-chrome", toReturn])
    return toReturn

def notYetDefinedError(lang, functionName):
    toReturn = functionName + " is not yet defined for " + str(lang)
    raise EngScriptException(toReturn)

def logger(func):
    def inner(*args, **kwargs): #1
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs) #2
    return inner

def endCodeBlock(lang):
    if acs(lang, "CoffeeScript,Cobra,Python,Haskell,F#,Cython,Nimrod"):
        return "";
    elif acs(lang, "REBOL"):
        return "]";
    elif acs(lang, "JavaScript,PowerShell,Hack,D,Ceylon,ActionScript,Rust,TypeScript,Swift,AutoHotKey,Gosu,AWK,bc,C,Nemerle,Tcl,Groovy,R,Java,Dart,Scala,Squirrel,JavaScript,C#,Haxe,Perl,PHP,Go,C++,Vala,Dylan,Pike"):
        return "}";
    elif acs(lang, "Lua,Ruby,MATLAB,Oz,Falcon,Julia"):
        return "end";
    elif acs(lang, "Clojure,Hy,Emacs Lisp,Common Lisp,Racket,Scheme,LispyScript,Sibilant"):
        return ")";
    elif acs(lang, "Delphi,Pascal"):
        return "end;"
    else:
        notYetDefinedError(lang, inspect.stack()[0][3])
    #return examples.EngScript_examples.Python.engScriptFunctions.engScript_endCodeBlock(lang)

def callFunctionWithNamedArgs(lang, functionName, argumentNames, theArgs, fromClass):
    notYetDefinedError(functionName = inspect.stack()[0][3])

def crossLanguageStatement(functionName, params):
    toReturn = "("+functionName + " "
    i=0
    while i < len(params):
        if (type(params[i]) is list or (params[i] is None)):
            params[i] = str(params[i])
        toReturn += params[i]
        if i < (len(params)-1):
            toReturn += " "
        i += 1
    return toReturn
    notYetDefinedError(inspect.stack()[0][3])

def sqrt(lang, number):
    #square root
    number = getVariableName(lang, number)
    if lang in "Python,Lua".split(","):
        return "math.sqrt(" + number + ")"
    '''
    else:
        return examples.EngScript_examples.Python.engScriptFunctions.engScript_endCodeBlock(lang)
    '''
    if lang in "Racket,Common Lisp".split(","):
        return "(sqrt " + number + ")"
    if lang in "Swift,PHP".split(","):
        return "sqrt(" + number + ")"
    if lang in "Java,JavaScript,TypeScript,CoffeeScript,Haxe".split(","):
        return "Math.sqrt(" + number + ")"
    if lang in "REBOL".split(","):
        return "square-root " + number
    if lang in "C#".split(","):
        return "Math.Sqrt(" + number + ")"
    notYetDefinedError(lang, inspect.stack()[0][3])
    
def startWhile(lang, condition):
        #return examples.EngScript_examples.Python.engScriptFunctions.engScript_startWhile(lang, condition)
        condition = getVariableName(lang, condition)
        #print("The condition is " + str(condition))
        toReturn = ""
        if lang in "Python,Cython,Nimrod".split(","):
            return "while @condition:"
        if lang in "OpenOffice Basic":
            return"Do While " + condition
        if lang in "Common Lisp":
            return "(loop while " + condition + " do"
        if lang in "CoffeeScript,Julia,Cobra,crosslanguage".split(","):
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
        elif acs(lang, "C,PowerShell,Hack,Gosu,AutoHotKey,Ceylon,D,TypeScript,ActionScript,Nemerle,Dart,Swift,Groovy,Scala,Java,JavaScript,PHP,C#,Perl,C++,Haxe,R,AWK,Vala"):
            return "while(" + condition + "){"
        elif lang in "Tcl,bc".split(","):
            return "while{" + condition + "}{"
        elif lang in "Go".split(","):
            toReturn = "for @condition {"
        elif lang in "Rust".split(","):
            toReturn =  "for @condition {"
        elif lang in "Octave".split(","):
            toReturn= "while (@condition)"
        elif lang in "Visual Basic,Visual Basic .NET,AutoIt".split(","):
            toReturn= "While @condition"
        elif lang in "Pascal,Delphi".split(","):
            toReturn= "while @condition do \nbegin"
        elif acs(lang,"Hy"):
            return "(while @condition"
        #use stringInterpolation here
        if toReturn == "":
            notYetDefinedError(lang, inspect.stack()[0][3])
        else:
            return stringInterpolation(toReturn, "@condition", [condition])

def endWhile(lang):
    #return examples.EngScript_examples.Python.engScriptFunctions.engScript_endWhile(lang)
    if acs(lang, "C,PowerShell,Nimrod,Hy,AutoHotKey,Hack,Gosu,AutoHotKey,Common Lisp,Ceylon,D,Rust,TypeScript,ActionScript,Julia,Delphi,Pascal,Nemerle,CoffeeScript,Swift,Cobra,Groovy,Scala,Dart,bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,Haxe,JavaScript,C#,Perl,crosslanguage,Ruby,C++,Lua,PHP,Go,MATLAB"):
        return endCodeBlock(lang)
    if lang in "Bash,OCaml".split(","):
        return "done"
    if lang in "Fortran".split(","):
        return "enddo"
    if lang in "Ada".split(","):
        return "end loop;"
    if lang in "Octave".split(","):
        return "endwhile"
    if lang in "Visual Basic,Visual Basic .NET".split(","):
        return "End While"
    if lang in "Gambas".split(","):
        return "WEND"
    if lang in "AutoIt".split(","):
        return "WEnd"
    if lang in "OpenOffice Basic".split(","):
        return "Loop"
    notYetDefinedError(lang, inspect.stack()[0][3])

def startFor(lang, initializer, condition, increment):
    if lang in "Java,Groovy,JavaScript,Dart,TypeScript,PHP,C#,Perl,C++,AWK".split(","):
        return "for(" + semicolon(lang, initializer) +" "+ semicolon(lang, condition) +" "+ increment + "){";
    if lang == "Tcl":
        return "for {"+initializer+"} {"+condition+"} {"+increment+"} {"
    if lang == "C":
        splitInitializer = initializer.split(" ")
        initializerType = splitInitializer[0]
        initializerName = splitInitializer[1]
        startingString = initializerType +" "+ initializerName+";\n"
        initializerWithoutType = initializer[len(splitInitializer[0])+1:len(initializer)]
        return startingString + "for(" + semicolon(lang, initializerWithoutType) +" "+ semicolon(lang, condition) +" "+ increment + "){";
    "for languages that don't have a for loop"
    if lang in "Python,REBOL,Lua,CoffeeScript,Ruby,Octave,Scala,Haxe".split(","):
        return [initializer,startWhile(lang, condition)]
    if lang in ["crosslanguage"]:
        return "(for" +" "+ initializer +" "+ condition +" "+ increment + ")"
    if lang in ["Go"]:
        return "for "+initializer+"; "+condition+"; "+increment+" {"
    notYetDefinedError(lang, inspect.stack()[0][3])



def callFunction(lang, function, fromClass, parameters):
    if fromClass != None:
        if not fromClass.startswith("EngScript_"):
            fromClass = "EngScript_"+fromClass
    
    #raise Exception(fromClass)
    
    if type(parameters) == str:
        parameters = [parameters]
    parameters = [getVariableName(lang, foo) for foo in parameters]
    if not function.startswith("engScript_"):
        function = "engScript_"+removeInitialDollarSign(function)
    newArr = [function] + parameters
    
    #raise Exception(newArr)
    
    if fromClass in ["this", "self"]:
        raise Exception("Call the function " + function + "with the parameters " + parameters + " for an instance of this class.")
    
    if lang in "Haskell,Clojure,Common Lisp,Racket,Scheme,crosslanguage,Hack".split(","):
        return "(" + " ".join(newArr) + ")"
    elif lang in "REBOL,Red,Polish notation".split(","):
        if fromClass != None:
            newArr[0] = fromClass + "/" + newArr[0]
    
        return " ".join(newArr)
    elif lang in "Reverse Polish notation".split(","):
        return " ".join(parameters) + " " + function
    elif lang in ["Oz"]:
        return "{" + " ".join(newArr) + "}"
    elif lang in ["Tcl"]:
        return "[" + " ".join(newArr) + "]"
    elif lang in ["Bash"]:
        return "$(" + " ".join(newArr) + ")"
    elif lang in "Swift,Groovy,Scala,CoffeeScript,Julia,C,TypeScript,Fortran,Octave,C++,Go,Cobra,Ruby,Vala,F#,Java,OCaml,Erlang,Python,C#,Lua,Haxe,JavaScript,Dart,bc,Visual Basic,Visual Basic .NET,PHP,Perl".split(","):
        aString=""
        if len(parameters) == 0:
            aString = ""
        else:
            i=0
            while i < len(parameters):
                if type(parameters[i]) == "str":
                    parameters[i] = initializeVar()
                aString += str(parameters[i]);
                if i != len(parameters) -1:
                    if lang == "crosslanguage":
                        aString += " "
                    else:
                        aString += ","
                i += 1
        if fromClass == None:
            return function + "(" + aString + ")"
        else:
            return fromClass + "." + function + "(" + aString + ")"
    notYetDefinedError(lang, inspect.stack()[0][3])
    
def accessArray(lang, arrayName, indexList):
    toReturn = None
    if type(indexList) != list:
        indexList = [indexList]
    i = 0
    for current in indexList:
        indexList[i] = str(current)
        i += 1
    arrayName = getVariableName(lang, arrayName)
    if lang in ["crosslanguage"]:
        return "accessArray(" + ", " + lang + ", " + arrayName + ", " + indexList
    
    if lang in ["Haskell"]:
        newIndexList = [arrayName] + indexList
        return "!!".join(newIndexList)
    
    if lang in "Python,Nimrod,AutoIt,Cython,CoffeeScript,Dart,TypeScript,AWK,Vala,Perl,Java,JavaScript,Ruby,Go,C++,PHP,Haxe,C".split(","):
        toReturn = arrayName + "[" + "][".join(indexList) + "]"
    if lang in "Scala".split(","):
        toReturn = arrayName + "(" + ")(".join(indexList) + ")"
    elif lang in ["REBOL"]:
        return arrayName + "/(" + " + 1)/(".join(indexList)+" + 1)";
    elif lang in ["Lua"]:
        i = 0;
        toReturn = arrayName + "[";
        while(i < len(indexList)):
            toReturn += str(indexList[i]);
            if i < len(indexList)-1:
                toReturn += "+1][";
            i += 1;
        toReturn += "+1]";
    elif lang in ["C#", "Julia"]:
        toReturn = arrayName + "[" + ", ".join(indexList) + "]"
    elif lang in ["Visual Basic"]:
        toReturn = arrayName + "(" + ", ".join(indexList) + ")" 
    if toReturn != None:
        return toReturn;
    else:
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def charAt(lang, aString, index):
        #return examples.EngScript_examples.Python.engScriptFunctions.engScript_charAt(lang)
        aString = getVariableName(lang, aString)
        index = getVariableName(lang, index)
        if lang in "Python,Nimrod,CoffeeScript,TypeScript,Dart,Vala,JavaScript,Ruby,C#,PHP,REBOL,C".split(","):
            return accessArray(lang=lang, arrayName=aString, indexList = [index])
        #else:
        #    return examples.EngScript_examples.Python.engScriptFunctions.engScript_charAt(lang)
        elif lang in "Java,Haxe,Scala".split(","):
            return aString + ".charAt(" + index + ")"
        elif lang in "Tcl".split(","):
            return "[string index " + aString + " " + index + "]"
        elif lang in "crosslanguage".split(","):
            return "(charAt " + aString + " " + index + ")"
        elif lang in "Visual Basic,F#".split(","):
            return aString+".Chars("+index+")"
        elif lang in "Haskell".split(","):
            return aString + " !! " + index
        elif lang in "Go".split(","):
            return "string([]rune(" + aString + ")[" + index + "])"
        elif lang in "Lua".split(","):
            return "string.sub(" + aString + "," + index + " + 1," + index + " + 1)"
        elif lang in "Perl".split(","):
            return "substr("+aString+", "+index+"-1, 1)"
        notYetDefinedError(lang, inspect.stack()[0][3])

def index(theObject, theType, indexList):
    if getCorrespondingType(theType) == getCorrespondingType("string"):
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

def Error(lang, message):
        #return examples.EngScript_examples.Python.engScriptFunctions.engScript_Error(lang)
        if lang in "Python".split(","):
            return "raise Exception(" + message + ")"
        elif lang in "Java,PHP,C#".split(","):
            return "throw new Exception(" + message + ");";
        elif lang in "JavaScript,CoffeeScript,Haxe".split(","):
            return "throw " + message;
        elif lang in "Haskell,Scheme,crosslanguage".split(","):
            return "(error " + message + ")";
        elif lang in "Haskell,Scheme".split(","):
            return "(error " + message + ")";
        elif lang in "crosslanguage".split(","):
            return "error(" + message + ")";
        elif lang in "REBOL".split(","):
            return "make error! "+message;
        elif lang in "Ruby".split(","):
            return "raise " + message;
        notYetDefinedError(lang, inspect.stack()[0][3])

def getComment(lang, comment):
        #use interpolateString here
        toReturn=""
        if lang in "Bash,Nimrod,CoffeeScript,Julia,AWK,Ruby,Perl,R,Tcl,bc,Python".split(","):
            toReturn= "#{comment}"
        elif lang in "ALGOL 68".split(","):
            toReturn=  "# {comment} #"
        elif lang in "Gambas,Visual Basic,Visual Basic .NET".split(","):
            toReturn=  "'{comment}"
        elif lang in "REBOL".split(","):
            toReturn= "[comment {comment}]"
        elif lang in "Fortran".split(","):
            toReturn= "! {comment}"
        elif lang in "OCaml".split(","):
            toReturn= "(*{comment}*)"
        elif lang in "Java,Dart,TypeScript,Swift,Vala,C#,JavaScript,Haxe,Scala,Go,C,C++,PHP,F#,Nemerle,crosslanguage".split(","):
            toReturn= "//{comment}"
        elif lang in "MATLAB,Octave,Erlang,Prolog".split(","):
            toReturn= "%{comment}"
        elif lang in "Lua,Haskell,Ada".split(","):
            toReturn= "--{comment}"
        elif acs(lang,"Racket,AutoIt,AutoHotKey,Common Lisp,Clojure"):
            toReturn= ";{comment}"
            
        if toReturn == "":
            notYetDefinedError(lang, inspect.stack()[0][3])
        else:
            return toReturn.format(comment=comment)

def getFunctionParameterList(lang, parameterNames, parameterTypes):
    if type(parameterNames) == str:
        parameterNames = [parameterNames]
    if type(parameterTypes) == str:
        if parameterTypes == "[]":
            parameterTypes = ""
        else:
            parameterTypes = [parameterTypes]
    
    if parameterNames == parameterTypes:
        parameterTypes = [getCorrespondingType(lang, x) for x in parameterTypes]
    parameterNames = [getVariableName(lang, i) for i in parameterNames]
    

    
    #if name == "junk":
    #    raise Exception(parameterNames)
    if (parameterNames == parameterTypes) or parameterNames[0] in ["[]", "$[]", "None", "$None"]:
        parameterNames = []
    elif(methodRequiresParameterTypes(lang)):
        parameterTypes = [getCorrespondingType(lang, x) for x in parameterTypes]    #raise Exception(parameterNames)
    
    
    if lang in ["PHP"]:
        parameterNames = [addInitialDollarSign(val) for val in parameterNames]
    elif lang in ["Tcl"]:
        parameterNames = [removeInitialDollarSign(val) for val in parameterNames]
    if methodRequiresParameterTypes(lang) == True:
        parameterTypes = [getCorrespondingType(lang = lang, dimension=None, theType=i) for i in parameterTypes]
    
    if parameterNames in [["None"], None, []] and parameterTypes in [["None"], None, []]:
        parameterNames = []
    if parameterNames in [["None"], None, []] and parameterTypes in [["None"], None, []]:
        parameterNames = []
        parameterTypes = []
    if parameterNames in [None, ["None"], "", "[]"]:
        parameterNames = []
    if parameterTypes in [None, ["None"], "", "[]"]:
        parameterTypes = []
    
    '''
    Get the parameter list for a function definition
    '''
    if lang in "Bash":
        i = 0
        for current in parameterNames:
            parameterNames[i] = "    " + (parameterNames[i])[1:len(parameterNames[i])] + "=" + "$" + str(i+1)
            i += 1
        return parameterNames
    
    
    if lang in "Perl":
        toReturn = ""
        for current in parameterNames:
            toReturn += "\n" + current + " = shift;"
        return toReturn
    
    elif lang in "Haskell,Clojure,F#,ML,Racket,OCaml,Tcl,Common Lisp".split(","):
        return " ".join(parameterNames);
    elif (lang, "Python,CoffeeScript,Fortran,Octave,AutoHotKey,Julia,Prolog,AWK,Kotlin,Dart,JavaScript,Nemerle,Erlang,PHP,AutoIt,Lua,Ruby,R,bc"):
        i = 0;
        return ", ".join(parameterNames)
    else:
        'for java, haxe, C++, etc'
        for current in parameterTypes:
            current = getCorrespondingType(lang=lang, dimension=None, theType=current)
        i = 0;
        toReturn = ""
        while i < len(parameterNames):
            if lang in ["Go"]:
                toReturn += parameterNames[i] +" "+ parameterTypes[i]
            elif lang in "Haxe,Nimrod,TypeScript,Gosu,Delphi,Nemerle,Scala,Swift".split(","):
                toReturn += parameterNames[i] +" : "+ parameterTypes[i]
            elif lang in "Visual Basic,Visual Basic .NET".split(","):
                toReturn += parameterNames[i] +" as "+ parameterTypes[i]
            elif lang in "OpenOffice Basic".split(","):
                toReturn += parameterNames[i] +" As "+ parameterTypes[i]
            elif lang in "C#,Java,ALGOL 68,Groovy,D,C++,Vala,C,crosslanguage".split(","):
                toReturn += parameterTypes[i] +" "+ parameterNames[i]
            elif lang in "REBOL".split(","):
                toReturn += parameterNames[i] +" ["+ parameterTypes[i]+"]"
            else:
                notYetDefinedError(lang, inspect.stack()[0][3])
            if i < len(parameterNames) -1:
                if lang == "crosslanguage":
                    toReturn += " "
                elif lang in ["Delphi"]:
                    toReturn += "; "
                else:
                    toReturn += ", "
            i += 1;
        return toReturn;
    notYetDefinedError(lang, inspect.stack()[0][3])

getParameterList = getFunctionParameterList

def methodRequiresParameterTypes(lang):
    '''
        Return true if the start of the method requires parameter types, and otherwise return false.
    '''
    if acs(lang, "Haskell,PowerShell,Hy,CoffeeScript,Octave,Clojure,AutoHotKey,Julia,AWK,Prolog,F#,Nemerle,ML,AutoIt,Erlang,Python,Lua,JavaScript,Bash,Ruby,Perl,Racket,Common Lisp,Tcl,R,bc"):
        return False
    elif acs(lang, "Java,OCaml,Hack,Gambas,OpenOffice Basic,Cython,REBOL,ALGOL 68,Scala,PHP,Dart,Ceylon,D,TypeScript,Fortran,Gosu,Groovy,Delphi,Swift,Pike,C,Objective-C,C#,Haxe,Go,C++,Visual Basic,Visual Basic .NET,crosslanguage,Vala"):
        return True
    notYetDefinedError(lang, inspect.stack()[0][3])

def startMethod(lang, name, returnType, parameterNames, parameterTypes, isStatic=False, isInstanceMethod=False):    
    toReturn=""
    name = removeInitialDollarSign(name)
    
    if methodRequiresReturnType(lang):
        returnType = getCorrespondingType(lang=lang, dimension=None, theType=returnType)
    
    parameterList = getParameterList(lang=lang, parameterNames=parameterNames, parameterTypes=parameterTypes)
    if isInstanceMethod:
        if lang in ["Python"]:
            if parameterList == "":
                parameterList = "self"
            else:
                parameterList = "self, " + parameterList
        elif lang in ["Groovy", "Java", "Ruby", "C#", "C++", "Haxe", "Scala", "Dart", "TypeScript"]:
            pass
        elif lang in ["JavaScript"]:
            return "this."+name+" = function("+parameterList+"){"
        elif lang in ["TypeScript"]:
            return name+"("+parameterList+"){"
        elif lang in ["PHP"]:
            return "public function " + name + "(" + parameterList + "){"
        elif lang in ["CoffeeScript"]:
            return name + ": ("+parameterList+") ->"
        else:
            notYetDefinedError(lang, inspect.stack()[0][3])
    elif isStatic:
        if lang in ["Python"]:
            return ["@static", "def " + name + "(" + parameterList + "):"]
        elif lang in ["Sibilant"]:
            return "(def functionName ("+parameterList+")"
        elif lang in ["Ruby"]:
            name = "static."+name
        elif lang in ["C++", "Dart"]:
            return "static " + returnType + " " + name + "(" + parameterList + "){"
        elif lang in ["Haxe"]:
            return "static function " + name + "(" + parameterList + ") : "+returnType+" {";
        elif lang in ["TypeScript"]:
            return "public static " + name + "(" + parameterList + "): "+returnType+"{"
        elif lang in ["C#", "Java", "Groovy"]:
            return "public static " + returnType +" "+ name + "(" + parameterList + "){"
        elif lang in ["PHP"]:
            return "public static function " +" "+ name + "(" + parameterList + "){"
        elif lang in ["Scala"]:
            pass
        elif lang in ["CoffeeScript"]:
            return "@" + name + ": ("+parameterList+") ->"
        else:
            notYetDefinedError(lang, inspect.stack()[0][3])
    if acs(lang, "Hack"):
        toReturn= "function @name(@parameterList): @returnType {"
    if lang in ["OpenOffice Basic"]:
        toReturn= 'Function @name(@parameterList)'
    if lang in ["OCaml"]:
        toReturn= "let @name @parameterList ="
    if acs(lang, "AutoHotKey"):
        toReturn= "@name(@parameterList){"
    if lang in ["Perl"]:
        toReturn= "sub @name { parameterList"
    if lang in ["Python"]:
        toReturn = "def @name(@parameterList):"
    if lang in ["Groovy"]:
        toReturn = "def @name(@parameterList)\{"
    if lang in ["Prolog"]:
        toReturn = "@name(@parameterList) :- "
    if lang in ["Visual Basic", "Visual Basic .NET"]:
        toReturn= "Function @name(@parameterList) As @returnType"
    if lang in ["Erlang"]:
        toReturn= "@name(@parameterList) ->"
    if lang in ["R"]:
        toReturn= "@name <- function(@parameterList){"
    if lang in ["REBOL"]:
        toReturn= "@name: func [@parameterList] ["
    if lang in ["Tcl"]:
        toReturn= "proc @name{@parameterList} {"
    if lang in ["bc"]:
        toReturn= "define @name(@parameterList){"
    if lang in ["Ruby"]:
        toReturn= "def @name(@parameterList)"
    if lang in ["Go"]:
        toReturn= "func @name(@parameterList) @returnType{"
    if lang in ["Java", "C#"]:
        toReturn= "public @returnType @name(@parameterList){"
    if lang in ["Haxe"]:
        toReturn= "function @name(@parameterList) : @returnType{"
    if lang in ["Gosu"]:
        toReturn= "function @name(@parameterList) : @returnType {"
    if lang in ["Swift"]:
        toReturn= "func @name(@parameterList) {"
    if lang in ["Scala"]:
        toReturn= "def @name(@parameterList) : @returnType = {"
    if lang in ["Nemerle"]:
        toReturn= "@name(@parameterList) : @returnType {"
    if lang in "JavaScript,PHP,AWK,PowerShell".split(","):
        toReturn= "function @name(@parameterList){"
    if lang in ["TypeScript"]:
        toReturn= "@name(@parameterList): @returnType{"
    if lang in ["Lua", "Julia"]:
        toReturn= "function @name(@parameterList)"
    if lang in ["AutoIt"]:
        toReturn= "Func @name(@parameterList)"
    if lang in ["C++", "Vala","C", "Dart", "Ceylon", "Pike", "D"]:
        toReturn= "@returnType @name (@parameterList){"
    if lang in ["crosslanguage"]:
        toReturn= "(def @returnType @name (@parameterList)"
    if lang in ["Haskell"]:
        toReturn= "@name @parameterList ="
    if lang in ["F#"]:
        toReturn= "let @name @parameterList ="
    if lang in ["ML"]:
        toReturn= "fun @name(@parameterList) ="
    if lang in ["Racket"]:
        toReturn= "(define (@name @parameterList)"
    if lang in ["Emacs Lisp", "Common Lisp"]:
        toReturn= "(defun @name(@parameterList)"
    if lang in ["Clojure"]:
        toReturn= "(defn @name [@parameterList]"
    if lang in ["Bash"]:
        return ["function "+name+" {"] + parameterList
    if lang in ["Delphi"]:
        toReturn = "procedure @name(@parameterList): @returnType;\nbegin"
    if lang in ["Octave"]:
        toReturn= "function retval = @name(@parameterList)"
    if lang in ["CoffeeScript"]:
        toReturn= "@name = (@parameterList) ->"
    if lang in ["ALGOL 68"]:
        toReturn= "proc @name = (@parameterList) @returnType:"
    if lang in "Cython".split(","):
        toReturn= "cdef @returnType @name(@parameterList):"
    if acs(lang, "Hy"):
        toReturn = '(defn @name [@parameterList]'
    if lang in ["Fortran"]:
        parameterTypeString = ""
        for i in range(0, len(parameterNames)):
            parameterTypeString += "\n    " + parameterTypes[i] + " :: " + parameterNames[i]
        return "FUNCTION "+name+"("+parameterList+") RESULT(retval)\n    "+returnType+" :: retval" + parameterTypeString
    if toReturn == "":
        notYetDefinedError(lang, inspect.stack()[0][3])
    else:
        #print toReturn
        return stringInterpolation(toReturn, "@name,@parameterList,@parameterTypes,@parameterNames,@returnType", [name,parameterList,parameterTypes,parameterNames,returnType])

def getCorrespondingTypeWithoutBrackets(lang, theType):
        if theType in ["None", None, ""]:
            return None
        if theType in "True,true".split(","):
            if lang in "Java,Rust,Clojure,Nimrod,Hack,Ceylon,D,Groovy,CoffeeScript,TypeScript,Octave,Prolog,Julia,F#,Swift,Nemerle,Vala,C++,Dart,JavaScript,Ruby,Erlang,C#,Haxe,Go,OCaml,Lua,Scala,PHP,crosslanguage,REBOL".split(","):
                return "true"
            elif lang in "Python,Hy,Cython,AutoIt,Haskell,Visual Basic .NET,Visual Basic".split(","):
                return "True"
            elif lang in "R,Gambas".split(","):
                return "TRUE"
            elif lang in "Perl,AWK,Tcl,C".split(","):
                return "1"
            elif lang in "Racket".split(","):
                return "#t"
            elif lang in "Common Lisp".split(","):
                return "t"
        if theType in "False,false".split(","):
            if lang in "Java,Clojure,Nimrod,Groovy,D,Ceylon,TypeScript,CoffeeScript,Octave,Prolog,Julia,Vala,F#,Swift,C++,Nemerle,Dart,JavaScript,Ruby,Erlang,C#,Haxe,Go,OCaml,Lua,Scala,PHP,crosslanguage,REBOL".split(","):
                return "false"
            elif lang in "Python,Hy,Cython,AutoIt,Haskell,Visual Basic .NET,Visual Basic".split(","):
                return "False"
            elif lang in "Gambas".split(","):
                return "TRUE"
            elif lang in "Perl,AWK,Tcl,C".split(","):
                return "0"
            elif lang in "Racket".split(","):
                return "#f"
            elif lang in "Common Lisp".split(","):
                return "nil"
        if theType in "fixnum".split(","):
            if lang in "Ruby".split(","):
                return "fixnum"
        if theType in "Int,int,Integer,integer,INTEGER,integer!".split(","):
            if lang in "Hack,Cython,ALGOL 68,D,Octave,Tcl,ML,AWK,Julia,Gosu,OCaml,F#,Pike,Objective-C,Go,Cobra,Dart,Groovy,Python,Hy,Java,C#,C,C++,Vala,Nemerle,crosslanguage".split(","):
                return "int"
            elif lang in "PHP".split(","):
                return "integer"
            elif lang in "Fortran".split(","):
                return "INTEGER"
            elif lang in "REBOL".split(","):
                return "integer!"
            elif lang in "Ceylon,Gambas,OpenOffice Basic,Pascal,Erlang,Delphi,Visual Basic,Visual Basic .NET".split(","):
                return "Integer"
            elif lang in "Haxe,Swift,Scala".split(","):
                return "Int"
            elif lang in "JavaScript,TypeScript,CoffeeScript,Lua,Perl".split(","):
                return "number"
            elif lang in "Haskell".split(","):
                return "Num"
            elif lang in "Ruby".split(","):
                return "fixnum"
            #elif lang in "Perl".split(","):
            #    return "scalar"
        elif theType in "boolean,Boolean,bool,Bool,LOGICAL".split(","):
            if lang in "TypeScript,Python,Hy,Java,JavaScript,PHP,Lua,Perl".split(","):
                return "boolean"
            if lang in "Visual Basic,OpenOffice Basic,Ceylon,Delphi,Scala".split(","):
                return "Boolean"
            if lang in "C++,Dart,D,Vala,crosslanguage,Go,Cobra,C#,F#".split(","):
                return "bool"
            if lang in "C,Cython".split(","):
                return "int"
            if lang in "Fortran".split(","):
                return "LOGICAL"
            if lang in "Haxe,Haskell,Swift".split(","):
                return "Bool"
            if lang in "REBOL".split(","):
                return "logic!"
        elif theType in "String,str,string,string!".split(","):
            if lang in "Python,Hy,crosslanguage".split(","):
                return "str"
            elif lang in "Vala,Nimrod,ALGOL 68,TypeScript,CoffeeScript,Octave,Tcl,AWK,Julia,C#,F#,Perl,Lua,JavaScript,Go,PHP,C++,Nemerle,Erlang".split(","):
                return "string"
            elif lang in "REBOL".split(","):
                return "string!"
            elif lang in "C,Cython".split(","):
                return "char*"
            elif lang in "Java,Ceylon,Gambas,Dart,Gosu,Groovy,Scala,Pascal,Swift,Ruby,Haxe,Haskell,Visual Basic,Visual Basic .NET".split(","):
                return "String"
        if theType in ["char"]:
            if lang in "C,Java,C#".split(","):
                return "char"
            elif lang in "Python,Hy,JavaScript".split(","):
                return getCorrespondingTypeWithoutBrackets(lang, "String")
        if theType in ["number"]:
            if lang in "JavaScript,TypeScript,CoffeeScript".split(","):
                return "number"
        elif theType in "Void,void,Unit".split(","):
            if lang in "Python,Hy,Cython,Haxe,Go,Pike,Objective-C,Java,C,C++,C#,Vala,crosslanguage,TypeScript".split(","):
                return "void"
            elif lang in "Visual Basic".split(","):
                return "Nothing"
            elif lang in "Scala".split(","):
                return "Unit"
        elif theType in ["dictionary", "dict"]:
            if lang in ["Scala"]:
                return "Map";
        raise EngScriptException("getCorrespondingTypeWithoutBrackets is not yet defined for " + str(lang) + " and the type " + theType)

def getCorrespondingType(lang, theType, dimension=None):
    if theType in ["None", None, "", "[]"]:
        return None
    #print(theType)
    if "[]" in theType:
        if lang in ["JavaScript"]:
            return "Array"
        if lang in ["Python"]:
            return "list"
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
    if theVar[0] == "$":
        return theVar[1:len(theVar)]
    else:
        return theVar
        
def addInitialDollarSign(theVar):
    if theVar[0] != "$":
        return "$" + theVar
    else:
        return theVar
    
def removeInitialAtSign(theVar):
    if theVar[0] == "$":
        return theVar[1:len(theVar)]
    else:
        return theVar

def addInitialAtSign(theVar):
    if theVar[0] != "@":
        return "@" + theVar
    else:
        return theVar

def isIdentifier(theExpression):
    if theExpression.startswith('"') or theExpression.startswith("'"):
        return False
    if " " in theExpression or "." in theExpression or "->" in theExpression or "(" in theExpression or "[" in theExpression or "!" in theExpression or "{" in theExpression or '"' in theExpression:
        if is_number(theExpression) == False :
            return False
    else:
        return True

def getVariableName(lang, theVar):
    if(type(theVar) == int):
        theVar = str(theVar)
    elif type(theVar) == list:
        #raise Exception("theVar is a list. Figure out what to do now.")
        return getArrayInitializer(lang, theVar)
    elif theVar in ["False", "True", "false", "true", False, True]:
        return getCorrespondingType(lang, theVar)
    theVar = str(theVar)
    if is_number(theVar):
        return theVar
    theVar = removeInitialDollarSign(theVar)
    if isIdentifier(theVar):
        if not theVar.startswith("engScript_"):
            theVar = "engScript_"+theVar
    if acs(lang, "PHP,Perl,Bash,Tcl,AutoIt,Perl 6,Puppet,Hack,AWK,PowerShell"):
        if isIdentifier(theVar):
            return addInitialDollarSign(theVar)
        else:
            return theVar
    elif lang in ["Erlang"]:
        if isIdentifier(theVar):
            theVar = theVar[0].upper() + theVar[1:len(theVar)]
            return theVar
        else:
            return theVar
    elif acs(lang, "Java,Hy,OCaml,Julia,AutoIt,C#,Gosu,AutoHotKey,Groovy,Rust,R,Swift,Vala,Go,Scala,Nemerle,Visual Basic,Visual Basic .NET,Clojure,Haxe,CoffeeScript,Dart,JavaScript,C#,Python,Ruby,Haskell,C,Lua,Gambas,Common Lisp,Scheme,REBOL,F#"):
        return theVar;
    raise Exception("GetVariableName is not defined for "+lang+". The variable name is " + theVar)

def getClassBeginning(lang, className, parameterNames=None, parameterTypes=None):
        if parameterNames == None and parameterTypes == None:
            parameterList = None
        else:
            parameterList = getParameterList(lang=lang, parameterNames=parameterNames, parameterTypes=parameterTypes)
        
        if lang in "Python".split(","):
            return "class " + className + ":"
        if lang in "Smalltalk-80":
            return "Object subclass: #"+className
        if lang in "REBOL".split(","):
            return className+": make object! ["
        if lang in "crosslanguage".split(","):
            return "(class " + className
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "Public Class " + className
        elif lang in "Ruby,CoffeeScript".split(","):
            return "class " + className
        elif lang in "Java,ActionScript,C#,Vala".split(","):
            return "public class " + className + "{"
        elif lang in "Go,TypeScript,Swift,Haxe,C++,PHP,Groovy,Dart".split(","):
            return "class " + className + "{"
        elif lang in "JavaScript".split(","):
            return "function " + className + "("+parameterList+"){"
        elif lang in "Perl,Erlang,Lua,Bash,Racket,Common Lisp,Tcl,bc,AWK,Haskell".split(","):
            return ""
        elif lang in ["Scala"]:
            return "class "+className+"("+parameterList+"){"
        notYetDefinedError(lang, inspect.stack()[0][3])

def endClass(lang):
        if lang in "PHP,Dart,Scala,ActionScript,TypeScript,Swift,Python,Ruby,REBOL,Java,Nemerle,C#,crosslanguage,Go,Groovy,Haxe,JavaScript,Vala".split(","):
            return endCodeBlock(lang)
        elif lang in "C++".split(","):
            return "};"
        elif lang in "CoffeeScript,Perl,OCaml,Erlang,Lua,Bash,Haskell,bc,AWK".split(","):
            return ""
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End Class"
        notYetDefinedError(lang, inspect.stack()[0][3])

def add(lang, numArray):
    numArray = [getVariableName(lang, x) for x in numArray]
    if acs(lang, "Java,PowerShell,Gosu,Nimrod,Cython,OpenOffice Basic,ALGOL 68,D,Ceylon,Rust,CoffeeScript,ActionScript,TypeScript,Fortran,Octave,ML,AutoHotKey,Prolog,Delphi,Pascal,F#,Self,Swift,Nemerle,Dart,C,AutoIt,Cobra,Julia,Groovy,Scala,OCaml,Erlang,Gambas,Hack,C++,MATLAB,REBOL,Red,Lua,Go,AWK,Haskell,Perl,Python,JavaScript,C#,PHP,Ruby,R,Haxe,Visual Basic,Visual Basic .NET,Vala,bc,crosslanguage"):
        return  "(" + " + ".join(numArray) + ")"
    else:
        if arrayContainsSplit(lang, "Tcl"):
            return "[expr " + " + ".join(numArray) + "]";
        elif arrayContainsSplit(lang, "Bash"):
            return "((" + " + ".join(numArray) + "))";
        elif arrayContainsSplit(lang, "Racket,Hy,LispyScript,Sibilant,Clojure,Common Lisp,Scheme"):
            return "(+ " + " ".join(numArray) + ")";
        if arrayContainsSplit(lang, "Polish notation"):
            return "+" + " ".join([""]+numArray[0:len(numArray)-1]) + " " + numArray[len(numArray)-1]
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

#raise to power
def raiseToExponent(lang, num1, num2):
    num1 = getVariableName(lang,num1)
    num2 = getVariableName(lang,num2)
    
    #num1 is the base and num2 is the exponent
    
    if acs(lang, "Python,AWK,R,F#,AutoHotKey,Tcl,AutoIt,Groovy,Octave,Ruby,Perl,Fortran"):
        return "("+num1 + "**" + num2+")"
    #else:
    #    return examples.EngScript_examples.Python.engScriptFunctions.engScript_raiseToExponent(lang)
    if lang in "Julia,Visual Basic,Gambas,Go,Ceylon".split(","):
        return "("+num1 + " ^ " + num2+")"
    if lang in "JavaScript,CoffeeScript,TypeScript,Java,Lua,Haxe".split(","):
        return  "Math.pow(" + num1 + "," + num2+")"
    if lang in "C#".split(","):
        return  "Math.Pow(" + num1 + "," + num2+")"
    if lang in "Dart".split(","):
        return  "math.pow(" + num1 + "," + num2+")"
    if lang in "C,C++,PHP,Hack,Swift".split(","):
        return  "pow(" + num1 + "," + num2+")"
    if lang in "Erlang".split(","):
        return  "math:pow(" + num1 + "," + num2+")"
    if lang in "REBOL".split(","):
        return "power " + num1 + " " + num2
    if lang in ["Polish notation"]:
        return "^ " + num1 + " " + num2
    if lang in ["Reverse Polish notation"]:
        return num1 + " " + num2 + " ^"
    elif lang in ["Rust"]:
        return "num::pow("+num1+", "+num2+")"
    elif lang in ["Scala"]:
        return "scala.math.pow("+num1+","+num2+")"
    elif lang in ["Common Lisp", "Racket", "Clojure"]:
        return "(expt "+num1+" "+num2+")"
    elif lang in ["Hy"]:
        return "(expt "+num1+" "+num2+")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def mod(lang, numArray):
    numArray = [getVariableName(lang, x) for x in numArray]
    if lang in "Java,AWK,Julia,Scala,F#,Swift,R,Perl,Nemerle,Haxe,PHP,Vala,Lua,Tcl,Go,Dart,JavaScript,Python,C,C++,C#,Ruby".split(","):
        return  "(" + " % ".join(numArray) + ")"
    elif lang in "Haskell".split(","):
        return  "(" + " mod ".join(numArray) + ")"
    elif lang in "Visual Basic".split(","):
        return  "(" + " Mod ".join(numArray) + ")"
    elif lang in ["Prolog"]:
        if len(numArray) == 2:
            return "mod(" + numArray[0] + ", " + numArray[1] + ")"
    elif lang in "REBOL".split(","):
        return  "(" + "mod " +  " mod ".join(numArray[0:len(numArray)-1]) +" "+ numArray[len(numArray)-1] + ")"
    elif lang in ["Racket"]:
        if len(numArray) == 2:
            return "(modulo " + numArray[0] +" "+ numArray[1] + ")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def multiply(lang, numArray):
    numArray = [getVariableName(lang, x) for x in numArray]
    for idx, val in enumerate(numArray):
        numArray[idx] = str(val)
    if (lang, "C,PowerShell,Gosu,AWK,Gambas,Nimrod,AutoHotKey,Julia,OpenOffice Basic,ALGOL 68,D,Groovy,Ceylon,Rust,CoffeeScript,ActionScript,TypeScript,Fortran,Octave,ML,Haxe,Pascal,Delphi,Swift,Nemerle,Vala,R,Red,C++,Erlang,Scala,AutoIt,Cobra,F#,Perl,PHP,Go,Ruby,Lua,Haskell,Hack,Java,OCaml,REBOL,Python,JavaScript,C#,Visual Basic,Visual Basic .NET,Dart".split):
        return  "(" + " * ".join(numArray) + ")"
    if lang in ["Tcl"]:
        return "[expr " + " * ".join(numArray) + "]"
    if lang in ["Bash"]:
        return  "((" + " * ".join(numArray) + "))"
    if lang in "Racket,Common Lisp,Clojure,LispyScript,Sibilant".split(","):
        return  "(* " + " ".join(numArray) + ")"
    if lang in "Polish notation":
        return "*".join([""]+numArray[0:len(numArray)-1]) + " " + numArray[len(numArray)-1]
    if lang in "Reverse Polish notation":
        return numArray[0] +" "+ "*".join(numArray[1:len(numArray)] + [""]) 
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def subtract(lang, numArray):
    numArray = [getVariableName(lang, x) for x in numArray]
    for idx, val in enumerate(numArray):
        numArray[idx] = str(val)
    if acs(lang, "Java,PowerShell,OpenOffice Basic,Cython,ALGOL 68,D,Groovy,Ceylon,Rust,CoffeeScript,ActionScript,TypeScript,Fortran,Octave,ML,AutoHotKey,AWK,Julia,Delphi,Pascal,Swift,Nemerle,Vala,R,Go,Dart,C,C++,AutoIt,Scala,Perl,Erlang,F#,Hack,OCaml,Haskell,Python,REBOL,Red,JavaScript,C#,PHP,Visual Basic,Visual Basic .NET,Ruby,Haxe,Lua"):
        return  "(" + " - ".join(numArray) + ")"
    if lang in ["Tcl"]:
        return "[expr " + " - ".join(numArray) + "]"
    if lang in ["Racket", "Common Lisp", "Clojure"]:
        return  "(- " + " ".join(numArray) + ")"
    if lang in "Polish notation":
        return "-".join([""]+numArray[0:len(numArray)-1]) + " " + numArray[len(numArray)-1]
    if lang in "Reverse Polish notation":
        return numArray[0] +" "+ "-".join(numArray[1:len(numArray)] + [""]) 
    notYetDefinedError(lang, inspect.stack()[0][3])

def divide(lang, numArray):
    numArray = [getVariableName(lang, x) for x in numArray]
    if acs(lang, "Java,PowerShell,Gosu,Gambas,Nimrod,OpenOffice Basic,ALGOL 68,D,Groovy,Ceylon,Rust,CoffeeScript,ActionScript,TypeScript,Fortran,Octave,ML,AutoHotKey,AWK,Julia,F#,Visual Basic,Swift,Nemerle,Vala,Go,Dart,R,C,C++,Python,Scala,AutoIt,Perl,Erlang,Hack,Ruby,Haxe,Lua,Haskell,OCaml,JavaScript,C#,PHP"):
        return  "(" + " / ".join(numArray) + ")"
    if lang in ["Tcl"]:
        return "[expr " + " / ".join(numArray) + "]"
    if lang in "REBOL,Red".split(","):
        return  "(" + " / ".join(numArray) + ")"
    if acs(lang, "Racket,Hy,Common Lisp,Clojure,LispyScript,Sibilant"):
        return  "(/ " + " ".join(numArray) + ")"
    elif lang in ["Polish notation"]:
        return "/".join([""]+numArray[0:len(numArray)-1]) + " " + numArray[len(numArray)-1]
    if lang in "Reverse Polish notation":
        return numArray[0] +" "+ "/".join(numArray[1:len(numArray)] + [""]) 
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

mul = multiply
sub=subtract
Add = add


def concatenateStrings(lang, stringArray):
    stringArray = [getVariableName(lang, i) for i in stringArray]
    
    if lang in "Java,Nemerle,D,Cython,Ceylon,CoffeeScript,TypeScript,Dart,Gosu,Groovy,Scala,Swift,F#,Python,JavaScript,C#,Haxe,Ruby,C++,Vala".split(","):
        return  "(" + " + ".join(stringArray) + ")"
    elif lang in "Visual Basic,Gambas,Nimrod,AutoIt,Visual Basic .NET,OpenOffice Basic".split(","):
        return  " & ".join(stringArray)
    elif lang in ["Lua"]:
        return  " .. ".join(stringArray)
    elif lang in ["Bash"]:
        return  "".join(stringArray)
    elif lang in ["Haskell"]:
        return  " ++ ".join(stringArray)
    elif lang in ["OCaml"]:
        return  " ^ ".join(stringArray)
    elif lang in ["PHP", "AutoHotKey", "Hack"]:
        return " . ".join(stringArray)
    elif lang in ["AWK"]:
        return "("+ " ".join(stringArray) + ")"
    elif lang in ["crosslanguage"]:
        return "("+ " . ".join(stringArray)+")"
    elif lang in ["Octave"]:
        return "strcat(" + ", ".join(stringArray) + ")"
    elif lang in ["Erlang"]:
        return "string:concat(" + ", ".join(stringArray) + ")"
    elif lang in ["Perl"]:
        return "(join " + ", ".join(['""'] + stringArray) + ")"
    elif lang in ["Go"]:
        return "strings.Join([]string{" + ", ".join(stringArray) + "}, \" \")"
    elif lang in ["Racket"]:
        return "(string-append " + " ".join(stringArray) + ")"
    elif lang in ["Clojure"]:
        return "(str " + " ".join(stringArray) + ")"
    elif lang in ["Hy"]:
        return "(str " + " ".join(stringArray) + ")"
    elif lang in ["Common Lisp"]:
        return "(concatenate 'string " + " ".join(stringArray) + ")"
    if lang in ["REBOL", "Red"]:
        lastElement = stringArray[len(stringArray)-1]
        arrayOfArrays = stringArray[0:len(stringArray) - 1]
        return "append " + " append ".join(arrayOfArrays) + " " + lastElement
    elif lang in "Delphi":
        return "Concat(" + ", ".join(stringArray) + ")"
    elif lang in "R":
        return "paste(" + ", ".join(stringArray) + ", sep=\"\")"
    elif lang in "Julia":
        return "string(" + ", ".join(stringArray) + ")"
    elif lang in "Clojure":
        return "(str " + " ".join(stringArray) + ")"
    notYetDefinedError(lang, inspect.stack()[0][3])

def concatenateArrays(lang, arrayOfArrays):
    arrayOfArrays = [getVariableName(lang, x) for x in arrayOfArrays]
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
    if lang in ["Nemerle"]:
        return " :: ".join(arrayOfArrays)
    if lang in ["Java"]:
        '''
        http://stackoverflow.com/questions/80476/how-to-concatenate-two-arrays-in-java
        '''
    if lang in ["JavaScript", "CoffeeScript"]:
        firstElement = arrayOfArrays[0]
        arrayOfArrays = arrayOfArrays[1:len(arrayOfArrays)]
        return firstElement + ".concat(" + ", ".join(arrayOfArrays) + ")"
    if lang in ["REBOL"]:
        lastElement = arrayOfArrays[len(arrayOfArrays)-1]
        arrayOfArrays = arrayOfArrays[0:len(arrayOfArrays) - 1]
        return "append " + " append ".join(arrayOfArrays) + " " + lastElement
    if lang in ["C#"]:
        firstElement = arrayOfArrays[0]
        toReturn = "(" + ").Concat(".join(arrayOfArrays)+").ToArray()"
        return toReturn
    elif lang in ["Common Lisp"]:
        return "(append "+" ".join(arrayOfArrays)+")"
    elif lang in ["Clojure"]:
        return "(concat "+" ".join(arrayOfArrays)+")"
        
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def getJavaInitializer(lang, theArray, opening, closing, comma):
    if isinstance(theArray,list):
        toReturn = opening
        i=0
        while i < len(theArray):
            toReturn += getJavaInitializer(lang, theArray[i], opening, closing, comma)
            if i < (len(theArray)-1):
                if lang in "REBOL,Red,Polish notation".split(","):
                    toReturn += " "
                else:
                    toReturn += comma
            i = i + 1
        toReturn += closing
        return toReturn
    else:
        return str(theArray)

def getArrayInitializer(lang, arrayObject):
    arrayObject = [getVariableName(lang, x) for x in arrayObject]
    
    if lang in "Java,C#,Go,Lua,C++,C,Visual Basic .NET,Visual Basic".split(","):
        return getJavaInitializer(lang=lang,opening="{", closing="}", theArray = arrayObject, comma = ",")
    if lang in "Python,Cython,Groovy,Dart,TypeScript,CoffeeScript,Nemerle,JavaScript,Haxe,Haskell,Ruby,REBOL,Polish notation,Swift".split(","):
        return getJavaInitializer(lang=lang, opening="[", closing="]", theArray = arrayObject, comma = ",")
    elif lang in ["PHP"]:
        return getJavaInitializer(lang=lang, opening="array(", closing=")", theArray = arrayObject, comma = ",")
    elif lang in ["Scala"]:
        return getJavaInitializer(lang=lang, opening="Array(", closing=")", theArray = arrayObject, comma = ",")
    elif lang in ["Perl"]:
        return getJavaInitializer(lang=lang, opening="(", closing=")", theArray = arrayObject, comma = ",")
    elif lang in ["F#"]:
        return getJavaInitializer(lang=lang, opening="[|", closing="|]", theArray = arrayObject, comma = ";")
    elif lang in ["crosslanguage"]:
        return crossLanguageStatement("getArrayInitializer", [arrayObject])
    notYetDefinedError(lang, inspect.stack()[0][3])

initializerList = getArrayInitializer

def startConstructor(lang, className, parameterNames, parameterTypes):
    parameterList = getParameterList(lang=lang, parameterNames=parameterNames, parameterTypes=parameterTypes);
    if lang == "Python":
        return "def __init__("+"self, "+parameterList+"):"
    if lang in ["TypeScript"]:
        return "constructor("+parameterList+") {"
    if lang in ["Java", "C#", "Vala", "Groovy"]:
        return "public " + className+"("+parameterList+"){"
    if lang in ["Dart", "C++"]:
        return className+"("+parameterList+"){"
    if lang == "JavaScript":
        return ""
    if lang == "PHP":
        return "public function __construct("+parameterList+")"
    if lang == "Haxe":
        return "public function new("+parameterList+") {"
    if lang == "Ruby":
        return "def initialize(" + parameterList + ")"
    if lang == "CoffeeScript":
        return "constructor: ("+parameterList+") ->"
    if lang in ["Scala"]:
        return ""
    if lang in ["REBOL"]:
        return "new: func ["+parameterList+"] [ make self ["
    notYetDefinedError(lang, inspect.stack()[0][3])
    
def endConstructor(lang):
    if lang == "JavaScript":
        return ""
    elif lang in ["Java", "Dart", "Haxe", "C++", "CoffeeScript", "TypeScript", "Ruby", "Vala", "C#", "Python", "PHP", "crosslanguage"]:
        return endCodeBlock(lang)
    elif lang in ["Scala", "Groovy"]:
        return ""
    elif lang in "REBOL":
        return "] ]"
    notYetDefinedError(lang, inspect.stack()[0][3])
    

def constructor(lang, className, parameterNames, parameterTypes, body):
    if not className.startswith("engScript_"):
        className = "EngScript_"+className
    
    toAdd = []
    if lang in ["Scala", "JavaScript"]: #Scala doesn't use constructors
        return ""
    elif lang in ["Perl"]:
        return '''
                sub new {
                my ($class, %args) = @_;
                return bless { %args }, $class;
                }
                '''
    body = concatenateAllElements(body)
    body = toAdd + body
        

    body = [indent(i) for i in body]
    #raise Exception(body)
    body = [startConstructor(lang, className, parameterNames, parameterTypes)] +body+ [endConstructor(lang)]
    return body

def startCase(lang, condition):
    condition = getVariableName(lang, condition)
    toReturn=""
    if lang == "Racket":
        if condition.startswith("(") == False:
            condition = "("+condition+")"
        return "[" + condition
    if lang in "Common Lisp,Clojure".split(","):
        return "(" + condition
    if lang == "Scala":
        toReturn = "case @condition =>"
    if lang in ["Erlang"]:
        return startIf(lang, condition)
    if lang in "Dart,D,TypeScript,Hack,Swift,JavaScript,C#,Java,Groovy,C++,PHP,C,Go,Haxe,AWK,Vala".split(","):
        toReturn = "case @condition:"
    if lang in ["REBOL"]:
        toReturn = "@condition ["
    if lang in ["Fortran"]:
        toReturn = "case (@condition)"
    if lang in ["Ceylon"]:
        toReturn = "case (@condition){"
    if lang in ["crosslanguage"]:
        toReturn = "(case @condition"
    if lang in ["Visual Basic", "AutoIt", "Visual Basic .NET","OpenOffice Basic"]:
        toReturn = "Case @condition"
    if lang in ["Ruby","CoffeeScript"]:
        toReturn = "when @condition"
    if lang in ["COBOL"]:
        toReturn = "WHEN @condition"
    if lang in ["Haskell"]:
        toReturn = "@condition ->"
    if lang in ["Bash"]:
        toReturn = "@condition)"
    if acs(lang, "Tcl,PowerShell"):
        toReturn = "@condition {"
    if lang in ["OCaml", "F#"]:
        toReturn = "| @condition ->";
    if lang in ["Octave"]:
        toReturn = "case @condition"
    if lang in ["Fortran"]:
        toReturn = "CASE (@condition)"
    if lang in ["Gambas"]:
        toReturn = "CASE @condition"
    if lang in ["Nimrod"]:
        toReturn = "of @condition:"
    if toReturn == "":
        notYetDefinedError(lang = lang, functionName = inspect.stack()[0][3])
    else:
        return stringInterpolation(toReturn, "@condition", [condition])
    
def endCase(lang):
    #This should not enable fall-through.
    if lang in ["C#", "PHP", "D", "JavaScript","TypeScript", "Java", "AWK", "Vala", "Dart"]:
        return "break;"
    if lang in ["crosslanguage", "CoffeeScript", "REBOL", "Common Lisp"]:
        return endCodeBlock(lang);
    if lang in "COBOL,Clojure,Gambas,Nimrod,AutoIt,OpenOffice Basic,Octave,Hack,F#,Swift,Groovy,Scala,OCaml,Ada,Ruby,C++,PHP,C,Go,Haskell,Haxe,Visual Basic,Visual Basic .NET,Fortran".split(","):
        return ""
    if lang in ["Erlang"]:
        return ";"
    if lang in ["Bash"]:
        return ";;"
    if lang in ["Tcl", "Ceylon", "PowerShell"]:
        return "}"
    if lang in ["Racket"]:
        return "]"
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def case(lang, condition, body):
    body = concatenateAllElements(body)
        
    body = [indent(i) for i in body]
    body = [startCase(lang, condition)] +body+ [endCase(lang)]
    return body

def startDefault(lang):
    if lang in "JavaScript,C,D,TypeScript,Swift,Groovy,Dart,Java,C#,C++,Haxe,Hack,PHP,AWK,Vala,Go".split(","):
        return "default:"
    if lang in ["Fortran"]:
        return "case default"
    if lang in ["crosslanguage"]:
        return "(default"
    elif lang in ["Scala"]:
        return "_ =>"
    elif lang in ["Haskell", "Erlang"]:
        return "_ ->"
    elif lang in ["OCaml", "F#"]:
        return "| _ ->"
    if lang in ["Visual Basic", "Visual Basic .NET", "OpenOffice Basic"]:
        return "Case Else"
    if lang in ["Bash"]:
        return "*)"
    if lang in ["Ruby", "CoffeeScript"]:
        return "else"
    if lang in ["Nimrod"]:
        return "else"
    if lang in ["Ceylon"]:
        return "else{"
    if lang in ["Tcl"]:
        return "default"
    if lang in ["REBOL"]:
        return "] ["
    if lang in ["Racket"]:
        return "[else"
    if lang in ["Common Lisp"]:
        return "(otherwise"
    if lang in ["Octave"]:
        return "otherwise"
    if acs(lang, "PowerShell"):
        return "default {"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    
def endDefault(lang):
    if lang in "Dart,Nimrod,OpenOffice Basic,D,TypeScript,Octave,C,Tcl,Hack,Common Lisp,F#,Swift,Groovy,Scala,JavaScript,OCaml,REBOL,Erlang,Java,Vala,C#,C++,Haxe,Haskell,PHP,Go,Visual Basic,Visual Basic .NET,Ruby,Fortran,AWK".split(","):
        return ""
    if lang in ["Bash"]:
        return ";;"
    if acs(lang, "Ceylon,PowerShell"):
        return "}"
    if lang in ["Racket"]:
        return "]"
    if lang in ["crosslanguage", "CoffeeScript"]:
        return endCodeBlock(lang)
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def default(lang, body):
    body = concatenateAllElements(body)
        
    body = [indent(i) for i in body]
    body = [startDefault(lang)] +body+ [endDefault(lang)]
    return body

def instanceVariable(lang, variableName, className):
    variableName = getVariableName(lang, variableName)
    if lang in "Java,Dart,Groovy,TypeScript,JavaScript,C#,C++,Haxe".split(","):
        return "this."+variableName
    elif lang in "Python".split(","):
        return "self."+variableName
    elif lang in "REBOL".split(","):
        return "self/"+variableName
    elif lang in "Ruby,CoffeeScript".split(","):
        return "@"+variableName
    elif lang in "Swift,Scala".split(","):
        return variableName
    elif lang in "PHP".split(","):
        return "$this->" + removeInitialDollarSign(variableName)
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def startSwitch(lang, variableToCheck):
    variableToCheck = getVariableName(lang, variableToCheck)
    toReturn=""
    if lang in ["Scala"]:
        toReturn= variableToCheck + " match {"
    if lang in "JavaScript,PowerShell,Nemerle,D,TypeScript,Hack,Swift,Groovy,Dart,AWK,C#,Java,C++,PHP,C,Go,Haxe,Vala".split(","):
        toReturn= "switch($variableToCheck){"
    if lang in ["crosslanguage"]:
        toReturn= "(switch $variableToCheck"
    if lang in ["Ceylon"]:
        toReturn= "switch($variableToCheck)"
    if lang in ["Tcl"]:
        toReturn= "switch $variableToCheck {"
    if lang in ["REBOL"]:
        toReturn= "switch/default $variableToCheck ["
    if lang in ["F#"]:
        toReturn= "match ($variableToCheck) with"
    if lang in ["Haskell", "Erlang"]:
        toReturn= "case $variableToCheck of"
    if lang in ["Nimrod"]:
        toReturn= "case($variableToCheck) of"
    if lang in ["Cobra"]:
        toReturn= "branch $variableToCheck"
    if lang in ["Ruby"]:
        toReturn= "case $variableToCheck"
    if lang in ["Bash"]:
        toReturn= "case $variableToCheck in"
    if lang in ["Visual Basic", "Visual Basic .NET", "OpenOffice Basic"]:
        toReturn= "Select Case $variableToCheck"
    if lang in ["OCaml"]:
        toReturn= "match $variableToCheck with"
    if lang in ["AutoIt"]:
        toReturn= "Switch $variableToCheck"
    if lang in ["CoffeeScript"]:
        toReturn= "switch $variableToCheck"
    if lang in ["COBOL"]:
        toReturn= "EVALUATE $variableToCheck"
    if lang in ["Octave"]:
        toReturn= "switch ($variableToCheck)"
    if lang in "Racket,Common Lisp".split(","):
        toReturn= "(case $variableToCheck"
    if lang in "Fortran".split(","):
        toReturn= "SELECT CASE ($variableToCheck)"
    if lang in "Gambas".split(","):
        toReturn= "SELECT CASE $variableToCheck"
    if lang in "Puppet".split(","):
        toReturn = "case $variableToCheck {"
    if lang in "Clojure".split(","):
        toReturn= "(case $variableToCheck"
    if toReturn == "":
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    else:
        return stringInterpolation(toReturn, "variableToCheck", [variableToCheck])

def endSwitch(lang):
    if lang in "C,PowerShell,Nimrod,Hack,Clojure,Puppet,D,TypeScript,Racket,Common Lisp,F#,Dart,Swift,Groovy,Scala,JavaScript,REBOL,crosslanguage,Nemerle,AWK,Ruby,Vala,Haskell,C#,Java,C++,PHP,Go,Haskell,Haxe,Ruby,Tcl".split(","):
        return endCodeBlock(lang)
    elif lang in ["Visual Basic","Visual Basic .NET", "OpenOffice Basic"]:
        return "End Select"
    elif lang in ["Bash"]:
        return "esac"
    elif lang in ["Ada"]:
        return "end case;"
    elif lang in ["Erlang"]:
        return "end"
    elif lang in ["AutoIt"]:
        return "EndSwitch"
    elif lang in ["COBOL"]:
        return "END-EVALUATE"
    elif lang in ["Octave"]:
        return "endswitch"
    elif lang in ["OCaml", "CoffeeScript", "Ceylon"]:
        return ""
    elif lang in "Fortran,Gambas".split(","):
        return "END SELECT"
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def Switch(lang, condition, body):
    body = concatenateAllElements(body)
        
    body = [indent(i) for i in body]
    body = [startSwitch(lang, condition)] +body+ [endSwitch(lang)]
    return body

def initializeEmptyArray(lang, variableType, variableName, arrayStarter, arrayDimensions):
    try:
        if lang in ["Python"] :
            return "numpy.empty(" + call(function = "", parameters = arrayDimensions, fromClass=None)+")"
        if lang in ["Java"]:
            return variableType + arrayStarter + " " + variableName + " = new " + getArrayAccessor(arrayName=variableType, indexList = arrayDimensions)
        if lang in ["JavaScript"] :
            return "var " + variableName+" = "+callFunction(function="createArray", parameters=arrayDimensions, fromClass=None)
        if lang in ["C#"] :
            return variableType +"["+arrayStarter+"] " + variableName + " = new " + getArrayAccessor(arrayName=variableType, indexList = arrayDimensions)
        if lang in ["crosslanguage"]:
            return crossLanguageStatement("initializeEmptyArray", [variableType, variableName, arrayStarter, arrayDimensions])
    except Exception:
        raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + " and the dimensions " + str(arrayDimensions))
    finally:
        return "None"
    
def initializeArrayWithValue(lang, variableType, arrayStarter, variableName, initialValue, arrayDimensions):
    if type(initialValue) == list:
        arrayDimensions = list(numpy.shape(initialValue))
        initialValue = initializerList(lang=lang, arrayObject=initialValue)

    if arrayStarter == None:
        arrayStarter = ""
    
    
    if lang in ["Perl"]:
        return addInitialAtSign(variableName) + " = " + initialValue + ";"
    if lang in ["crosslanguage"]:
        return crossLanguageStatement("initializeArrayWithValue", [variableType, arrayStarter, variableName, initialValue, arrayDimensions])
    if lang in ["Java"]:
        return variableType + arrayStarter + " " + variableName + " = "+ initialValue
    if lang in ["Swift"] :
        return "var " + variableName + ": " + variableType + arrayStarter + " = "+ initialValue
    if lang in ["Python", "Lua", "Ruby", "PHP"]:
        return variableName + " = "+ initialValue
    if lang in ["REBOL"]:
        return variableName + ": "+ initialValue
    if lang in ["Haskell"]:
        return "let " + variableName + " = "+ initialValue
    if lang in ["JavaScript", "Haxe"]:
        return "var " + variableName + " = "+ initialValue
    if lang in ["C#"]:
        variableType = variableType.replace("[]", "")
        return variableType+"["+arrayStarter+"] "+variableName+" = new " + accessArray(lang=lang, arrayName=variableType, indexList=arrayDimensions) + initialValue
    if lang in ["C++", "C"]:
        #raise Exception(variableType)
        return variableType.replace("[]", "")+" "+variableName+arrayStarter+" = " + initialValue
    if lang in ["Go"]:
        #raise Exception(variableType)
        return  "var "+variableName+" = " + variableType.replace("[]", "")+arrayStarter+initialValue
    if lang in ["Visual Basic"]:
        #raise Exception(variableType)
        return  "Dim "+variableName+" = " + initialValue
    if lang in ["F#"]:
        return "let "+variableName+" = " + initialValue
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + ", the dimensions " + str(arrayDimensions) + ", and the initial value " + str(initialValue))


def getArrayStarter(lang, arrayDimensions):
    arrayStarter = ""
    if type(arrayDimensions) is list:
        arrayDimensions = [str(i) for i in arrayDimensions]
        if lang in ["C", "C++", "Go"]:
            arrayStarter = "[" + "][".join(arrayDimensions) + "]";
            #raise Exception(arrayStarter)
        else:
            for i in arrayDimensions :
                if lang == "Java":
                    arrayStarter += "[]"
                if lang == "C#":
                    arrayStarter += ","
        if lang == "C#":
            arrayStarter = arrayStarter[1:len(arrayStarter)]
    return arrayStarter

def initializeDictionary2(lang, initialValue):
    initialValue = getVariableName(lang, initialValue)
    if lang in ["Ruby", "Python", "Dart", "JavaScript", "CoffeeScript", "Haxe"]:
        return "{" + ", ".join(initialValue) + "}"
    elif lang in ["Scala"]:
        return "Map(" + ", ".join(initialValue) + ")"
    elif lang in ["Groovy"]:
        return "[" + ", ".join(initialValue) + "]"
    elif lang in ["REBOL"]:
        return "to-hash ["+" ".join(initialValue)+"]"
    elif lang in ["Perl", "Perl 6"]:
        return "(" + ", ".join(initialValue) + ")"
    elif lang in ["PHP"]:
        return "array(" + ", ".join(initialValue) + ")"
    elif lang in ["Java"]:
        return "new HashMap<String, String>();\n" + ";\n".join(initialValue)
    notYetDefinedError(lang, inspect.stack()[0][3]);

def initializeDictionary(lang, dictName, initialValue):
    dictName = getVariableName(lang, dictName)
    initialValue = getVariableName(lang, initialValue)
    
    theDict = initializeDictionary2(lang, initialValue)
    
    if lang in "Ruby,Python,CoffeeScript,Groovy,PHP".split(","):
        return dictName + " = " + theDict
    if lang in ["Dart", "JavaScript"]:
        return "var " + dictName + " = " + theDict
    if lang in ["Haxe"]:
        return dictName + " = " + theDict
    elif lang in ["Perl"]:
        return "%"+dictName + " = " + theDict
    elif lang in ["Scala"]:
        return "var "+dictName + " = " + theDict
    elif lang in ["Java"]:
        return "Map<String, String> " + dictName + " = " + theDict
    elif lang in ["REBOL"]:
        return dictName+": " + theDict
    notYetDefinedError(lang, inspect.stack()[0][3]);


def initializeVar(lang, variableName, variableType, initialValue, arrayDimensions=None):
    #if lang == "C" and getCorrespondingType(variableType) == "char[]":
    #    raise Exception("derp")
    
    if variableType in ["dict", "dictionary"]:
        return initializeDictionary(lang, variableName, initialValue)
    
    if type(initialValue) is list:
        arrayDimensions = list(numpy.shape(initialValue))
    
    if initializationRequiresType(lang) and "[]" in getCorrespondingType(lang, variableType):
        return initializeArrayWithValue(lang=lang, variableType=variableType, arrayStarter=getArrayStarter(lang, arrayDimensions), variableName=variableName, initialValue=initialValue, arrayDimensions=arrayDimensions)
    if arrayDimensions in ["None"]:
        arrayDimensions = None
    
    #raise Exception(variableName)
    if type(variableName) != str:
        raise Exception("This is a function declaration, not a variable declaration.")
    
    if initializationRequiresType(lang) == True:
        variableType = getCorrespondingType(lang=lang, theType=variableType)
    
    variableName = getVariableName(lang, variableName)
    
    if arrayDimensions == 0:
        arrayDimensions = None;
    arrayStarter = getArrayStarter(lang, arrayDimensions)
    
    
    if type(initialValue) is list:
        initialValue = initializerList(lang, initialValue)
    if type(initialValue) is int:
        initialValue = str(initialValue)
    '''
    to do: if initialValue is a list, then convert it to a string using initializerList
    '''
    
    
    '''if the type isn't an array:'''
    if arrayDimensions==None:
        return initializeScalar(lang=lang, variableType=variableType, variableName=variableName, initialValue=initialValue)
        '''If the initial value is not defined:'''
    elif (type(arrayDimensions) is list) & (initialValue == None):
        return initializeEmptyArray(arrayDimensions=arrayDimensions, variableType=variableType, variableName=variableName, arrayStarter = arrayStarter)
        '''If the initial value is defined:'''
    elif (type(arrayDimensions) is list) and type(initialValue) is str:
        return initializeArrayWithValue(lang=lang, variableType=variableType, arrayStarter=getArrayStarter(lang, arrayDimensions), variableName=variableName, initialValue=initialValue, arrayDimensions=arrayDimensions)
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + str(variableType) + ", the dimensions " + str(arrayDimensions) + ", and the initial value " + str(initialValue))


def initializationRequiresType(lang):
    '''
    Return true if a variable initialization must include the type of the variable, and return false otherwise.
    '''
    if lang in "Dart,OpenOffice Basic,Hack,Cython,ALGOL 68,Scala,Ceylon,D,TypeScript,Fortran,C++,Delphi,Swift,Cobra,Java,C#,C,Visual Basic,Visual Basic .NET,Vala,crosslanguage".split(","):
        return True
    elif acs(lang, "Common Lisp,Hy,AutoHotKey,OCaml,Scala,Clojure,Nemerle,Rust,CoffeeScript,Octave,AutoHotKey,AWK,Gosu,Groovy,Python,F#,Go,AutoIt,Julia,REBOL,Erlang,Haxe,Lua,JavaScript,Ruby,Bash,PHP,Haskell,Racket,Tcl,R,bc,Perl"):
        return False
    notYetDefinedError(lang, inspect.stack()[0][3]);

def initializeScalar(lang, variableType, variableName, initialValue):
    #See also: setvar
    variableName = getVariableName(lang, variableName)
    initialValue = getVariableName(lang, initialValue)
    if(initializationRequiresType(lang)):
        theCorrespondingType = getCorrespondingType(lang=lang, dimension=None, theType = variableType)
    if initialValue in ["None", None]:
        raise Exception("The initial value should not be None")
    '''initialValue is not None here'''
    if acs(lang,"Python,PowerShell,Hy,CoffeeScript,Octave,Julia,REBOL,PHP,Hack,Cobra,R"):
        return setVar(lang=lang, valueToGet = initialValue, valueToChange = variableName)
    elif lang in "Lua,Ruby,bc,Perl,AWK,Erlang,AutoIt".split(","):
        return variableName + " = " + initialValue
    elif lang in ["Cython"]:
        return "cdef " + variableType + " " + variableName + " = " + initialValue
    elif lang in ["Tcl"]:
        return "set " + removeInitialDollarSign(variableName) + " " + initialValue
    elif lang in ["Fortran"]:
        return variableType + " :: " + variableName + " = " + initialValue
    elif lang in ["Bash"]:
        return "local "+variableName[1:len(variableName)]+"="+initialValue
    elif lang in ["Go", "AutoHotKey"]:
        return variableName + " := " + initialValue
    elif lang in "Java,ALGOL 68,Ceylon,D,C#,C,C++,Vala".split(","):
        return theCorrespondingType +" "+ variableName + " = " + initialValue
    elif lang in ["crosslanguage"]:
        return "(initialize " + getCorrespondingType(lang, variableType) +" "+ variableName +" "+ initialValue+")"
    elif lang in ["Sibilant,LispyScript"]:
        return "(var " + variableName+" "+initialValue+")"
    elif lang in ["JavaScript", "TypeScript", "Scala", "Dart", "Swift", "Gosu"]:
        return "var " + variableName + " = " + initialValue
    elif lang in ["Haxe", "Nimrod"]:
        return "var " + variableName + ": " + variableType + " = " + initialValue
    elif lang in ["Groovy"]:
        return "def " + variableName + " = " + initialValue
    elif lang in ["Haskell", "OCaml"]:
        return "let " + variableName + " = " + initialValue
    elif lang in ["F#"]:
        return "let mutable " + variableName + " = " + initialValue
    elif lang in ["Nemerle"]:
        return "def " + variableName + " = " + initialValue
    elif lang in ["Visual Basic","Visual Basic .NET", "OpenOffice Basic"]:
        return "Dim "+variableName+" As "+getCorrespondingType(lang, variableType)+" = "+initialValue
    elif lang in ["Common Lisp"]:
        return "(setf "+variableName+" "+initialValue+")"
    raise EngScriptException(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " with the type " + variableType + " and the initial value " + str(initialValue))

def typeConversion(lang, objectToConvert, convertFrom, convertTo):
    objectToConvert = getVariableName(lang, objectToConvert)
    convertFrom = getCorrespondingType(lang=lang, theType = convertFrom)
    convertTo = getCorrespondingType(lang=lang, theType = convertTo)
    if convertFrom == convertTo:
        return objectToConvert;
    if lang in "crosslanguage":
        return "(convert " + objectToConvert +" from "+ convertFrom +" to "+ convertTo + ")"
    if lang in ["JavaScript"]:
        if convertTo in ["string"]:
            return objectToConvert + ".toString()"
        if convertFrom in ["string"]:
            if convertTo in ["number"]:
                return "parseFloat(" + objectToConvert + ")"
    if lang in ["Python"]:
        if convertTo in ["str"]:
            return "str("+str(objectToConvert) + ")"
        if convertTo in ["int"]:
            return "int("+str(objectToConvert) + ")"
    if lang in ["Java"]:
        if convertTo in "String":
            return objectToConvert + ".toString()"
        if convertTo == "int":
            if convertFrom == "String":
                return "Integer.parseInt("+objectToConvert+")"
    if lang in ["C#"]:
        if convertTo == "int":
            if convertFrom == "string":
                return "Convert.ToInt32("+objectToConvert+")"
        if convertTo == "string":
            if convertFrom == "int":
                return objectToConvert+".ToString()"
    if lang in ["Haskell"]:
        if convertTo == getCorrespondingType("string"):
            if convertFrom == getCorrespondingType(lang, "int"):
                return "show("+objectToConvert+")"
    if lang in ["PHP"]:
        if convertFrom == getCorrespondingType(lang, "string"):
            if convertTo == getCorrespondingType(lang, "int"):
                return "(int)"+objectToConvert
        if convertTo == getCorrespondingType(lang, "string"):
            if convertFrom == getCorrespondingType(lang, "int"):
                return "(string)"+objectToConvert
    if lang in ["Perl"]:
        stringType = getCorrespondingType(lang, "string")
        intType = getCorrespondingType(lang, "int")
        if convertFrom in [intType, stringType] and convertTo in [intType, stringType]:
            return objectToConvert
            
    raise Exception(inspect.stack()[0][3] + " is not yet defined for " + str(lang) + " from the type " + convertFrom + " to the type " + convertTo);

def toString(lang, objectToConvert, convertFrom):
    return typeConversion(objectToConvert=objectToConvert, convertFrom=convertFrom, convertTo="String")

def subString(lang, aString, start, end):
        aString = getVariableName(lang, aString)
        start = getVariableName(lang, start)
        end = getVariableName(lang, end)
        if lang in "JavaScript,CoffeeScript,TypeScript,Java,Scala,Dart".split(","):
            return aString + ".substring(" + start + ", " + end + ")"
        elif lang in "C++".split(","):
            return aString + ".substr(" + start + ", " + end + " - "+start + ")"
        elif lang in "Vala".split(","):
            return aString + ".substr(" + start + ", " + end + " - "+start + ")"
        elif lang in "crosslanguage".split(","):
            return "(substring " + aString + " " + start + " " + end + ")"
        elif lang in "C#,Visual Basic .NET,Nemerle".split(","):
            return aString + ".Substring(" + start + ", " + end + ")"
        elif lang in "Lua".split(","):
            return "string.sub(" + aString + ", " + start + ", " + end + ")"
        elif lang in "Tcl".split(","):
            return "[string range " + aString + " " + start + ' ' + end + "]"
        elif lang in "Ruby,Pike,Groovy".split(","):
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
        elif lang in "Common Lisp".split(","):
            return "(subseq " + aString + " " + start + " " + end + ")"
        elif lang in "Erlang".split(","):
            return "string:sub_string("+aString+", "+start+", "+end+")"
        elif lang in "Clojure".split(","):
            return "(subs " + aString +" "+ start +" "+ end + ")"
        elif lang in "REBOL".split(","):
            return "copy/part skip "+aString+" "+start+" "+end
        notYetDefinedError(lang, inspect.stack()[0][3])
    
'''
def subString(string, start, end):
    if(lang in ["JavaScript", "Java"]):
        return string + ".substring("+start+", " + end + ")";
    if(lang in ["Python", "Go"]):
        return string + "["+ start +":"+ end +"]";

    
    notYetDefinedError(functionName = inspect.stack()[0][3]);
'''

def newObject(lang, objectName, objectType, functionCall):
    objectName = getVariableName(lang, objectName)
    '''
    Create a new instance of an object.
    Refer to the implementation of callFunction when implementing this.
    '''    
    if lang in ["Java", "C#"]:
        return objectName +" "+ objectType + " = new " + functionCall
    if lang in ["JavaScript", "Haxe", "TypeScript", "Groovy", "Scala", "Dart"]:
        return "var "+ objectName + " = new " + functionCall
    if lang in ["CoffeeScript", "PHP"]:
        return objectName + " = new " + functionCall
    if lang in ["Python"]:
        return objectName + " = " + functionCall
    if lang in ["Ruby"]:
        return objectName + " = " + functionCall.replace(objectType, objectType+".new", 1)
    if lang in ["C++"]:
        return objectType + " " + functionCall.replace(objectType, objectName, 1)
    if lang in "REBOL":
        return objectName + ": " + functionCall.replace(objectType, objectType+"/new", 1)
    notYetDefinedError(lang, inspect.stack()[0][3])

def initializePrivateMember(lang, variableName, variableType, initialValue=None, arrayDimensions=None):
    variableType = getCorrespondingType(lang, variableType)
    variableName = getVariableName(lang, variableName)
    '''
        This method declares an instance variable in each language.
    '''
    if initialValue in ["None", None]:
        if lang in "C++,Dart".split(","):
            return variableType +" "+ variableName
        if lang in "Java,Groovy,C#".split(","):
            return "private " + variableType +" "+ variableName
        if lang in "Python,REBOL,Ruby,Scala,CoffeeScript".split(","):
            return ""
        if lang in "Haxe".split(","):
            return "var " + variableName + " : "+variableType
        if lang in "PHP".split(","):
            return "var " + variableName
        if lang in "JavaScript".split(","):
            return "this." + variableName + " = " + variableName
        if lang in ["TypeScript"]:
            return variableName + ": " + variableType
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    else:
        initialization = initializeVar(lang, variableName, variableType, initialValue, arrayDimensions)
        if lang in ["Java", "C#", "Vala"]:
            return "private "  + initialization
        if lang in ["PHP"]:
            return "private " + initialization
        '''in Python, it doesn't need to be declared'''
        if lang in ["Python"]:
            return "self."+initialization
        if lang in ["JavaScript"]:
            return "this."+initialization
        if lang in ["Ruby"]:
            return "@"+initialization
        if lang in ["Scala", "Swift", "C++", "REBOL", "Haxe", "Groovy", "Dart"]:
            return initialization
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def endFor(lang, increment):
    increment = getVariableName(lang, increment)
    "Do this for all languages that have a while loop but not a for loop"
    if lang in "Python,REBOL,Lua,Haxe,CoffeeScript,Ruby,Octave,Scala".split(","):
        return "    " + increment + "\n" + endWhile(lang)
    elif lang in "C,Groovy,Dart,TypeScript,Java,JavaScript,C#,crosslanguage,Go,C++,Perl,PHP".split(","):
        return endCodeBlock(lang)
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    
def indexOf(lang, string, substring):
    string = getVariableName(lang,string)
    substring = getVariableName(lang,substring)
    '''
    Should return the index if present, and -1 otherwise.
    '''
    toReturn=""
    if lang in ["JavaScript","Java","CoffeeScript"]:
        toReturn= "$string.indexOf($substring)"
    elif lang in ["Ruby"]:
        toReturn= "$string.index($substring)"
    elif lang in ["C#"]:
        toReturn= "$string.IndexOf($substring)";
    elif lang in ["Python"]:
        toReturn= "$string.find($substring)";
    elif lang in ["Go"]:
        toReturn= "strings.Index($string, $substring)"
    elif lang in ["PHP"]:
        toReturn= "strstr($string, $substring)"
    
    if toReturn == "":
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    else:
        return stringInterpolation(toReturn, "$string,$substring", [string, substring])

def startElse(lang):
        if lang in "Python,Cython,Nimrod".split(","):
            return "else:"
        elif lang in "Hack,PowerShell,Puppet,Ceylon,D,Rust,TypeScript,Scala,AutoHotKey,Gosu,Groovy,Java,Swift,Dart,AWK,JavaScript,Haxe,PHP,C#,Go,Perl,C++,C,Tcl,R,Vala,bc".split(","):
            return "else {"
        elif lang in "Ada,ALGOL 68,Julia,Bash,Ruby,CoffeeScript,Lua,Haskell,MATLAB,Octave,Gambas,OCaml,Fortran,F#,Oz,Nemerle".split(","):
            return "else"
        elif lang in "Delphi".split(","):
            return "else\nbegin"
        elif lang in "Racket,crosslanguage,Clojure,Hy".split(","):
            return "(else"
        elif lang in "Visual Basic,Visual Basic .NET,AutoIt,OpenOffice Basic".split(","):
            return "Else"
        elif lang in "COBOL".split(","):
            return "ELSE"
        elif lang in "Erlang".split(","):
            return "; true ->"
        elif lang in "REBOL".split(","):
            return "true ["
        elif lang in ["Prolog"]:
            return "";
        elif lang in "Common Lisp".split(","):
            return "(t"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def startElseIf(lang, condition):
        condition = getVariableName(lang, condition)
        if lang in "Common Lisp,Hy,Racket,Clojure".split(","):
            return startIf(lang, condition)
        if lang in "D,Ceylon,Scala,TypeScript,AutoHotKey,AWK,R,Groovy,Gosu,Java,Swift,Nemerle,C,Dart,Vala,JavaScript,C#,C++,Haxe".split(","):
            return "else if(" + condition + "){"
        elif lang in ["Delphi"]:
            return "else if " + condition + " then\nbegin"
        elif lang in "Go,Rust".split(","):
            return "else if " + condition + " {"
        elif lang in "Visual Basic,Visual Basic .NET,AutoIt".split(","):
            return "ElseIf " + condition + " Then"
        elif lang in "PHP,Hack,PowerShell".split(","):
            return "elseif(" + condition + "){"
        elif lang in "crosslanguage".split(","):
            return "elif " + condition
        elif lang in "MATLAB,Julia".split(","):
            return "elseif " + condition
        elif lang in "Python,Cython,Nimrod".split(","):
            return "elif " + condition + ":"
        elif lang in "F#,ALGOL 68".split(","):
            return "elif " + condition + " then"
        elif lang in "Perl".split(","):
            return "elsif(" + condition + "){"
        elif lang in "Puppet".split(","):
            return "elsif " + condition + " {"
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
        elif lang in "REBOL".split(","):
            return condition + " ["
        elif lang in "Tcl".split(","):
            return "elseif {" + condition + " } {"
        elif lang in ["Octave"]:
            return "elseif("+condition+")"
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def endElse(lang):
    if lang in "Hack,PowerShell,Hy,Cython,Clojure,Common Lisp,Ceylon,D,Rust,TypeScript,CoffeeScript,AutoHotKey,AWK,Gosu,C,Swift,Nemerle,REBOL,Groovy,Scala,Tcl,Dart,R,Vala,Python,F#,Java,JavaScript,Haxe,PHP,C#,crosslanguage,Perl,C++,Go,Haskell,Racket".split(","):
        return endCodeBlock(lang)
    elif lang in ["Delphi"]:
        return "end"
    elif lang in "COBOL,OpenOffice Basic,ALGOL 68,Ada,Julia,Prolog,Bash,AutoIt,Lua,Ruby,Visual Basic,Visual Basic .NET,Octave,MATLAB,Gambas,Fortran,Erlang".split(","):
        return ""
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def endElseIf(lang):
        if lang in "Hack,PowerShell,Hy,Cython,Clojure,Common Lisp,Ceylon,D,Rust,TypeScript,Scala,AutoHotKey,Gosu,Swift,REBOL,C,Nemerle,Groovy,CoffeeScript,Tcl,Vala,AWK,R,Python,F#,Java,Dart,JavaScript,Haxe,PHP,C#,crosslanguage,Perl,C++,Go,Racket".split(","):
            return endCodeBlock(lang)
        elif lang in "Ada,ALGOL 68,Julia,Bash,Lua,Ruby,AutoIt,Haskell,Visual Basic,Visual Basic .NET,MATLAB,Octave,Gambas,Fortran,OCaml,Erlang".split(","):
            return ""
        elif lang in "Delphi".split(","):
            return "end"
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);
def elseIf(lang, condition, body):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startElseIf(lang=lang, condition=condition)] +body+ [endElseIf(lang)]
    return body
    
def declareConstant(lang, variableType, arrayDimensions, variableName, initialValue):
    variableDeclaration = initializeVar(variableType=variableType, initialValue=initialValue, arrayDimensions=arrayDimensions, variableName=variableName)
    if lang in ["Python"]:
        return variableDeclaration
    if lang in ["Java"]:
        return "final " + variableDeclaration
    if lang in ["JavaScript"]:
        return variableDeclaration
    if lang in ["C#"]:
        return "Const " + variableDeclaration
    if lang in ["Go"]:
        return "Const " + variableDeclaration
    if lang in ["crosslanguage"]:
        return crossLanguageStatement()
    notYetDefinedError(functionName = inspect.stack()[0][3]);

def printSomething(lang):
    theIndentation = 0;
    print(getClassBeginning(className="Main"));
    theIndentation = theIndentation + 1;
    
    print(startMethod(isDefined = False, requiresTheFunctions=False, name = "testFunction", returnType="int", parameterNames=["thing1", "thing2"], parameterTypes=["int", "int"]));
    
    '''print(getComment(lang="Python", comment="Hi!", indent=theIndentation));'''
    
    theIndentation = theIndentation - 1;
    print(endClass());

def testStatementsInLanguage(arr):
    print("Testing statements in each language using " + inspect.stack()[0][3])
    i = 0;
    while(i < len(arr)):
        if arr[i] != arr[i+1]:
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
        if type(arr[i]) == str:
            arr[i] = [arr[i]]
        i += 1
    
    import itertools;
    arr = list(itertools.chain(*arr))
    newArr = []
    i=0
    while i < len(arr):
        if type(arr[i]) == str and (arr[i].strip() != ""):
            newArr += [arr[i]]
        if type(arr[i]) == list:
            newArr += arr[i]
        i = i + 1
    return newArr;

def include(lang, fileName):
    if lang in "Haskell,Java,Python,Haxe,Scala,Go,Groovy".split(","):
        return "import " + fileName
    elif lang in "Dart".split(","):
        return "import '" + fileName+".dart'"
    elif lang in "C#".split(","):
        return "using " + fileName
    elif lang in "Ruby,Lua".split(","):
        return "require '" + fileName + "'"
    elif lang in "crosslanguage".split(","):
        return "(include " + fileName + ")"
    elif lang in "JavaScript".split(","):
        return "var "+fileName + " = include('" + fileName + ".js')"
    elif lang in "C++".split(","):
        return '#include "'+fileName+'.h"'
    elif lang in "PHP".split(","):
        return "include '"+fileName+".php'"
    elif lang in "REBOL".split(","):
        return fileName+": load %"+fileName+".r"
    elif lang in "Perl".split(","):
        return "use "+fileName
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

'''
def include(fileName):
    '/''
    include is the file or class name, without the file extension.
    '/''
    if(lang in "VBScript"):
        return 'includeFile "'+fileName+'.vbi"'
    notYetDefinedError(functionName = inspect.stack()[0][3])
'''

def getClass(lang, className, parameterNames, parameterTypes, body):
    if not className.startswith("EngScript_"):
        className = "EngScript_"+className
    
    i = 0
    classBeginning = getClassBeginning(parameterNames=parameterNames, parameterTypes=parameterTypes,className=className,lang=lang)
    body = concatenateAllElements(body)
    if type(body) == str:
        body = [body]
    while i < len(body):
        if classBeginning != "":
            body[i] = indent(body[i])
        i = i + 1
    body = [classBeginning] +body+ [endClass(lang)]
    toReturn = ""
    i = 0
    while i < len(body):
        toReturn += body[i]+"\n";
        i = i + 1
    return toReturn



def methodRequiresReturnType(lang):
    '''
    Return true if the method requires a return type, and return false otherwise.
    '''
    if acs(lang, "Haskell,PowerShell,Hy,Gambas,OpenOffice Basic,CoffeeScript,Octave,Clojure,AutoHotKey,Julia,Groovy,Prolog,F#,Swift,Nemerle,ML,AutoIt,Dart,REBOL,Erlang,AWK,Python,JavaScript,Bash,PHP,Lua,Ruby,Perl,Racket,Common Lisp,R,Tcl,bc"):
        return False
    if acs(lang, "Java,OCaml,Cython,Rust,ALGOL 68,Ceylon,D,TypeScript,Fortran,Hack,Gosu,Scala,Pascal,Delphi,Pike,Objective-C,C++,C,C#,Go,Haxe,Visual Basic,Visual Basic .NET,crosslanguage,Vala"):
        return True
    notYetDefinedError(lang, inspect.stack()[0][3])

def endMethod(lang, methodName):
        if acs(lang, "bc,PowerShell,Hy,Hack,Cython,Ceylon,D,CoffeeScript,TypeScript,AutoHotKey,Julia,Gosu,Groovy,Swift,Pike,C,Dart,Tcl,Clojure,Scala,Nemerle,MATLAB,Vala,REBOL,Common Lisp,Emacs Lisp,AWK,R,C++,F#,PHP,Lua,Python,Java,JavaScript,C#,Haxe,Perl,crosslanguage,Ruby,Go,Racket"):
            return endCodeBlock(lang)
        elif lang in "Haskell,OCaml,ALGOL 68".split(","):
            return ""
        elif lang in "Erlang,Prolog".split(","):
            return "."
        elif lang in "Ada".split(","):
            return "end " + methodName + ";"
        elif lang in "ML".split(","):
            return "end"
        elif lang in "Delphi".split(","):
            return "end;"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "End Sub"
        elif lang in "OpenOffice Basic".split(","):
            return "End Function"
        elif lang in "Gambas".split(","):
            return "END"
        elif lang in "Bash".split(","):
            return "}"
        elif lang in "Octave".split(","):
            return "endfunction"
        elif lang in "AutoIt".split(","):
            return "EndFunc"
        elif lang in "Fortran".split(","):
            return "END FUNCTION " + methodName
        elif lang in "OCaml".split(","):
            return ";;"
        notYetDefinedError(lang, inspect.stack()[0][3]);

def getFunction(lang, functionName, isInstanceMethod, parameterNames, parameterTypes, returnType, body, isPublic=False, isStatic=False):
    if not functionName.startswith("engScript_"):
        functionName = "engScript_"+functionName
    
    #print("Parameter names: ", parameterNames)
    #print("Parameter types: ", parameterTypes)
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startMethod(lang=lang, isStatic=isStatic, isInstanceMethod=isInstanceMethod, returnType = returnType, name = functionName, parameterNames = parameterNames, parameterTypes = parameterTypes)] +body+ [endMethod(lang=lang, methodName=functionName)]
    return body


def startPublicMethod(lang, returnType, functionName, parameterNames, parameterTypes):
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3])

def endPublicMethod(lang, functionName):
    if lang in ["JavaScript"]:
        return endMethod(lang, functionName)
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3])


def publicMethod(lang, returnType, functionName, parameterTypes, parameterNames, body):
    return getFunction(lang=lang, parameterNames=parameterNames, parameterTypes=parameterTypes, returnType=returnType, functionName=functionName, body=body, isInstanceMethod=True)

def includeForLang(lang, langToInclude, body):
    if langToInclude == lang:
        '''body = concatenateAllElements(body)'''
        return body
    else:
        return "";
    
def forLoop(lang, initializer, condition, increment, body):
    if type(body) == str:
        body = body[0]
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startFor(lang=lang, initializer=initializer, condition=condition, increment=increment)] +body+ [endFor(lang=lang, increment=increment)]
    return body

def startConditionalBlock(lang):
    if lang in "TypeScript,PowerShell,Cython,ALGOL 68,Ceylon,D,Rust,COBOL,CoffeeScript,AutoHotKey,Julia,Gosu,Delphi,C,Swift,Nemerle,Groovy,AutoIt,Scala,Dart,Tcl,OCaml,bc,AWK,R,Octave,Ada,Gambas,Python,Java,JavaScript,C++,Bash,Haxe,Perl,Ruby,C#,Lua,PHP,Go,Haskell,F#,MATLAB,Visual Basic,Visual Basic .NET,Fortran,Vala".split(","):
        return "";
    if acs(lang, "Scheme,Racket,Common Lisp,Hy"):
        return "(cond"
    if lang in ["crosslanguage"]:
        return "cond"
    if lang in ["Erlang"]:
        return "if"
    if lang in ["Prolog"]:
        return "("
    if lang in ["REBOL"]:
        return "case ["
    if lang in ["Sibilant"]:
        return "(if-else"
    notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3])

def endConditionalBlock(lang):
    if lang in "REBOL,PowerShell,Cython,Hy,Common Lisp,AutoHotKey,Lua,Ruby,Scheme,Racket".split(","):
        return endCodeBlock(lang)
    if lang in "TypeScript,Ceylon,D,Rust,CoffeeScript,Gosu,C,Swift,Nemerle,Scala,Groovy,Tcl,OCaml,bc,R,Python,Java,Dart,C++,JavaScript,Haxe,Perl,C#,PHP,Go,Haskell,F#,AWK,Vala".split(","):
        return "";
    elif lang in ["Bash"]:
        return "fi"
    elif lang in ["ALGOL 68"]:
        return "fi;"
    elif lang in ["Prolog"]:
        return ")"
    elif lang in ["Delphi"]:
        return ";"
    elif lang in ["Octave"]:
        return "endif"
    elif lang in ["MATLAB", "Erlang", "Julia"]:
        return "end"
    elif lang in ["crosslanguage"]:
        return ")"
    elif lang in ["Visual Basic", "Visual Basic .NET"]:
        return "End If"
    elif lang in ["AutoIt"]:
        return "EndIf"
    elif lang in ["Gambas"]:
        return "ENDIF";
    elif lang in ["COBOL"]:
        return "END-IF";
    elif lang in ["Fortran"]:
        return "end if"
    elif lang in ["Ada"]:
        return "end if;"
    elif lang in ["Pascal"]:
        return "end if;"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def conditionalBlock(lang, body):
    body = concatenateAllElements(body)
    body = [startConditionalBlock(lang)] +body+ [endConditionalBlock(lang)]
    return body

def startMain(lang):
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
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def endMain(lang):
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
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def main(lang, body):
    i = 0
    body = concatenateAllElements(body)
    while i < len(body):
        if startMain(lang) != "":
            body[i] = indent(body[i])
        i = i + 1
    body = [startMain(lang)] +body+ [endMain(lang)]
    return body
    
def whileLoop(lang, body, condition):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startWhile(lang=lang,condition=condition)] +body+ [endWhile(lang)]
    return body
    
def startIf(lang, condition):
        condition = getVariableName(lang, condition)
        
        toReturn=""
        #use stringInterpolation here
        if lang in 'Python,Cython,Nimrod'.split(','):
            toReturn = 'if @condition:'
        elif lang in 'Common Lisp'.split(','):
            toReturn = '(@condition'
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            toReturn = 'If @condition'
        elif lang in 'AutoIt,OpenOffice Basic'.split(","):
            toReturn = 'If @condition Then'
        elif lang in 'Erlang,Prolog'.split(','):
            toReturn= '@condition ->'
        elif lang in 'REBOL'.split(","):
            toReturn= '@condition ['
        elif lang in 'Octave,CoffeeScript,Julia'.split(','):
            toReturn= 'if @condition'
        elif lang in "crosslanguage".split(','):
            toReturn= '(if @condition'
        elif lang in 'Racket,Clojure'.split(','):
            toReturn= '(@condition'
        elif lang in 'Hy'.split(','):
            toReturn= '[@condition'
        elif acs(lang, 'Java,PowerShell,D,Ceylon,TypeScript,ActionScript,Hack,AutoHotKey,Gosu,Nemerle,Swift,Nemerle,Pike,Groovy,Scala,Dart,JavaScript,C#,C,C++,Perl,Haxe,PHP,R,AWK,Vala,bc,Squirrel'):
            toReturn= 'if(@condition){'
        elif lang in 'Tcl'.split(','):
            toReturn= 'if{@condition}{'
        elif lang in 'Go,Rust'.split(','):
            toReturn= 'if @condition {'
        elif lang in 'Bash'.split(','):
            toReturn= 'if [ @condition ] then'
        elif lang in 'Fortran'.split(','):
            toReturn= "if (@condition) then"
        elif lang in 'Gambas'.split(','):
            toReturn= 'IF @condition THEN'
        elif lang in 'Haskell,ALGOL 68,OCaml,Lua,Ruby,F#'.split(','):
            toReturn= 'if @condition then'
        elif lang in "Delphi".split(","):
            toReturn = "If @condition then\nbegin"
        elif lang in "COBOL".split(","):
            toReturn = "IF @condition"
            
        if toReturn == "":
            notYetDefinedError(lang= lang, functionName = inspect.stack()[0][3]);
        else:
            return stringInterpolation(toReturn, "@condition", [condition])
def endIf(lang):
        if acs(lang, "C,PowerShell,Cython,Clojure,Common Lisp,D,Ceylon,Rust,TypeScript,Hack,Scala,AutoHotKey,Gosu,Swift,Nemerle,Groovy,CoffeeScript,bc,Tcl,REBOL,Vala,AWK,R,F#,Python,Java,Dart,JavaScript,C#,crosslanguage,C++,Perl,PHP,Go,Haxe,Haskell,Racket,Pike"):
            return endCodeBlock(lang)
        if lang in ["Delphi"]:
            return "end"
        elif lang in "COBOL,OpenOffice Basic,ALGOL 68,Ada,Julia,Erlang,Bash,AutoIt,Lua,Ruby,Octave,MATLAB,Gambas,Visual Basic,Visual Basic .NET,Fortran,OCaml".split(","):
            return ""
        elif acs(lang, "Hy"):
            return "]"
        elif lang in "Prolog".split(","):
            return ";"
        notYetDefinedError(lang=lang,functionName = inspect.stack()[0][3]);

def ifStatement(lang, condition, body):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startIf(lang=lang, condition=condition)] +body+ [endIf(lang)]
    return body

def getFileExtension(lang):
        if lang in "Lua".split(","):
            return "lua"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            return "vb"
        elif lang in "PowerShell".split(","):
            return "ps1"
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
        elif lang in "Perl,Perl 6".split(","):
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
        elif lang in "Groovy".split(","):
            return "groovy"
        elif lang in "Scala".split(","):
            return "groovy"
        elif lang in "Dart".split(","):
            return "groovy"
        elif lang in "CoffeeScript".split(","):
            return "coffee"
        elif lang in "Swift".split(","):
            return "swift"
        elif lang in "TypeScript".split(","):
            return "ts"
        elif lang in "ALGOL 68".split(","):
            return "a68"
        elif lang in "Common Lisp".split(","):
            return "lisp"
        elif lang in "LispyScript".split(","):
            return "ls"
        elif lang in "Clojure".split(","):
            return "clj"
        elif lang in "Cython".split(","):
            return "pyx"
        elif lang in "Hack".split(","):
            return "hh"
        elif lang in "OpenOffice Basic".split(","):
            return "mod"
        elif lang in "Gambas".split(","):
            return "gambas"
        elif lang in "Julia".split(","):
            return "jl"
        elif lang in "AutoIt".split(","):
            return "au3"
        elif lang in 'Nemerle'.split(","):
            return "n"
        elif lang in 'Oz'.split(","):
            return "oz"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def elseStatement(lang, body):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startElse(lang)] +body+ [endElse(lang)]
    return body

def getRegexMatches(string, regex):
    '''Return a string array of each regex match in the array.'''

def regexMatchesString(lang, aString, regex):
        if lang in "Python".split(","):
            return "re.compile(" + regex + ").match(" + aString + ")"
        if lang in "Java,Scala".split(","):
            return aString + ".matches(" + regex + ")"
        if lang in "C#".split(","):
            return regex + ".isMatch(" + aString + ")"
        if lang in "JavaScript,CoffeeScript".split(","):
            return "regex.test(" + aString + ")"
        elif lang in "Haxe".split(","):
            return regex+".match("+aString+")"
        elif lang in "PHP".split(","):
            return "(preg_match("+regex+", "+aString+")>0)"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);


def puts(lang, toPrint):
        toPrint = getVariableName(lang, toPrint)
        if lang in "Python,Cython,Ceylon,R,Gosu,Dart,Vala,Perl,PHP,AWK".split(","):
            return "print(" + toPrint + ")"
        if lang in "Hy".split(","):
            return "(print" + toPrint + ")"
        elif lang in "Rust".split(","):
            return "println!(toPrint)"
        elif lang in "C,Cython".split(","):
            return "printf(" + toPrint + ")"
        elif lang in "bc".split(","):
            return "print " + toPrint
        elif lang in ["OCaml"]:
            return getFunctionCall(lang=lang, function="print_string", parameters=["toPrint"], fromClass=None)
        elif lang in "Erlang".split(","):
            return "io:fwrite(" + toPrint + ")"
            
        elif lang in "Octave".split(","):
            return "printf(" + toPrint + ")"
        elif lang in "MATLAB".split(","):
            return "disp(" + toPrint + ")"
        elif lang in "Gambas".split(","):
            return "PRINT " + toPrint
        elif lang in "Racket".split(","):
            return "(display " + toPrint + ")"
        elif lang in "Common Lisp".split(","):
            return "(write " + toPrint + ")"
        elif lang in "Clojure".split(","):
            return "(println " + toPrint + ")"
        elif lang in "Haskell".split(","):
            return "putStr(" + toPrint + ")"
        elif lang in "Bash".split(","):
            return "(echo " + toPrint + ")"
        elif lang in "Nimrod".split(","):
            return "echo(" + toPrint + ")"
        elif lang in "REBOL".split(","):
            return "print " + toPrint
        elif lang in "C++".split(","):
            return "cout << " + toPrint
        elif lang in "JavaScript,CoffeeScript,TypeScript".split(","):
            return "console.log(" + toPrint + ")"
        elif lang in "Java,Groovy".split(","):
            return "System.out.println(" + toPrint + ")"
        elif lang in "C#,Nemerle".split(","):
            return "Console.WriteLine(" + toPrint + ")"
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
            return "trace(" + toPrint + ")"
        elif lang in "Go".split(","):
            return "fmt.Println(" + toPrint + ")"
        elif lang in "Scala".split(","):
            return "println(" + toPrint + ")"
        elif lang in "Lua".split(","):
            return "io.write(" + toPrint + ")"
        elif lang in "Pike".split(","):
            return "write(" + toPrint + ")"
        elif lang in "Julia,Swift".split(","):
            return "println(" + toPrint + ")"
        elif lang in "F#".split(","):
            return "printfn " + toPrint
        elif lang in "Pascal".split(","):
            return "WriteLn(" + toPrint + ")"
        elif lang in ["Delphi"]:
            return "ShowMessage(" + toPrint + ")"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def split(lang, string, separator):
        string = getVariableName(lang, string)
        separator = getVariableName(lang, separator)
        if lang in "JavaScript,CoffeeScript,Java,Python,Dart,Scala,Groovy,Haxe,Ruby".split(","):
            return string + ".split(" + separator + ")"
        elif lang in ["Octave"]:
            return "strsplit("+string+", "+separator+")"
        elif lang in "Go".split(","):
            return "strings.Split(" + string + ", " + separator + ")"
        elif lang in "PHP".split(","):
            return "explode(" + separator + ", " + string + ")"
        elif lang in "Perl".split(","):
            return "split(" + separator + ", " + string + ")"
        elif lang in "REBOL".split(","):
            return "split " + string + " " + separator
        elif lang in "C#".split(","):
            return string + ".Split(new string[] {" + separator + "}, StringSplitOptions.None)"
        elif lang in "Tcl".split(","):
            return "[split " + string + " " + separator + "]"
        elif lang in "crosslanguage".split(","):
            return "(split " + string + " " + separator + ")"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);


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
    #This function does not initialize the variable: it will change the value of an existing variable
    
    valueToGet = getVariableName(lang, valueToGet)
    valueToChange = getVariableName(lang, valueToChange)
    if type(valueToGet) is list:
        valueToGet = getArrayInitializer(valueToGet)
    
    if acs(lang, "JavaScript,Hack,Nimrod,OpenOffice Basic,Groovy,TypeScript,Rust,CoffeeScript,Fortran,AWK,Go,Swift,Vala,C,Julia,Scala,Cobra,Erlang,AutoIt,Dart,Java,OCaml,Haxe,C#,MATLAB,C++,PHP,Perl,Python,Lua,Ruby,Gambas,Octave,Visual Basic,Visual Basic .NET,bc"):
        return valueToChange + " = " + valueToGet
    elif lang in ["REBOL"]:
        return valueToChange + ": " + valueToGet
    elif lang in "Common Lisp".split(","):
        return "(setf " + valueToChange + " " + valueToGet + ")"
    elif lang in "Hy".split(","):
        return "(setf " + valueToChange + " " + valueToGet + ")"
    elif lang in "Racket":
        return "(set! "+valueToChange+" "+valueToGet+")"
    elif lang in ["Tcl"]:
        return "set " + removeInitialDollarSign(valueToChange) + " " +  valueToGet
    elif lang in "R,F#".split(","):
        return valueToChange + " <- " + valueToGet    
    elif lang in ["Haskell", "Bash"]:
        return "let " + valueToChange + " = " + valueToGet
    elif acs(lang, "Pascal,Delphi,AutoHotKey"):
        return valueToChange + " := " + valueToGet
    elif lang in ["crosslanguage"]:
        return "(set " + valueToChange + " " + valueToGet + ")"
    elif lang in ["Nemerle"]:
        return "def " + valueToChange + " = " + valueToGet
    elif lang in ["Polish notation"]:
        return "= " + valueToChange + " " + valueToGet
    return notYetDefinedError(lang = lang, functionName = inspect.stack()[0][3])


def arrayContains(lang, valueToCheck, array):
        valueToCheck = getVariableName(lang, valueToCheck)
        array = getVariableName(lang, array)
        if lang in "Python".split(","):
            return valueToCheck + " in " + array
        elif lang in "REBOL".split(","):
            return "not none? find "+array+" "+valueToCheck
        elif lang in "JavaScript,CoffeeScript".split(","):
            return array + ".indexOf(" + valueToCheck + ") !== -1"
        elif lang in "CoffeeScript".split(","):
            return array + ".indexOf(" + valueToCheck + ") != -1"
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
        elif lang in "Haskell".split(","):
            return "(elem " + valueToCheck + " " + array + ")"
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
    array = getVariableName(lang, array)
    if acs(lang, "Python,Cython,Go"):
        return "len(" + array + ")"
    elif lang in "Hy".split(","):
        return "(len " + array + ")"
    elif lang in "Clojure".split(","):
        return "(count " + array + ")"
    elif lang in "Common Lisp".split(","):
        return "(list-length "+array+")"
    elif lang in "PHP".split(","):
        return "count(" + array + ")"
    elif lang in "Java,Scala,D,CoffeeScript,TypeScript,Dart,Vala,JavaScript,Ruby,Haxe,Cobra".split(","):
        return array + ".length"
    elif lang in "C#,Visual Basic,PowerShell".split(","):
        return array + ".Length"
    elif lang in "Rust".split(","):
        return array + ".len()"
    elif lang in "C".split(","):
        return "sizeof("+array+")/sizeof("+array+"[0])"
    elif lang in "C++,Groovy".split(","):
        return array+".size()"
    elif lang in "Emacs Lisp,Scheme,Racket,Haskell".split(","):
        return "(length " + array + ")"
    elif lang in "Perl".split(","):
        return "(scalar " + array + ")"
    elif lang in "REBOL".split(","):
        return "length? " + array
    elif lang in "Swift".split(","):
        return array+".count"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def stringLength(lang, aString):
        aString = getVariableName(lang, aString)
        if lang in "C#,D,REBOL,Vala,JavaScript,CoffeeScript,TypeScript,Dart,Cobra,Python,Go,Ruby,Haxe,Haskell".split(","):
            # Do this when the string length function is the same as the array length function.
            return arrayLength(lang, aString)
        elif acs(lang, "AutoHotKey"):
            return "StringLen("+aString+")"
        elif lang in "Scala,Gosu".split(","):
            return aString + ".length"
        elif lang in "Tcl".split(","):
            return "[string length " + aString + "]"
        elif lang in "Groovy".split(","):
            return aString + ".size()"
        elif lang in "Erlang".split(","):
            return "len(" + aString + ")"
        elif lang in "Hy".split(","):
            return "(len " + aString + ")"
        elif lang in "crosslanguage".split(","):
            return "stringLength(" + aString + ")"
        elif lang in "Ceylon".split(","):
            return aString + ".size"
        elif lang in "Lua".split(","):
            return "string.len(" + aString + ")"
        elif lang in "AWK".split(","):
            return "length(" + aString + ")"
        elif lang in "R".split(","):
            return "nchar(" + aString + ")"
        elif lang in "Racket".split(","):
            return "(string-length " + aString + ")"
        elif lang in "Clojure".split(","):
            return "(count " + aString + ")"
        elif lang in "Common Lisp".split(","):
            return "(length " + aString + ")"
        elif lang in "PHP,C".split(","):
            return "strlen(" + aString + ")"
        elif lang in "Java,C++".split(","):
            return aString + ".length()"
        elif lang in "Visual Basic,Visual Basic .NET,Gambas".split(","):
            return "Len(" + "theString" + ")"
        elif lang in "Perl,Octave".split(","):
            return "length( " + aString + ")"
        elif lang in "AutoIt".split(","):
            return "StringLen(" + aString + ")"
        elif lang in "Swift".split(","):
            return "countElements( " + aString + ")"
        elif lang in "Nemerle".split(","):
            return aString + ".Length"
        elif lang in "OCaml".split(","):
            return getFunctionCall(lang=lang,function="length", parameters=[aString], fromClass=None)
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
    
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
    array = getVariableName(lang, array)
    separator = getVariableName(lang, separator)
    '''join a string array using a separator.'''
    if lang in ["Python"]:
        return separator+".join("+array+")"
    if lang in ["JavaScript","CoffeeScript","Ruby", "Groovy"]:
        return array+".join("+separator+")"
    if lang in ["C#"]:
        return "String.Join("+separator+", "+array+")"
    if lang in ["PHP"]:
        return "implode(" +separator+","+array+")"
    if lang in ["Perl"]:
        return "join(" +separator+","+array+")"
    if lang in ["Swift"]:
        return "implode(" +separator+","+array+")"
    if lang in ["PHP"]:
        return "(intercalate " +separator+" "+array+")"
    if lang in ["Lua"]:
        return "table.concat("+array+", "+separator+")"
    if lang in ["Go"]:
        return "strings.Join("+array+","+separator+")"
    if lang in ["Octave"]:
        return "strjoin ("+array+", "+separator+")"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def args(lang):
        if lang in "Python".split(","):
            return "sys.argv"
        elif lang in "Lua":
            return "arg"
        elif lang in "AutoIt":
            return "$CmdLine"
        elif lang in "Swift":
            return "C_ARGC"
        elif lang in "Julia":
            return "ARGS"
        elif lang in "Perl".split(","):
            return "@ARGV"
        elif lang in "Java,Scala,crosslanguage".split(","):
            return "args"
        elif lang in "C#".split(","):
            return "Environment.GetCommandLineArgs()"
        elif lang in "JavaScript".split(","):
            return "process.argv"
        elif lang in "Ruby".split(","):
            return "ARGV"
        elif lang in "Go".split(","):
            return "os.Args"
        elif lang in "PHP,Tcl".split(","):
            return "$argv"
        elif lang in "Haxe":
            return "Sys.args()"
        elif lang in "Visual Basic":
            return "My.Application.CommandLineArgs"
        notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);

def startForEach(lang, array, variableName, typeInArray):
        if lang in ["Java","C#"] and type(array) == list:
            theStringList = ""
            for current in numpy.shape(array):
                theStringList += "[]"
                array = "new " + typeInArray + theStringList + getVariableName(lang, array)
        else:
            array = getVariableName(lang, array)
        variableName = getVariableName(lang, variableName)
        toReturn = ""
        if lang in "Python,Nimrod".split(","):
            toReturn= "for $variableName in $array:"
        elif acs(lang, "Hy"):
            toReturn= "(for [$variableName $array]"
        elif lang in "Clojure".split(","):
            toReturn= "(doseq [$variableName $array]"
        elif lang in "Swift".split(","):
            toReturn= "for $variableName in $array {"
        elif lang in "Cobra,CoffeeScript".split(","):
            toReturn= "for $variableName in $array"
        elif lang in "AWK".split(","):
            toReturn= "for($variableName in $array){"
        elif lang in "crosslanguage".split(","):
            toReturn= "foreach(" + getCorrespondingType(lang, getCorrespondingType(lang, typeInArray)) + " $variableName in $array)"
        elif lang in "F#".split(","):
            toReturn= "for $variableName in $array do"
        elif lang in "Tcl".split(","):
            toReturn= "foreach $variableName $array {"
        elif lang in "Bash".split(","):
            toReturn= "for $variableName in {$array[@]}; do"
        elif lang in "Lua".split(","):
            toReturn= "for _, $variableName in $array do"
        elif lang in "C++".split(","):
            toReturn= "for(" + getCorrespondingType(lang, typeInArray) + " & $variableName : $array){"
        elif lang in "Ruby".split(","):
            toReturn= "$array.each do |$variableName|"
        elif lang in "Go".split(","):
            toReturn= "for $variableName := range $array {"
        elif lang in "Haxe".split(","):
            toReturn= "for($variableName in $array){"
        elif lang in "PHP,Hack".split(","):
            toReturn= "foreach ($array as $variableName){"
        elif lang in "Nemerle,PowerShell".split(","):
            toReturn= "foreach ($variableName in $array){"
        elif lang in "JavaScript".split(","):
            toReturn= "$array.forEach(function($variableName){"
        elif lang in "TypeScript".split(","):
            toReturn= "$array.forEach($variableName => {"
        elif lang in "C#,Vala".split(","):
            toReturn= "foreach (" + getCorrespondingType(lang, typeInArray) + " $variableName in $array){"
        elif lang in "Java".split(","):
            toReturn= "for(" + getCorrespondingType(lang, typeInArray) + " $variableName : $array){"
        elif lang in "Scala".split(","):
            toReturn= "for($variableName -> $array){"
        elif lang in "Groovy".split(","):
            toReturn= "for($variableName in $array){"
        elif lang in "Visual Basic,Visual Basic .NET".split(","):
            toReturn= "For Each $variableName As " + getCorrespondingType(lang, typeInArray)  + " In $array"
        elif lang in "Gambas":
            toReturn= "FOR EACH $variableName IN $array"
        elif lang in "REBOL".split(","):
            toReturn= "foreach $variableName $array ["
        elif lang in "Perl".split(","):
            return "foreach " + variableName + "(" +addInitialAtSign(array)+ "){"
        elif lang in "Dart".split(";"):
            toReturn= "$array.forEach(($variableName) {"
        elif lang in "Racket":
            toReturn= "(for ([$variableName $array])"
        elif lang in "Common Lisp".split(";"):
            toReturn= "(loop for $variableName in $array do"
        elif lang in "AutoIt".split(","):
            toReturn= "For $variableName In $array"
        if toReturn=="":
            notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3]);
        else:
            return stringInterpolation(lang, "$variableName,$array", [variableName,array])

def endForEach(lang):
    if lang in "Perl,PowerShell,Hy,R,Hack,Nemerle,Clojure,Common Lisp,Racket,CoffeeScript,Tcl,Swift,Scala,F#,C++,AWK,REBOL,Groovy,Python,Java,C#,Haxe,Go,PHP,Ruby,Lua,Go,Vala,crosslanguage".split(","):
        return endCodeBlock(lang)
    elif lang in "JavaScript,TypeScript,Dart".split(","):
        return "});"
    elif lang in "Ada".split(","):
        return "end loop;"
    elif lang in "Visual Basic,Visual Basic .NET,AutoIt".split(","):
        return "Next"
    elif lang in "Gambas".split(","):
        return "NEXT"
    elif lang in "Bash".split(","):
        return "done"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def forEach(lang, array, variableName, body, typeInArray=None):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startForEach(lang=lang, array=array, variableName=variableName, typeInArray=typeInArray)] +body+ [endForEach(lang)]
    return body

def startForInRange(lang, varName, startWith, endWith):
    toReturn = ""
    if lang in "Python".split(","):
        toReturn = "for varName in range(startWith, endWith):"
    elif lang in "R".split(","):
        toReturn="for (varName in startWith:endWith ) {"
    elif lang in "REBOL".split(","):
        toReturn= "for varName startWith endWith 1 ["
    elif lang in "Rust".split(","):
        toReturn = "for varName in range(startWith, endWith){"
    elif lang in "OCaml".split(","):
        toReturn = "for varName = startWith to endWith do"
    elif lang in "F#".split(","):
        toReturn = "for varName = startWith to endWith do"
    elif lang in "Common Lisp".split(","):
        toReturn = "(loop for varName from startWith upto endWith do"
    elif lang in "Visual Basic".split(","):
        toReturn = "For varName As Integer = startWith To endWith"
    elif lang in "Scala":
        toReturn = "for(varName <- startWith to endWith){"
    elif lang in "Java,Vala,AWK,Go,Dart,TypeScript,Haxe,PHP,JavaScript,Tcl,C#,C++,C,Bash,Perl".split(","):
        return startFor(lang=lang, initializer=initializeScalar(lang, variableType="int", variableName=varName, initialValue=startWith), condition = lessThan(lang=lang, theThings=[varName, endWith]), increment=setVar(lang=lang, valueToChange=varName, valueToGet=add(lang, [varName, 1])))
    elif lang in "AppleScript".split(","):
        toReturn = "repeat with varName from startWith to endWith"
    elif lang in "Lua".split(","):
        toReturn = "for varName = startWith, endWith, 1 do"
    elif lang in "Gambas,AutoIt".split(","):
        toReturn = "For varName = startWith To endWith"
    elif lang in "Racket".split(","):
        toReturn = "(for ([varName (in-range startWith endWith)])"
    elif lang in "Common Lisp".split(","):
        pass
    elif lang in "CoffeeScript".split(","):
        toReturn = "for varName in [startWith...endWith]"
    elif lang in "Julia".split(","):
        toReturn = "for varName = startWith:endWith"
    elif lang in "Nemerle".split(","):
        toReturn = "foreach(varName in [startWith .. endWith])"
    elif lang in "Ruby".split(","):
        toReturn = "for varName in startWith..endWith"
    elif lang in "Nimrod".split(","):
        toReturn = "for varName in startWith..endWith:"
    elif lang in "Swift".split(","):
        toReturn = "for varName in startWith...endWith{"
    elif lang in "Groovy".split(","):
        toReturn= "for(varName in startWith..endWith) {"
        
    if toReturn == "":
        notYetDefinedError(lang = lang, functionName = inspect.stack()[0][3])
    else:
        return stringInterpolation(toReturn, "varName,startWith,endWith", [varName,startWith,endWith])

def endForInRange(lang, increment):
    if lang in "Python,JavaScript,R,Groovy,REBOL,Go,AWK,Rust,C,Vala,Dart,Nimrod,TypeScript,F#,Haxe,Common Lisp,PHP,Tcl,Swift,Nemerle,Scala,Perl,Ruby,Julia,CoffeeScript,Racket,Java,Lua,C#".split(","):
        return endCodeBlock(lang)
    elif lang in "Visual Basic,Gambas,AutoIt":
        return "Next"
    elif lang in "OCaml":
        return "done"
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def forInRange(lang, varName, startWith, endWith, body):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startForInRange(lang = lang, varName=varName, startWith = startWith, endWith = endWith)] +body+ [endForInRange(lang=lang, increment = setVar(lang=lang, valueToChange=varName, valueToGet=add(lang, [varName, 1])))]
    return body

    
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
    elif lang in "REBOL".split(","):
        return "type? " + theObject
    return notYetDefinedError(lang, inspect.stack()[0][3])

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
    
#def return
def getReturnStatement(lang, toReturn):
    toReturn = getVariableName(lang, toReturn)
    if acs(lang, "Java,PowerShell,Rust,D,Ceylon,TypeScript,Hack,AutoHotKey,Gosu,Swift,Pike,Objective-C,C,Groovy,Scala,CoffeeScript,Julia,Dart,C#,JavaScript,Go,Haxe,PHP,C++,Perl,Vala,Lua,Python,REBOL,Ruby,Tcl,AWK,bc"):
        return "return " + toReturn
    elif lang in ["R"]:
        return "return(" + toReturn + ")"
    elif lang in ["crosslanguage"]:
        return "(return " + toReturn + ")"
    elif lang in "Erlang,Hy,Sibilant,LispyScript,ALGOL 68,Clojure,Prolog,Common Lisp,F#,OCaml,Haskell,ML,Racket,Nemerle".split(","):
        return toReturn
    elif lang in ["Bash"]:
        return ["(echo " + toReturn+")"] + ["return 0;"]
    elif lang in ["Gambas"]:
        return "RETURN " + toReturn
    elif lang in ["Visual Basic", "Visual Basic .NET", "AutoIt"]:
        return "Return " + toReturn
    elif lang in ["Delphi"]:
        return "Result := "+toReturn
    elif lang in "Octave,Fortran".split(","):
        return "retval = " + toReturn
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def Int(lang, objectToConvert, convertFrom):
    objectToConvert = getVariableName(objectToConvert)
    return convert(objectToConvert=objectToConvert, convertTo="int", convertFrom=convertFrom)
    
def String(lang, objectToConvert, convertFrom):
    objectToConvert = getVariableName(objectToConvert)
    return convert(objectToConvert=objectToConvert, convertTo="String", convertFrom=convertFrom)

def stringContains(lang, inString, checkFor):
    inString = getVariableName(lang, inString)
    checkFor = getVariableName(lang, checkFor)
    toReturn=""
    if lang == "Perl":
        toReturn= "(index($inString, $checkFor) != -1)"
    elif lang == "Dart":
        toReturn= "$inString.contains($checkFor)"
    elif lang in "JavaScript,CoffeeScript".split(","):
        return "("+indexOf(lang=lang, string=inString, substring=checkFor)+"!= -1)"
    elif lang == "Python":
        toReturn= "($checkFor in $inString)"
    elif lang == "Java":
        toReturn= "$inString.contains($checkFor)"
    elif lang == "Lua":
        toReturn= "$inString.find($checkFor)"
    elif lang == "Ruby":
        toReturn= "($inString.include? $checkFor)"
    elif lang == "PHP":
        toReturn= "strpos($inString, $checkFor)"
    elif lang in "REBOL".split(","):
        return arrayContains(lang=lang,valueToCheck=checkFor, array = inString)
    elif lang in "C#,Visual Basic .NET".split(","):
        toReturn= "$inString.Contains($checkFor)"
    elif lang in "C".split(","):
        toReturn= "(strstr($inString, $checkFor) != NULL)"
    elif acs(lang, "Hy"):
        toReturn= "(in $checkFor $inString)"
    if toReturn == "":
        return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    else:
        return stringInterpolation(toReturn, "$inString,$checkFor",[inString,checkFor])

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
    if acs(lang, "JavaScript,Hack,Gosu,Rust,AutoIt,AutoHotKey,TypeScript,Ceylon,Groovy,D,Octave,AWK,Julia,Scala,F#,Swift,Nemerle,Vala,Go,Perl,Java,Haskell,Haxe,C,C++,C#,Dart,R"):
        return "(" + " || ".join(listOfThings) + ")"
    if acs(lang, "PowerShell"):
        return "(" + " -or ".join(listOfThings) + ")"
    elif lang in ["Tcl"]:
        return "[expr " + " || ".join(listOfThings) + "]"
    elif acs(lang, "Python,OCaml,Nimrod,CoffeeScript,Pascal,Delphi,Erlang,REBOL,Lua,PHP,crosslanguage,Ruby"):
        return "(" + " or ".join(listOfThings) + ")"
    elif lang in ["Visual Basic"]:
        return "(" + " Or ".join(listOfThings) + ")"
    elif lang in ["Fortran"]:
        return "(" + " .OR. ".join(listOfThings) + ")"
    elif lang in ["Gambas"]:
        return "(" + " .OR. ".join(listOfThings) + ")"
    elif acs(lang, "Common Lisp,Racket,Sibilant,Clojure,Hy"):
        return "(or " + " ".join(listOfThings) + ")"
    elif lang in ["Prolog"]:
        return "(" + ", ".join(listOfThings) + ")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
        
def And(lang, listOfThings):
    '''
    Both of these things are boolean.
    '''
    if acs(lang, "JavaScript,Hack,Gosu,Rust,AutoIt,AutoHotKey,TypeScript,Ceylon,Groovy,Octave,Julia,Scala,F#,Swift,Nemerle,Vala,Dart,C,C++,C#,OCaml,AWK,Java,Haskell,Haxe,Bash,Haxe,Go,Perl,R"):
        return "(" + " && ".join(listOfThings) + ")"
    if acs(lang, "PowerShell"):
        return "(" + " -and ".join(listOfThings) + ")"
    elif lang in ["Tcl"]:
        return "[expr " + " && ".join(listOfThings) + "]"
    elif lang in "Ruby,Nimrod,CoffeeScript,D,Delphi,Pascal,Python,Lua,PHP,Erlang,crosslanguage,REBOL".split(","):
        return "(" + " and ".join(listOfThings) + ")"
    elif lang in ["Fortran"]:
        return "(" + " .AND. ".join(listOfThings) + ")"
    elif lang in ["Gambas"]:
        return "(" + " AND ".join(listOfThings) + ")"
    elif lang in ["Visual Basic", "Visual Basic .NET", "OpenOffice Basic"]:
        return "(" + " And ".join(listOfThings) + ")"
    elif lang in ["Common Lisp", "Racket", "Clojure", "Sibilant", "Hy"]:
        return "(and " + " ".join(listOfThings) + ")"
    elif lang in ["Prolog"]:
        return "(" + "; ".join(listOfThings) + ")"
    return notYetDefinedError(lang, inspect.stack()[0][3])

def Not(lang, theVar):
    theVar = getVariableName(lang, theVar)
    if lang in "Python,Hy,OCaml,Clojure,Erlang,Pascal,Delphi,F#,ML,Lua,Racket,Common Lisp,crosslanguage,REBOL,Haskell,Sibilant".split(","):
        return "(not "+theVar + ")"
    if acs(lang, "PowerShell"):
        return "(" + " -not " +theVar+ ")"
    elif lang in ["Visual Basic", "Visual Basic .NET", "AutoIt"]:
        return "(Not "+theVar + ")"
    elif lang in ["Fortran"]:
        return "(.NOT. "+theVar + ")"
    elif lang in ["Gambas"]:
        return "(NOT "+theVar + ")"
    elif acs(lang, "CoffeeScript,Java,AutoHotKey,Groovy,Scala,Hack,Rust,Octave,TypeScript,Julia,AWK,Swift,Scala,Vala,Nemerle,Pike,Perl,C,C++,Objective-C,Tcl,JavaScript,R,Dart,Java,Go,Ruby,PHP,Haxe,C#"):
        return "(!"+theVar + ")"
    elif lang in "Prolog".split(","):
        return "(\\+ "+theVar + ")"
    return notYetDefinedError(lang, inspect.stack()[0][3])

def seriesOfAnds(lang, theThings, theFunction):
    toReturn = []
    for i in range(0, len(theThings)-1):
        toReturn += [theFunction(lang, [theThings[i], theThings[i+1]])]
    return And(lang, toReturn)

def greaterThan(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang, theThings[i])
    if lang in "Racket,Hy,Common Lisp,Emacs Lisp,Clojure,Sibilant,LispyScript".split(","):
            return "(> "+" ".join(theThings)+")"
    elif len(theThings) != 2:
        #raise Exception("greaterThan is not defined when (len(theTheThings) == "+str(len(theThings))+")")
        return seriesOfAnds(lang, theThings, greaterThan)
    elif len(theThings) == 2:
        thing1 = getVariableName(lang,theThings[0])
        thing2 = getVariableName(lang,theThings[1])
        if acs(lang, "Pascal,Gosu,Gambas,Nimrod,AutoIt,ALGOL 68,Ceylon,Groovy,Rust,CoffeeScript,TypeScript,Fortran,Octave,ML,Hack,AutoHotKey,Scala,Delphi,Tcl,Swift,Vala,C,F#,C++,Dart,JavaScript,REBOL,Julia,Erlang,OCaml,crosslanguage,C#,Nemerle,AWK,Java,Lua,Perl,Haxe,Python,PHP,Haskell,Go,Ruby,R,bc,Visual Basic,Visual Basic .NET"):
            return "("+thing1 + " > " + thing2+")"
        if acs(lang, "PowerShell"):
            return "(" +thing1+ " -gt " +thing2+ ")"
        if lang in ["Tcl"]:
            return "[expr " + thing1 + " > " + thing2 + "]"
        if lang in "Polish notation".split(","):
            return "> "+thing1 + " " + thing2
        if lang in "Reverse Polish notation".split(","):
            return thing1 + " " + thing2 + " >"
    #print theThings
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def greaterThanOrEqual(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang, theThings[i])
    if acs(lang, "Racket,Hy,Scheme,Clojure,Common Lisp,Emacs Lisp,Sibilant,LispyScript"):
            return "(>= "+" ".join(theThings)+")"
    elif len(theThings) == 2:
        if acs(lang, "C,ALGOL 68,Gambas,Nimrod,Gosu,AutoIt,Ceylon,D,Groovy,Rust,CoffeeScript,TypeScript,Octave,Hack,AutoHotKey,Julia,Scala,Pascal,Delphi,Swift,Visual Basic,F#,Objective-C,Pike,Python,Oz,ML,Vala,Dart,C++,Java,OCaml,REBOL,Erlang,C#,Nemerle,Ruby,PHP,Lua,Visual Basic .NET,Haskell,Haxe,Perl,JavaScript,R,AWK,crosslanguage,Go"):
            #raise Exception("(" + theThings[0] + " >= " + theThings[1]+")")
            return "(" + theThings[0] + " >= " + theThings[1]+")"
        if acs(lang, "PowerShell"):
            return "(" +theThings[0]+ " -ge " +theThings[1]+ ")"
        if acs(lang, "Tcl"):
            return "[expr " + theThings[0] + " >= " + theThings[1] + "]"
        if acs(lang, "Fortran"):
            return "(" + theThings[0] + " .GE. " + theThings[1]+")"
    else:
        return seriesOfAnds(lang, theThings, greaterThanOrEqual)
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def lessThan(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang,theThings[i])
    if acs(lang, "Scheme,Hy,Racket,Clojure,Common Lisp,Emacs Lisp,Sibilant,LispyScript"):
        return "(< "+" ".join(theThings)+")"
    elif len(theThings) == 2:
        thing1 = theThings[0]
        thing2 = theThings[1]
        if acs(lang, "C,F#,Gambas,Nimrod,AutoIt,ALGOL 68,Ceylon,C++,D,Dart,TypeScript,CoffeeScript,Rust,Fortran,Octave,Tcl,ML,Hack,Swift,AutoHotKey,Java,Gosu,Groovy,Scala,Pascal,Delphi,JavaScript,Cobra,Julia,OCaml,Nemerle,C#,Erlang,Perl,AWK,Lua,Java,Haxe,Python,PHP,Go,Ruby,Vala,R,bc,Visual Basic,Visual Basic .NET,Haskell,crosslanguage,REBOL"):
            return "("+thing1 + " < " + thing2+")"
        if acs(lang, "PowerShell"):
            return "(" +thing1+ " -lt " +thing2+ ")"
        if acs(lang, "Bash"):
            return "("+thing1 + " -lt " + thing2+")"
        if acs(lang, "Tcl"):
            return "[expr " + thing1 + " < " + thing2 + "]"
        elif acs(lang, "Polish notation"):
            return "< "+thing1 + " " + thing2
        elif acs(lang, "Reverse Polish notation"):
            return thing1 + " " + thing2 + " >"
    else:
        return seriesOfAnds(lang, theThings, lessThan)
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def lessThanOrEqual(lang, theThings):
    for i in range(0, len(theThings)):
        theThings[i] = getVariableName(lang, theThings[i])
    if acs(lang, "Racket,Hy,Sibilant,LispyScript,Scheme,Clojure,Common Lisp,Emacs Lisp"):
        return "(<= "+" ".join(theThings)+")"
    elif len(theThings) > 2:
        return seriesOfAnds(lang, theThings, lessThan)
    if acs(lang, "PowerShell"):
        return "(" +theThings[0]+ " -le " +theThings[1]+ ")"
    elif acs(lang, "C,F#,Rust,Gosu,Gambas,Nimrod,Visual Basic,AutoIt,ALGOL 68,Ceylon,D,Groovy,CoffeeScript,TypeScript,Octave,ML,Hack,Swift,AutoHotKey,Julia,AWK,Scala,Vala,Delphi,Pascal,Python,C++,Dart,Cobra,REBOL,OCaml,Go,Java,Ruby,C#,Nemerle,PHP,Erlang,Lua,Visual Basic .NET,Haskell,Haxe,Perl,JavaScript,R,crosslanguage"):
        return "("+theThings[0] + " <= " + theThings[1] +")"
    elif acs(lang, "Tcl"):
        return "[expr " + theThings[0] + " <= " + theThings[1] + "]"
    elif acs(lang, "Fortran"):
        return "(" + theThings[0] + " .LE. " + theThings[1]+")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def keyValuePair(lang, theKey, theValue):
    if acs(lang, "Python,Groovy,Dart,JavaScript,CoffeeScript"):
        return theKey +" : "+ theValue
    elif lang in ["REBOL"]:
        return theKey +" "+ theValue
    elif acs(lang, "PHP,Ruby,Haxe"):
        return theKey + " => " + theValue
    elif lang in ["Lua"]:
        return theKey + " = " + theValue
    elif lang in ["Scala"]:
        return "("+theKey + ", " + theValue+")"
    elif acs(lang,"Perl,Perl 6"):
        return "("+theKey + ", " + theValue+")"
    elif lang in ["Java"]:
        return "map.put("+theKey+", "+theValue+")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def compare(lang, theThings, theType):
    #raise Exception(theThings)
    #print theThings
    if type(theThings) != list:
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
        if theType == getCorrespondingType(lang, "int"):
            if acs(lang, "Hy"):
                return "(= "+thing1 +" "+ thing2+")"
            if acs(lang, "Lua,C++,Ceylon,CoffeeScript,Octave,Swift,AWK,Julia,Perl,Groovy,Erlang,Haxe,CoffeeScript,Scala,Java,Vala,Dart,Python,C#,C,Go,Haskell,Ruby"):
                return "("+thing1 + " == " + thing2+")"
            if lang in ["Tcl"]:
                return "[expr " + thing1 + " == " + thing2 + "]"
            if acs(lang,"JavaScript,PHP,TypeScript"):
                return "("+thing1 + " === " + thing2+")"
            if acs(lang, "REBOL,F#,AutoIt,Pascal,Delphi,Prolog,Visual Basic"):
                return "("+thing1 + " = " + thing2+")"
        if theType == getCorrespondingType(lang, "string"):
            if acs(lang, "Hy"):
                return "(= "+thing1 +" "+ thing2+")"
            if acs(lang,"Visual Basic,Visual Basic.NET,F#"):
                return "("+thing1 + " = " + thing2+")"
            if acs(lang, "Python,Go,Vala,AutoIt,REBOL,Ceylon,Groovy,Scala,CoffeeScript,AWK,Ruby,Haskell,Haxe,Dart,Lua,Swift"):
                return "("+thing1 + " == " + thing2+")"
            if lang in ["Tcl"]:
                return "[expr "+thing1+" == "+thing2+"]"
            if lang in ["Java"]:
                return thing1 + ".equals(" + thing2 + ")"
            if lang in ["C++"]:
                return thing1 + ".compare(" + thing2 + ")"
            if acs(lang, "JavaScript,PHP,TypeScript"):
                return "("+thing1 + " === " + thing2+")"
            if lang in ["C#"]:
                return thing1+".Equals("+thing2+", StringComparison.Ordinal)"
            if lang in ["C", "Octave"]:
                return "strcmp(" + thing1 + ", " + thing2 + ")"
            if lang in ["Erlang"]:
                return "string:equal("+thing1+", "+thing2+")"
            if lang in ["Perl"]:
                return "(" + thing1 + " eq " + thing2+")"
        if lang in ["crosslanguage"]:
            return crossLanguageStatement("compare", [thing1, thing2, theType])
    else:
        toReturn = []
        for i in range(0, len(theThings)-1):
            toReturn += [compare(lang, [theThings[i], theThings[i+1]], theType)]
        return And(lang, toReturn)

    raise EngScriptException("compare is not yet defined for the type " + theType + " and the language " + lang + " and the list " + str(theThings))
    
    
def randomIntInRange(lang, minNum, maxNum):
    
    minNum = getVariableName(lang, minNum)
    maxNum = getVariableName(lang, maxNum)
    
    'Random integer less than min and greater than max'
    
    #lessThan = getVariableName(lang, minNum)
    #greaterThan = getVariableName(lang, maxNum)
    if lang in "Python,Cython".split(","):
        return "random.randint("+minNum+"+1,"+maxNum+"-1)"
    elif lang in ["Java"]:
        return "((new Random()).nextInt(("+maxNum+" - "+minNum+") + 1)" + minNum+")"
    elif lang in ["JavaScript", "CoffeeScript"]:
        return "(Math.floor(Math.random() * ("+maxNum+" - 1 - "+minNum+")) + minNum"+"+2)"
    elif lang in ["Lua"]:
        return "math.random("+minNum+"+1,"+maxNum+"-1)"
    elif lang in ["PHP"]:
        return "rand("+minNum+"+1, "+maxNum+"-1)"
    elif lang in ["C++"]:
        return "(rand()%("+maxNum+"-"+minNum+"-1)+"+minNum+"+1)"
    elif lang in ["Erlang"]:
        return "gen_rand_integer("+minNum+"+1, "+maxNum+"-1)"
    elif lang in "Ruby".split(","):
        return "Random.new.rand(("+minNum+"+1)..("+maxNum+"-1))"
    elif lang in "REBOL".split(","):
        return "(random ("+maxNum+" - 1 - "+minNum+")) + +"+minNum
    '''This site explains how to do this in several languages:
    
    http://langref.org/all-languages/numbers/random/random-integer
    
    '''
    notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

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
    if lang in ["Python"]:
        return ['''#This is a test of includeInEachFile for Python.''']
    if lang in ["C"]:
        return ["#include <stdbool.h>"]
    elif lang in ["REBOL"]:
        return [getComment(lang, "This code is written in REBOL 3.")]
    elif lang in ["C#"]:
        return [
        '''using System;''',
        '''using System.Linq;'''
        ]
    elif lang in ["Java"]:
        return ['''import java.util.ArrayList;''',
        '''import java.util.Arrays;'''
        ]
    elif lang in ["Erlang"]:
        return [getComment(lang, "All variables and parameter names in Erlang must start with capital letters. Function names should be lower-case.")
        ]
    elif lang in "crosslanguage":
        return ["//How to parse Lisp files in Python: ",
                "// http://stackoverflow.com/questions/14058985/parsing-a-lisp-file-with-python",
                "//The compiler should automatically insert parentheses whenever indentation is made here.",
                "//If a symbol (but not an enclosed parentheses) directly precedes an opening parentheses, then it should be automatically moved inside those parentheses."
                "//After these changes are made, it can be parsed like normal Lisp code."
            ]
    else:
        return [""];
    return notYetDefinedError(functionName = inspect.stack()[0][3])

def startModule(lang, moduleName):
    toInclude = "\n".join(includeInEachFile(lang))
    if lang in "Perl":
        if moduleName == None:
            return toInclude
        else:
            return "package "+moduleName+";\n"+toInclude
    elif lang in ["Java", "C#"]:
        return toInclude + getClassBeginning(lang=lang, className=moduleName)
    elif lang in ["Python"]:
        return ""
    elif lang in ["Ruby"]:
        return "module " + moduleName
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def endModule(lang, moduleName):
    if lang in ["Java", "C#", "Scala", "Ruby"]:
        return endCodeBlock(lang);
    elif lang in ["Perl", "Python"]:
        return ""
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def module(lang, body, moduleName):
    #print("Parameter names: ", parameterNames)
    #print("Parameter types: ", parameterTypes)
    body = concatenateAllElements(body)
    if moduleName == None:
        return "\n".join(includeInEachFile(lang) + body)
    body = [indent(i) for i in body]
    endOfModule = endModule(lang, moduleName)
    body = "\n".join([startModule(lang, moduleName)] +body+ [endOfModule])
    #raise Exception(body)
    return body

def removeWhitespace(theFile):
    ''''''
    theFile = theFile.split("\n")
    i = 0
    while i < len(theFile):
        if theFile[i].strip() == "":
            theFile.pop(i)
        else:
            i += 1
    return "\n".join(theFile)

def getMacroParameters(lang, parameters):
    parameters = [getVariableName(lang, current) for current in parameters]
    if acs(lang, "LispyScript,Clojure,Racket,Common Lisp,Sibilant,Hy"):
        return " ".join(parameters)
    elif lang in "C".split(","):
        return ", ".join(parameters)
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])
    
def startMacroDefinition(lang, name, parameters):
    parameters = getMacroParameters(lang, parameters)
    name = getVariableName(lang, name)
    if lang in "Racket".split(","):
        return "(define-syntax-rule ("+name+" "+parameters+")"
    if lang in "C".split(","):
        return "#define "+name+"("+parameters+")"
    elif lang in "Common Lisp".split(","):
        return "(defmacro "+name+" ("+parameters+")"
    elif lang in "Clojure".split(","):
        return "(defmacro " + name + "[" + parameters + "]"
    elif lang in "LispyScript,Sibilant".split(","):
        return "(macro "+ name+ " ("+parameters+")"
    elif lang in "newLisp".split(","):
        "(define-macro ("+name +" "+ parameters+")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def endMacroDefinition(lang):
    if lang in "Racket,Common Lisp,Clojure,LispyScript,Sibilant".split(","):
        return endCodeBlock(lang)
    elif lang in 'C':
        return ""
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

def defineMacro(lang, name, parameterNames, body):
    body = concatenateAllElements(body)
    body = [indent(i) for i in body]
    body = [startMacroDefinition(lang=lang, name=name, parameters=parameterNames)] +body+ [endMacroDefinition(lang)]
    return body

def globalReplace(lang, toReplace, inTheString, replaceWith):
    if lang in "Python".split(","):
        return inTheString+".replace("+toReplace+", "+replaceWith+")"
        # There is an error: the JavaScript version does not replace it globally
    if lang in "JavaScript,CoffeeScript".split(","):
        return inTheString+".split("+toReplace+").join("+replaceWith+")"
    elif lang in "Java".split(","):
        return inTheString+".replaceAll("+toReplace+", "+replaceWith+")"
    elif lang in "Ruby,Lua".split(","):
        return inTheString+".gsub("+toReplace+", "+replaceWith+")"
    elif lang in "C#".split(","):
        return inTheString+".Replace("+toReplace+", "+replaceWith+")"
    elif lang in "PHP".split(","):
        return "str_replace("+toReplace+", "+replaceWith+", "+inTheString+")"
    return notYetDefinedError(lang=lang, functionName = inspect.stack()[0][3])

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
        

#os.chdir("polyglotFunctions")



#getFileIgnoringExceptions(["Gambas", "MATLAB", "Octave", "Visual Basic", "Racket", "C#", "JavaScript", "Java", "Python", "C++", "Perl", "Bash", "Lua","Ruby", "Bash", "PHP","Go","Haxe","Haskell"], ["HelloWorld", "TypeofExample", "HaskellExample"])


'''
getFileIgnoringExceptions(["Lua", "JavaScript", "Python", "Java", "Ruby", "C#", "Go", "Haxe", "VBScript", "Scala"])
'''