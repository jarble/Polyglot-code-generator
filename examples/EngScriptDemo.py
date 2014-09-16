import syntaxRules
from grammar import grammar
from EngScript import outputString
import polyglotCodeGenerator
import polishNotation2
EngScriptException = polyglotCodeGenerator.EngScriptException

theSyntaxRules = syntaxRules.makeSyntaxRules(grammar)
theSyntaxRules = polishNotation2.makeReallyNewInfoArray(theSyntaxRules, "Python")

listOfLanguages = "PHP,Tcl,Lua,ML,PHP,Racket,Common Lisp,Clojure,Hack,Swift,Prolog,AWK,Ruby,Java,Scala,Julia,JavaScript,Perl,Lua,Haxe,Erlang,Python,R,Vala,Delphi,Gosu,AutoHotKey,Groovy,Common Lisp,Dart,F#,Swift,Pike,C,C++,Nemerle,Oz,AutoIt,ML,Haskell,Julia,C#,REBOL,Go,Visual Basic,PHP,Kotlin"

listOfLanguages = "Swift,PHP,C#,Scala"

listOfLanguages = "REBOL,CoffeeScript,TypeScript,Tcl,J,F#,Visual Basic,Clojure,Racket,Haxe,Erlang,Python,AutoHotKey,C#,Java,PHP,Lua,Swift,Scala,Nemerle,Perl,AutoIt,Ruby,Common Lisp,Julia"

listOfLanguages = "Racket,LispyScript,Sibilant,Nimrod,Lua,Perl,Visual Basic,AutoIt"

listOfLanguages = "Rust,Racket,Clojure,Common Lisp"

listOfLanguages = "Puppet,PowerShell,C#,Gambas,Java,Python,C,Lua,PHP,Dart,CoffeeScript,Haxe,Hack,Ruby,Clojure,Perl,Visual Basic,Common Lisp,Nemerle,Scala,Go,AutoIt,Vala,Swift,R,Rust,Groovy,AutoHotkey,Gosu,REBOL,Julia,AWK,F#,OCaml"

#listOfLanguages = "C#,Java,Ruby,JavaScript"

#listOfLanguages = "Hy,OCaml"

listOfLanguages = listOfLanguages.split(",")



#listOfLanguages = "Ruby,Lua,PHP,TypeScript,CoffeeScript,Python,C#,Java".split(",")

#listOfLanguages = "Haxe,Lua,Tcl,Scala,C#,Java".split(",")

#listOfLanguages = "C#,D"

#listOfLanguages= "Groovy"

'''
listOfLanguages = ",".join(set(listOfLanguages.split(",")))
raise Exception(listOfLanguages)
'''

#Testing parser for ambiguous grammar
'''
import re
theMatches = re.finditer("(foo|bar)", "foo is foo bar")
arrayOfMatches = [(m.start(0), m.end(0)) for m in theMatches]

raise Exception(arrayOfMatches)
'''


def testCode(code, theLangs):
    #print(thingToEval)
    if type(theLangs) == str:
        theLangs = theLangs.split(",")
    for current in theLangs:
        #for _ in range(1):
        #    print("\nTesting " + current+"\n"), 
        outputString(current, code, "aModule")

def testCodeSamples(codeSamples, langs, theSyntaxRules):
    listOfExceptions = []
    for current1 in codeSamples:
        code = syntaxRules.testMacro(theSyntaxRules,current1)
        #raise Exception(code)
        #raise Exception(code)
        for current2 in langs:
            try:
                testCode(code, current2)
            except EngScriptException as e:
                import traceback
                listOfExceptions += [str(e).split(" is not yet defined for ")]
                print traceback.format_exc()
    if listOfExceptions != []:
        currentFunction = listOfExceptions[0][0]
        stringToPrint = ""
        for i in range(1, len(listOfExceptions)):
            if listOfExceptions[i][0] == listOfExceptions[i - 1][0] and len(listOfExceptions[i]) > 1:
                listOfExceptions[i][1] = listOfExceptions[i-1][1] + "," + listOfExceptions[i][1]
                listOfExceptions[i-1] = []
        for i in listOfExceptions:
            if (i != []) and (len(i) == 2):
                stringToPrint = stringToPrint + i[0] + " is not yet defined for " + i[1]+"\n"
        #raise Exception(stringToPrint)
        
        text_file = open("listOfErrors.txt", "w+")
        text_file.write(stringToPrint)
        print(stringToPrint)
        text_file.close()
    return listOfExceptions

import os
import re

def getFileText(inputFileName, moduleName):
    inputFile = open(inputFileName, "r")
    inputText = inputFile.read()
    #raise Exception(repr(inputText))
    inputFile.close()
    
    inputText = "\n"+inputText+"\n"
    #raise Exception(inputText)
    #raise Exception(inputText)
    return "\n" + "\n".join([ll.rstrip() for ll in inputText.splitlines() if ll.strip()]) + "\n"

def getFileInLanguage(lang, theOutputString, outputPath, outputFile, theSyntaxRules):
    
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
        
    outputFile = outputPath + outputFile
    
    f = open(outputFile,'w')
    f.write(theOutputString) # python will convert \n to os.linesep
    f.close() # you can omit in most cases as the destructor will call if
    print(outputFile + " saved")

def getFileInLanguages(langs, fileName):
    for current in langs:
        getFileInLanguage(current, fileName, "EngScript_examples/"+current+"/", fileName.replace(".txt", "")+"."+polyglotCodeGenerator.getFileExtension(current))



#getFileInLanguages(["Java", "C#", "Lua", "Perl", "PHP"], "moduleTest.txt")

def getFilesInLanguages(langs, theSyntaxRules):
    theFileNames = []
    for fileName in os.listdir("EngScript_examples"):
        if fileName.endswith(".txt"):
            theFileNames += [fileName]
    for current in langs:
        for fileName in theFileNames:
            try:
                inputFilePath = "EngScript_examples/"+fileName
                inputText = getFileText(inputFilePath, fileName.replace(".txt", ""))
                theOutputString = outputString(current, syntaxRules.testMacro(theSyntaxRules,inputText), fileName.replace(".txt", ""))
                #print(theOutputString)
                getFileInLanguage(
                    lang = current,
                    theOutputString = theOutputString,
                    outputPath = "EngScript_examples/"+current+"/",
                    outputFile = fileName.replace(".txt", "")+"."+polyglotCodeGenerator.getFileExtension(current),
                    theSyntaxRules = theSyntaxRules
                )
            except Exception as e:
                pass
                #import traceback
                #print traceback.format_exc()
                

stringToTest = '''
module
    a ^ 2;
    a / 2;
    a + 2;
    def int add [int, int] [a, b]
        return a + b;
    def int multiply [int, int] [a, b]
        return a * b;
'''

#fromFile = getFileText("EngScript_examples/moduleTest.txt")

getFilesInLanguages(["Python"], theSyntaxRules)

def testMacros(theSyntaxRules):
    testCodeSamples([
        "a is a substring of b",
        "a + a",
        "a / a",
        "a * a",
        "a > 2",
        "a < 2",
        "a >= b",
        "a <= b",
        "compare the integers [10, 5]",
        "bool b = false",
        "int i = 1;",
        "(not a)",
        "replace the string foo in the string bar with the string baz",
        "the regex a matches the string b",
        '''foreach int i in j
            a;
        ''',
        '''macro macro1 [param1, param2]
            return 1;
        ''',
        "a and b",
        "a or b",
        '''
        def int doSomething [int, int] [a, b]
            return a + b;
        ''',
        '''
        main
            1;
        '''
        '''switch q
            case a
                1;
            default
                g;
        ''',
        '''
        while a
            1;
        ''',
        "a .. b",
        "index 3 of the array foo",
        "the length of the string foo",
        "the length of the array bar",
        "index 1 of the string a",
        "while (a > 2) (print a)",
        "for i from 3 to 10 (print i)",
        "10 ^ 2",
        '''
        cond
            if (the integers [a, 2] are equal)
                a;
            elif (the integers [a, 2] are equal)
                a;
            else
                a;
        ''',
        "switch a (case a (return true))",
        "compare the strings [a, b]",
        "main (1)",
        "the strings [a, b, c] are equal"
    ], listOfLanguages, theSyntaxRules)


testMacros(theSyntaxRules)
getFilesInLanguages(listOfLanguages, theSyntaxRules)

raise Exception("This is the end of the script. The other files should be moved elsewhere.")

testCodeSamples([
'''
module
    the character at index 1 in the string foo
    the array a contains b
    the string x contains the string y
    (foo * 2) for foo in bar where (the integers [foo, 2] are equal)
    class foo [int, int] [a, b]
        foo;
    #concatenate the arrays [a,b,c,d]
    concatenate the strings [a,b,c,d]
    def int foo [int, int] [a, b]
        return true;
    while a
        b;
    bool q = true;
    int q = 1;
    string foo = "wow";
    cond
        if c
            g;
        elif p
            d;
        else
            q;
    compare the integers [a, b];
    concatenate the strings [a, b, c];
    compare the strings [lol, lol, lol];
    string a = 'haha';
    a and b;
    a or b;
    3 + a;
    3 * a;
    a > b;
    b < d;
    c >= 10;
    c <= 10;
    3 to the power of 4;
    switch a
        case 4
            foo;
        default
            bar;
 '''], listOfLanguages)

testCodeSamples(['''
module
    string a = "haha";
    (a and b)
    (c or d)
    3 + 4
    4 - 4
    3 * 3
    3 / 6
    boolean g = true;
    int i = 0;
    boolean k = false;
    def int k [int, int] [a, b]
        return 1;
    cond
        while a
            a;
        if a
            a;
        elif b
            b;
        else
            d;
        the length of the string a;
'''],
listOfLanguages)

testCodeSamples([

'''
int a = 10;
switch a
    case a
        a;
    default
        a;
def int foo [int, int] [a, b]
    return 1;
while foo
    doo;
if foo
    foo
elif bar
    bar
else
    s
''',
"return 1;", "3 + 4", "5 - 7", "10 * 6", "10 / 2", "4 < 5", "5 < 6", "3 <= 4", "10 >= 7", "2 ^ 3",
"index 4 of the array foo",
"the character at index 1 in the string foo",
"foo{1};",
'''
cond
    if a
        a;
    elif b
        b
    else
        c
''',
'''while a
    a
''',
                 "[1, 2, 3, 4]", "not true", "concatenate the strings [a,b]", "compare the strings ['hello', 'hello']", "compare the integers [3, 4]", "x < 4", "x > 4", "x >= 5", "x + 1", "x - 2", "x * 4", "x / 4", "x ^ 4", "concatenate the strings [a, b]"], listOfLanguages)

'''
testCode('''
'''
(sin{x} ^ cos{x});
(3 + 4 + 5);
(((b ^ 2) - (4 * a * c)) / (2 * a));
'''
''', "Polish notation,Reverse Polish notation")
'''

#thing = [((x % 2) == 0) for ((x % 2) == 0) in [2,4,6] if x]

#raise Exception([(x > 0) for x in [1,2,3,4]])



testCodeSamples(['''
module
    for (i = 0) (i < 10) (i++)
        for (j = 0) (j < 10) (j++)
            print i + j;
    for foo in [1,2,3,4]
        print foo;
    while a
        s
    cond
        if a
            a
        elif b
            b
        else
            c
    x * 2
    x + 2
    x - 2
    x / 3
    #x ^ 2
    boolean a = false;
    boolean a = true;
    string hello = 1;
    static boolean foo [int, int] [a, b]
        return (a > b);
    def boolean notFoo [int, int] [a, b]
        return not foo{a, b};
'''], listOfLanguages)

testCodeSamples(
['''
module
    def int foo [int, int] [a, b]
        return (a > b);
    not a
    a and b
    a or b 
    a > b
    a < b
    a >= b
    a <= b
    a+b
    a-b
    a*b
    a/b
    switch c
        case 1
            c
    cond
        if a
            a
        else
            dude
        endif
    class aClass
        private int foo = 1;
        constructor aClass [int, int] [foo, bar]
            foo = bar;
    print{self.aVar};
    foo ^ bar;
    boolean foo = true;
    boolean bar = false;
    #the strings "foo" and "bar" are equal;
    the integers 1 and 1 are equal;
    int a = 10;
    a *= 2;
    3 and 4
    3 or 4
    #(the string "foo" equals "bar")
    #(concatenate the strings [foo, bar, baz])
    (3 and 4 and 5)
    (3 or 4 or 5)
    3 > 4;
    3 < 4;
    9 >= 9
    9 <= 9
    def void junk [] []
        foo - bar;
        foo * bar;
        foo / bar;
        switch a
            case 1
                a;
            default
                c;
        cond
            if foo:
                bar;
            elif bar:
                bar;
            else:
                baz;
    def int sum [int, int] [foo, bar]
        return foo + bar;
    print sum{3, subtract{4, }};
    print 3 + (5 - 2);
    print (concatenate the strings ["foo ", "bar"]);
'''],
listOfLanguages)

testCodeSamples(['''
module
    #int[] j = [1,2,3,4];
    3 + 5
    3 - 6
    7 / 8
    9 + 9
    3 > 4;
    5 >= 7;
    7 <= 7;
    0 < 2;
    if foo:
        foo;
    elseif foo:
        foo;
    else:
        bar;
    switch q
        case b
            g;
        default
            x;
    #the character at index 0 of the string "hello";
    #print (the first letter of the string "derp");
    def boolean isEven [int] [num]
        cond
            if (num is divisible by 2):
                return true;
            else:
                return false;
    cond
        if (thing1 < thing2)
            return thing1;
        else if (thing1 < thing2)
            bah;
        else
            return thing2;
    def string boldText [string] [theString]:
        return concatenate the strings ["<b>", theString, "</b>"];
    def void replaceIn1DArray [int[], int, int, int] [theArray, arrayLength, toFind, toReplace]:
        int i = 0;
        while(i < arrayLength):
            cond
                if (the integer (index [i] of the array theArray) equals toFind):
                    (index i of array theArray) = toReplace;
            i++;
        return theArray;
    def int arrayContains [int[], int, int] [theArray, arrayLength, toFind]:
        int i = 0;
        while(i < arrayLength):
            cond
                if (the integer (index [i] of the array theArray) equals toFind):
                    return true;
            i++;
        return false;
    def int numberOfOccurrences [int[], int, int] [theArray, arrayLength, toFind]:
        int i = 0;
        int num = 0;
        while(i < arrayLength):
            cond
                if (the integer (index [i] of the array theArray) equals toFind):
                    num += 1;
            i++;
        return num;
    def bool rangesOverlap [int, int, int, int] [startA, endA, startB, endB]:
        return (startA <= endB)  and  (endA >= startB);
    def bool greaterThan [int, int] [thing1, thing2]:
        return (thing1 > thing2);
    def bool lessThan [int, int] [thing1, thing2]:
        return (thing1 < thing2);
    def bool divisibleBy [int, int] [thing1, thing2]:
        return (thing1 is divisible by thing2);
    def integer sum [int, int] [thing1, thing2]:
        return thing1 + thing2;
    def int largest [int, int] [thing1, thing2]:
        cond
            if (thing1 > thing2)
                return thing1;
            else
                return thing2;
    def int smallest [int, int] [thing1, thing2]:
        cond
            if (thing1 < thing2)
                return thing1;
            else
                return thing2;
    #3 % 2;
    3 != 4;
    #the string "hello" equals "wow";
    #the string "hello" concatenated to the string "wow";
    #concatenate the string "hello" to the string "wow";
    1 equals the integer 2;
    true and false;
    false or true;
    #3 >= 4;
    #3 <= 4;
    #3 += 4;
    #3 *= 4;
    #3 -= 4;
    #3 > 4;
    #3 < 4;
    cond
        if foo
            foo
        if bar
            bar;
        else
            baz;
    #switch foo
    #    case a
    #        a
    #    default
    #        a
    #concatenate the strings [bar, baz];
    
        
'''], listOfLanguages)

testCodeSamples(['''
module
    print 3 ^ 4;
    #while a:
    #    return a;
    #print (the type of foo);
    #while (i < 10):
    #    print i;
    #print (convert "5" to int from string) + ("23" converted from type string to type int);
    print (the integers 10 and 10 are equal)
    print (the integer 12 is equal to 12)
    print (12 is equal to the integer 12)
    #print (compare the string "hello" with "wow")
    #print (compare "hello" with the string "wow")
    #print (convert 10 from type int to type string)
    join the strings ["hello", "world"] using the string ", " as a delimiter;
    split the string ["hello,wow,wow"] using the string "," as a separator;
    print(concatenate these strings: ["hello", "wow", "derp"]);
    #every string in ["o", "he", "ll", "oh"] that is a substring of "hello";
    #each x in [1,2,3,4] where (x is divisible by 2);
    #x for x in [1,2,3,4] if (x is divisible by 2);
    #numbers in [1,2,3,4] that are greater than 0;
    #numbers in [1,2,3,4] that are less than 10;
    #numbers in [3,5,7] that are odd;
    #numbers in [1,2,3,4] that are even;
    #x in [1,2,3,4] where (x is divisible by 2)
    #numbers in [2,4,6] that are divisible by 2;
    print(substring of the string "hello" on indices 1 to 4);
    #the length of the string "hi";
    3 < 4;
    3 > 4;
    3 <= 4;
    #the size of the array foo;
    #split the string "hello" with the separator "(ll)";
    3 + 4 + 5;
    3 - 4 - 5;
    #3 + 4 * 5;
    #concatenate the arrays [[1,2,3], [1,2,3]]
    #print (the array [[1],[2],[3],[4]] contains 1);
    #foo{bar} = bar ^ 2;
    #string addStr{str1, str2} = substring of str1 from index 1 to index 2
    def bool hello [bool, bool] [x, y]:
        #switch goo
        #    case 1
        #        print 1;
        #    case 2
        #        print 1;
        #    default
        #        print 1;
        #for int i in baz
        #    print i;
        #while true:
        #    print "Hi!"
        int[] woo = [a,v,d,a];
        bool foo = true;
        int stuff = 1;
        string hello = "Hello!";
        #print substring of "foo" from 1 to 2;
        #print the length of the string foo;
        bool sampleBool = true;
        print (true and false);
        print (true or false);
        print (not false);
        print (7 % 3 % 4);
        #print 2 to the power of 4
        #print{index 1 of string "7 + 7"};
        #return (substring of "hello" from 1 to 3);
        t = t * 4;
        t += g;
        t *= g;
        t -= g;
        t = t/g;
        #switch q
        #    case 1
        #        print 1;
        #    default
        #        print 5;
        cond
            if 5 > 4 then
                print "hello!";
            elif y then
                print "derp!";
            else
                t = "12";
        return 1;
'''], listOfLanguages
)

testCodeSamples(['''
module
    boolean x = true;
    boolean y = false;
    class exampleClass:
        print "lol!";
        private int hello = 3;
        def int printHello
            print this.hello;
    exampleClass.printHello{};
    exampleClass.printHello{1,1};
'''], listOfLanguages)

theCode = '''
        module
            cond
                if (compare int [x, 3]) then
                    print "hello!";
                elsif (compare int [x, 10]) then
                    print "hi!";
                else
                    print "lulz";
            print (3 is in [1,2,3,4])
            print (11 is greater than 10);
            print the sum of 10 and 2;
            print 3 multiplied by 5;
            print the quotient of 10 and 5;
            int x = 10 + 1;
            x += 3 + 4 + 5;
            print x + 12;
            until x is greater than 12:
                x += 1;
                print x;
                print x divided by 4;
            if 24 is divisible by 4 then
                print (1 + 10 + 5);
                x = 1 + 3 + 4;
                x *= 3 + 4;
                print x to the power of 4;
                print x;
            print 2 is more than 1 and less than 3;
            print 2 is less than 3 and more than 1;
            print sort ["foo", "bar", "baz"] in alphabetical order;
            print index 1 of array (each x in [1,2,3,4] where (x is divisible by 2));
            print array index [0] of (split the string "hello,world,wow" with the separator ",");
            print concatenate strings ["hello", "wow"];
            for int current in [1,2,3,4]
                print current;
            print concatenate strings ["foo", "bar", "baz"]
            print 7 minus 4;
            #print{concatenate arrays [[1,2], [3,4], [7,4]]};
            print the sum of 5 and 10;
            print 10 divided by 5;
            print 10 * 3;
            print the length of the array "hi";
            print the length of the string "hi";
            #print{split string "hello,wow" with separator ","};
            #print{the regex foo matches the string bar};
            #class ExampleClass
            #    private int[][] something;
            #    private string hello;
            #    (self.hello) = "Hi!";
            #    #self.derp{};
            #    static int hello with parameter names [parm1] and parameter types [int]
            #        return 1;
            #def int something [int, int] [param, param1]:
                print{string "foo" index 2};
                print the substring of "foo" from 1 to 2;
                print index 2 of string "foo";
                print (compare string ["hello", "hello"]);
                int foo = 1;
                while(foo < 3)
                    print foo;
                    foo++;
                cond
                    unless (param is 100 at most)
                        print{1};
                cond
                    unless (3 is less than or equal to 4)
                        print{1};
                cond
                    unless (3 is greater than 4)
                        print{1};
                cond
                    unless (3 is greater than 4)
                        print{1};
                cond
                    if true
                        print{1};
                        print{1};
                    else if false
                        print{1};
                        print{1};
                    else
                        print{1};
                        print{1};
            #def string surroundWithParentheses with parameter names [string1] and parameter types [string]
            #    return (concatenate these strings: ["(", string1, ")"]);
            #for initializer (int x = 1) condition (x < 3) update (x ++)
            #class derp
            #    print{+ "concatenate" str{var2} " several " str{var1} "strings with variables"}
            #    print{+ (+ str{1} "hello2") str{4}}
            #    #print{(x^2) for x in [1, 2, 3, 4]}
            #    print{1,1}; print{2};
            #    while goo
            #        gah
            #foreach gee in bee
            #    while true
            #        woo
            #    print{range{0,10}};
            #    print{1};
            #print(the string 'hello' contains 'ell')
            something{1,3};
            myArray = [1,3,[4,5,6]];
            int hello = 5;
            hello += 3;
            hello++;
            hello -= 4;
            hello--;
            print{compare the int a to 5};
            print{compare int a to 5};
            print{compare a to int 5};
            print{compare a to the int 5};
            (print{11}) if (compare [c, 5] of type int);
            #hello = (4 to the power of 3);
            print{hello};
            #while true
            #    print{1};
            #    return 2;
            #def int something [paramNames] [int]
        '''