grammar = [
    [["the string <<aString>> matches the (regular expression|regex(p|)) <<regex>>", "the (regex(|p)|regular expression) <<regex>> matches the string <<aString>>"], "(regexMatchesString <<aString>> <<regex>>)", "final"],
    [["replace the string <<foo>> in the string <<bar>> with the string <<baz>>"], "(globalReplace <<foo>> <<bar>> <<baz>>)", "final"],
    [["macro <<name>> <<parameters>> <<body>>"], "(macro <<name>> <<parameters>> (, <<body>>))", "final"],
    [["main <<foo>>"], "(main <<foo>>)", "final"],
    [["the command line arguments"], "(args 1)", "final"],
    [["(loop |)for <<foo>> from <<bar>> to <<baz>> <<body>>", "for <<foo>> in <<bar>> .. <<baz>> <<body>>"], "(forInRange <<foo>> <<bar>> <<baz>> (, <<body>>))", "final"],
    [["((a |)random|an|) (integer|number) between <<min>> and <<max>>", "((a |)random|an) (integer|number)( that is|) (greater|bigger|more|larger) than <<min>> (and|but) less than <<max>>", "((a |)random|an) (integer|number)( that is|) less than <<max>> (and|but) (greater|more|bigger|larger) than <<min>>"], "(randomIntInRange <<min>> <<max>>)", "final"],
    [["(raise )(error|(e|E)xception) <<foo>>"], "(Error <<foo>>)", "final"],
    [["comment <<foo>>", "// <<foo>>"], "(getComment <<foo>>)", "final"],
    [["module <<moduleName>> <<body>>"], "(module <<moduleName>> (, <<body>>))", "final"],
    [["<<key>> : <<value>>"], "(keyValuePair <<key>> <<value>>)", "final"],
    [["(import|include) <<fileName>>"], "(include <<fileName>>)", "final"],
    [["(|public )static <<returnType>> <<functionName>> <<parameterTypes>> <<parameterNames>> <<body>>"], "(staticMethod <<returnType>> <<functionName>> <<parameterTypes>> <<parameterNames>> <<body>>)", "final"],
    [["public <<returnType>> <<functionName>> <<parameterTypes>> <<parameterNames>> <<body>>"], "(publicMethod <<returnType>> <<functionName>> <<parameterTypes>> <<parameterNames>> <<body>>)", "final"],
    [["<<objectType>> <<objectName>> = new <<functionCall>>"], "(newObject <<objectName>> <<objectType>> <<functionCall>>)", "final"],
    [["(the |)square root of <<foo>>"], "(sqrt <<foo>>)", "final"],
    [["(c|)for(loop|) <<foo>> <<bar>> <<baz>> <<body>>"], "(forLoop <<foo>> <<bar>> <<baz>> (, <<body>>))", "final"],
    [["constructor <<className>> <<parameterTypes>> <<parameterNames>> <<body>>"], "(constructor <<className>> <<parameterNames>> <<parameterTypes>> (, <<body>>))", "final"],
    [["((the |)type(| )of) <<foo>>"], "(typeOf <<foo>>)", "final"],
    [["convert <<var>> from type <<foo>> to type <<bar>>", "convert <<var>> to type <<bar>> from type <<foo>>", "convert <<var>> from <<foo>> type to <<bar>> type", "convert <<var>> to <<bar>> type from <<foo>> type"], "(typeConversion <<var>> <<foo>> <<bar>>)", "final"],
    [["(merge|join) the (strings|list|array) <<x>> (with|using) the (separator|delimiter) <<y>>", "(join)(| the strings) <<x>> (with|using) the string <<y>> as (the|a) (delimiter|separator)"], "(join <<x>> <<y>>)", "final"],
    [["the string <<foo>> contains the string <<bar>>", "<<bar>> is a substring of (the string|)<<foo>>", "the string <<foo>> contains <<bar>>"], "(stringContains <<foo>> <<bar>>)", "final"],
    [["<<a>> for <<b>> in <<c>> (if|where) <<d>>"], "(listComprehension2 <<a>> <<b>> <<c>> <<d>>)", "final"],
    [["<<type>> <<foo>> { <<bar>> } = <<baz>>"], "(choo)", "final"],
    [["<<foo>> { <<bar>> }"], "(<<foo>> {(<<bar>>)})", "final"],
    [["<<foo>> ;"], "(; <<foo>>)", "final"],
    [["<<foo>> <<bar>> = <<baz>>"], "(= <<foo>> <<bar>> <<baz>>)", "final"],
    [["module <<foo>>"], "(module (, <<foo>>))", "final"],
    [["<<foo>> = <<bar>>"], "(= <<foo>> <<bar>>)", "final"],
    [["while <<foo>> <<bar>>", "while <<foo>> (do|:) <<bar>>"], "(while <<foo>> (, <<bar>>))", "final"],
    [["return <<foo>>"], "(return <<foo>>)", "final"],
    [["cond <<foo>>"], "(cond <<foo>>)", "final"],
    [["if <<foo>> <<bar>>", "if <<foo>> (then|:) <<bar>>"], "(if <<foo>> (, <<bar>>))", "final"],
    [["(elsif|elif|else if|elseif) <<foo>> <<bar>>", "(elsif|elif|else if|elseif) <<foo>> (then|:) <<bar>>"], "(elsif <<foo>> (, <<bar>>))", "final"],
    [["else <<foo>>", "else : <<foo>>"], "(else (, <<foo>>))", "final"],
    [["switch <<foo>> <<bar>>"], "(switch <<foo>> <<bar>>)", "final"],
    [["case <<x>> <<bar>>"], "(case <<x>> (, <<bar>>))", "final"],
    [["default <<x>>"], "(default (, <<x>>))", "final"],
    [["def <<functionType>> <<functionName>> <<paramTypes>> <<paramNames>> <<body>>", "def <<functionType>> <<functionName>> <<paramTypes>> <<paramNames>> : <<body>>"], "(def <<functionType>> <<functionName>> <<paramNames>> <<paramTypes>> (, <<body>>))", "final"],
    [["[ <<x>> ]"], "(<<x>>)", "final"],
    [["not <<x>>"], "(not <<x>>)", "final"],
    [["for(|(| )(each|every)) <<type>> <<foo>> in <<bar>> <<baz>>"], "(foreach <<type>> <<foo>> in <<bar>> (, <<baz>>))", "final"],
    [["for((| )(each|every)) <<foo>> in <<bar>> <<baz>>"], "(foreach None <<foo>> in <<bar>> (, <<baz>>))", "final"],
    [["class <<className>> <<parameterNames>> <<parameterTypes>>(| :) <<body>>"], "(class <<className>> <<parameterNames>> <<parameterTypes>> (, <<body>>))", "final"],
    [["<<x>> for <<y>> in <<z>>"], "(listComprehension <<x>> <<y>> <<z>>)", "final"],
    [["for initializer <<x>> condition <<y>> update <<z>>"], "(forLoop <<x>> <<y>> <<z>>)", "final"],
    [["<<x>> ,"], "<<x>> ,", "final"],
    [["concatenate ((|the )strings|these strings :) <<x>>"], "(concatenateStrings <<x>>)", "final"],
    [["concatenate (|the )arrays <<x>>"], "(concatenateArrays <<x>>)", "final"],
    [["compare the <<y>>s <<x>>", "compare <<x>> of type <<y>>", "compare (each|every) <<y>> <<x>>"], "(compare <<x>> <<y>>)", "final"],
    [["(the |)(|character at )index <<foo>> (of|in) (|the )string <<bar>>", "character at index <<foo>> (of|in) <<bar>>"], "(charAt <<bar>> <<foo>>)","final"],
    [["index <<foo>> (of|in) (|the )array <<bar>>"], "(accessArray <<bar>> <<foo>>)","final"],
    [["(|the )(length|size) of (|the )string <<x>>"], "(stringLength <<x>>)", "final"],
    [["(|the )(length|size) of (|the )array <<x>>"], "(arrayLength <<x>>)", "final"],
    [["(|the )string <<foo>> matches (the )(regex|regular expression) <<bar>>", "(|the )(regex|regular expression) <<bar>> matches (the )(string) <<foo>>"], "(regexMatchesString <<foo>> <<bar>>)", "final"],
    [["split(| the) string <<x>> (with|using)(| the) (delimiter|separator|string) <<y>>", "split the string <<x>> (with|using) the string <<y>> as (a|the) (delimiter|separator)"], "(splitString <<x>> <<y>>)", "final"],
    [["private <<variableType>> <<variableName>>"], "(privateMember <<variableName>> <<variableType>>)", "final"],
    [["private <<variableType>> <<variableName>> = <<initialValue>>"], "(privateMember <<variableName>> <<variableType>> <<initialValue>>)", "final"],
    [["<<x>> % <<y>>"], "(mod <<x>> <<y>>)", "final"],
    [["(sort|arrange) <<x>> in alphabetical order", "alphabetize <<x>>", "<<x>> (alphabetized|(sort|arrang)ed in alphabetical order)"], "(alphabeticalOrder <<x>>)", "final"],
    [["<<x>> (spelled|written) (backwards|in reverse)", "reverse the string <<x>>"], "(spelledBackwards <<x>>)", "final"],
    [["(puts|print) <<foo>>"], "(puts <<foo>>)", "final"],
    [["(|(the |)array )<<foo>> contains <<bar>>", "<<bar>> is in (|(|the )array )<<foo>>"], "(arrayContains <<bar>> <<foo>>)", "final"],
    [["<<foo>> . <<bar>> {}"], "(<<foo>> . <<bar>> {})", "final"],
    #privateMember(lang, variableName, variableType, initialValue, arrayDimensions=None)
    
    #End of final macros
    
    
    
    #Beginning of non-final macros
    [["<<foo>> *= <<bar>>"], "<<foo>> = (<<foo>> * <<bar>>)"],
    [["array <<foo>> index <<bar>>", "index <<bar>> array <<foo>>", "array index <<bar>> (in|of) <<foo>>"], "index <<bar>> of array <<foo>>"],
    [["string <<foo>> index <<bar>>", "index <<bar>> string <<foo>>"], "index <<foo>> of string <<bar>>"],
    [["compare(| the) <<x>> <<y>> (to|and|with) <<z>>", "compare <<z>> (to|and|with)(| the) <<x>> <<y>>"], "compare [<<z>>, <<y>>] of type <<x>>"],
    [["compare <<x>> (and|to|with) <<y>> of type <<z>>"], "compare [<<x>>, <<y>>] of type <<z>>"],
    [["unless <<foo>> <<bar>>"], "if (not <<foo>>) then <<bar>>"],
    [["<<foo>> += <<bar>>"], "<<foo>> = (<<foo>> + <<bar>>)"],
    [["<<foo>> -= <<bar>>"], "<<foo>> = (foo - bar)"],
    [["<<foo>> ++"], "<<foo>> += 1"],
    [["<<foo>> --"], "<<foo>> -= 1"],
    [["<<foo>> to the power of <<bar>>"], "<<foo>> ^ <<bar>>"],
    [["(def|function|func) <<theType>> <<functionName>> with(| the) parameter types <<paramTypes>> and( the|) parameter(s named| names) <<paramNames>> <<body>>", "(def|function|func) <<theType>> <<functionName>> <<paramNames>> <<paramTypes>> <<body>>", "(def|function|func|static) <<theType>> <<functionName>> with(| the) parameter(s named| names) <<paramNames>> and( the|) parameter types <<paramTypes>> <<body>>"], "def <<theType>> <<functionName>> <<paramNames>> <<paramTypes>> <<body>>"],
    [["<<foo>> is (greater|more) than <<bar>>"], "<<foo>> > <<bar>>"],
    [["<<foo>> is (less than or equal to|at most) <<bar>>"], "<<foo>> <= <<bar>>"],
    [["<<foo>> is ((more|greater) than or equal to|at least) <<bar>>"], "<<foo>> >= <<bar>>"],
    [["<<foo>> is <<bar>> at most"], "<<foo>> is at most <<bar>>"],
    [["<<foo is <<bar>> at least"], "<<foo>> is at least <<bar>>"],
    [["<<x>> if <<y>>"], "if <<y>> then <<x>>"],
    [["(the |)substring (in|of)( the string|) <<x>> (from|on|at)(| (index|indices)) <<y>> to(| index) <<z>>", "(the |)substring (of|in) <<x>> between(| index) <<y>> and(| index) <<z>>", "(the |)substring (of|in) <<x>> (start|beginn)ing at(| index) <<y>> and ending at(| index) <<z>>"], "(substring <<x>> <<y>> <<z>>)", "final"],
    [["compare <<x>> <<y>>"], "compare <<y>> of type <<x>>"],
    [["(def|function|defun) <<type>> <<x>> with parameter names <<y>> and parameter types <<z>> <<a>>"], "def <<type>> <<x>> with parameter types <<z>> and parameter names <<y>> <<a>>"],
    [["concatenate (each|the(|se)) string(|s): <<foo>>"], "concatenate the strings <<foo>>"],
    [["(|the )sum of <<foo>> and <<bar>>", "<<foo>> added to <<bar>>"], "<<foo>> + <<bar>>"],
    [["<<x>> divided by <<y>>"], "<<x>>/<<y>>"],
    [["(|the )product of <<x>> and <<y>>", "<<x>> times <<y>>"], "<<x>>*<<y>>"],
    [["<<x>> minus <<y>>"], "<<x>> - <<y>>"],
    [["<<foo>> is divisible by <<bar>>"], "compare int [(<<foo>> % <<bar>>), 0]"],
    [["<<x>> (is) (less|fewer) than <<y>>"], "<<x>> < <<y>>"],
    [["<<x>> (>|is (greater|more) than) <<y>> and (<|less than) <<z>>", "<<x>> (<|is less than) <<z>> and (>|(greater|more) than) <<y>>"], "(<<x>> > <<y>>) and (<<x>> < <<z>>)"],
    [["until <<x>> : <<y>>"], "while(not <<x>>): <<y>>"],
    [["<<x>> multiplied by <<y>>"], "<<x>> * <<y>>"],
    [["(|the )quotient of <<x>> and <<y>>"], "<<x>> / <<y>>"],
    [["<<x>> in <<y>> (where|such that) <<z>>", "(every|all|each) <<x>> in <<y>> (where|such that) <<z>>"], "<<z>> for <<x>> in <<y>>"],
    
    [["numbers in <<foo>> that are divisible by <<bar>>"], "(x is divisible by <<bar>>) for x in <<foo>>"],
    [["numbers in <<x>> that are even"], "(y is divisible by 2) for y in <<z>>"],
    [["<<x>> is an even number"], "<<x>> is divisible by 2"],
    [["<<y>> is an odd number"], "not (<<y>> is an even number)"],
    [["numbers in <<x>> that are odd"], "(y is an odd number) for y in <<x>>"],
    [["numbers in <<foo>> that are greater than <<bar>>"], "(x > <<bar>>) for x in <<foo>>"],
    [["numbers in <<foo>> that are less than <<bar>>"], "(x < <<bar>>) for x in <<foo>>"],
    #[["<<functionName>> <<parameters>> = <<toReturn>>"]],
    [["every string in <<foo>> that is a substring of <<bar>>"], "every x in <<foo>> such that (x is a substring of <<bar>>)"],
    [["the <<type>>s <<foo>> and <<bar>> are equal", "the <<type>> <<foo>> (equals|is equal to) <<bar>>", "compare the <<type>> <<foo>> to <<bar>>", "compare <<foo>> to <<type>> <<bar>>"], "compare the <<type>>s [<<foo>>, <<bar>>]"],
    [["<<foo>> (equals|is equal to) the <<type>> <<bar>>"], "the <<type>> <<foo>> equals <<bar>>"],
    [["the string <<foo>> concatenated to the string <<bar>>", "concatenate the string <<foo>> to the string <<bar>>"], "concatenate these strings: [<<foo>>, <<bar>>]"],
    [["<<foo>> != <<bar>>"], "not (the integer <<foo>> equals <<bar>>)"],
    [["<<foo>> (does not equal|is not equal to) <<bar>>"], "<<foo>> != <<bar>>"],
    [["(the |)(first|initial) (letter|character) of the string <<str>>"], "index 0 of string <<str>>"],
    [["def <<type>> <<name>> <<body>>"], "def <<type>> <<name>> None None <<body>>"],
    [["the <<type>>s <<foo>> are equal"], "compare the <<type>>s <<foo>>"],
    [["<<foo>> . <<bar>> = <<baz>>"], "((<<foo>> . <<bar>>) = <<baz>>)"],
    [["a random index of the array <<foo>>"], "a random number between (0 -1) and (the length of the array <<foo>>)"],
    [["(a |)random (item|element) (from|in|of|selected from) the (list|array) <<foo>>"], "index (a random index of the array <<foo>>) in the array <<foo>>"],
    [["for <<a>> from <<b>> to <<c>> (if|where) <<d>> <<body>>"], "for <<a>> from <<b>> to c (if <<d>> (, <<body>>))"],
    [["for <<type>> <<a>> in <<b>> if <<d>> <<body>>"], "for <<type <<a>> in <<b>> (if <<d>> (, body))"],
]