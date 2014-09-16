#
#
#
#
#The demo for this script is in EngScriptDemo.py in the Examples folder.
########################################################################
#
#
#


# your code goes here

import polishNotation2
#polishNotation2.isSeparatedBy

from pyparsing import OneOrMore, nestedExpr
import polyglotCodeGenerator #The only method you should use is testMacro.
import syntaxRules
from grammar import grammar


def nonSeparatorParts(theArray):
    #print("lolol")
    nonSeparatorParts = []
    for i in range(0, len(theArray)):
        if(((i + 1) % 2) != 0):
            nonSeparatorParts += [theArray[i]]
    return nonSeparatorParts

#print(nonSeparatorParts(["3", "+", "4", "+", "5"]))

def stringToSyntaxTree(theString):
    return OneOrMore(nestedExpr()).parseString(theString)[0]

def getMacroOutput(lang, theArr):
    def notYetDefinedError():
        raise Exception(str(theArr)+" is not yet defined for "+str(lang))
    "This should return output in the format that is used as input for polyglotCodeGenerator.py"
    "The input should be a syntax tree"
    
    if(type(theArr) == str):
        theArr = stringToSyntaxTree(theArr)
        #print(theArray)
    theArr = list(theArr)
    
    if len(theArr) == 3 and theArr[1] == ".":
        #raise Exception(theArray[2])
        if type(theArr[2]) == str:
            #print(theArray[0], theArray[1], theArray[2])
            #raise Exception("Decide what to do when the input is an instance variable from a class.")
            return polyglotCodeGenerator.instanceVariable(lang, theArr[2], theArr[0])
            return ","
        elif theArr[2][1] == "{":
            theArr[2][2] = getMacroOutput(lang, theArr[2][2])
            #raise Exception("Decide what to do when the input is a function being called from a class. The input is " + str(theArray))
            return polyglotCodeGenerator.call(lang=lang, function=theArr[2][0], fromClass=theArr[0], parameters=theArr[2][2])
    
    if len(theArr) == 1:
        if type(theArr[0]) == str:
            return theArr[0]
    
    for current in polishNotation2.listOfSeparators():
        if polishNotation2.isSeparatedBy(theString=current, theArray=theArr):
            #print(theArray)
            #print(nonSeparatorParts(theArray))
            return getMacroOutput(lang, [current] + nonSeparatorParts(theArr))
    
    for i in range(0, len(theArr)):
        if(type(theArr[i]) != str):
            #print(type(theArray[i]))
            theArr[i] = getMacroOutput(lang, theArr[i])
            
    #print theArray
    starting = theArr[0]
    if len(theArr) >= 3:
        if theArr[1] == "[" and theArr[len(theArr)-1] == "]":
            raise Exception("Figure out what to do when the input is an array accessor.")
    if starting in ["conditionalBlock", "cond"]:
        return polyglotCodeGenerator.conditionalBlock(lang, theArr[1:len(theArr)])
    if starting == "**" and len(theArr) == 3:
        return polyglotCodeGenerator.raiseToExponent(lang=lang, num1=theArr[1], num2=theArr[2])
    if starting == ",":
        return theArr[1:len(theArr)]
    if starting == ";":
        return polyglotCodeGenerator.seriesOfStatements(lang, theArr[1:len(theArr)])
    if starting == "=":
        if len(theArr) == 3:
            return polyglotCodeGenerator.setVar(lang, theArr[2], theArr[1])
        if len(theArr) == 4:
            if type(theArr[2]) == list:
                raise Exception(theArr)
                
            #raise Exception("Figure out what to do when initializing a variable.")
            return polyglotCodeGenerator.initializeVar(lang=lang, variableName=theArr[2], variableType=theArr[1], initialValue=theArr[3], arrayDimensions=None)
    if starting == "==":
        #raise Exception(theArray)
        toReturn = polyglotCodeGenerator.compare(lang, theArr[1:len(theArr)], "int")
        #raise Exception(toReturn)
    if starting == "compare":
        #raise Exception(theArray)
        toReturn = polyglotCodeGenerator.compare(lang, theArr[1], theArr[2])
        #raise Exception(toReturn)
        return toReturn
    if starting == "][":
        return theArr
    if starting == ">":
        return polyglotCodeGenerator.greaterThan(lang, theArr[1:len(theArr)])
    if starting in ["%", "mod"]:
        return polyglotCodeGenerator.mod(lang, theArr[1:len(theArr)])
    if starting == "*":
        return polyglotCodeGenerator.multiply(lang, theArr[1:len(theArr)])
    if starting == "+":
        return polyglotCodeGenerator.add(lang, theArr[1:len(theArr)])
    if starting == "-":
        return polyglotCodeGenerator.subtract(lang, theArr[1:len(theArr)])
    if starting == "/":
        return polyglotCodeGenerator.divide(lang, theArr[1:len(theArr)])
    if starting == "..":
        return polyglotCodeGenerator.concatenateStrings(lang,theArr[1:len(theArr)])
    if starting == "++":
        return polyglotCodeGenerator.concatenateArrays(lang,theArr[1:len(theArr)])
    if starting == "<":
        return polyglotCodeGenerator.lessThan(lang, theArr[1:len(theArr)])
    if starting == "<=":
        return polyglotCodeGenerator.lessThanOrEqual(lang, theArr[1:len(theArr)])
    if starting == ">=":
        #raise Exception(theArray)
        return polyglotCodeGenerator.greaterThanOrEqual(lang, theArr[1:len(theArr)])
    if starting in ["or", "||"]:
        return polyglotCodeGenerator.Or(lang, theArr[1:len(theArr)])
    if starting in ["concatenateStrings"]:
        return polyglotCodeGenerator.concatenateStrings(lang, theArr[1])
    if starting in ["concatenateArrays"]:
        return polyglotCodeGenerator.concatenateArrays(lang, theArr[1])
    if starting in ["and", "&&", "&"]:
        return polyglotCodeGenerator.And(lang, theArr[1:len(theArr)])
    if starting in ["func", "def", "function", "defun"]:
        #Use polyglotCodeGenerator.getFunction
        
        
        
        #polyglotCodeGenerator.getFunction(functionName, isStatic, parameterNames, parameterTypes, returnType, body, requiresTheFunctions, isDefined, description)
        
        if len(theArr) == 3:
            raise Exception("Figure out what to do when the input is a function definition without parameters")
            #polyglotCodeGenerator.getFunction(functionName=theArray[1], isStatic=True, parameterNames=None, parameterTypes=None, returnType=None, body, requiresTheFunctions, isDefined, description)
        elif len(theArr) == 4:
            raise Exception("The input is a function definition with parameter names but no parameter types")
        elif len(theArr) == 6:
            return polyglotCodeGenerator.getFunction(lang=lang, functionName=theArr[2], isInstanceMethod=False, parameterNames=theArr[3], parameterTypes=theArr[4], returnType=theArr[1], body=theArr[5])
            #raise Exception("The input is a function definition with parameter names, parameter types, and a return type")
        #print(theArr)
        raise Exception("Figure out what to do when the input is a function definition")
    if starting == "switch":
        newArray = []
        for i in range(2, len(theArr)):
            newArray += theArr[i]
        return polyglotCodeGenerator.switch(lang, theArr[1], newArray)
    if starting == "module":
        if len(theArr) == 2:
            return polyglotCodeGenerator.module(lang=lang, body=theArr[1], moduleName=None)
        else:
            return polyglotCodeGenerator.module(lang=lang, body=theArr[2], moduleName=theArr[1])
    if starting == "if":
        #raise Exception(polyglotCodeGenerator.If(lang, theArray[1], theArray[2]))
        return polyglotCodeGenerator.If(lang, theArr[1], theArr[2])
    if starting in ["elif", "elsif"]:
        return polyglotCodeGenerator.Elif(lang, theArr[1], theArr[2])
    if starting == "while":
        #print(theArr)
        return polyglotCodeGenerator.While(lang, theArr[2], theArr[1])
    if starting == "case":
        return polyglotCodeGenerator.case(lang, theArr[1], theArr[2])
    if starting == "not" or starting == "!":
        return polyglotCodeGenerator.Not(lang, theArr[1])
    if starting == "else":
        return polyglotCodeGenerator.Else(lang, theArr[1])
    if starting == "default":
        return polyglotCodeGenerator.default(lang, theArr[1])
    if starting == "return":
        return polyglotCodeGenerator.Return(lang, theArr[1])
    if starting in ["foreach", "for"]:
        #raise Exception(theArray)
        if (len(theArr) == 6) and theArr[3] == "in":
            return polyglotCodeGenerator.forEach(lang=lang, array=theArr[4], variableName=theArr[2], typeInArray=theArr[1], body=theArr[5])
    if starting in ["class"]:
        #raise Exception("create a class named " + str(theArray[1]) + " with " + str(theArray[2]))
        return polyglotCodeGenerator.getClass(lang=lang, className=theArr[1], parameterTypes=theArr[2], parameterNames=theArr[3], body=theArr[4])
        '''
        elif len(theArr) > 3:
            newArray = []
            for current in range(2, len(theArr)):
                newArray += theArr[i]
            newArray = getMacroOutput(lang, ["class"] +[theArr[1]]+ ["\n".join(newArray)])
            #raise Exception(polyglotCodeGenerator.concatenateAllElements(newArray))
        '''
    if starting == "substring":
        arr1, arr2, arr3 = theArr[1], theArr[2], theArr[3]
        return polyglotCodeGenerator.subString(lang, aString=arr1, start=arr2, end=arr3)
    if starting == "listComprehension":
        x = theArr[1]
        y = theArr[2]
        z = theArr[3]
        return polyglotCodeGenerator.listComprehension(lang, x, y, z)
    if starting == "listComprehension2":
        return polyglotCodeGenerator.listComprehension2(lang, theArr[1], theArr[2], theArr[3], theArr[4])
    if starting == "charAt":
        return polyglotCodeGenerator.charAt(lang=lang, aString=theArr[1], index=theArr[2])
    if starting == "join":
        return polyglotCodeGenerator.join(lang, theArr[1], theArr[2])
    if starting == "sqrt":
        return polyglotCodeGenerator.sqrt(lang, theArr[1])
    if starting == "stringContains":
        return polyglotCodeGenerator.stringContains(lang, theArr[1], theArr[2])
    if starting == "accessArray":
        return polyglotCodeGenerator.accessArray(lang=lang, arrayName=theArr[1], indexList=theArr[2])
    if starting == "stringLength":
        return polyglotCodeGenerator.stringLength(lang,theArr[1])
    if starting == "arrayLength":
        return polyglotCodeGenerator.arrayLength(lang,theArr[1])
    if starting == "regexMatchesString":
        return polyglotCodeGenerator.regexMatchesString(lang, aString=theArr[1], regex=theArr[2])
    if starting == "splitString":
        return polyglotCodeGenerator.split(lang=lang, string=theArr[1], separator=theArr[2])
    if starting == "arrayContains":
        return polyglotCodeGenerator.arrayContains(lang, theArr[1], theArr[2])
    if starting == "newObject":
        return polyglotCodeGenerator.newObject(lang, theArr[1], theArr[2], theArr[3])
    if starting == "typeConversion":
        return polyglotCodeGenerator.typeConversion(lang, theArr[1], theArr[2], theArr[3])
    if starting == "typeOf":
        return polyglotCodeGenerator.typeOf(lang, theArr[1])
    if starting == "keyValuePair":
        return polyglotCodeGenerator.keyValuePair(lang, theArr[1], theArr[2])
    if starting == "constructor":
        return polyglotCodeGenerator.constructor(lang, theArr[1], theArr[2], theArr[3], theArr[4])
    if starting == "Error":
        return polyglotCodeGenerator.Error(lang, theArr[1])
    if starting == "publicMethod":
        return polyglotCodeGenerator.publicMethod(lang, theArr[1], theArr[2], theArr[3], theArr[4], theArr[5])
    if starting == "include":
        return polyglotCodeGenerator.include(lang, theArr[1])
    if starting == "getComment":
        return polyglotCodeGenerator.getComment(lang, theArr[1])
    if starting == "randomIntInRange":
        return polyglotCodeGenerator.randomIntInRange(lang, theArr[1], theArr[2])
    if starting == "staticMethod":
        return polyglotCodeGenerator.getFunction(isStatic=True, isInstanceMethod=False, lang=lang, returnType=theArr[1], functionName=theArr[2], parameterTypes=theArr[3], parameterNames=theArr[4], body=theArr[5])
        #['staticMethod', 'int', 'derp', '[]', '[]', ['return 1']]
    if starting == "forLoop":
        if theArr[2] == "in":
            #raise Exception("This is a foreach loop. Decide what to do next.")
            return polyglotCodeGenerator.forEach(lang=lang, array=theArr[3], variableName=theArr[1], typeInArray=None, body=theArr[4])
        else:
            return polyglotCodeGenerator.forLoop(lang, theArr[1], theArr[2], theArr[3], theArr[4])
    if starting == "forInRange":
        return polyglotCodeGenerator.forInRange(lang, theArr[1], theArr[2], theArr[3], theArr[4])
    if starting == "macro":
        return polyglotCodeGenerator.defineMacro(lang, theArr[1], theArr[2], theArr[3])
    if starting == "globalReplace":
        return polyglotCodeGenerator.globalReplace(lang, theArr[1], theArr[2], theArr[3])
    
    param1 = polyglotCodeGenerator.getVariableName(lang, theArr[1])
    if starting == "alphabeticalOrder":
        #sort string list in alphabetical order
        if lang == "Python":
            return "sorted("+param1+")"
        if lang == "JavaScript":
            return param1+".sort()"
        if lang == "Ruby":
            return param1+".sort_by{|word| word}"
        
        raise Exception(starting + " needs to be defined here for "+lang+".")
    if starting == "puts" and theArr[1] != "{":
        return polyglotCodeGenerator.puts(lang, theArr[1])
    if starting == "main":
        return polyglotCodeGenerator.args(lang) 
    if starting == "args":
        return polyglotCodeGenerator.args(lang) 
        
        raise Exception(starting + " needs to be defined here for "+lang+".")
    if starting == "spelledBackwards":
        notYetDefinedError();
        raise Exception(starting + " needs to be defined here for "+lang+".")
    
    if starting == "privateMember":
        #raise Exception(theArray[1])
        if len(theArr) == 3:
            return polyglotCodeGenerator.initializePrivateMember(lang=lang, variableName=theArr[1], variableType=theArr[2])
        elif len(theArr) == 4:
            return polyglotCodeGenerator.initializePrivateMember(lang=lang, variableName=theArr[1], variableType=theArr[2], initialValue=theArr[3])
    if theArr[0] == "[" and theArr[len(theArr)-1] == "]":
        #print("THe array is", theArr)
        #raise Exception("Figure out what to do when the input is an array initializer")
        return getMacroOutput(lang, [","] + theArr[1:len(theArr)-1])
    if len(theArr) == 4 and theArr[2] == "=":
        raise Exception("Figure out what to do when a variable is being initialized with a type.")
    if (len(theArr) == 4) and (theArr[1] == "{") and (theArr[3] == "}"):
        #raise Exception("Decide what to do when a function is being called.")
        return polyglotCodeGenerator.call(lang=lang, function=theArr[0], fromClass=None, parameters=theArr[2])
    if (len(theArr) == 4) and (theArr[1] == ".") and (theArr[3] == "{}"):
        #raise Exception("Decide what to do when a function is being called.")
        return polyglotCodeGenerator.call(lang=lang, function=theArr[2], fromClass=theArr[0], parameters=[])
    
    raise Exception("The output of " + str(theArr) +  "is not yet defined.")

def outputString(lang, theMacro, moduleName):
    #raise Exception(type(theMacro))
    return polyglotCodeGenerator.module(lang=lang, body=getMacroOutput(lang,theMacro), moduleName=None)





import re
        
def tokenizeString(aString, separators):
    #sort separators in order of descending length
    separators.sort(key=len)
    listToReturn = []
    i = 0
    while i < len(aString):
        theSeparator = ""
        for current in separators:
            if current == aString[i:i+len(current)]:
                theSeparator = current
        if theSeparator != "":
            listToReturn += [theSeparator]
            i = i + len(theSeparator)
        else:
            if listToReturn == []:
                listToReturn = [""]
            if(listToReturn[-1] in separators):
                listToReturn += [""]
            listToReturn[-1] += aString[i]
            i += 1
    return listToReturn

def mergeStrings(theArray):
    theCurrent = ""
    for current in theArray:
        if current in ["'", '"', "'''", '"""']:
            if current == theCurrent:
                pass
            current = theCurrent
            


#print(tokenizeString(aString = "\"\"\"hi\"\"\" hello + world += (1*2+3/5) '''hi'''", separators = ["'''", '+=', '+', "/", "*", "\\'", '\\"', "-=", "-", " ", '"""', "(", ")"]))

class EngScript:
    def __init__(self, theString):
        #Use instance variables instead of methods. The instance variables can be easily accessed.
        self.theString = theString
        self.split = filter(None, re.split("(<<|>>)", self.theString))
        self.parameterNames = []
        for i in range(0, len(self.split)):
            if self.split[i] == "<<":
                self.parameterNames += [self.split[i + 1]]
        self.withMergedBrackets = [];
        for current in self.split:
            if current == "<<":
                self.withMergedBrackets += [current]
            elif (self.withMergedBrackets != []):
                if (current == ">>") or (self.withMergedBrackets[len(self.withMergedBrackets)-1] == "<<"):
                    self.withMergedBrackets[len(self.withMergedBrackets)-1] += current
                else:
                    self.withMergedBrackets += [current]
        theTokens = ["{}", "][", "[]", "!=", "*/", "/*", "//", "\n", "#", "!", "==", ":=", ";", ":", ",", "++", "[", "]", "&&", "&", "|", "||", "..", "...", "*", "/", "+", ".", "^", "**", ">>", "<<", ">", "<", "'''", '"""', "\\'", '\\"', "+=", "-=", "'", '"', " ", "(", ")", "{", "}", ">=", "=", "<="]
        self.tokenized = tokenizeString(separators=theTokens, aString=theString)
        
#print                 
        
        #now sort tokenizingList in order of decreasing length
        
        #Next, define a regular expression using self.withMergedBrackets.

#print(repr("\"\'hi\'\""))        
#print(repr("\'hi\'"))

engscriptSample = EngScript(
'''#ha
z[4][4], {}; a[][] // != */ /* !{apple}; dude == dude; ga := 4; herp; 3:4 dude(3,4,5) apple[4][5], (3^4), 3..4 4...5 foo(3.5).bar(4.1) 3>4<5 += -= *= ** 4>=3<=4 <<foo>> \"'\" <<bar>> and <<baz>>'''
)
#print engscriptSample.parameterNames
#print engscriptSample.tokenized

#print("")