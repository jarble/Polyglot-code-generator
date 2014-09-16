;; ==============================================
;; Script: rebolide.r
;; downloaded from: www.REBOL.org
;; on: 11-Aug-2014
;; at: 18:44:43.038427 UTC
;; owner: crazyaxe [script library member who can
;; update this script]
;; ==============================================
;; ===============================================
;; email address(es) have been munged to protect
;; them from spam harvesters.
;; If you were logged on the email addresses would
;; not be munged
;; ===============================================
Rebol [ 
Title: "Rebolide" 
File: %rebolide.r 
Author: "Massimiliano Vessi" 
Date: 2010-12-31 
Version: 5.4.39
email: %maxint--tiscali--it
Purpose: {A Rebol IDE for beginners that helps learning Rebol. 
	I suggest you to put this script in a separete folder.} 
Library: [ level: 'intermediate
platform: 'all 
type: [tool demo ide] 
domain: [all] 
tested-under: [view 2.7.7.3.1 Windows Linux ] 
support: %maxint--tiscali--it 
license: 'gpl
see-also: none ] 
]


;thanks to Graham, Nick Antonaccio, Semseddin Moldibi, Zoltan Eros, R. v.d.Zee

yv1:  to-block { label "Words" return label "Blocks" return label "Functions" return label "Objects"}
; function to find object, function, etc. in your source
findall: func [ a_findall /local temp temp2  ] [
	temp: copy []
	temp: copy to-block  a_findall	
	variabili: copy []
	funzioni: copy []
	blocchi: copy []
	oggetti: copy []
	foreach item temp [
		tipo: false
			if ((type? item) = set-word!) [	
			if   (  temp/2  = 'func ) [ append funzioni item   tipo: true ]
			if   (  temp/2 = 'make ) [ append oggetti  item tipo: true]
			if   ( (type? temp/2 ) = block! ) [ append blocchi  item tipo: true]
			if tipo = false [ append variabili  item ]		
			]
		temp: next temp
		]	
	sort funzioni
	sort oggetti
	sort blocchi
	sort variabili
	return (reduce [ "functions"  funzioni "objects" oggetti "blocks" blocchi "words" variabili])	
	]


;Return the usage of every command
utilizzo:  func [
    "Prints information about words and values."
    'word [any-type!]
    /local value args item type-name refmode types attrs rtype temp4
][
temp4: copy []
if all [word? :word not value? :word] [word: mold :word]
    if any [string? :word all [word? :word datatype? get :word]] [
        types: dump-obj/match system/words :word
        sort types
        if not empty? types [
            return reform ["Found these words:" newline types]
            exit
        ]
        return reform ["No information on" word "(word has no value)"]
        exit
    ]
    type-name: func [value] [
        value: mold type? :value
        clear back tail value
        join either find "aeiou" first value ["an "] ["a "] value
    ]
    if not any [word? :word path? :word] [
        return reform [mold :word "is" type-name :word]
        exit
    ]
    value: either path? :word [first reduce reduce [word]] [get :word]
    if not any-function? :value [
        append temp4 [uppercase mold word "is" type-name :value "of value: "]
        append temp4 either object? value [print "" dump-obj value] [mold :value]
         return reform temp4
        exit
    ]
    args: third :value
    
    append temp4  "USAGE: "
    if not op? :value [append temp4 (append uppercase mold word " ")]
    while [not tail? args] [
        item: first args
        if :item = /local [break]
        if any [all [any-word? :item not set-word? :item] refinement? :item] [
            append temp4 (append mold :item " ")
            if op? :value [append temp4 (append uppercase mold word " " value: none)]
        ]
        args: next args
    ]
    return reform temp4
    ]



;functio to insert text in the source area
inni: func [testo2 /local temp3] [
	set-text/caret a testo2	
	temp3: parse testo2 none
	temp3: to-word first temp3
	temp3: utilizzo :temp3	
	uso/text: to-string temp3
	show uso
	]


filep: none ;file path and name

;save as file function
saveas: func [] [
	filen: request-value  "File name?" 
	filed: to-file request-dir
	filep:  to-file rejoin [ filed  filen]
	salva
	]
	
;save file function
salva: func [] [
	if filep = none [ saveas ]
	write filep a/text
	set-text testo reform ["Saved as " filep ]
	]



;to launch soirce or examples
lancia: func [ temp /local corpo ] [	
	corpo: copy temp
	insert corpo "Rebol [] "
	write %temp.r  corpo	
	launch (clean-path %temp.r) ;clean-path is necessary on Linux
	]


;check Rebgui existance and version
if not (exists? %rebgui.r) [ 
	Alert  "Rebgui not found, I'll try to download it"		
	temp: request-download http://www.dobeash.com/RebGUI/rebgui.r 
	temp: decompress skip temp 8
	write %rebgui.r  temp
	]
if  (exists? %rebgui.r ) [
  temp: load/header %rebgui.r
  if (temp/1/version <> 117 ) [ alert "Watch out, your RebGUI version is different from 117; this script could not work properly!"]
]

;block with al converion functions
allconverions:  [to-binary 
    to-bitset to-block to-char to-closure to-datatype to-date to-decimal to-email to-error to-file to-function to-get-path to-get-word to-hash 
    to-hex to-idate to-image to-integer to-issue to-itime to-library to-list to-lit-path to-lit-word to-local-file to-logic to-map 
    to-money to-none to-pair to-paren to-path to-port to-rebol-file 
    to-refinement to-relative-file to-set-path to-set-word to-string to-tag to-time to-tuple to-typeset to-url to-word
]


do %rebgui.r



display "Rebolide" [


 
menu #LW data [ 
	"File" [
		"Open"  [filep:  to-file request-file
			temp: read filep
			set-text a  temp
			set-text testo reform ["Opened " filep ]
			] 
		"Save (CTRL+D)"  [ 
			salva ;it save the source text
			]  
		"Save as... (CTRL+SHIFT+D)" [ 
			saveas
			write filep a/text
			]  
		]
	"Modify" [ 
		"GO! (CTRL+G)" [lancia a/text  ]
		"Modify colors" [ request-ui]
		]  
	"Help" [ 
		"About" [display "about" aboutpage] 
		"Shortcuts" [display "Shortcuts" shortcuts]
		"Core" [ view/new coremanual_main ]
		"VID" [ 
			if not exists? %nyc.jpg [
				attempt [
					temp: read/binary http://www.rebol.com/view/nyc.jpg
					write/binary %nyc.jpg temp
					]
				]	
			display "VID Guide" guida_vid 
			]
		"VID events" [ display "Vid events guide" guida_handler]	
		"DRAW" [ display "DRAW dialect guide" guida_DRAW]
		"SHAPE" [ display "SHAPE dialect guide"  guida_shape  ] 
		
		]
	] 
button -1 "GO!" [ lancia a/text]
text -1 (rejoin ["Version: " system/script/header/version ])

return

a: area 90x113 on-key [
	if event/key = #"^D" [ salva]   
	if (event/key = #"^D") and event/shift  [ saveas]   
	if (event/key = #"^G")  [lancia a/text  ]
	true]  
tab-panel  data [
	"Core" [
		scroll-panel 80x100 data [
			button -1 "Example" [ inni {Rebol []
print "Hello word!"
wait 10} ] tip "Example"
			return 
			group-box "Comparison" data [
				button -1 "<" [ inni "< " ] tip "Returns TRUE if the first value is less than the second value"
				button -1 "<=" [ inni "<= " ] tip "Returns TRUE if the first value is less than or equal to the second value"
				button -1 "<>" [ inni "<> " ] tip "Returns TRUE if the values are not equal"
				button -1 "=" [ inni "= " ] tip "Returns TRUE if the values are equal"
				button -1 "==" [ inni "== " ]  tip "Returns TRUE if the values are equal and of the same datatype"
				return 
				button -1 "=?" [ inni "=? " ]  tip "Returns TRUE if the values are identical.(same memory)"
				button -1 ">" [ inni "> " ]  tip "Returns TRUE if the first value is greater than the second value"
				button -1 ">=" [ inni ">= " ]  tip "Returns TRUE if the first value is greater than or equal to the second value"
				button -1 "!=" [ inni "!= " ]  tip "Returns TRUE if the values are not equal"
				button -1 "!==" [ inni "!== " ]  tip "Returns TRUE if the values are not equal and not of the same datatype"
				return 
				button -1 "=?" [ inni "?= " ]  tip "Returns TRUE if the values are identical"
				]
			return 
			group-box "Context" data [
				button -1 "alias" [ inni "alias " ]  tip "Creates an alternate alias for a word"
				button -1 "bind" [ inni "bind /copy " ]  tip "Binds words to a specified context"
				button -1 "bind?" [ inni "bind?  " ]  tip "Returns the context in which a word is bound?"
				button -1 "body-of" [ inni "body-of  " ]  tip "Returns a copy of the body of a function or object"
				return 
				button -1 "bound?" [ inni "bound?  " ]  tip "Returns the context in which a word is bound"
				return 
				button -1 "closure" [ inni "closure [] []  " ]  tip "Defines a closure function"
				button -1 "closure?" [ inni "closure? " ]  tip "Returns TRUE if it is this type"
				button -1 "collect" [ inni "collect /into [] " ]  tip "Evaluates a block, storing values via KEEP function, and returns block of collected values"
				return 
				button -1 "collect-words" [ inni "collect-words /deep /set /ignore [] " ]  tip " Collect unique words used in a block (used for context construction)"
				
				button -1 "construct" [ inni "construct /with " ]  tip "Creates an object, but without evaluating its specification"
				return 
				button -1 "context" [ inni "context " ]  tip "Defines a unique (underived) object"
				button -1 "default" [ inni "default " ]  tip "Set a word to a default value if it hasn't been set yet"
				button -1 "free" [ inni "free " ]  tip " Frees a REBOL resource. (Command version only)"
				button -1 "get" [ inni "get /any " ]  tip "Gets the value of a word"
				button -1 "in" [ inni "in " ]  tip "Returns the word in the object's context"
				
				
				return 
				button -1 "link-app?" [ inni "link-app? " ]  tip " Tell whether a script is running under a Link application context"				
				button -1 "protect" [ inni "protect " ]  tip "Protect a word or block to prevent from being modified"
				button -1 "protect-system" [ inni "protect-system " ]  tip "Protects all system functions and the system object from redefinition"
				return 
				button -1 "reflect" [ inni "reflect" ]  tip "Returns definition-related details about a value"				
				button -1 "resolve" [ inni "resolve /only /all " ]  tip "Copy context by setting values in the target from those in the source."     
				button -1 "set" [ inni "set /any /pad " ]  tip "Sets a word or block of words to specified value(s)"
				button -1 "unbind" [ inni "unbind  /deep" ]  tip "Unbinds words from context"
				return 
				button -1 "unset?" [ inni "unset?  " ]  tip "Returns TRUE for unset values"
				return 
				button -1 "unprotect" [ inni "unprotect " ]  tip "Unprotects a word or block of words"
				 
				button -1 "unset" [ inni "unset " ]  tip "Unsets the value of a word"				
				button -1 "use" [ inni "use " ]  tip "Defines words local to a block"
				button -1 "value?" [ inni "value? " ]  tip "Returns TRUE if the word has been set"
				
				
				]
			return 
			group-box "Control" data [
				button -1 "also" [ inni "also [] []  " ]  tip " Returns the first value, but also evaluates the second"
				button -1 "break" [ inni "break /return " ]  tip "Breaks out of a loop, while, until, repeat, foreach, etc"
				button -1 "case" [ inni "case /all [] " ]  tip " Evaluates each condition, and when true, evaluates what follows it."
				button -1 "catch" [ inni "catch [ throw ] " ]  tip "Catches a THROW from a block and returns its value"
				return				
				button -1 "disarm" [ inni "disarm " ]  tip "Returns the error value as an object"
				button -1 "do" [ inni "do /args /next [] " ]  tip "Evaluates a block, file, URL, function, word, or any other value"
				button -1 "do-boot" [ inni "do-boot " ]  tip "Does a value only if it and its file (URL) and it's dependent exists"
				button -1 "do-browser" [ inni "do-browser " ]  tip "Evaluate browser script"
				return 
				button -1 "do-events" [ inni "do-events " ]  tip " Process all View events"
				button -1 "do-face" [ inni "do-face " ]  tip "(undocumented)"
				button -1 "do-face-alt" [ inni "do-face-alt " ]  tip "(undocumented)"
				return 
				button -1 "do-thru" [ inni "do-thru /args /update /check /boot " ]  tip "Do a net file from the disk cache"
				button -1 "does" [ inni "does [] " ]  tip "A shortcut to define a function that has no arguments or locals"
				button -1 "either" [ inni "either [] []  " ]  tip "If condition is TRUE, evaluates the first block, else evaluates the second"
				button -1 "else" [ inni "else []  " ]  tip "Else is obsolete; use either"
				return 
				button -1 "exists-thru?" [ inni "exists-thru? /check  " ]  tip "Checks if a file is in the disk cache. Returns: none, false (out of date), or file"
				 button -1 "exit" [ inni "exit " ]  tip "Exits a function, returning no value"
				button -1 "for" [ inni "for word start end bump [] " ]  tip "Repeats a block over a range of values"
				button -1 "forall" [inni "forall " ] tip "Evaluates a block for every value in a series"
				return 
				button -1 "foreach" [inni "foreach word series [] " ] tip "Evaluates a block for each value(s) in a series"
				button -1 "forever" [ inni "forever [] " ]  tip "Evaluates a block endlessly"
				button -1 "forskip" [ inni "forskip word skip-num series [] " ]  tip "Evaluates a block for periodic values in a series"
				return
				button -1 "func" [ inni {func [ /local "usage" /refinemet "refinemet usage"] []} ]  tip "Creates a function"
				button -1 "funct" [ inni {funct [spec body /with object]} ]  tip "Defines a function with all set-words as locals"
				button -1 "function" [ inni {function [spec var body]} ]  tip "Defines a user function with local words"
				button -1 "halt" [ inni "halt " ]  tip "Stops evaluation and returns to the input prompt"
				button -1 "has" [ inni "has " ]  tip "A shortcut to define a function that has local variables but no arguments"
				return 
				button -1 "if" [ inni "if  cond [] " ]  tip "If condition is TRUE, evaluates the block"
				return
				button -1 "in-dir" [ inni "in-dir " ]  tip "Evaluate a block while in a directory"
				button -1 "launch" [ inni "launch " ]  tip "Launches a new REBOL interpreter process"
				button -1 "launch-thru" [ inni "launch-thru /update /check " ]  tip " Launch a net file from the disk cache"
				button -1 "loop" [ inni "loop n [] " ]  tip "Evaluates a block a specified number of times"
				return 			
				button -1 "repeat" [ inni "repeat " ]  tip "Evaluates a block a specified number of times"
				button -1 "quit" [ inni "quit " ]  tip "Stops evaluation and exits the interpreter"
				button -1 "quote" [ inni "quote " ]  tip "Returns the value passed to it without evaluation"
				button -1 "reduce" [ inni "reduce " ]  tip "Evaluates an expression or block expressions and returns the result"
				return
				button -1 "rejoin" [ inni "rejoin " ]  tip "Reduces and joins a block of values"
				button -1 "return" [ inni "return " ]  tip "Returns a value from a function"
				button -1 "secure" [ inni "secure []  " ]  tip "Specifies security policies (access levels and directories)"
				button -1 "switch" [ inni "switch /default [] " ]  tip "Selects a choice and evaluates what follows it"
				return				
				button -1 "throw" [ inni "throw /name " ]  tip "Throws control back to a previous catch"
							
				button -1 "until" [ inni "until []  " ]  tip "Evaluates a block until its last command is TRUE"
				button -1 "unless" [ inni "unless  " ]  tip "Evaluates the block if condition is not TRUE"
				return
				button -1 "wait" [ inni "wait /all " ]  tip "Waits for a duration, port, or both"				
				button -1 "while" [ inni "while [] [] " ]  tip "While the first block is TRUE, evaluates the second block"				
				]
			return 
			group-box "Datatype" data [
					button -1 " datatypes" [ inni " datatypes  " ]  tip "Variable that contains all datatypes"
					return 
				group-box "Conversion" data [
					button -1 "to" [ inni "to binary!/bitset!/block!/char!/date!/decimal!/email!/file!/get-word!/hash!/hex!/idate!/image!/integer!/issue!/list!/lit-path!/lit-word!/logic!/money!/pair!/paren!/path!/refinement!/set-path!/set-word!/string!/tag!/time!/tuple!/url!/word!" ]  tip "Constructs and returns a new value after conversion"
					text "or"
					drop-list "to-"  30 data allconverions [ inni  face/text ]
					return 
					button -1 "as-pair" [ inni "as-pair  " ]  tip "Combine X and Y values into a pair"
					button -1 "as-binary" [ inni "as-binary  " ]  tip "Coerces any type of string into a binary! datatype without copying it"
					button -1 "as-string" [ inni "as-string  " ]  tip "Coerces any type of string into a string! datatype without copying it"
					return 
					button -1 "cvs-date" [ inni "cvs-date  " ]  tip "Converts CVS date"
					button -1 "cvs-version" [ inni "cvs-version  " ]  tip "Converts CVS version number"
					]
				return 

				button -1 "action?" [ inni "action?  " ]  tip "Returns TRUE for action values"
				return 				
				button -1 "ascii?" [ inni "ascii?  " ]  tip " Returns TRUE if value or string is in ASCII character range (below 128)"
				button -1 "binary?" [ inni "binary? " ]  tip "Returns TRUE for binary values"
				return
				button -1 "bitset?" [ inni "bitset?  " ]  tip "Returns TRUE for bitset values"
				button -1 "block?" [ inni "block?  " ]  tip " Returns TRUE for block values"
				button -1 "char?" [ inni "char?  " ]  tip " Returns TRUE for char values"				
				button -1 "datatype?" [ inni "datatype?  " ]  tip "Returns TRUE for datatype values"				
				return
				button -1 "date?" [ inni "date?  " ]  tip "Returns TRUE for date values"
				button -1 "decimal?" [ inni "decimal? " ]  tip "Returns TRUE for decimal values"
				button -1 "email?" [ inni "email?  " ]  tip " Returns TRUE for email values"
				return
				button -1 "error?" [ inni "error?  " ]  tip "Returns TRUE for error values"
				button -1 "function?" [ inni "function?  " ]  tip "Returns TRUE for function values"
				button -1 "get-word?" [ inni "get-word?  " ]  tip " Returns TRUE for get-word values"
				return 
				button -1 "get-path?" [ inni "get-path?  " ]  tip " Returns TRUE for get-path values"
				return
				button -1 "hash?" [ inni "hash?  " ]  tip "Returns TRUE for hash values"
				button -1 "image?" [ inni "image?  " ]  tip "Returns TRUE for image values"
				button -1 "integer?" [ inni "integer?  " ]  tip " Returns TRUE for integer values"
				button -1 "issue?" [ inni "issue?  " ]  tip "Returns TRUE for issue values"
				return
				button -1 "library?" [ inni "library?  " ]  tip "Returns TRUE for library values"
				button -1 "list?" [ inni "list?  " ]  tip "Returns TRUE for list values"
				button -1 "lit-path?" [ inni "lit-path?  " ]  tip " Returns TRUE for lit-path values"
				return
				button -1 "lit-word?" [ inni "lit-word?  " ]  tip " Returns TRUE for lit-word values"
				button -1 "logic?" [ inni "logic?  " ]  tip " Returns TRUE for logic values"
				button -1 "make" [ inni "make  " ]  tip " Constructs and returns a new value"
				return
				button -1 "map?" [ inni "map?  " ]  tip "Returns TRUE for hash values"
				button -1 "money?" [ inni "money?  " ]  tip " Returns TRUE for money values"
				button -1 "native?" [ inni "native?  " ]  tip "Returns TRUE for native values"
				return 
				button -1 "native" [ inni "native  " ]  tip "(undocumented)"
				button -1 "none?" [ inni "none?  " ]   tip "Returns TRUE for none values"
				return
				button -1 "number?" [ inni "number?  " ]  tip "Returns TRUE for number values"
				button -1 "object?" [ inni "object?  " ]  tip "Returns TRUE for object values"
				button -1 "op?" [ inni "op?  " ]  tip " Returns TRUE for op values"
				return
				button -1 "pair?" [ inni "pair?  " ]  tip " Returns TRUE for pair values"
				button -1 "paren?" [ inni "paren?  " ]  tip " Returns TRUE for paren values"
				button -1 "path?" [ inni "path?  " ]  tip "Returns TRUE for path values"
				button -1 "port?" [ inni "port?  " ]  tip " Returns TRUE for port values"
				return
				button -1 "refinement?" [ inni "refinement?  " ]  tip "Returns TRUE for refinement values"
				button -1 "routine?" [ inni "routine?  " ]   tip "Returns TRUE for routine values"
				return
				button -1 "series?" [ inni "series?  " ]  tip "Returns TRUE for series values"
				button -1 "set-path?" [ inni "set-path?  " ]  tip "Returns TRUE for set-path values"
				button -1 "set-word?" [ inni "set-word?  " ]  tip "Returns TRUE for set-word values"
				return
				button -1 "scalar?" [ inni "scalar?  " ]  tip " Returns TRUE for scalar values"
				button -1 "string?" [ inni "string?  " ]  tip " Returns TRUE for string values"
				button -1 "struct?" [ inni "struct? " ]  tip "Returns TRUE for struct values"
				button -1 "tag?" [ inni "tag?  " ] tip "Returns TRUE for tag values"
				return
				button -1 "time?" [ inni "as-pair  " ] tip "Returns TRUE for time values"
				return 
				button -1 "tuple?" [ inni "tuple?  " ]  tip "Returns TRUE for tuple values"
				button -1 "type?" [ inni "type?  " ]  tip "Returns a value's datatype"
				button -1 "typeset?" [ inni "typeset?  " ]  tip "Returns TRUE if it is this type"
				return
				button -1 "unset?" [ inni "unset?  " ]  tip "Returns TRUE for unset values"
				button -1 "url?" [ inni "url?  " ]  tip " Returns TRUE for url values"
				button -1 "utf?" [ inni "utf?  " ]  tip "Returns the UTF encoding from the BOM (byte order marker): + for BE; - for LE"
				button -1 "word?" [ inni "word?  " ]  tip " Returns TRUE for word values"
				]
			return 
			group-box "Debug"  data [
				button -1 "asert" [ inni "assert [] " ]  tip "Assert that condition is true, else throw an assertion error"
				button -1 "attempt" [ inni "attempt [] " ]  tip "Tries to evaluate and returns result or NONE on error"
				button -1 "cause-error" [ inni "cause-error  err-type err-id args " ]  tip "Causes an immediate error with the provided information"
				return 
				button -1 "comment" [ inni "comment []  " ]  tip "Ignores the argument value and returns nothing"
				button -1 "component?" [ inni "component?  " ]  tip "Returns specific REBOL component info if enabled"
				button -1 "dump-obj" [ inni "dump-obj /match " ]  tip "Returns a block of information about an object"				
				return 
				button -1 "dbug" [ inni "dbug " ]  tip "(Undocumented)"
				button -1 "probe" [ inni "probe " ]  tip "Prints a molded, unevaluated value and returns the same value"
				return 
				button -1 "source" [ inni "source " ]  tip "Prints the source code for a word"
				button -1 "stats" [ inni "stats /pools /types /series /frames /recycle /evals /clear " ]  tip "System statistics.  Default is to return total memory used"
				button -1 "trace" [ inni "trace /net /function " ]  tip "Enables and disables evaluation tracing"
				button -1 "throw-error" [ inni "throw-error " ]  tip "Causes an immediate error throw with the provided information"
				return 
				button -1 "throw-on-error" [ inni "throw-on-error " ]  tip "Evaluates a block, which if it results in an error, throws that error"
				button -1 "title-of" [ inni "title-of " ]  tip "Returns a copy of the title of a function"
				button -1 "try" [ inni "try [] " ]  tip "Tries to DO a block and returns its value or an error"
				return 
				button -1 "types-of" [ inni "types-of " ]  tip "Returns a copy of the types of a function"
				button -1 "values-of" [ inni "values-of " ]  tip "Returns a copy of the values of an object"
				button -1 "vbug" [ inni "vbug " ]  tip "(undocumented)"
				button -1 "?" [ inni "? " ]  tip "Prints information about words and values"
				button -1 "??" [ inni "?? " ]  tip "Prints a variable name followed by its molded value"
				return
				button -1 "about" [ inni "about " ]  tip "Information about REBOL"
				button -1 "what" [ inni "what " ]  tip "Prints a list of globally-defined functions"
				button -1 "words-of" [ inni "words-of " ]  tip "Returns a copy of the words of a function or object"
				]
			return			 
			group-box "Email" data [
				button -1 "build-attach-body" [ inni "build-attach-body  BODY FILES BOUNDARY_STRING" ]  tip "Return an email body with attached files"
				button -1 "build-markup" [ inni "build-markup /quite" ]  tip "Return markup text replacing <%tags%> with their evaluated results"
				return 
				button -1 "build-tag" [ inni "build-tag " ]  tip "Generates a tag from a composed block"
				button -1 "import-email" [ inni "import-email /multiple " ]  tip "Constructs an email object from an email message"
				return 
				button -1 "parse-email-addrs" [ inni "parse-email-addrs " ]  tip "Create a series from a string conaining multiple email adresses."
				button -1 "send" [ inni "send /only /header /attach /subject /show address message " ]  tip "Send a message to an address(es)"
				button -1 "resend" [ inni "resend " ]  tip "Relay a message"
				]
			return 
			group-box "Encryption & Compression" data [
				button -1 "compress" [ inni "compress  " ]  tip "Compresses a string series and returns it"
				button -1 "decompress" [ inni "decompress  " ]  tip "Decompresses a binary series back to a string"
				return
				button -1 "shift" [ inni "shift /left /logical /part   " ]  tip " Perform a bit shift operation. Right shift (decreasing) by default"
				return 
				button -1 "encloak" [ inni "encloak /with " ]  tip "Scrambles a string or binary based on a key"
				button -1 "decloak" [ inni "decloak /with  " ]  tip " Descrambles the string scrambled by encloak"
				return 
				button -1 "dh-compute-key" [ inni "dh-compute-key  " ]  tip "Computes the resulting, negotiated key from a private/public key pair and the peer's public key"
				button -1 "dh-generate-key" [ inni "dh-generate-key  " ]  tip "Generates a new DH private/public key pair"
				return 
				button -1 "dh-make-key" [ inni "dh-make-key  /generate " ]  tip "Creates a key object for DH"
				return 
				button -1 "dsa-generate-key" [ inni "dsa-generate-key " ]  tip "Generates a new private/public key pair"
				button -1 "dsa-make-key" [ inni "dsa-make-key /generate" ]  tip "Creates a key object for DSA"
				return 
				button -1 "dsa-make-signature" [ inni "dsa-make-signature /sign " ]  tip "Creates a DSA signature"
				return 
				button -1 "dsa-verify-signature" [ inni "dsa-verify-signature  " ]  tip "Verifies if the DSA signature of a binary is correct"
				return 
				button -1 "rsa-encrypt" [ inni "rsa-encrypt /decrypt /private /padding  " ]  tip "Encrypts or decrypts some data"
				button -1 "rsa-generate-key" [ inni "rsa-generate-key " ]  tip "Creates a new private/public key pair"
				return 
				button -1 "rsa-make-key" [ inni "rsa-make-key " ]  tip "Creates a key object for RSA"
				]
			return 
			group-box "File & Directory" data [
				button -1 "to-local-file" [ inni "to-local-file  " ]  tip "Converts a REBOL file path to the local system file path"
				button -1 "to-rebol-file" [ inni "to-rebol-file  " ]  tip "Converts a local system file path to a REBOL file path"
				return 
				button -1 "change-dir" [ inni "change-dir " ]  tip "Changes the active directory path"				
				button -1 "cd" [ inni "cd " ]  tip "Change directory (shell shortcut function)"
				button -1 "clean-path" [ inni "clean-path " ]  tip "Cleans-up '.' and '..' in path; returns the cleaned path"
				return 
				button -1 "create-link" [ inni "create-link /start /note /args " ]  tip "Creates file links"
			
				button -1 "delete" [ inni "delete " ]  tip "Deletes the specified file(s) or empty directory(s)"
				button -1 "delete-dir" [ inni "delete-dir " ]  tip "Deletes a directory including all files and subdirectories"
				return
				button -1 "dir?" [ inni "dir? " ]  tip "Returns TRUE if a file or URL is a directory"
				button -1 "dirize" [ inni "dirize " ]  tip "Returns a copy of the path turned into a directory"
				button -1 "echo" [ inni "echo %file  ^/  echo none " ]  tip "Copies console output to a file"
				button -1 "exists?" [ inni "exists? " ]  tip "Determines if a file or URL exists"
				return
				button -1 "file?" [ inni "file? " ]  tip " Returns TRUE for file values"
				button -1 "info?" [ inni "info? " ]  tip "The information is returned within an object that has SIZE, DATE, and TYPE words"
				button -1 "list-dir" [ inni "list-dir " ]  tip "Prints a multi-column sorted listing of a directory"
				return 
				button -1 "link-relative-path" [ inni "link-relative-path " ]  tip "Remove link-root from a file path"				
				button -1 "more" [ inni "more " ]  tip "Print file (shell shortcut function)"
				button -1 "make-dir" [ inni "make-dir " ]  tip "Creates the specified directory. No error if already exists"
				return
				button -1 "modified?" [ inni "modified? " ]  tip "Returns the last modified date of a file or URL"
				button -1 "path-thru" [ inni "path-thru " ]  tip "Return a path relative to the disk cache"
				button -1 "rm" [ inni "rm  /any " ]  tip "Deletes the specified file(s)"
				button -1 "rename" [ inni "rename " ]  tip "Renames a file to a new name"
				return 
				button -1 "pwd" [ inni "pwd " ]  tip " Prints the active directory path"
				button -1 "save" [ inni "save /header /bmp /png /all " ]  tip "Saves a value or a block to a file or url"
				
				button -1 "save-user" [ inni "save-user " ]  tip " Save user.r, prompting for overwrite permission"
				button -1 "size?" [ inni "size? " ]  tip "Returns the size of a file or URL's contents"
				return
				button -1 "split-path" [ inni "split-path " ]  tip "Returns a block containing path and target"
				button -1 "suffix?" [ inni "suffix? " ]  tip "Return the suffix (ext) of a filename or url, else NONE"
				button -1 "undirize" [ inni "undirize" ]  tip {Returns a copy of the path with any trailing "/" removed}
				return 
				button -1 "what-dir " [ inni "what-dir  " ]  tip "Prints the active directory path"
				return
				button -1 "write" [ inni "write /binary /string /append /no-wait /lines /with /allow /mode /custom destination value  " ]  tip "Writes to a file, url, or port-spec"
				button -1 "write-io" [ inni "write-io  " ]  tip "Low level write to a port"
				]	
			
			return 	
			group-box "I/O" data [
				button -1 "ask" [ inni "ask /hide " ]  tip "Ask the user for input"
				button -1 "browse" [ inni "browse /only " ]  tip "Opens the default web browser"
				button -1 "call" [ inni "call /input  /output  /error  /wait /console /shell /info /show " ]  tip "Executes a shell command to run another process"
				button -1 "checksum" [ inni "checksum /tcp /secure /hash /mehod /key  " ]  tip "Returns a CRC or other type of checksum"
				return 
				button -1 "close" [ inni "close " ]  tip "Closes an open port connection"
				return 
				button -1 "connected?" [ inni "connected?  " ]  tip "Returns TRUE when connected to the Internet"
				button -1 "crypt-strength?" [ inni "crypt-strength?  " ]  tip "Returns 'full, 'export or none"
				return
				button -1 "debase" [ inni {debase  /base "" } ]  tip "Converts a string from a different base representation to binary"
				button -1 "decode-cgi" [ inni {decode-cgi } ]  tip "Converts CGI argument string to a block of set-words and value strings"
				button -1 "decode-url" [ inni {decode-url } ]  tip " Decode a URL into an object"
				
				
				return 
				button -1 "dispatch" [ inni "dispatch [] " ]  tip "Wait for a block of ports. As events happen, dispatch port handler blocks"
				button -1 "enbase" [ inni "enbase  " ]  tip "Converts a string to a different base representation"
				
				button -1 "get-env" [ inni "get-env " ]  tip " Gets the value of an operating system environment variable"
				return 
				button -1 "get-modes" [ inni "get-modes " ]  tip "Returns mode settings for a port"
				button -1 "get-net-info" [ inni "get-net-info " ]  tip "(undocumented)"
				
				return
				button -1 "input" [ inni "input /hide " ]  tip "Inputs a string from the console. New-line character is removed"
				button -1 "input?" [ inni "input? " ]  tip "Returns TRUE if input characters are available"
				button -1 "import-email" [ inni "import-email /multiple " ]  tip "Constructs an email object from an email message"
				button -1 "load" [ inni "load /header /next /library /markup /all " ]  tip "Loads a file, URL, or string. Binds words to global context"
				return 
				button -1 "load-image" [ inni "load  /update /clear " ]  tip "Load an image through an in-memory image cache"
				button -1 "load-stock" [ inni "load-stock  /block " ]  tip "Load and return stock image"
				return 
				button -1 "load-stock-block" [ inni "load-stock-block   " ]  tip "Load a block of stock image names. Return block of images"
				button -1 "load-thru" [ inni "load-thru  /update /binary /to local-file /all /expand /check    " ]  tip "Load a net file from the disk cache"
				button -1 "open" [ inni "open /binary /string /direct /new /write /no-wait /lines /with /allow /mode / custom /skip " ]  tip "Opens a new port connection"
				return
				button -1 "parse-xml" [ inni "parse-xml " ]  tip "Parses XML code and returns a tree of blocks"
				button -1 "prin" [ inni "prin " ]  tip "Outputs a value with no line break"
				button -1 "print" [ inni "print  " ]  tip "Outputs a value followed by a line break"
				button -1 "query" [ inni "query  " ]  tip "Returns information about a file, port or URL"
				return
				button -1 "read" [ inni "read  /binary /string /direct /new /write /no-wait /lines /with /allow /mode / custom /skip " ]  tip "Reads from a file, url, or port-spec"
				button -1 "read-io" [ inni "read-io " ]  tip "Low level read from a port"
				button -1 "read-cgi" [ inni "read-cgi /limit " ]  tip "Read CGI data from web server input stream. Return data as string"
				button -1 "read-net" [ inni "read-net /progress " ]  tip "Read a file from the net (web). Update progress bar. Allow abort"
				return 
				button -1 "read-thru" [ inni "read-thru /progress  /update /expand /check /to " ]  tip "Read a net file from thru the disk cache. Returns binary, else none on error"
				button -1 "script?" [ inni "script? " ]  tip "Checks file, url, or string for a valid script header"
				button -1 "set-modes" [ inni "set-modes " ]  tip "Changes mode settings for a port"
				return
				button -1 "set-net" [ inni "set-net " ]  tip "Network setup"
				
				button -1 "update" [ inni "update " ]  tip "Updates the data related to a port"
				
				]	
			return	
			group-box "Logic" data [
				button -1 "all" [ inni "all [] " ]  tip "Shortcut for AND. Evaluates and returns at the first FALSE or NONE"
				button -1 "and" [ inni "and " ]  tip "Returns the first value ANDed with the second"
				button -1 "assert" [ inni "assert " ]  tip "Assert that condition is true, else throw an assertion error"
				return 
				button -1 "any" [ inni "any [] " ]  tip "Shortcut OR. Evaluates and returns the first value that is not FALSE or NONE"
				button -1 "any-block?" [ inni "any-block? [] " ]  tip " Returns TRUE for any block values"
				return 
				button -1 "any-function?" [ inni "any-function? [] " ]  tip " Returns TRUE for any function values"
				button -1 "any-object?" [ inni "any-object? [] " ]  tip " Returns TRUE for any object values"
				return 
				button -1 "any-path?" [ inni "any-path? [] " ]  tip " Returns TRUE for any path values"
				button -1 "any-string?" [ inni "any-string? [] " ]  tip " Returns TRUE for any string values"
				button -1 "any-type?" [ inni "any-type? [] " ]  tip " Returns TRUE for any type values"
				return 
				button -1 "any-word?" [ inni "any-word? [] " ]  tip " Returns TRUE for any word values"
				return
				button -1 "complement" [ inni "complement " ]  tip "Returns the one's complement value"
				return				
				button -1 "not" [ inni "not " ]  tip "Returns the logic complement"
				button -1 "true?" [ inni "true? " ]  tip "Returns true if an expression can be used as true"
				button -1 "!" [ inni "! " ]  tip "Returns the logic complement"
				button -1 "or" [ inni "or " ]  tip "Returns the first value ORed with the second"
				button -1 "xor" [ inni "xor " ]  tip "Returns the first value exclusive ORed with the second"				
				]
			return	
			group-box "Math" data [
				button -1 "*" [ inni "*  " ]  tip "Returns the first value multiplied by the second"
				button -1 "**" [ inni "**  " ]  tip "Returns the first number raised to the second number"
				button -1 "+" [ inni " +  " ]  tip "Returns the result of adding two values"
				button -1 "-" [ inni " -  " ]  tip "Returns the second value subtracted from the first"
				button -1 "/" [ inni " /  " ]  tip "Returns the first value divided by the second"
				button -1 "//" [ inni "//  " ]  tip "Returns the remainder of first value divided by second"
				button -1 "abs" [ inni "abs " ]  tip "Returns the absolute value"
				return
				button -1 ">=" [ inni ">= " ]  tip " Returns TRUE if the first value is greater than or equal to the second value"
				button -1 ">" [ inni ">= " ]  tip " Returns TRUE if the first value is greater than the second value"
				button -1 "=" [ inni "= " ]  tip " Returns TRUE if the first value is equal to the second value"
				button -1 "<" [ inni "< " ]  tip " Returns TRUE if the first value is less than the second value"
				button -1 "<=" [ inni "<= " ]  tip " Returns TRUE if the first value is less than or equal to the second value"
				return 
				button -1 "arccosine" [ inni "arccosine " ]  tip "Returns the trigonometric arccosine in degrees"
				button -1 "arcsine" [ inni "arcsine " ]  tip "Returns the trigonometric arcsine in degrees"
				button -1 "arctangent" [ inni "arctangent " ]  tip "Returns the trigonometric arctangent in degrees"
				return
				button -1 "cosine" [ inni "cosine " ]  tip "Returns the trigonometric cosine in degrees"
				button -1 "even?" [ inni "even? " ]  tip "Returns TRUE if the number is even"
				button -1 "exp" [ inni "exp " ]  tip "Raises E (natural number) to the power specified"
				button -1 "log-10" [ inni "log-10 " ]  tip "Returns the base-10 logarithm"
				return
				button -1 "log-2" [ inni "log-2 " ]  tip "Return the base-2 logarithm"
				button -1 "log-e" [ inni "log-e " ]  tip "Returns the base-E (natural number) logarithm"
				button -1 "maximum-of" [ inni "maximum-of [] " ]  tip "Finds the largest value in a series"
				return
				button -1 "minimum-of" [ inni "minimum-of [] " ]  tip "Finds the smallest value in a series"
				button -1 "mod" [ inni "mod  " ]  tip "Compute a nonnegative remainder of A divided by B"
				button -1 "modulo" [ inni "modulo  " ]  tip "Wrapper for MOD that handles errors like REMAINDER. Negligiblevalues (compared to A and B) are rounded to zero"
				return 
				button -1 "negate" [ inni "negate " ]  tip "Changes the sign of a number"
				button -1 "negative?" [ inni "negative? " ]  tip "Returns TRUE if the number is negative"
				return
				button -1 "odd?" [ inni "odd? " ]  tip "Returns TRUE if the number is odd"
				button -1 "pi" [ inni "pi " ]  tip "3.14159265358979"
				button -1 "positive?" [ inni "positive? " ]  tip "Returns TRUE if the value is positive"
				button -1 "random" [ inni "random /seed /secure /only " ]  tip "Returns a random value of the same datatype"				
				return 
				button -1 "round" [ inni "round /even /down /half-down /floor /ceiling /half-ceiling /to scale"] tip "Returns the nearest integer. Halves round up (away from zero) by default."
				return
				button -1 "sign?" [ inni "sign? " ]  tip "Returns sign of number as 1, 0, or -1"				
				button -1 "sine" [ inni "sine " ]  tip "Returns the trigonometric sine in degrees"
				button -1 "square-root" [ inni "square-root " ]  tip "Returns the square root of a number"
				return 
				button -1 "tangent" [ inni "tangent /radians " ]  tip "Returns the trigonometric tangent in degrees"
				
				button -1 "zero?" [ inni "zero? " ]  tip "Returns TRUE if the number is zero"
				]
			return	
			group-box "Series" data [
				button -1 "ajoin" [ inni "ajoin []" ]  tip " Reduces and joins a block of values into a new string"
				button -1 "alter" [ inni "alter series value " ]  tip "If a value is not found in a series, append it; otherwise, remove it"
				button -1 "append" [ inni "append /only series value " ]  tip "Appends a value to the tail of a series and returns the series head"
				button -1 "apply" [ inni "append /only func [] " ]  tip "Apply a function to a reduced block of arguments"
				button -1 "array" [ inni "array /initial size " ]  tip "Makes and initializes a series of a given size"
				return 
				button -1 "at" [ inni "at series index " ]  tip "Returns the series at the specified index"
				button -1 "back" [ inni "back " ]  tip "Returns the series at its previous position"
				
				button -1 "change" [ inni "change /part /only /dup series value " ]  tip "Changes a value in a series and returns the series after the change"
				button -1 "clear" [ inni "clear " ]  tip "Removes all values from the current index series to the tail. Returns at tail"
				button -1 "compose" [ inni "compose /deep /only [ ( ) ] " ]  tip "Evaluates a block of expressions, only evaluating parens, and returns a block"
				return 
				button -1 "copy" [ inni "copy /part /deep " ]  tip "Returns a series copy"				
				button -1 "cp" [ inni "cp /part /deep " ]  tip "Returns a series copy"
				button -1 "difference" [ inni "difference /case /skip " ]  tip "Return the difference of two series"
				button -1 "exclude" [ inni "exclude " ]  tip "Return the first series less the second"
				return 
				button -1 "extract" [ inni "extract series width " ]  tip "Extracts a value from a series at regular intervals"
				button -1 "empty?" [ inni "empty? " ]  tip "Returns TRUE if a series is at its tail"
				
				button -1 "find" [ inni "find /part /only /case /any /with /skip /match /tail /last /reverse series values " ]  tip "nds a value in a series and returns the series at the start of it"
				button -1 "found?" [ inni "found? " ]  tip "Returns TRUE if value is not NONE"
				return
				button -1 "head" [ inni "head " ]  tip "Returns the series at its head"
				button -1 "head?" [ inni "head? " ]  tip "Returns TRUE if a series is at its head"
				button -1 "index?" [ inni "index? " ]  tip "Returns the index number of the current position in the series"
				button -1 "insert" [ inni "insert /part /only /dup series value " ]  tip "Inserts a value into a series and returns the series after the insert"
				return
				button -1 "intersect" [ inni "intersect /case /skip " ]  tip "Create a new value that is the intersection of the two series"
				button -1 "join" [ inni "join " ]  tip "Concatenates values"
				button -1 "last" [ inni "last " ]  tip "Returns the last value of a series"
				button -1 "last?" [ inni "last? " ]  tip " Returns TRUE if the series length is 1"
				return
				button -1 "length?" [ inni "length? " ]  tip "Returns the length of the series from the current position"
				button -1 "map-each" [ inni "map-each /into " ]  tip " Evaluates a block for each value(s) in a series and returns them as a block"
				button -1 "move" [ inni "move /part /skip /to " ]  tip "Move a value or span of values in a series"
				button -1 "next" [ inni "next " ]  tip "Returns the series at its next position"
				return 
				button -1 "new-line" [ inni "new-line /all /skip  " ]  tip "Sets or clears the new-line marker within a block"
				button -1 "new-line?" [ inni "new-line?  " ]  tip "Returns the state of the new-line marker within a block"
				button -1 "offset?" [ inni "offset? " ]  tip "Returns the offset between two series positions"
				button -1 "pick" [ inni "pick series index " ]  tip "Returns the value at the specified position in a series"
				return 
				button -1 "poke" [ inni "poke series index newdata " ]  tip "Returns value after changing its data at the given index"

				button -1 "remove" [ inni "remove /part " ]  tip "Removes value(s) from a series and returns after the remove"
				button -1 "remove-each" [ inni "remove-each word series body " ]  tip "Removes a value from a series for each block that returns TRUE"
				return
				button -1 "replace" [ inni "replace series search replace " ]  tip "Replaces the search value with the replace value within the target series"
				
				button -1 "repend" [ inni "repend /only series value " ]  tip "Appends a reduced value to a series and returns the series head"
				button -1 "reverse" [ inni "reverse /part " ]  tip "Reverses a series"
				button -1 "reduce" [ inni "reduce  /only " ]  tip "Evaluates an expression or block expressions and returns the result"
				return 				
				button -1 "select" [ inni "select /part /only /case /any /with /skip series value " ]  tip "Finds a value in the series and returns the value or series after it"
							
				button -1 "skip" [ inni "skip series offset " ]  tip "Returns the series forward or backward from the current position"
				button -1 "sort" [ inni "sort /case /skip /compare /part /all /reverse " ]  tip "Sorts a series"
				button -1 "swap" [ inni "swap " ]  tip "Swaps elements of a series. (Modifies)"
				button -1 "tail" [ inni "tail " ]  tip "Returns the series at the position after the last value"
				return
				button -1 "tail?" [ inni "tail? " ]  tip "Returns TRUE if a series is at its tail"
				button -1 "take" [ inni "take /last /part " ]  tip "Copies and removes from series. (Modifies)"
				button -1 "union" [ inni "union /case /skip " ]  tip "Returns all elements present within two blocks or strings ignoring the duplicates"
				button -1 "unique" [ inni "unique /case /skip " ]  tip "Returns a set with duplicate values removed"
				return
				button -1 "++" [ inni "++ " ]  tip "Increment an integer or series index. Return its prior value"
				button -1 "--" [ inni "-- " ]  tip "Decrement an integer or series index. Return its prior value"
				return
				group-box "Data extraction" data [
					button -1 "first" [ inni "first  " ]  tip " Returns the first  value of a series"				
					button -1 "first+" [ inni "first+  " ]  tip "Return FIRST of series, and increment the series index"
					button -1 "second" [ inni "second  " ]  tip " Returns the second value of a series"
					button -1 "third" [ inni "third  " ]  tip " Returns the third value of a series"
					return 
					button -1 "fourth" [ inni "fourth  " ]  tip " Returns the fourth value of a series"
					
					button -1 "fifth" [ inni "fifth  " ]  tip " Returns the fifth  value of a series"
					button -1 "sixth" [ inni "sixth  " ]  tip " Returns the sixth  value of a series"
					button -1 "seventh" [ inni "seventh  " ]  tip " Returns the seventh  value of a series"
					return 
					button -1 "eighth" [ inni "eighth " ]  tip " Returns the eighth value of a series"
					button -1 "ninth" [ inni "ninth  " ]  tip " Returns the ninth  value of a series"
					button -1 "tenth" [ inni "tenth  " ]  tip " Returns the tenth value of a series"
					]
				]
			return	
			group-box "String" data [
				button -1 "build-tag" [ inni "build-tag []  " ]  tip "Generates a tag from a composed block"
				button -1 "charset" [ inni {charset ""} ]  tip "Makes a bitset of chars"
				button -1 "detab" [ inni "detab /size " ]  tip "Converts tabs in a string to spaces,standard tab size is 4"
				button -1 "dehex" [ inni "dehex  " ]  tip "Converts URL-style hex encoded (%xx) strings"
				return 
				button -1 "deline" [ inni "deline  " ]  tip "Converts string terminators to standard format, e.g. CRLF to LF. (Modifies)"				
				button -1 "entab" [ inni "entab /size " ]  tip "Converts spaces in a string to tabs,standard tab size is 4"
				button -1 "enline" [ inni "enline /with " ]  tip " Converts standard string terminators to current OS format, e.g. LF to CRLF. (Modifies)"
				button -1 "form" [ inni "form  " ]  tip "Converts a value to a string"
				return 
				button -1 "latin1?" [ inni "latin1?  " ]  tip "Returns TRUE if value or string is in Latin-1 character range (below 256)"
				 
				button -1 "lowercase" [ inni "lowercase " ]  tip "Converts string of characters to lowercase"		
				button -1 "cr" [ inni "cr " ]  tip "char CR"				
				button -1 "lf" [ inni "lf " ]  tip "char LF"
				button -1 "crlf" [ inni "crlf " ]  tip "char CRLF"
				return 
				button -1 "bs" [ inni "bs " ]  tip "char BACKSPACE"
				
				button -1 "mold" [ inni "mold /only /all /flat " ]  tip "Converts a value to a REBOL-readable string"
				
				button -1 "newline" [ inni "newline " ]  tip "New line char"
				button -1 "newpage" [ inni "newpage " ]  tip "New page char"
				button -1 "tab" [ inni "tab " ]  tip "TAB char"
				return 
				button -1 "escape" [ inni "escape " ]  tip "Escape char"
				return
				button -1 "parse" [ inni "parse /all /case " ]  tip "Parses a series according to rules"
				button -1 "reform" [ inni "reform " ]  tip "Forms a reduced block and returns a string with spaces"
				button -1 "rejoin" [ inni "rejoin " ]  tip "Reduces and returns a string without spaces"
				button -1 "remold" [ inni "remold " ]  tip "Forms a reduced block and returns a string with spaces and sqare-bracket"
				return
				button -1 "trim" [ inni "trim /head /tail /auto /lines /all /with  " ]  tip "Removes whitespace from a string. Default removes from head and tail"
				button -1 "uppercase" [ inni "uppercase /part " ]  tip "Converts string of characters to uppercase"
				button -1 "utf?" [ inni "utf? /utf " ]  tip "Returns the UTF encoding from the BOM (byte order marker): + for BE; - for LE"
				button -1 "invalid-utf?" [ inni "invalid-utf?  " ]  tip " Checks for proper UTF encoding and returns NONE if correct or position where the error occurred."
				]
			return 
			group-box "Time" data [	
				button -1 "now" [ inni "now /year /month /day /time /zone /date /weekday /precise " ]  tip "Returns the current local date and time"
				button -1 "dt" [ inni "dt " ]  tip " Delta-time - returns the time it takes to evaluate the block"
				]		
			return
			group-box "Special" data [
				button -1 "access-os" [ inni "access-os /set" ]  tip "Access to various operating system functions (getuid, setuid, getpid, kill, etc.)"
				button -1 "desktop" [ inni "desktop " ]  tip "Display the REBOL viewtop"
				button -1 "editor" [ inni "editor /app " ]  tip "Lauch internal editor"
				button -1 "help" [ inni "help " ]  tip " Prints information about words and values"
				return 
				button -1 "install" [ inni "install " ]  tip "Install Rebol on windows"
				return 
				button -1 "license" [ inni "license " ]  tip "Prints the REBOL license"
				button -1 "link?" [ inni "link? " ]  tip "Returns true if REBOL/Link capability is enabled"
				button -1 "net-error" [ inni "net-error " ]  tip "(undocumented)"
				return 
				button -1 "open-events" [ inni "open-events " ]  tip "(undocumented)"
				button -1 "parse-header" [ inni "parse-header /multiple" ]  tip " Returns a header object with header fields and their values"
				return 
				button -1 "parse-header-date" [ inni "parse-header-date  " ]  tip "(undocumented)"
				button -1 "path" [ inni "path  " ]  tip "Path selection"
				button -1 "recycle" [ inni "recycle  /off /on /torture " ]  tip " Recycles unused memory"
				return 
				button -1 "run" [ inni "run /as " ]  tip "  Runs the system application associated with a file"
				button -1 "script" [ inni "script " ]  tip "Checks file, url, or string for a valid script header"
				button -1 "secure" [ inni "secure " ]  tip " Specifies security policies (access levels and directories). Returns prior settings"
				button -1 "set-user" [ inni "set-user" ]  tip "(undocumented)"
				return 
				button -1 "set-user-name" [ inni "set-user-name" ]  tip "(undocumented)"
				button -1 "spec-of" [ inni "spec-of " ]  tip "Returns a copy of the spec of a function"
				return 
				button -1 "user-prefs" [ inni "user-prefs " ]  tip "Variable that contains user data"
				button -1 "sound" [ inni "sound " ]  tip "Variable that contains suond settings"
				button -1 "list-env" [ inni "list-env " ]  tip "Returns a block of OS environment variables (for current process)"
				return 
				button -1 "suffix-map" [ inni "suffix-map " ]  tip "Variable that contains suffix identifications (pdf, doc...)"
				button -1 "speed?" [ inni "speed? /no-io /times " ]  tip " Returns approximate speed benchmarks [eval cpu memory file-io]"
				button -1 "uninstall" [ inni "uninstall " ]  tip "Uninstall Rebol under windows"
				return 
				button -1 "upgrade" [ inni "upgrade " ]  tip "Download a new version of REBOL if available"
				button -1 "viewtop" [ inni "viewtop /only " ]  tip "Display the REBOL viewtop"
				button -1 "view-root" [ inni "view-root " ]  tip "Variables that contains Rebol user directory"
				return 
				button -1 "write-user" [ inni "write-user " ]  tip "Write network config to user.r file"
				]
						
			]
		]
	"VID" [

		scroll-panel 80x100 data [
			button -1 "Example" [ inni {view layout [button "Hello World!!!" [alert "Hello word!!!"]]} ]  tip "Typical usage of VID"
			return 			
			group-box "Inform" data [
				button -1 "alert" [ inni "alert " ]  tip " Flashes an alert message to the user. Waits for a user response"
				button -1 "flash" [ inni "flash " ]  tip "Flashes a message to the user and continues"
				button -1 "inform" [ inni "inform /offset /title /timeout " ]  tip "Display an exclusive focus panel for alerts, dialogs, and requestors"
				button -1 "notify" [ inni "notify " ]  tip "lashes an informational message to the user. Waits for a user response"
				]
			return 
			group-box "Request" data [
				button -1 "choose" [ inni "choose /style /window /offset /across " ]  tip "Generates a choice selector menu, vertical or horizontal"
				button -1 "confirm" [ inni "confirm /with " ]  tip "Confirms a user choice"
				button -1 "emailer" [ inni "emailer /to /subject " ]  tip "Pops up a quick email sender"
				button -1 "request" [ inni "request /offset /ok /only /confirm /type /timeout " ]  tip "Requests an answer to a simple question"
				return
				button -1 "request-color" [ inni "request-color /color /offset  " ]  tip " Requests a color value"
				button -1 "request-date" [ inni "request-date /offset " ]  tip "Requests a date"
				return 
				button -1 "request-dir" [ inni "request-dir /title /dir  /keep /offset " ]  tip "Requests a directory"
				return
				button -1 "request-download" [ inni "request-download /to " ]  tip "Request a file download from the net. Show progress. Return none on error"
				button -1 "request-file" [ inni "request-file /title /file /filter /keep /omly /path /save " ]  tip "Requests a file using a popup list of files and directories"
				return
				button -1 "request-list" [ inni "request-list title [] " ]  tip "Requests a selection from a list"
				button -1 "request-pass" [ inni "request-pass  /offset /user /only /title  " ]  tip "Requests a username and password"
				return
				button -1 "request-text" [ inni "request-text /offset /default  " ]   tip "Requests a text string be entered"
				
				]
			return 
			group-box "Colors" data [
				button -1 "aqua" aqua [ inni "aqua  " ]   
				beg: button -1 "base-effect"   [ inni "base-effect " ]   				
				button -1 "black" black [ inni "black  " ]   				
				button -1 "blue" blue [ inni "blue  " ]   
				return 
				button -1 "brown" coal [ inni "brown  " ]   
				button -1 "brick " brick  [ inni "brick   " ] 
				button -1 "beige" beige [ inni "beige  " ] 
				button -1 "base-color" base-color [ inni "base-color  " ]   
				 return 
				button -1 "button-color" 44.80.132 [ inni "button-color  " ]   
				button -1 "bar-color"  bar-color  [ inni "bar-color   " ]   
				bag: button -1 "bar-effect"   [ inni "bar-effect " ]   
				; to apply effects on buttons
				do [
					append beg/effect base-effect  
					append bag/effect bar-effect  
					show [ beg bag]
					]
				return 
				button -1 "coal" coal [ inni "coal  " ]   
				button -1 "cyan" cyan [ inni "cyan  " ]   
				button -1 "coffee" coffee [ inni "coffee  " ]   
				button -1 "crimson" crimson [ inni "crimson  " ]
				return 
				button -1 "forest" forest [ inni "forest  " ]   
				return 
				button -1 "gray" gray [ inni "gray  " ]   
				button -1 "green" green [ inni "green  " ]   
				button -1 "gold" gold [ inni "gold  " ]   
				
				button -1 "ivory" ivory [ inni "ivory  " ]   
				button -1 "khaki" khaki [ inni "khaki  " ]   
				return 
				button -1 "leaf" leaf [ inni "leaf  " ]   
				button -1 "linen" linen [ inni "linen  " ]   
				
				button -1 "maroon " maroon  [ inni "maroon   " ]   
				  
				button -1 "magenta" magenta [ inni "magenta  " ]   
				return 
				button -1 "mint" mint [ inni "mint  " ]
				return 				
				button -1 "main-color" main-color [ inni "main-color  " ]   
				button -1 "navy" navy [ inni "navy  " ]   
				button -1 "olive" olive [ inni "olive  " ]   
				button -1 "orange" orange [ inni "orange  " ] 
				return 
				button -1 "oldrab" oldrab [ inni "oldrab  " ]   
				button -1 "over-color" over-color [ inni "over-color  " ]   
				button -1 "pewter" pewter [ inni "pewter  " ]   
				button -1 "purple"  purple [ inni " purple  " ]   
				return 
				button -1 "pink"  pink [ inni "pink  " ]   
				button -1 "papaya"  papaya [ inni "papaya  " ]   
				  
				button -1 "red" red [ inni "red  " ]   
				button -1 "rebolor" rebolor [ inni "rebolor  " ]   
				return 
				button -1 "reblue" reblue [ inni "reblue  " ]
				return 
				button -1 "silver" silver [ inni "silver  " ] 
				button -1 "snow" snow [ inni "snow  " ] 
				button -1 "sienna" sienna [ inni "sienna  " ] 
				button -1 "sky" sky [ inni "sky  " ] 
				button -1 "teal" teal [ inni "teal  " ] 	
				return 
				button -1 "tan" tan [ inni "tan  " ] 
				return 
				button -1 "violet" violet [ inni "violet  " ] 	
				button -1 "white" white [ inni "white  " ]   
				button -1 "water" water [ inni "water  " ]   
				button -1 "wheat" white [ inni "wheat " ]   
				return 
				button -1 "yello" yello [ inni "yello " ]   
				
				button -1 "yellow" yellow [ inni "yellow " ]   
				]
			return 	
			group-box "Rebol images" data [
				image exclamation.gif [inni "exclamation.gif" ] 
				image info.gif [inni "info.gif" ] 
				image logo.gif [inni "logo.gif" ] 
				return 
				image stop.gif [inni "stop.gif" ] 
				image help.gif [inni "help.gif" ] 
				 
				image btn-up.png [inni "btn-up.png" ] 
				image btn-dn.png [inni "btn-dn.png" ] 
				]	
			return 			
			group-box "Position" data [
				button -1 "across" [ inni "across  " ]   tip "Put items horizontally"
				button -1 "at" [ inni "at  " ]   tip "Put items at the specified position (pair!)"
				button -1 "below" [ inni "below  " ]   tip "Put items vertically (standard)"
				button -1 "guide" [ inni "guide  " ]   tip "Set a guide line"
				button -1 "indent" [ inni "indent  " ]   tip "Indent horizontally"
				return 
				button -1 "offset" [ inni "offset  " ]   tip "Set the output face position"
				button -1 "origin" [ inni "origin  " ]   tip "Specify the layout starting position"
				button -1 "pad" [ inni "pad  " ]   tip "Insert extra spacing"
				button -1 "return" [ inni "return " ]   tip "Return to the current guide position"
				button -1 "space" [ inni "space " ]   tip "Set the auto-spacing used between faces"
				return 
				button -1 "size" [ inni "size " ]   tip "Set the output face size"
				button -1 "tabs" [ inni "tabs  " ]   tip "Secify tab space, even a series fo different spaces. Also pairs!"
				button -1 "tab" [ inni "tab  " ]   tip "Put tab spaces between items"
				]	
				
			return 
			group-box "Text" data [
				button -1 "title" [ inni "title  " ]   tip "Big title"
				button -1 "text" [ inni "text  " ]   tip "Normal text"
				button -1 "head 1" [ inni "h1  " ]   tip "Heding 1"
				button -1 "head 2" [ inni "h2  " ]   tip "Heading 2"
				return 
				button -1 "head 3" [ inni "h3  " ]   tip "Heading 3"
				 
				button -1 "head 4" [ inni "h4  " ]   tip "Heading 4"
				button -1 "head 5" [ inni "h5  " ]   tip "Heading 5"
				return 
				button -1 "code" [ inni "code  " ]   tip "Bold code style text"
				button -1 "tt" [ inni "tt  " ]   tip "Code style text"
				button -1 "banner" [ inni "banner  " ]   tip "Big coloured title"
				return 
				button -1 "video text" [ inni "vtext  " ]   tip "text with shadow"
				button -1 "Video h1" [ inni "vh1  " ]   tip "Heading 1 with shadow"
				button -1 "Video h2" [ inni "vh2  " ]   tip "Heding 2 with shadow"
				return 
				button -1 "Video h3" [ inni "vh3  " ]   tip "Heding 3 with shadow"
				button -1 "Video h4" [ inni "vh4  " ]   tip "Heding 4 with shadow"
				button -1 "Label" [ inni "label  " ]   tip "bold contrasted text"	
				return 
				button -1 "base-text" [ inni "base-text  " ]   tip "text"	
				button -1 "lab" [ inni "lab  " ]   tip "label"	
				button -1 "lbl" [ inni "lbl  " ]   tip "label"	
				button -1 "vlab" [ inni "vlab  " ]   tip "video label"	
				button -1 "txt" [ inni "txt  " ]   tip "text"	
				]
			return 
			group-box "Fields" data [
				button -1 "field" [ inni "field  " ]   tip "Text entry field"
				button -1 "info" [ inni "info  " ]   tip "Same as FIELD style, but read-only"
				button -1 "area" [ inni "area  " ]   tip "Text editing area for paragraph entry"
				]
			return 
			group-box "Backgrounds" data [
				button -1 "backdrop" [ inni "backdrop  " ]   tip "Use an image or effect to fill the background"
				button -1 "backtile" [ inni "info  " ]   tip "Repeat an image to fill the background"
				]
			return 	
			group-box "Items" data [
				button -1 "image" [ inni "image  " ]   tip "Display a JPEG, BMP, PNG, or GIF image"
				button -1 "logo-bar" [ inni "logo-bar  " ]   tip "A vertical Rebol ogo bar"
				button -1 "box" [ inni "box  " ]   tip "A shortcut for drawing a rectangular box"
				button -1 "bar" [ inni "bar  " ]   tip "An horzontal bar (change size for vertical)"
				button -1 "btn" [ inni "btn  " ]   tip "Auto resize button"
				return 
				button -1 "btn-cancel" [ inni "btn-cancel  " ]   tip "Auto resize button"
				button -1 "btn-enter" [ inni "btn-enter  " ]   tip "Auto resize button"
				button -1 "btn-help" [ inni "btn-help  " ]   tip "Auto resize button"
				return 
				button -1 "icon" [ inni "icon  " ]   tip "Display a thumbnail sized image with text caption"
				button -1 "led" [ inni "led  " ]   tip "An indicator light"
				button -1 "anim" [ inni "anim  " ]   tip "Display an animated image"
				button -1 "button" [ inni "button  " ]   tip "Button"
				return 
				button -1 "drop-down" [ inni "drop-down  " ]   tip "Drop down list"
				return 
				button -1 "scroller" [ inni "scroller  " ]   tip "A panel scroller, sizes give the direction"
				 
				button -1 "toggle" [ inni "toggle  " ]   tip "Similar to BUTTON but has a dual state"
				button -1 "tog" [ inni "tog  " ]   tip "Similar to BUTTON but has a dual state"
				button -1 "rotary" [ inni "rotary  " ]   tip "Similar to BUTTON but allows multiple states"
				return 
				button -1 "choice" [ inni "choice  " ]   tip "A pop-up button that displays multiple choices"
				return 
				button -1 "check" [ inni "check  " ]   tip "A check box"
				button -1 "check-line" [ inni "check-line  " ]   tip "A check box"
				button -1 "check-mark" [ inni "check-mark  " ]   tip "A check box"
				return
				button -1 "radio" [ inni "radio " ]   tip "A rounded radio button"
				button -1 "radio-line" [ inni "radio-line " ]   tip "A rounded radio button"
				return 
				button -1 "arrow" [ inni "arrow  " ]   tip "An arrow button with a beveled edge"
				button -1 "progress" [ inni "progress  " ]   tip "A sliding progress bar"
				button -1 "slider" [ inni "slider  " ]   tip "A slider bar"
				button -1 "panel" [ inni "panel  " ]   tip "A sub-layout"
				return 
				button -1 "list" [ inni "list  " ]   tip "An iterated sub-layout"				
				button -1 "text-list" [ inni "text-list  " ]   tip "A simple form of the LIST style"
				
				
				]	
			return 
			group-box "Style" data [	
				button -1 "style" [ inni "style  " ]   tip "Define a custom style"
				button -1 "styles" [ inni "styles  " ]   tip "Use styles from a stylesheet"
				button -1 "backcolor" [ inni "backcolor  " ]   tip "Set the color of the background"
				button -1 "backdrop" [ inni "backdrop  " ]   tip "Scale an image over the entire layout window"
				return 
				button -1 "backtile" [ inni "backtile  " ]   tip "Tile an image over the entire layout window"
				
				]
			return 
			group-box "Events" data [	
				button -1 "sensor" [ inni "sensor  " ]   tip "An invisible face that senses mouse events"
				button -1 "key" [ inni "key  " ]   tip "A keyboard shortcut"
				]
			return 
			group-box "Special  functions" data [
				button -1 "brightness?" [ inni "brightness? " ]  tip "Returns the monochrome brightness (0.0 to 1.0) for a color value"
				button -1 "caret-to-offset" [ inni "caret-to-offset  " ]  tip " Returns the offset position relative to the face of the character position"
				return 
				button -1 "center-face" [ inni "center-face  " ] tip "Center a face on screen or relative to another face"
				button -1 "clear-fields" [ inni "clear-fields  " ] tip "Clear all text fields faces of a layout"
				button -1 "confine" [ inni "confine  " ] tip "Return the correct offset to keep rectangular area in-bounds"
				return 
				button -1 "deflag-face" [ inni "deflag-face  " ] tip "Clears a flag in a VID face"
				button -1 "do" [ inni "do []  " ] tip "	Evaluate a block"
				button -1 "do-events" [ inni "do-events " ]  tip "When this function is called the program becomes event driven"
				return 
				button -1 "dump-face" [ inni "dump-face " ]  tip "Print face info for entire pane"
				button -1 "dump-pane" [ inni "dump-pane " ]  tip "Print face info for entire pane"
				button -1 "event?" [ inni "event? " ]  tip "Returns TRUE for event values"
				return 
				button -1 "edge-size?" [ inni "edge-size? " ]  tip "Return total size of face edge (both sides), even if missing edge"
				button -1 "flag-face" [ inni "flag-face " ]  tip "Sets a flag in a VID face"
				button -1 "flag-face?" [ inni "flag-face? " ]  tip "Checks a flag in a VID face"
				return 
				button -1 "find-window" [ inni "find-window " ]  tip "Find a face's window face"
				button -1 "find-key-face" [ inni "find-key-face /check " ]  tip "Search faces to determine if keycode applies"
				button -1 "focus" [ inni "focus " ]  tip "Focuses key events on a specific face"
				return 
				button -1 "get-face" [ inni "get-face " ]  tip "Returns the primary value of a face"
				button -1 "get-style" [ inni "get-style " ]  tip " Get the style by its name"
				button -1 "hide" [ inni "hide " ]  tip " Hides a face or block of faces"
				return 
				button -1 "hide-popup" [ inni "hide-popup /timeout" ]  tip "(undocumented)"
				button -1 "hilight-all" [ inni "hilight-all " ]  tip "(undocumented)"
				button -1 "hilight-text" [ inni "hilight-text " ]  tip "(undocumented)"
				return 
				button -1 "hsv-to-rgb" [ inni "hsv-to-rgb " ]  tip "Converts HSV (hue, saturation, value) to RGB"
				return
				button -1 "in-window?" [ inni "in-window? " ]  tip " Return true if a window contains a given face"
				button -1 "inside?" [ inni "inside? " ]  tip "TRUE if both X and Y of the second pair are less than the first"
				return 
				button -1 "insert-event-func" [ inni "insert-event-func " ]  tip "Add a function to monitor global events. Return the func"
				return 
				button -1 "remove-event-func" [ inni "remove-event-func " ]  tip "Remove an event function previously added"
				button -1 "layout" [ inni "layout /size /pffset /parent /origin /styles /keep /tight " ]   tip "Return a face with a pane built from style description dialect"
				return 
				button -1 "make-face" [ inni "make-face /styles /clones /spec /offset /keep " ]  tip "Make a face from a given style name or example face"
				return
				button -1 "offset-to-caret" [ inni "offset-to-caret face offset" ]  tip " Returns the offset in the face's text corresponding to the offset pair"
				button -1 "outside?" [ inni "outside?" ]  tip "TRUE if either X and Y of the second pair are greater than the first"
				button -1 "overlap?" [ inni "overlap?" ]  tip "Returns TRUE if faces overlap each other"
				return 
				button -1 "rgb-to-hsv" [ inni "rgb-to-hsv " ] tip " Converts RGB value to HSV (hue, saturation, value)" 
				button -1 "reset-face" [ inni "reset-face /no-show " ] tip "Resets the primary value of a face"
				button -1 "resize-face" [ inni "resize-face  /x /y /no-show" ] tip "Resize a face"
				return 
				button -1 "screen-offset?" [ inni "screen-offset? " ] tip "Returns the absolute screen offset for any face"
				button -1 "show" [ inni "show " ] tip "Display a face or block of faces"
				button -1 "show-popup" [ inni "show-popup  /window  /away " ] tip "(undocumented)"
				return 
				button -1 "size-text" [ inni "size-text " ]  tip " Returns the size of the text in a face"
				return
				button -1 "span?" [ inni "span? " ]  tip "Returns a block of [min max] bounds for all faces"
				button -1 "scroll-drag" [ inni "scroll-drag /back /page " ]  tip "Move the scroller drag bar"
				button -1 "scroll-face" [ inni "scroll-face /x /y /no-show " ]  tip "Scroll a face. Default is vertical"
				return 
				button -1 "scroll-para" [ inni "scroll-para  " ]  tip "Scroll a text face, given a scroller/slider face"
				button -1 "set-face" [ inni "set-face /no-show " ]  tip "Sets the primary value of a face. Returns face object (for show)"
				button -1 "set-font" [ inni "set-font  " ]  tip "(undocumented)"
				return 
				button -1 "set-para" [ inni "set-para  " ]  tip "(undocumented)"
				button -1 "set-style" [ inni "set-style /style " ]  tip "Set a style by its name"
				button -1 "size-text" [ inni "size-text" ]  tip "Returns the size of the text in a face"
				return 
				button -1 "stylize" [ inni "stylize /master /styles " ]  tip " Return a style sheet block"
				button -1 "textinfo" [ inni "textinfo " ]  tip "Sets the line text information in an object for a face"
				button -1 "unfocus" [ inni "unfocus  " ]  tip " Removes the current key event focus"
				button -1 "unview" [ inni "unview /all /only" ]  tip " Closes window(s)"
				return 
				button -1 "unlight-text" [ inni "unlight-text" ]  tip "(undocumented)"
				return
				button -1 "view" [ inni "view /new /offset /options /title " ]  tip "Displays a window face"
				button -1 "viewed?" [ inni "viewed? " ]  tip "Returns TRUE if face is displayed"
				button -1 "within?" [ inni "within? point offset size " ]  tip " Return TRUE if the point is within the rectangle bounds"
				return 
				button -1 "win-offset?" [ inni "win-offset? " ]  tip "Returns the offset of a face within its window"
				]			

			]

		]

	"DRAW" [
		scroll-panel 80x100 data [
			button -1 "Example" [ inni {view layout [box 300x200 effect [draw [
pen navy fill-pen yellow
box 20x20 80x80
fill-pen 0.200.0.150
pen maroon
box 30x30 90x90
image logo.gif 150x100   
line 2x2  2x150 150x100 2x2
pen green
shape [ move 100x100
    arc 200x100
    line 100x100
 ] 
]]]} ]   tip "Example"
			return 
			group-box "Effects" data [
				button -1 "anti-alias" [ inni "anti-alias  " ]   tip "Antialias on/off (on is standard)"
				button -1 "clip" [ inni {clip 0x0 10x10  
				...  ; draw commands
				clip none } ]   tip  "The drawing commands between clips will be displayedonly in the clip region"
				button -1 "fill-pen" [ inni "fill-pen  " ]   tip {fill-pen color (grad-mode  grad-offset grad-start-rng grad-stop-rng grad-angle grad-scale-x 
				grad-scale-y grad-color1 grad-color2 grad-color3 ... image)}
				button -1 "fill-rule" [ inni "fill-rule  " ]   tip "fill-rule mode"
				return 
				button -1 "font" [ inni "font  " ]   tip "font font-object"
				return 
				button -1 "gamma" [ inni "gamma  " ]   tip "gamma gamma-value"
				button -1 "invert-matrix" [ inni "invert-matrix  " ]   tip "Applies an algebric matrix inversion operation on the current transformation matrix"
				button -1 "image-filter" [ inni "image-filter  " ]   tip "image-filter filter-type"
				return 
				button -1 "line-cap" [ inni "line-cap  " ]   tip "line-cap butt/square/round"
				button -1 "line-join" [ inni "line-join  " ]   tip "line-join miter/miter-bevel/round/bevel"
				button -1 "line-pattern" [ inni "line-pattern  " ]   tip "line-pattern stroke-size dash-size (stroke-size dash-size stroke-size dash-size ...)"
				return 
				button -1 "line-width" [ inni "line-width  " ]   tip "line-width size"
				button -1 "matrix" [ inni "matrix  " ]   tip "Premultiply the current transformation matrix with the given block"
				button -1 "pen" [ inni "pen  " ]   tip "pen (stroke-color dash-color image)"				
				button -1 "push" [ inni "push  " ]   tip "Stores the current matrix setup in stack"
				return 
				button -1 "reset-matrix" [ inni "reset-matrix  " ]   tip "Resets the current transformation matrix to its default values"
				button -1 "rotate" [ inni "rotate  " ]   tip "Sets the clockwise rotation, in degrees, for drawing commands"
				button -1 "scale" [ inni "scale  " ]   tip "Sets the scale for drawing commands"
				return 
				button -1 "transform" [ inni "transform  " ]   tip "You can apply a transformation such as translation, scaling, and rotation to any DRAW result"
				button -1 "translate" [ inni "translate  " ]   tip "translate offset"
				
				]
			return	
			group-box "Geometry" data [	
				button -1 "arc" [ inni "arc  " ]   tip "Arc center radius (angle-start angle-end angle-lenght closed)"
				button -1 "arrow" [ inni "arrow  0x0" ]   tip "arrow mode-x-mode"
				button -1 "box" [ inni "box  " ]   tip "box up-left low-right (radius)"
				button -1 "circle" [ inni "circle  " ]   tip "circle center radiusX (radiusY)"
				button -1 "curve" [ inni "curve  " ]   tip "curve point point point (point)"
				return 
				button -1 "image" [ inni "image  " ]   tip "image (up-left low-right/up-right low-left low-right key-color border)"
				return 
				button -1 "line" [ inni "line  " ]   tip "line point point (point point ...)"
				button -1 "polygon" [ inni "polygon  " ]   tip "polygon point point point (point point ...)"				
				button -1 "spline" [ inni "spline  " ]   tip "spline  (segmentation closed) point point (point point ...)"
				button -1 "text" [ inni "text  " ]   tip "text sting offset anti-aliased/vectorial/aliased"
				
				]
			return	
			group-box "Shape commands" data [	
				button -1 "shape" [ inni "shape []  " ]   tip "Draws shapes using the SHAPE sub-dialect, for relative positions"
				button -1 "arc" [ inni "arc  " ]   tip "arc center radiusX radiusY angle sweep true/false"
				button -1 "curv" [ inni "curv  " ]   tip "curv point point (point point ...)"
				button -1 "curve" [ inni "curve  " ]   tip "curve point point point (point ...)"
				button -1 "hline" [ inni "hline  " ]   tip "hline endX"
				return 
				button -1 "line" [ inni "line  " ]   tip "line point (point point ...)"
				return 
				button -1 "move" [ inni "move  " ]   tip "Set's the starting point for a new path without drawing anything"
				button -1 "qcurve" [ inni "qcurve  " ]   tip "qcurve point"
				button -1 "vline" [ inni "vline  " ]   tip "vline endY"
				]

			]

		]

		

	"Your vars" [
		button -1 "Update!" [ 
			
			either (attempt [findall a/text] ) [listaoggetti: findall a/text ] [alert {There is an error, check " and {}} ]
			
			clear  wordsyv/data
			 insert wordsyv/data  (select listaoggetti "words")
			 clear blocksyv/data
			 insert blocksyv/data (select listaoggetti "blocks")
			 clear functionsyv/data
			insert functionsyv/data (select listaoggetti "functions")
			clear objectsyv/data
			insert objectsyv/data (select listaoggetti "objects")
			wordsyv/redraw
			 blocksyv/redraw
			functionsyv/redraw
			objectsyv/redraw
			]
		return	
		scroll-panel 80x90 data [
			label "Words"
			return wordsyv: text-list data []
			return label "Blocks"
			return blocksyv: text-list data []
			return label "Functions"
			return functionsyv: text-list data []
			return label "Objects"
			return objectsyv: text-list data []
			]
		
		]
			
	]
return	
uso: text "USAGE:" 140
return 
testo: text text-color red 140
]

;Other windows




;about page

aboutpage: [
text 50 {Author: Massimiliano Vessi
Feel free to contact me. 
This script should make it easier to learn Rebol.
If you found bugs or errors please email me.}
return
link "www.maxvessi.net"
return
link (rejoin [ "maxint" "@" "tiscali.it"] )
return
text 50 {Thanks to Graham, Nick Antonaccio, Semseddin Moldibi, Zoltan Eros}
]


;Shortcuts page
shortcuts: [
table 100x50 options ["Key(s)" left 0.4 "Description" left 0.6] data [
"Ctrl+G" "GO! Lauch script."
"Ctrl+D" "Save"
"Ctrl+Shift+D" "Save as..."
"Ctrl+S" 	"Spellcheck All"
"BackSpc" 	"Delete previous character"
"Del" 	"Delete next character"
"Ctrl+BackSpc" 	"Delete to start of word"
"Ctrl+Del" 	"Delete to end of word"
"Ctrl+T" 	"Delete to end of line"
"ArwLeft" 	"Character left"
"ArwRight" 	"Character right"
"ArwDn" 	"Line down"
"ArwUp" 	"Line up"
"Home" 	"Start of line"
"End" 	"End of line"
"PgUp" 	"Page Up"
"PgDn" 	"Page Down"
"Ctrl+ArwLeft" 	"Word left"
"Ctrl+ArwRight" 	"Word right"
"Ctrl+ArwDn" 	"Page down"
"Ctrl+ArwUp" 	"Page up"
"Ctrl+Home" 	"Start of text"
"Ctrl+End" 	"End of text"
"Ctrl+PgUp" 	"Start of text"
"Ctrl+PgDn" 	"End of text"
"Shift+Arrow" 	"Select characters"
"Double click" 	"Select word"
"Ctrl+A" 	"Select All"
"Ctrl+Z" 	"Undo" 
"Ctrl+Y" 	"Redo"
"Ctrl+X" 	"Cut"
"Ctrl+C" 	"Copy"
"Ctrl+V" 	"Paste"
"Shift+Del" 	"Cut"
"Shift+Ins" 	"Paste"
"Ins" 	"Toggle Insert/Overwrite mode"
"Tab" 	"Move focus to next tabable widget"
"Shift+Tab" 	"Move focus to previous tabable widget"
	]


]

;VID guide page


guida_vid: [
	heading "REBOL/View VID Developer's Guide"
	return
	text italic bold "You can click on the examples to see the results"
	return 
	scroll-panel 120x100 data [
		text 100 {This document describes VID, the Visual Interface Dialect for creating graphical user interfaces in REBOL 2.
By their nature, graphical user interfaces (GUI) are more descriptive than they are functional. In REBOL, the Visual Interface Dialect (VID) provides an efficient method of describing GUIs. VID is implemented as a layer that rides on top of the REBOL/View graphical compositing system. VID provides shortcut expressions that are automatically translated into View objects and functions. You can seamlessly combine VID and View code and data for great power and flexibility.}
return
heading "Layout Concepts"
return 
text 100 {A VID layout is a block of words and values that is used to describe a GUI. It provides the names, attributes, and operations that are used to display text areas, buttons, checkboxes, input fields, slider bars, and more. The format of the VID layout block is organized according to the rules of VID.}
return 
heading {Layout Structure}
return 
text 100 {A layout block consists of:
"Keywords"  Layout keywords that describe face positioning and other layout attributes.
"Styles"	Face styles that are used to specify the faces that are displayed. These can be predefined styles like TITLE, BUTTON, FIELD, TEXT, or your own custom styles.
"Facets"	Attributes that describe variations in the style of a face, such as the size, color, alignment, border, or image.
"Variables"  Definitions that hold either faces or layout positions. These variables can be used later to access face objects or to affect face positions.
"Styledefs" New style definitions that are to be used within the layout. Single styles or entire stylesheets can be provided.

These elements can be mixed and matched in whatever order is necessary to create a layout.}
return 
label "Simple Examples"
return 
text 100 {The easiest way to learn VID layouts is by example. The single line below creates and displays a window that contains the obligatory "Hello World!" example:}
return 
tooltip {view layout [title "Hello World!"]} [ lancia  { view layout [title "Hello World!"]  }] 
return 
text 100 {The layout block contains the VID description of what to display. The block is a dialect, not normal REBOL, and it is passed to the LAYOUT function to create the faces for the layout. The result of the LAYOUT function is passed to the VIEW function to display it on your screen:
The TITLE word is a predefined style and is followed by values and attributes that affect that style. In the example above, a string value provides the title text.
VID provides more than 40 predefined styles. For example, you can replace the TITLE style with the video BANNER style:}
return 
tooltip {view layout [banner "Hello World!!!"]} [ lancia {view layout [banner "Hello World!!!"]} ]
return 
text 100 "Within a layout, multiple styles can be provided. Each style creates another element of the interface. The example below shows a video heading (vh2), followed by text, then by a button:"
return 
tooltip {view layout [
    vh2 "Layout Definition:"
    text "Layouts describe graphical user interfaces."
    button "Remember"
]} [ lancia {tooltip {view layout [
    vh2 "Layout Definition:"
    text "Layouts describe graphical user interfaces."
    button "Remember"
]}} ]

return 
text 100 "Thousands of effects and variations are possible within a layout by specifying style attributes called facets. These attributes follow the style word. Here is an example that shows how an elaborate layout can be created in a few lines of VID code:"
return 
tooltip {view layout [
    backdrop effect [gradient 1x1 180.0.0 0.0.100]
    vh2 "Layout Definition:" 200x22 yellow
        effect [gradmul 1x0 50.50.50 128.128.128]
    vtext bold italic "Layouts describe graphical user interfaces."
    button "Remember" effect [gradient 0.0.0]
]} [ lancia {view layout [
    backdrop effect [gradient 1x1 180.0.0 0.0.100]
    vh2 "Layout Definition:" 200x22 yellow
        effect [gradmul 1x0 50.50.50 128.128.128]
    vtext bold italic "Layouts describe graphical user interfaces."
    button "Remember" effect [gradient 0.0.0]
]}]

return 
text 100 {Layouts can specify as many faces as your interface requires. For example, this layout uses styles, a backdrop, a heading, text labels, text input fields, and buttons:}
return 
tooltip {view layout [
    style lab label 100 right
    across
    vh2 "Provide Your Information:" gold return
    lab "User Name:" field return
    lab "Email Address:" field return
    lab "Date/Time:" field form now return
    lab "Files:" text-list data load %. return
    lab
    button 96 "Save"
    button 96 "Cancel"
    return
]} [lancia {view layout [
    style lab label 100 right
    across
    vh2 "Provide Your Information:" gold return
    lab "User Name:" field return
    lab "Email Address:" field return
    lab "Date/Time:" field form now return
    lab "Files:" text-list data load %. return
    lab
    button 96 "Save"
    button 96 "Cancel"
    return
]}]

return 
text 100 "The example shows how multiple styles can be specified within a layout."
return 
heading "Layout Function"
return 
text 100 {The LAYOUT function takes a layout block as an argument and returns a layout face as a result. The block describes the layout according to the rules of the Visual Interface Dialect. The block is evaluated and a face is returned.
The result of LAYOUT is can be passed directly to the VIEW function, but it can also be set to a variable or returned as the result of a function. The line:}
return 
tooltip {view layout block}
return 
text 100 "can also be written as:"
return 
tooltip {window: layout block
view window}
return 
text 100 "The result of the layout function is a face and can be used in other layouts. More on this later."
return 
heading "Layout Refinements"
return 
text 100 {In most cases, the LAYOUT function is called without refinements; however, these refinements are available when necessary:
/size	A PAIR! that specifies the size of the resulting face. This forces the face to be of a fixed size before the layout is performed. The default is to size the face dynamically based on the placement of items within the layout.
/offset	A PAIR! that provides the offset to where the window will be displayed within its parent face (often the screen).
/styles	A stylesheet block that was created with the STYLIZE function. A stylesheet defines custom styles used within the layout. This is equivalent to the STYLES keyword within a layout.
/origin	A PAIR! that sets the pixel offset to the first face within the layout. This is equivalent to the ORIGIN keyword within a layout.
/parent	Specifies the style of the top-level face that is produced from the layout. The parent can be specified as a style name or as an actual instance of the style.
/options	Specifies the VIEW options when the face is displayed with the VIEW function. See the VIEW function for details.}
return 
heading "Keywords"
return 
text 100 {Here is a summary of the layout keywords that describe face positioning and other layout attributes. These are reserved words. These words cannot be used for style names or for variables within a layout.
across	Set auto-layout to horizontal direction.
at	Locate a face to an absolute position.
backcolor	Set the color of the background.
below	Set auto-layout to vertical direction.
do	Evaluate a block.
guide	Set a guide line.
indent	Indent horizontally.
offset	Set the output face position.
origin	Specify the layout starting position.
pad	Insert extra spacing.
return	Return to the current guide position.
style	Define a custom style.
styles	Use styles from a stylesheet.
space	Set the auto-spacing used between faces.
size	Set the output face size.
tabs	Set tab stops.
tab	Advance to next tab position.

Each of these keywords is described in more detail in sections of this document.}
return 
heading "Face Styles"
return 
text 100 {Face styles are used to specify the faces that are displayed. These can be predefined styles, or they can be your own custom styles.}
return 
heading {Predefined Styles}
return 
text 100 {Predefined styles are part of VID and can be used in three ways.
-You can use any predefined style as-is and it will provide its default look and feel.
-You can specify variations on a style by providing facets such as color, size, font, effects, etc.
-You can use a style as the basis for defining a new custom style.

The predefined styles are listed below. For more information about each of these styles, refer to the Styles chapter (a separate document).
title	Document title heading.
h1	Top level heading used for documents.
h2	Heading use for document sections.
h3	Heading used for subsections.
h4	Heading used below subsections.
h5	Heading used below subsections.
banner	Title heading with video style.
vh1	Section heading used for video style.
vh2	Section heading used for video style.
vh3	Section heading used for video style.
text	Document body text.
txt	An alias for TEXT style above.
vtext	Inverse video body text.
tt	The teletype font for fixed width text.
code	Same as TT except defaults to bold.
label	Used for specifying GUI text labels.
field	Text entry field.
info	Same as FIELD style, but read-only.
area	Text editing area for paragraph entry.
sensor	An invisible face that senses mouse events.
image	Display a JPEG, BMP, PNG, or GIF image.
box	A shortcut for drawing a rectangular box.
backdrop	Scale an image over the entire layout window.
backtile	Tile an image over the entire layout window.
icon	Display a thumbnail sized image with text caption.
led	An indicator light.
anim	Display an animated image.
button	A button that goes down on a click.
toggle	Similar to BUTTON but has a dual state.
rotary	Similar to BUTTON but allows multiple states.
choice	A pop-up button that displays multiple choices.
check	A check box.
radio	A rounded radio button.
arrow	An arrow button with a beveled edge.
progress	A sliding progress bar.
slider	A slider bar.
panel	A sub-layout.
list	An iterated sub-layout.
text-list	A simple form of the LIST style.
key	Keyboard shortcut.

Here is an example that shows most of these custom styles:}
return 
tooltip {view layout [title "Document Title"
h1 "Heading 1"
h2 "Heading 2"
h3 "Heading 3"
h4 "Heading 4"
h5 "Heading 5"
banner "Video Title"
vh1 "Video heading 1"
vh2 "Video heading 2"
vh3 "Video heading 3"
text "Document body text"
tt "The teletype font for fixed width text"
code "Same as TT except defaults to bold"
vtext "Inverse video body text"
txt "An alias for BODY style above"
label "Used for specifying GUI text labels"
lbl "The video equivalent of LABEL"
field "Text entry field"
info "Same as FIELD style, but read-only"
area "Text editing area for paragraph entry"
do [if not exists? %nyc.jpg [
 write/binary %nyc.jpg read/binary %../nyc.jpg
 ]]
image %nyc.jpg 100x100
box blue
icon %nyc.jpg "NYC"
led
button "Button"
toggle "Toggle"
rotary "Rotary"
choice "Choice"
check
radio
arrow
progress
slider 200x16
text-list "A simple form of the LIST style"]} [ lancia {view layout [title "Document Title"
h1 "Heading 1"
h2 "Heading 2"
h3 "Heading 3"
h4 "Heading 4"
h5 "Heading 5"
banner "Video Title"
vh1 "Video heading 1"
vh2 "Video heading 2"
vh3 "Video heading 3"
text "Document body text"
tt "The teletype font for fixed width text"
code "Same as TT except defaults to bold"
vtext "Inverse video body text"
txt "An alias for BODY style above"
label "Used for specifying GUI text labels"
lbl "The video equivalent of LABEL"
field "Text entry field"
info "Same as FIELD style, but read-only"
area "Text editing area for paragraph entry"
do [if not exists? %nyc.jpg [write/binary %nyc.jpg read/binary %../nyc.jpg]]
image %nyc.jpg 100x100
box blue
icon %nyc.jpg "NYC"
led
button "Button"
toggle "Toggle"
rotary "Rotary"
choice "Choice"
check
radio
arrow
progress
slider 200x16
text-list "A simple form of the LIST style"]}]


return 
heading "Facets"
return 
text 100 "All of the styles above can be provided with additional information to vary their size, color, text, alignment, background, and more. This is described in detail in the Facets section below."
return 
heading "Custom Styles"
return 
text 100 "Any of the styles listed above can be used as the base style for creating your own custom style. This is covered in the Style Definition section later in this document."
return 
heading "Style Facets"
return 
text 100 {Within a layout, each face is specified by a style word that identifies the look and feel of the face. Each style word can be followed by optional facet attributes that further modify the face. Facets can control the text, size, color, images, actions, and most other aspects of a face.

All facets are optional. For example, the example below shows how you can create a button with a variety of facets. The facets can be provided alone or in combination.}
return 
tooltip {button
button "Easy"
button "Easy" 40x40
button "Easy" oldrab
button "Easy" [print "Fun"]
button "Easy" 40x40 maroon [print "Fun"]} [ lancia { view layout [button
button "Easy"
button "Easy" 40x40
button "Easy" oldrab
button "Easy" [print "Fun"]
button "Easy" 40x40 maroon [print "Fun"]]}]


return 
text 100 {Facets can appear in any order. You don't need to keep track of which goes first. All of these mean the same thing:}
return 
tooltip{
button "Easy" 40x40 navy [print "Fun"]
button navy "Easy" 40x40 [print "Fun"]
button 40x40 navy "Easy" [print "Fun"]
button [print "Fun"] navy 40x40 "Easy"} [ lancia { view layout [
button "Easy" 40x40 navy [print "Fun"]
button navy "Easy" 40x40 [print "Fun"]
button 40x40 navy "Easy" [print "Fun"]
button [print "Fun"] navy 40x40 "Easy"]}]


return 
heading "Text Facets"
return 
text 100 "Text string facets provide the text used for all faces. The text can be written as a short string in quotes, a long multiline string in braces, or provided as a variable or function that contains the string."
return 
tooltip {
text "Example string"
text 100 {This is a long, multilined text 
section that is put in a braced
string and will be displayed on the page.} 
text text-doc
text read %file.txt}
return 
text 100 "For some faces styles, more than one string can be provided. For instance, a choice button accepts multiple strings:"
return 
tooltip {choice "Steak" "Eggs" "Salad"} [lancia {view layout [ choice "Steak" "Eggs" "Salad"]}]
return 
heading "Size Facets"
return 
text 100 "The size of a face can be specified as a pair that provides the width and height of the face in pixels:"
return 
tooltip{image %nyc.jpg 100x200
text "example" 200x200
button "test" 50x24}[lancia {  view layout [ image %nyc.jpg 100x200
text "example" 200x200
button "test" 50x24]}]

return 
text 100 "The width of a face can also be expressed an integer, leaving the height to be computed automatically:"
return 
tooltip {text "example" 200
button "test" 50}[ lancia {  view layout [ text "example" 200
button "test" 50]}]

return 
heading "Color Facets"
return 
text 100 "A color is written as a tuple that provides the red, green, and blue components of the color."
return 
tooltip{image %nyc.jpg 250.250.0
text "example" 0.0.200
button "test" 100.0.0} [ lancia {  view layout [ image %nyc.jpg 250.250.0
text "example" 0.0.200
button "test" 100.0.0]}]

return 
text 100 "The are also about 40 predefined colors in REBOL that can be used:"
return 
tooltip {text red "Warning"
text blue "Cool down"
text green / 2 "Ok"} [ lancia {view layout [ text red "Warning"
text blue "Cool down"
text green / 2 "Ok"]}]
return 
text 100 {Notice in the last case how the color can be reduced by dividing it by two.

Some faces accept multiple colors. For instance:}
return 
tooltip{toggle "Test" red green
rotary "Stop" red "Caution" yellow "Go" green}[ lancia {view layout [ toggle "Test" red green
rotary "Stop" red "Caution" yellow "Go" green]}]
return 
heading "Image Facets"
return 
text 100 "An image can be provided as a filename, a URL, or as image data."
return 
tooltip{image %nyc.jpg
image http://www.rebol.com/view/nyc.jpg
button "Test" %nyc.jpg}[ lancia {view layout [ image %nyc.jpg
image http://www.rebol.com/view/nyc.jpg
button "Test" %nyc.jpg]}]
return 
text 100 "An image can also be loaded and used as a variable:"
return 
tooltip {town: %nyc.jpg
image town
image 30x30 town
icon town "NYC"}[ lancia {view layout [town: %nyc.jpg
image town
image 30x30 town
icon town "NYC"]}]
return 
heading "Action Facets"
return 
text 100 {An action is specified as a block. The action makes a face "hot". When a user clicks on the face, the block will be evaluated.}
return 
tooltip {image %nyc.jpg [print "hello"]
text "example" [print "there"]
button "Test" [print "user"]} [ lancia {view layout [image %nyc.jpg [print "hello"]
text "example" [print "there"]
button "Test" [print "user"]]}]
return 
text 100 {Some styles accept a second block that is used as an alternate action (right-click action). For example:}
return 
tooltip {text "Click Here" [print "left click"] [print "right click"]} [ lancia {view layout [text "Click Here" [print "left click"] [print "right click"]]}]
return 
heading "Character Facets"
return 
text 100 {A shortcut key is written as a character (a string with a # before it). If the user presses a shortcut key, the action block will be evaluated as if the user clicked on it.}
return 
tooltip {image %nyc.jpg #"i" [print "hello"]
text "example" #"^t" [print "there"]
button "Test" #" " [print "user"] } [ lancia {view layout [image %nyc.jpg #"i" [print "hello"]
text "example" #"^t" [print "there"]
button "Test" #" " [print "user"] ]}]
return 
heading "Face Facet Blocks"
return 
text 100 {Note that facet blocks are most useful when used in conjunction with custom styles.
font	A font block is used to specify other details about a font, such as its font name, point size, color, shadow, alignment, spacing, and more:}
return 
tooltip{text "black" font [color: 255.255.255 size: 16 shadow: none]} [ lancia {view layout [text "black" font [color: 255.255.255 size: 16 shadow: none]]}]
return 
text 100 {para	A para block specifies the paragraph attributes of a text face. This is where you adjust the spacing between paragraphs, margins, and other values.}
return 
tooltip{text "test" para [origin: 10x10 margin: 10x10]} [ lancia {view layout [text "test" para [origin: 10x10 margin: 10x10]]}]
return 
text 100 "edge	An edge block gives you a way to control the edge around the outside of a face. You can set its color, size, and effect."
return 
tooltip {image %nyc.jpg edge [size 5x5 color: 100.100.100 effect: [bevel]]}[ lancia {view layout [ image %nyc.jpg edge [size 5x5 color: 100.100.100 effect: [bevel]]]}]
return 
text 100 "effect	An effect block specifies special graphic effects for a face. Many effects are possible, such as gradients, colorize, flip, rotate, crop, multiply, contrast, tint, brighten, and various combinations."
return 
tooltip{image %nyc.jpg effect [contrast 20]
image %nyc.jpg effect [tint 120 brighten 30]
button "Test" effect [gradient 0x1 200.0.0]} [lancia { view layout [image %nyc.jpg effect [contrast 20]
image %nyc.jpg effect [tint 120 brighten 30]
button "Test" effect [gradient 0x1 200.0.0]]}]
return 
text 100 "with	The with block allows you to specify any other type of face characteristic using standard REBOL object format."
return 
heading "Attribute Keywords"
return 
text 100 "These words control the layout as it is being created. They affect the placement of faces within the layout."
return 
text bold "Size "
return 
text 100 "SIZE sets the size of the layout face. This must be done at the beginning of a layout before any styles are used. For example, the simple layout:"
return 
tooltip {size 200x100
h2 "Size Example"} [lancia { view layout [size 200x100
h2 "Size Example"]}]

return 
text 100 "This is equivalent to the /size refinement in the LAYOUT function. If no size is specified, then the layout is auto-sized based on the styles used within it."
return 
text bold "Offset"
return 
text 100 "OFFSET specifies the position of the layout face within its parent face (often the screen). This is the same as the /offset refinement in the LAYOUT function."
return 
tooltip {offset 10x32}
return 
text 100 "The offset need not be specified in the layout. It can be specified in the View if necessary. The default offset is 25x25."
return 
text bold "Origin"
return 
text 100 {ORIGIN sets the starting X and Y position of faces in the layout. The origin is specified as the number of pixels from the upper left corner of the layout window. However, the origin also determines the amount of spacing between the last face and the bottom right of the layout. The default origin is 20x20.
The example below uses an origin that is smaller than usual:}
return 
tooltip {origin 4x2
text bold "Origin at 4x2"} [ lancia{ view layout [ origin 4x2
text bold "Origin at 4x2"]}]
return 
text 100 "If an integer is specified for the origin, then both the X and Y positions will be set to that value, as in this example:"
return 
tooltip {origin 50
text bold "Origin at 50x50"}  [ lancia{ view layout [origin 50
text bold "Origin at 50x50"]}]
return 
text 100 {When no pair value is provided, the origin word returns the layout to its original origin position.}
return 
tooltip{box 34x40 beige
origin
text bold "Back at Origin"} [lancia { view layout [
box 34x40 beige
origin
text bold "Back at Origin"]}]

return text 100 {As you can see from the above examples, the origin also has an affect on the size of the resulting face when no size has been provided.

Setting the origin is especially important when creating panels and lists. Frequently the origin in lists is set to zero. For example:}
return tooltip {vh2 "Films:"
list 144x60 [
    origin 0
    across
    text 60
    text 80
] data [
    ["Back to the Future" "1:45"]
    ["Independence Day" "1:55"]
    ["Contact" "2:15"]
]} [lancia { view layout [
vh2 "Films:"
list 144x60 [
    origin 0
    across
    text 60
    text 80
] data [
    ["Back to the Future" "1:45"]
    ["Independence Day" "1:55"]
    ["Contact" "2:15"]
]]}]



return text 100 "The block provided to the LIST style is a layout with an origin of zero."
return heading "Auto-Layout Direction"
return text bold "Below"
return text 100 {BELOW specifies a vertical layout for faces that follow it. It is used along with ACROSS for auto layout of faces.
BELOW is the default layout direction when none is specified. For example:}
return tooltip {button "Button 1"
button "Button 2"
button "Button 3"} [lancia { view layout [ 
button "Button 1"
button "Button 2"
button "Button 3"]}]
return text 100 "You can switch between BELOW and ACROSS at any time during a layout. When BELOW is used, faces will be positioned below the current face. The example:"
return tooltip {across
button "Button 1"
button "Button 2"
return
below
button "Button 3"
button "Button 4"} [lancia { view layout [ 
across
button "Button 1"
button "Button 2"
return
below
button "Button 3"
button "Button 4"]}]
return text bold "Across"
return text 100 {ACROSS specifies a horizontal layout for faces that follow it. It is used along with BELOW for auto layout of faces.
When ACROSS is used, faces will be located to the right of the current face. The example:}
return tooltip {across
button "Button 1"
button "Button 2"
button "Button 3"} [lancia { view layout [ 
across
button "Button 1"
button "Button 2"
button "Button 3"]}]
return text 100 "You can switch between ACROSS and BELOW at any time during a layout."
return tooltip {vh2 "Example"
across
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"
return} [lancia { view layout [ vh2 "Example"
across
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"
return]}]
return text "The above example would display:"
return text bold "Return"
return text 100 {RETURN advances the position to the next row or column, depending on the layout direction. If the layout direction is across, return will start a new row. If the direction is below, return will start a new column.
The example:}
return tooltip {across
text "Name:" 100x24 right
field "Your name"
return
text "Address:" 100x24 right
field "Your address"
return}[lancia { view layout [ 
across
text "Name:" 100x24 right
field "Your name"
return
text "Address:" 100x24 right
field "Your address"
return]}]
return text "The position of the column is relative to the origin or to a guide."
return heading "Spacing"
return text "Space"
return text 100 {SPACE sets the auto-spacing to use between faces within the layout. The spacing can be changed at any time within your layout. Either a pair or an integer can be given. If you specify a pair, both the vertical and horizontal spacing is set.
Compare these two cases. The first specifies a small space:}
return tooltip {space 2x4
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"} [lancia { view layout [ 
space 2x4
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"]}]
return text "The second uses a larger space:"
return tooltip {space 20x16
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"
}[lancia { view layout [ 
space 20x16
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"]}]
return 100 "If the space you specify is an integer, only the spacing in the current direction (across or below) is set. The line would look like:"
return  tooltip {space 5} [lancia { view layout [ space 5]}]
return 
text bold "Pad"
return 
text 100 "PAD inserts extra spacing between the current position and the position of the next face. The distance can be specified as an integer or a pair. When it is a pair, the space will be added both horizontal and vertically."
return tooltip {text "Bar below"
pad 20x4
box 50x3 maroon} [lancia { view layout [ 
text "Bar below"
pad 20x4
box 50x3 maroon]}]

return text 100 {When the PAD is an integer, space is either vertical or horizontal depending on the current direction of auto layout (determined by below and across words).
A PAD used in a BELOW:}
return tooltip {below
text "Pad"
pad 40
text "Below"} [lancia { view layout [ 
below
text "Pad"
pad 40
text "Below"]}]


return text 100 "and a PAD used in an across:"
return tooltip {across
text "Pad"
pad 40
text "Across"} [lancia { view layout [ 
across
text "Pad"
pad 40
text "Across"]}]

return text "Note that negative pad values are also allowed."
return tooltip {text "Bar above"
pad 20x-30
box 50x3 maroon}[lancia { view layout [ 
text "Bar above"
pad 20x-30
box 50x3 maroon]}]


return text bold "Indent"
return text 100 {INDENT inserts spacing horizontally between the current position and the next face. It is not affected by the auto layout direction.
This example indents 20 pixels for every face after the heading:}
return tooltip {vh1 "About VID"
indent 20
text "This section is about VID."
button "Ok"
button "Cancel"}[lancia { view layout [ 
vh1 "About VID"
indent 20
text "This section is about VID."
button "Ok"
button "Cancel"]}]

return text "Negative values can also be used:"
return tooltip {vh1 "About VID"
indent 20
text "This section is about VID."
indent -20
button "Ok"
button "Cancel"}[lancia { view layout [ 
vh1 "About VID"
indent 20
text "This section is about VID."
indent -20
button "Ok"
button "Cancel"]}]

return heading "Aligning Faces"
return label "At"
return text 100 {AT sets an absolute layout position for the face that follows it. Here's a simple example that sets the next position of a layout:}
return tooltip {at 60x30
vh2 "Simple Example"}[lancia { view layout [ 
at 60x30
vh2 "Simple Example"]}]

return text 100 "Here is an example that places multiple faces on top of each other:"
return tooltip {at 0x0
backdrop effect [gradient 0x1 gray]
at 70x70
box effect [gradient 1x1]
at 50x50
box effect [gradient 1x1 200.0.0 0.0.100]
at 30x30
vtext bold italic 100 {This is an example of locating
   two faces using absolute positioning.}
at 20x160
button 40 "OK"}[lancia { view layout [ 
at 0x0
backdrop effect [gradient 0x1 gray]
at 70x70
box effect [gradient 1x1]
at 50x50
box effect [gradient 1x1 200.0.0 0.0.100]
at 30x30
vtext bold italic 100 {This is an example of locating
   two faces using absolute positioning.}
at 20x160
button 40 "OK"]}]

return label "Tabs"
return text 100 {TABS specifies the tab spacing that is used when a TAB word is encountered. The direction of the tab (horizontally or vertically) depends on the current direction of the layout as specified by BELOW and ACROSS.
To set the tab spacing an integer provides regular spacing of that amount:}
return tooltip {across
tabs 150
vh3 "Buttons:"
tab
button "Button 1"
tab
button "Button 2"} [lancia { view layout [ 
across
tabs 150
vh3 "Buttons:"
tab
button "Button 1"
tab
button "Button 2"]}]

return text 100 "Fixed tab positions can also be provided with a block of integers. In this example two tab-stops are defined to align the result:"
return tooltip {across
tabs [80 200]
h2 "Line 1"
tab field 100
tab field 100
return
h3 "Line 2"
tab check
text "Check"
tab button "Ok"
return
h4 "Line 3"
tab button "Button 1"
tab button "Button 2"}[lancia { view layout [ 
across
tabs [80 200]
h2 "Line 1"
tab field 100
tab field 100
return
h3 "Line 2"
tab check
text "Check"
tab button "Ok"
return
h4 "Line 3"
tab button "Button 1"
tab button "Button 2"]}]

return text 100 "Note that tabs also apply vertically and tabs can be changed at any time in a layout. For example:"
return tooltip {tabs 40
field "Field 1"
field "Field 2"
field "Field 3"
return
across
tabs 100
button "Button 1"
button "Button 2"
button "Button 3"} [lancia { view layout [ 
tabs 40
field "Field 1"
field "Field 2"
field "Field 3"
return
across
tabs 100
button "Button 1"
button "Button 2"
button "Button 3"]}]

return label "Tab"
return text 100 {TAB skips forward in the current direction (across or below) to the next tab position. Tabs positions are set with the TABS keyword. See the TABS description for more examples
The example:}
return tooltip {across
tabs 80
text "Name"  tab field return
text "Email" tab field return
text "Phone" tab field return}[lancia { view layout [ 
across
tabs 80
text "Name"  tab field return
text "Email" tab field return
text "Phone" tab field return]}]

return label "Guide"
return text 100 {GUIDE sets the return margin for face layout. When the RETURN word is used, an invisible guide-line determines where the next face will be placed. Guides can be thought of as virtual borders that align the placement of faces. If the guide has not been set, it defaults to be the origin.
A guide can be created by specifying a position, or if no position is provided, then the current position will be used. This example shows a heading, then creates a guide for the remaining faces:}
return tooltip {across
vh2 "Guides"
guide 60x100
label "Name:" 100x24 right
field
return
label "Address:" 100x24 right
field
return}[lancia { view layout [ 
across
vh2 "Guides"
guide 60x100
label "Name:" 100x24 right
field
return
label "Address:" 100x24 right
field
return]}]

return text 100 "Here is a good example of a problem that is solved by a guide. The layout below creates an undesired effect:"
return tooltip {vh2 "Without A Guide:"
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"}[lancia { view layout [ 
vh2 "Without A Guide:"
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"]}]


return text 100 "If a GUIDE is added after the heading:"
return tooltip {vh2 "With A Guide:"
guide
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"} [lancia { view layout [ 
vh2 "With A Guide:"
guide
button "Button 1"
button "Button 2"
return
button "Button 3"
button "Button 4"]}]


return heading "Style Definition: Custom Styles"
return  text 100 {You can define your own styles. This is useful if you use a style with the same facets multiple times in your layout. Defining your own style will make it easier to write and easier to modify your script later.
For instance, the code:}
return tooltip  {text black 200x24 bold "This"
text black 200x24 bold "is"
text black 200x24 bold "an"
text black 200x24 bold "example"} [lancia { view layout [ 
text black 200x24 bold "This"
text black 200x24 bold "is"
text black 200x24 bold "an"
text black 200x24 bold "example"]}]

return text 100 "would be easier to write if a new style called txt where defined:"
return tooltip {txt "This"
txt "is"
txt "an"
txt "example"}

return text 100 {The new style can be created in two ways. Styles can be defined in a layout, or they can be created in a stylesheet and applied to a layout.}

return label "Styles in Layouts"

return text 100 "To create a style that is defined only within a layout, use the style keyword. In this example, the txt style is created:"
return tooltip {style txt text black 200x24 bold
txt "This"
txt "is"
txt "an"
txt "example"} [lancia { view layout [ 
style txt text black 200x24 bold
txt "This"
txt "is"
txt "an"
txt "example"]}]

return text 100 {The style word is followed by the new style name, a base style to begin with, and a set of facets that modify it. Any facets can be supplied as part of the style, including text, images, and action.
The txt style is only valid within the layout block. It can be used within the block or within any subpanels or lists created by the block. However, if you attempt to use the style outside the block an error will occur.
Any number of custom styles can be added to the layout block.}

return label "Creating Stylesheets"
return text 100 {To create custom styles for multiple layouts, you will need to create a stylesheet with the stylize function.}
return tooltip {new-styles: stylize [
txt: text black 200x24 bold
btn: button 80x24 effect [gradient 0x1 0.80.0]
fld: field 100x24
]}

return text 100 {Each new style is written as a set word followed by a base style and list of facets.
To use the stylesheet within a layout, include it with a styles keyword:}
return tooltip {view layout [
    styles new-styles
    txt "Text"
    btn "Button"
    fld "Field"
]}  [lancia { view layout [ 
 styles new-styles
    txt "Text"
    btn "Button"
    fld "Field"
]}]

return text 100 {A layout can contain any number of styles from any combination of stylesheets and styles.}

return label "Style"

return text 100  {STYLE defines a new style that is local to the current layout. The format of the style begins with the new style name and is followed by a normal layout face specification.}

return tooltip {style blue-text text blue center 200}

return text 100 "Once a style has been defined, it can be used just like any other style:"
return tooltip {blue-text "Blue Text Here"}  [lancia { view layout [ 
style blue-text text blue center 200
blue-text "Blue Text Here"]}]

return text 100 "It is common to define a new button style in a layout:"
return tooltip {style btn button 80x22 leaf
btn "Test" [print "Test button pressed"]
btn "This" [print "This button pressed"]}  [lancia { view layout [ 
style btn button 80x22 leaf
btn "Test" [print "Test button pressed"]
btn "This" [print "This button pressed"]]}]

return text 100 {Predefined styles can be redefined with the STYLE word. For example, this line will redefine the BUTTON style used within a layout:}
return tooltip {style button button green 120x30}

return text 100 "Such changes are local to the layout and do not affect the button style used in other layouts."
return label "Styles"
return text 100 {STYLES allows you to use a predefined stylesheet in one or more layouts. When a stylesheet is provided, those styles become available to the layout.
A stylesheet is created with the STYLIZE function. Styles are defined similar to a layout, but with the new style name appearing as a variable definition.}
return tooltip {big-styles: stylize [
btn: button 300x40 navy maroon font-size 16
fld: field 300x40 bold font-size 16 middle center
lab: text 300x32 font-size 20 center middle red black
]} 

return text 100 "The new styles and their names are encapsulated within the stylesheet and can be used in any layout."
return tooltip {styles big-styles
lab "Enter CPU Serial Number:"
fld "#000-0000"
lab "Press to Eject CPU:"
btn "Eject Now"
btn "Cancel"}  [lancia { big-styles: stylize [
btn: button 300x40 navy maroon font-size 16
fld: field 300x40 bold font-size 16 middle center
lab: text 300x32 font-size 20 center middle red black
] 
view layout [ 
styles big-styles
lab "Enter CPU Serial Number:"
fld "#000-0000"
lab "Press to Eject CPU:"
btn "Eject Now"
btn "Cancel"]}]

return text 100 "Any number of stylesheets can be used within a layout."
return heading "Other Keywords"
return label "Do"
return text 100 {DO evaluates an expression during the process of making a layout.}
return tooltip {h2 "Introduction:"
do [
intro: either exists? %intro.txt [read %intro.txt]["NA"]
]
txt intro} [lancia { view layout [ 
h2 "Introduction:"
do [
intro: either exists? %intro.txt [read %intro.txt]["NA"]
]
txt intro]}]

return text 100 "Note that the DO is only evaluated once; when the layout is created. It is not evaluated when the layout face is shown."
return heading "Variables"
return label "Position Variables"
return text 100 {When creating a layout, you will sometimes need to know the position of a face on the page. To do this, a position variable can be set before any layout keyword.
For instance, a convenient way to get the current position is with the AT word. If you provide it with no new position, it will simply set a variable to the current position:}
return tooltip {here: at}

return text 100 {The variable here will hold the current position.
This can be useful if you need to use a position later in your layout. You may want to lay one face on top of another. Here is an example that places text on top of a transparent box:}
return tooltip {backdrop %nyc.jpg
banner "Example"
here: at
box 200x100 effect [multiply 60]
at here + 10x10
vtext bold 200x100 - 20x20 {
   This text is on top of the smoked
   glass, regardless of how the screen
   may layout.  That is the benefit of
   using a variable to set the position.
}}  [lancia { view layout [ 
backdrop %nyc.jpg
banner "Example"
here: at
box 200x100 effect [multiply 60]
at here + 10x10
vtext bold 200x100 - 20x20 {
   This text is on top of the smoked
   glass, regardless of how the screen
   may layout.  That is the benefit of
   using a variable to set the position.
}]}]

return label "Face Variables"

return text 100 {Some of the faces that you use in a layout will need to be changed when the page is being displayed. For instance, the action of a button may trigger a change in text or images that are displayed.
To obtain the face that was created with a style, set a variable just before the style word. For example, here the variable name will refer to the text face that is created:}
return tooltip {name: text "Merlot" 100x30}  [lancia { view layout [ name: text "Merlot" 100x30]}]

return text 100 "At another point on the page the text can be changed with a button that modifies the face's contents:"
return tooltip {name: button "Change" [name/text: "Cabernet"  show name]} [lancia { view layout [name: button "Change" [name/text: "Cabernet"  show name]]}]

return text 100 {When the button is pressed, the text field of the name face will be changed to "Cabernet". The show function is then used to update the face in the window so the change can be seen.}
return label "Avoiding Variable Collisions"
return text 100 "For large scripts that have a lot of position and face variables, it may become difficult to manage all of the names and keep them from interfering with each other. A simple solution to this problem is to define pages within objects that have the required variables defined locally to the objects. For instance here is an address book form that keeps all of its variables local:"
return tooltip {make object! [
title-name: name: email: phone: none
num: 1
page1: layout [
  title-name: title "Person 1:"
  box 200x3 red
  across
  text "Name"  tab name: field return
  text "Email" tab email: field return
  text "Phone" tab phone: field return
  button "Send" [
   send %luke--rebol--com [
     "Person " num newline
      name email phone newline
      ]
   num: num + 1
   title-name/text: reform [Person num]
   clear name/text
   clear email/text
   clear phone/text
   show [title-name name email phone]
        ]
    ]
]}

return text 100 "Be sure to add any new variables to the object definition."
return heading "Layout Dialect Keywords"
return label "Layout Organization"

return text 100 {As described in previous documents (soon), the layout dialect consists of:
-Layout keywords that describe face positioning and other layout attributes (see below).
-Face styles that are used to specify the faces that are displayed. These can be predefined styles (see Predefined Styles document) or custom styles.
-Variable definitions that hold either faces or layout positions. These variables can be used later to access face objects or to affect face positions.
-New style definitions that are to be used within the layout. Single styles or entire stylesheets can be provided.

This document will describe the layout keywords.

Note that all layout keywords are optional and most keywords can be used multiple times.}

return label "Layout Attributes"

return text 100 {These words control the layout as it is being created. They affect the placement of faces within the layout.}
return label "Offset"
return text 100 {OFFSET specifies the position of the layout face within its parent face (often the screen). (NA prior to Link 0.4.35)}
return tooltip {offset 10x32}
return text 100 {The offset need not be specified in the layout. It can be specified in the View if necessary. The default offset is 25x25.}
return label "Size"
return text 100 {SIZE sets the size of the layout face. This must be done at the beginning of a layout before any styles are used.}
return tooltip {size 800x600}
return text 100 {If no size is specified, then the layout is auto-sized based on the styles used within it.}
return label "Origin"
return text 100 {ORIGIN sets the starting position of faces in the layout. The origin is specified as the number of pixels from the upper left corner of the layout window. The default origin is 20x20.}
return tooltip {origin 100x100
text "Origin at 100x100"}
return text 100 {If an integer is specified, then both the X and Y positions will be set to that value:}
return tooltip {origin 100
text "Origin at 100x100"}
return text 100 {The origin can also be used within a layout to return the layout to the origin position.}
return tooltip {origin
text "Back at the origin"}
return text 100 {The origin value also determines the amount of spacing between the last face and the bottom right of the layout.
Setting the origin is especially important when creating panels and lists. Frequently the origin in lists is set to zero:}
return tooltip {list 400x80 [
    origin 0
    across
    txt 100
    txt 200
] data [
    ["Bobbie" "Smith"]
    ["Barbie" "Jones"]
    ["Bettie" "Rebol"]
]} [lancia { view layout [
list 400x80 [
    origin 0
    across
    txt 100
    txt 200
] data [
    ["Bobbie" "Smith"]
    ["Barbie" "Jones"]
    ["Bettie" "Rebol"]
]]}]

return heading "Facets"
return text 100 {Facets are attributes of a face. Facets include the face's location, size, color, image, font, style, paragraph format, rendering effects, behavior functions, and other details. Some facets are objects themselves, allowing the sharing of attributes several faces.}
return label "View Facets"
return text 100 {These are the primary facets used by the View display system to show faces. These facets can be inherited from the SYSTEM/view/face object which is also defined globally as the FACE object.

-offset	An X-Y PAIR that specifies the horizontal and vertical position of the face. If a face is outside it's parent face it will be clipped. Defaults to 0x0.
-size	An X-Y PAIR that specifies the width and height of the face. Defaults to 100x100.
-span	An optional X-Y PAIR that specify the range of a virtual coordinate system to use for the face. This can be used to create resolution independent displays. Normally this is set to NONE.
-pane	A face or block of sub-faces that are to be displayed within the face. This allows you to create faces that contain faces to any degree.
-text	The text contents of a face. The attributes of the text are determined by the FONT and PARA facets. Any printable value can be used.
-data	Used by VID for storing other information about the face. Outside of VID this field can be freely used by programs.
-color	The color of the face, specified as a TUPLE. When set to NONE the face is transparent. Default value is 128.128.128.
-image	An IMAGE to use for the face's body. This must be an IMAGE value not a file name. A wide range of image processing effects can be performed on the image with the EFFECT field.
-effect	A WORD or BLOCK that renders image processing effects on the face image or background. More than one effect can be used at the same time.
-edge	An OBJECT that specifies the edge of the face. It can include the color, size, and effects used for the edge.
-font	An OBJECT that specifies the font used for the text. This includes the font name, style, size, color, offset, space, align, and other attributes.
-para	An OBJECT that describes the paragraph characteristics of the text. It includes the origin, margin, indent, tabs, edit, wrap, and scrolling attributes.
-feel	An OBJECT that holds the functions that define the behavior of the face. These functions are evaluated during the rendering, selection, and hovering over a face and during events related to the face.
-rate	An INTEGER or TIME that specifies the rate of time events for a face. This is used for animation or repetitive events (such as holding the mouse down on certain types of user interface styles). An INTEGER indicates the number of events per second. A TIME provides the period between events.
-options	A BLOCK of optional flags for the face. These are normally used by a top-level view face. Options include NO-TITLE, RESIZE, NO-BORDER, ALL-OVER.
-saved-area	Enables faster rendering for transparent faces. When a face is transparent on a static (unchanging) backdrop, this field can be set to TRUE to accelerate redrawing. The face can change without requiring the backdrop to be rendered each time. The pixels for the area under the face will be saved into this field, changing it from a TRUE to an IMAGE. This field defaults to NONE.
-line-list	A BLOCK that is used to track the offsets of text lines when text is being displayed. When more than 200 characters of text are being displayed, this list should be set to NONE when large changes are made to the text. This allows REBOL to recalculate the locations of all TEXT lines.}

return heading "VID Extensions"

return text 100 {VID extends the face definition to include these additional facets. Faces that are created with the LAYOUT or MAKE-FACE functions will include these facets in addition to those described above.
-colors	A BLOCK of alternate colors used for the face. For example, this field would hold the colors for a button that changes colors on being selected.
-texts	A BLOCK of alternate text used for the face. For example, buttons that display different text on selection would store that text here.
-effects	A BLOCK of alternate effects used for a face. For example, a BUTTON style may use a different effect when it is in the down position.
-action	A BLOCK or FUNCTION that is evaluated when the face has been selected. The type of event that triggers this action depends on the style of the face.
-alt-action	An alternate BLOCK or FUNCTION that is evaluated on an alternate selection of the face.
-keycode	A CHAR or BLOCK of shortcut keys for the face. When pressed, these keys will evaluate the ACTION field.
-state	The event state of buttons. Indicates that the button is still being pressed.
-dirty?	A LOGIC flag that indicates that the text of the face has been modified. Whenever editing is performed upon a text face, this flag will be set to TRUE.
-help	An optional string that can be used for displaying information about a button or other type of GUI element. For example, when the mouse pointer hovers over a face, this string can be displayed as help information.
-file	The FILE path or URL of the image file used for the face. The image file is automatically loaded and cached by VID.
-style	The style WORD that was used to create the face. For example: BUTTON, FIELD, IMAGE, RADIO, etc.
-user-data	A field that is available to programs for storing data related to the face. This field is not used by the VID system.}

return label "Edge Facet"

return text 100 {The EDGE facet is an object that describes a rectangular frame that borders a face. It is used for creating image frames, button edges, table cell dividers, and other border effects. An edge is specified as an sub-object within the face object.
An EDGE object contains these fields:
-color	The color of the edge specified as a TUPLE.
-size	An X-Y PAIR that specifies the thickness of the edge. The x value refers to the thickness of the vertical edges on the left and right, and the Y value refers to the horizontal edges at the top and bottom.
-effect	A WORD or BLOCK that describes the effect to use for the edge. Edge effects include BEVEL, IBEVEL, BEZEL, IBEZEL, and NUBS.}

return label "Font Facet"

return text 100 {The FONT facet is an object that describes the attributes of the text to be used within a face. The font is specified as an sub-object within the face object.
The FONT object contains these fields:
-name	The name of the font to use for the text. There are three predefined variables for machine independent fonts that have a similar appearance: font-serif (times-like), font-sans-serif (helvetica-like), and font-fixed (courier fixed width). To create machine independent programs, avoid specifying custom fonts. The default is font-sans-serif.
-size	An INTEGER that specifies the point size of the font. The default size is 12.
-style	A WORD or BLOCK of words that describe the style of the text. Choices are: BOLD, ITALIC, and UNDERLINE. When set to NONE no styles are used (default).
-color	A TUPLE that specifies the color of the text. The default color is black (0.0.0).
-align	A WORD that provides the alignment of the text within the face. Choices are: LEFT, RIGHT, and CENTER.
-valign	A WORD that indicates the vertical alignment of the text within the face. Choices are: TOP, BOTTOM, and MIDDLE.
-offset	A PAIR that specifies the offset of the text from the upper left corner of the face. The PARA facet object also has an effect on this offset. Default is 2x2.
-space	A PAIR that specifies the spacing between characters and between lines. The x value affects the spacing between characters. The y value changes the spacing between lines. Positive values expand the text, negative values condense it. The default is 0x0.
-shadow	A PAIR that specifies the direction and offset of the drop shadow to use for the text. Positive values project a shadow toward the lower right corner. Negative values project toward the upper left. The default is NONE.}

return label "Para Facet"

return text 100 {The PARA facet is an object that controls the formatting of text paragraphs within the face. A para is specified as a sub-object within a face object.
The PARA object contains these fields:
-origin	An X-Y PAIR that specifies the offset of the text from the upper left corner of a face. The default is 2x2.
-margin	An X-Y PAIR that specifies the right-most and bottom limits of text display within the face. The position is relative to the bottom right corner of the face. The default is 2x2.
-indent	An X-Y PAIR that specifies the offset of a the first line of a paragraph. The X value specifies the indentation used for the first line of the paragraph. Positive and negative values may be used. The Y value specifies the spacing between the end of the previous paragraph and the first line of the next paragraph. The Y value has no affect on the first paragraph. The default is 0x0.
-scroll	An X-Y PAIR used for horizontal and vertical scrolling of text within a face. The scroll amount that modifies the offset of the text relative to the face. The origin and margin values are not affected. The default is 0x0.
-tabs	An INTEGER or BLOCK of integers that provide the tab spacing used within a paragraph. An INTEGER value indicates a fixed tab size spaced at regular intervals across the text. A BLOCK of integers provides the precise horizontal offset positions of each TAB in order. The default is 40.
-wrap?	A LOGIC value that indicates that automatic line wrapping should occur. When set to TRUE, text that exceeds the margin will be automatically wrapped to the origin. When set to FALSE, text will not be wrapped.}
return label "Feel Facet"

return text 100 {The FEEL facet controls face's behavior in response system events like redraw, mouse input, and keyboard input. The fields of the feel object are all functions that are called by the View system on specific events. A summary of these functions is provided below. See the Face Feeling chapter for details.
The FEEL object contains these fields:
-engage	The primary function called for the majority of events that occur within a face. The ENGAGE function is called when the mouse pointer is over it's face and either mouse button is pressed. The function will also be called if a mouse button has been pressed and the mouse is moved over the face. In addition, the function is called when time events occur, such as for animation or repetitive selection events.
-over	This function is called when the mouse pointer passes over the face and no buttons are pressed. This allows code to capture hover events and provide user feedback by changing the appearance of the face. For example, hot text may change the color of the text as the mouse passes over it. This field is separate from ENGAGE because it is not used for most faces. Over actions can occur at a high frequency, so setting the OVER field to NONE allows the system to ignore it.
-detect	This function is called each time any event passes through a face. This function can be used to process events that are directed toward any subface of the face. For example, the function is used by VID to process keyboard shortcuts. The DETECT function is normally used at the window face or screen face level. Note that the insert-event-func function should be used to trap screen-face global events.
-redraw	This function is called immediately before a face is displayed. Defining this function allows a face to dynamically modify any of its facets prior to being displayed. When not being used, it is critical that this function be set to NONE to speed up the display.}
return label "Effect Facet"
return text 100 {The EFFECT facet can be set to a WORD or a BLOCK that describes image processing operations to be performed on the backdrop of a face. When a block is used, multiple effects can be specified, and they are applied in the order in which they appear within the block. A wide range of hundreds of effects can be produced.
-fit	Scales an image to the size of the face, less the edge of the face if it exists. The image will be scaled both horizontally and vertically to fit within the face.
-aspect	Similar to FIT, but preserves the perspective of the image. The image is not distorted. If the image does not span the entire face, the remaining portion will be filled with the face background color.
-extend	Extends an image horizontally, vertically, or both. An image is stretched without affecting its scale. For instance, a button with rounded ends can be resized without affecting the dimensions of the rounded ends. This allows a single button bitmap to be reused over a wide variety of sizes. Two PAIRs are supplied as arguments. The first PAIR specifies the offset where the image should be extended. It can be horizontal, vertical, or both. The second PAIR specifies the number of pixels to extend in either or both directions.
-tile	Repeats the image over the entire face. This allows you to apply textures that span an entire face. The tile offset will be relative to the face.
-tile-view	Similar to TILE, but the tile offset will be relative to the window face.
-clip	Clips an image to the size of the face. This is normally done when the image is larger than the face, and the remaining effects do not need to be performed on the entire bitmap. The CLIP can be done at anytime in the effect block. For instance a CLIP done before a FLIP will produce a different result than a CLIP done after a FLIP.
-crop	Extracts a portion of an image. This effect takes two PAIRs: the offset into the image and the size of the area needed. This operation can be used to pick any part of an image to be displayed separately. It allows you to pan and zoom on images.
-flip	Flips an image vertically, horizontally, or both. A PAIR is provided as an argument to specify the direction of the flip. The X specifies horizontal and the Y specifies vertical.
-rotate	Rotates an image. An INTEGER specifies the number of degrees to rotate in the clockwise direction. (Currently only 0, 90, 180, and 270 degree rotations are supported.)
-reflect	Reflects an image vertically, horizontally, or both. A PAIR is used to indicate the direction of reflection. The X value will reflect horizontally, and the Y value will reflect vertically. Negative and positive values specify which portion of the image is reflected.
-invert	Inverts the RGB values of an image. (Inversion is in the RGB color space.)
-luma	  Lightens or darkens an image. An INTEGER specifies the degree of the effect. Positive values lighten the image and negative values darken the image.
-contrast	Modifies the contrast of the image. An INTEGER specifies the degree of the effect. A positive value increases the contrast and a negative value reduces the contrast.
-tint	Changes the tint of the image. An INTEGER specifies the color phase of the tint.
-grayscale	Converts a color image to black and white.
-colorize	Colors an image. A TUPLE specifies the COLOR. The image is automatically converted to grayscale before it is colorized. [???Note] in docs/view-guide.txt
-multiply	Multiplies each RGB pixel of an image to produce interesting coloration. An INTEGER, TUPLE, or IMAGE can be specified. An INTEGER will multiply each color component of each pixel by that amount. A TUPLE will multiply each of the red, green, and blue components separately. An IMAGE will multiply the red, green, and blue components of an image, allowing you to apply textures to existing images. [???Note] in docs/view-guide.txt
-difference	Computes a difference of RGB pixel values. This can be used to compare two images to detect differences between them. An IMAGE is provided as an argument. Each of its RGB pixel values will be subtracted from the face image.
-blur	Blurs an image. This effect may be used multiple times to increase the effect.
-sharpen	Sharpens an image. This effect may be used multiple times to increase the effect.
-emboss	Applies an emboss effect to the image.
-gradient	Generates a color gradient. A PAIR and two color TUPLEs can be supplied as arguments (optional). The PAIR is used to determine the direction of the gradient. The X value of one specifies horizontal and a Y value of one specifies vertical. Both X and Y can be specified at the same time, producing a gradient in both directions. Negative values reverse the gradient in that direction.
-gradcol	Colorizes an image to a gradient. Arguments are identical to GRADIENT. The image is colorized according to the colors of the gradient.
-gradmul	Multiplies an image over a gradient. Arguments are identical to GRADIENT. The image is multiplied according to the colors of the gradient.
-key	Creates a transparent image by keying. A TUPLE or INTEGER can specify a chroma or luma key effect. A TUPLE will cause all pixels of the same value to become transparent. An INTEGER will cause all pixels with lesser luma values to become transparent.
-shadow	Creates a drop shadow on a keyed image. Accepts the same arguments as KEY, but in addition to a creating transparent image it generates a 50 percent drop shadow.
-arrow	Generate an arrow image. An optional TUPLE can be used to specify the color of the arrow, otherwise the edge color will be used. The arrow is proportional to the size of the face. The direction of the arrow can be altered with FLIP or ROTATE.
-cross	Generate an X cross image. This is used for check boxes. An optional TUPLE can be used to specify the color of the cross, otherwise the edge color will be used. The cross is proportional to the size of the face.
-oval	Generate a oval image. An optional TUPLE can be used to specify the color of outside of the oval, otherwise the edge color will be used. The oval will be proportional to the size of the face.
-tab	Generate tab buttons with rounded corners. The optional arguments are: a PAIR that specifies the edge to round, a TUPLE that is used as an edge color, an INTEGER that indicates the radius of the curves, and an INTEGER that controls the thickness of the edge.
-grid	Generate a two dimensional grid of lines. This is a useful backdrop for graphical layout programs. The optional arguments are: a PAIR that specifies the horizontal and vertical spacing of the grid lines, a PAIR that specifies the offset of the first lines, a PAIR that indicates the THICKNESS of the horizontal and vertical lines, and a TUPLE that provides the color of the lines.
-draw	Draws simple lines, shapes, and fills within a face. See the Draw Dialect document for detailed information.
}
]
]

;VID handler guide
guida_handler: [
	heading "How to Handle User Interface Events"
	return
	text italic bold "You can click on the examples to see the results"
	return 
	scroll-panel 120x100 data [

label "How to Run the Examples"

return text 100 "To run any of the examples that are shown below, run a text editor and create a REBOL header line such as:"
return tooltip {REBOL [Title: "Example"]}
return text 100 {Then simply cut the example text and paste it after this line. Save the text file and give it a name, such as example.r. Then run the file just as you would run any REBOL file.}

return label "The Feel Object and Its Functions"
return text 100 {Every graphical object displayed by REBOL is a FACE. The look and feel of a face is specified by the fields of the object. One field of the object defines the FEEL of the object, and specifies how the object behaves on user input and events. When you type a key on the keyboard or move and click the mouse, it is the FEEL object that determines how the action is handled.
The REBOL/View event system is quite elegant and has evolved over many years prior to release. This is how the Visual Interface Dialect (VID) is able to create a range of behaviors for dozens of user interface objects in only a couple hundred lines of code.}
return label "Feel Functions"
return text 100 {The entire REBOL user interface system is handled by these four functions:
-redraw [face action position]
-over [face action position]
-engage [face action event]
-detect [face event]

These functions each have a specific purpose within the user interface event system:
-redraw	is called immediately before the face is drawn, allowing you to modify certain attributes of the face before it is shown. Each time the face refreshes its look, or each time it is shown or hidden, this function is called.
-over	is called whenever the mouse pointer passes over or off of a face. This may happen at a very high rate, because a user interface may consist of hundreds of faces and the user may move the mouse over those faces a lot. That's the reason why this is a single function and is not combined with the engage function. This function should be set to NONE if it is not needed allowing the system to ignore the face as the mouse passes over it.
-engage	is called whenever an event occurs for a face. This function handles events like mouse down, up, alt-down, double-click, timers, keyboard keys and more.
-detect	is called whenever any event occurs for a face, or for any of the faces that are contained within it. This allows a face to intercept events that are aimed at lower level graphical objects.

Any face can have a FEEL object with one or more of the above functions. This allows you to handle events from any type of graphical object, including images, text, boxes, or lines.

Note that most objects of the system share feel objects. For example, BUTTON faces share a single FEEL object that specifies the operations of a button. Modifying the FEEL object of a button will modify the FEEL object of all other buttons. Sometimes this effect may not be desired. To avoid the effect you can clone the FEEL object and only modify it for the face that you need.}
return label "The Redraw Feel"
return text 100 {The REDRAW feel function is quite useful when you need to modify the look of a face immediately before it is drawn. Doing this can minimize the amount of code needed to produce face state effects such as highlighting or changing a graphic when the mouse clicks on a face.
The REDRAW function has the form:

redraw face action position

The arguments of the function are:
-face	The face object being redrawn.
-action	A word that indicates the action that occurred on the face: DRAW, SHOW, HIDE.
-position	The X-Y position of the face if the face is iterated. Iterated faces will be covered in another document. For now, you can ignore this argument.

Here is a very simple example that will help you understand the REDRAW function:}
return tooltip{view layout [
    the-box: box "A Box" forest feel [
        redraw: func [face act pos] [print act]
    ]
    button "Show" [show the-box]
    button "Hide" [hide the-box]
]}[lancia { view layout [the-box: box "A Box" forest feel [
        redraw: func [face act pos] [print act]
    ]
    button "Show" [show the-box]
    button "Hide" [hide the-box]
]}]

return text 100 {This function will print the action word that is passed each time the REDRAW function is called. When you run the example, you will see the console immediately print:

show
draw

The show occurs when the VIEW function requests that the window be displayed. Then, the draw occurs immediately before the face is rendered.

If you click on the "Show" button, you will see the same two actions occur:

show
draw

This time the show is being done on the face directly.

When you click on the "Hide" button, the output will be:

hide

There is no show, so there is no draw either.}

return label "The Over Feel"

return text 100 {The OVER feel function senses the mouse passing over a face. It can be used to provide visual feedback that the mouse is over an object, or it can display help information about an item when the user hovers the mouse over it.
The OVER function has the form:

over face action position

The arguments to the OVER function are:
-face	The face object under the mouse pointer.
-action	A logic value that is either TRUE or FALSE to indicate if the mouse is entering or exiting the face.
-position	The current X-Y position of the mouse.

Here is a simple example that will help you understand the OVER function:}
return tooltip{print "Displaying..."
view layout [
    box "A Box" forest feel [
        over: func [face act pos] [print [act pos]]
    ]
]} [lancia { print "Displaying..."
view layout [box "A Box" forest feel [
        over: func [face act pos] [print [act pos]]
    ]
]}]

return text 100 {Run this example and pass the mouse over the box. The console will open first, then the window with the box. Make sure that the window with the box is the active window and pass the mouse over the box.

As the mouse enters the box you will see the console display:

true 23x72

And, when the mouse exits the box, you will see a message such as:

false 120x73

The action argument is TRUE when the mouse is entering and it is FALSE when the mouse is exiting.

Note that first PRINT in this example is done to open the console window to display the OVER results. If this is not done, then the first time you pass the mouse over the box, the console will open. On some systems, such as Windows, the window containing the box will lose focus, and the OVER function will immedately return FALSE. You can see this happen if you remove the first PRINT line.

Here are two examples that do something when the mouse passes over the face. The first example changes the text in the box to indicate the presence of the mouse:}
return tooltip {view layout [
    box "A Box" forest feel [
        over: func [face act pos] [
            face/text: either act ["Over"]["Away"]
            show face
        ]
    ]
]}  [lancia { view layout [
    box "A Box" forest feel [
        over: func [face act pos] [
            face/text: either act ["Over"]["Away"]
            show face
        ]
    ]
]}  ]

return text 100 {It shows the box with the word "Over" when the mouse is over the box, or "Away" when the mouse is off the box.

Notice that the SHOW function was called to display the new text for the face.

Here's an example that changes the color of the face as the mouse passes over:}
return tooltip {view layout [
    box "A Box" forest feel [
        over: func [face act pos] [
            face/color: either act [brick][forest]
            show face
        ]
    ]
]}  [lancia { view layout [
 box "A Box" forest feel [
        over: func [face act pos] [
            face/color: either act [brick][forest]
            show face
        ]
    ]
]}]

return text 100 {Here's an example that shows a "help line" based on where the mouse is:}
return tooltip {view layout [
    box "Top Box" forest feel [
        over: func [face act pos] [
            helper/text: either act ["Over top box."][""]
            show helper
        ]
    ]
    box "Bottom Box" navy feel [
        over: func [face act pos] [
            helper/text: either act ["Over bottom box."][""]
            show helper
        ]
    ]
    helper: text 100
]}   [lancia { view layout [
 box "Top Box" forest feel [
        over: func [face act pos] [
            helper/text: either act ["Over top box."][""]
            show helper
        ]
    ]
    box "Bottom Box" navy feel [
        over: func [face act pos] [
            helper/text: either act ["Over bottom box."][""]
            show helper
        ]
    ]
    helper: text 100
]}   ]

return label "Overlapping Faces"

return text 100 "When faces overlap the system will inform your code as you pass from one face to another. Here is an example that shows how this occurs:"
return tooltip {print "Displaying..."
view layout [
    box "A Box" forest feel [
        over: func [face act pos] [print ["A Box:" act]]
    ]
    pad 30x-40
    box "B Box" brick feel [
        over: func [face act pos] [print ["B Box:" act]]
    ]
]}  [lancia {
print "Displaying..."
view layout [
    box "A Box" forest feel [
        over: func [face act pos] [print ["A Box:" act]]
    ]
    pad 30x-40
    box "B Box" brick feel [
        over: func [face act pos] [print ["B Box:" act]]
    ]
]}]

return text 100 {As the mouse passes onto the A box the console prints:

A Box: true

When the mouse moves from the A box to the B box, then the console prints:

A Box: false
B Box: true

It first indicates that the mouse is no longer over the A box, then tells you that it is over the B box.}
return label "Continuous Over Events"

return text 100 "It is possible to track the mouse constantly while it is over a face. To do so, you must indicate to the top level window face that you want to know about all over events that occur:"
return tooltip {print "Displaying..."
out: layout [
    box "A Box" forest feel [
        over: func [face act pos] [print [act pos]]
    ]
]
view/options out [all-over]} [lancia {
print "Displaying..."
out: layout [
    box "A Box" forest feel [
        over: func [face act pos] [print [act pos]]
    ]
]
view/options out [all-over]}]
return text 100 {This code will report a continuous stream of mouse positions as the mouse moves over the face. Normally this is not necessary. It can slow down the user interface. Do it only when you need to.

Also, this is not the only way to track mouse movements. Other ways will be shown in the next sections.}
return label "The Engage Feel"
return text 100 {The engage function is called whenever any event other than a REDRAW or an OVER occurs for a face. It handles mouse click events, keyboard input, timers, and other types of events.
The ENGAGE function has the form:

engage face action event

Where its arguments are:
-face	The face that has the event.
-action	A word that indicates the action that has occurred.
-event	The event that provides detailed information about the action.}
return label "Mouse Event Example"

return text 100 "Here's a short example that will print mouse events that occur on a box:"
return tooltip {view layout [
    box "A Box" forest feel [
        engage: func [face action event] [
            print action
        ]
    ]
]} [lancia {
view layout [
    box "A Box" forest feel [
        engage: func [face action event] [
            print action
        ]
    ]
]}]

return text 100 {Run this example and click on the box. Right click on the box. Press the mouse button down, then move the mouse as if you were dragging the box.
As you use the mouse, you will see a stream of events such as:

down
up
alt-down
alt-up
down
over
over
over
up
down
over
over
over
away
away
away
away
away
up

These events reflect the actions you peformed with the mouse. Here is a summary of the events:
-down	the main mouse button was pressed.
-up	the main mouse button was released.
-alt-down	the alternate mouse button was pressed (right button).
-alt-up	the alternate mouse button was released.
-over	the mouse was moved over the face while either button was pressed.
-away	the mouse passed off the face while the button was pressed.}
return label "Drag and Drop Example"
return text 100 {Using some of the above actions, here is an example that shows how to drag a face around within a window:}
return tooltip {view layout [
    size 200x200
    box 40x40 coal "Drag Box" font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [start: event/offset]
            if find [over away] action [
                face/offset: face/offset + event/offset - start
                show face
            ]
        ]
    ]
]}  [lancia {
view layout [
    size 200x200
    box 40x40 coal "Drag Box" font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [start: event/offset]
            if find [over away] action [
                face/offset: face/offset + event/offset - start
                show face
            ]
        ]
    ]
]} ]
return text 100 {When the mouse is clicked in the box, the offset of the mouse relative to the box is stored in the START variable. As the mouse is moved with the button down, the over and away events are sent and the new offset is added to the position of the face. The START offset is subtracted to locate the face correctly relative to the mouse pointer.
If the start position is stored within the box face, then a style can be created and multiple drag and drop boxes can be made from a single style:}
return tooltip {view layout [
    size 240x240
    style dragbox box 40x40 font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [face/data: event/offset]
            if find [over away] action [
                face/offset: face/offset + event/offset - face/data
                show face
            ]
        ]
    ]
    dragbox "Box 1" navy
    dragbox "Box 2" teal
    dragbox "Box 3" maroon
    dragbox "Box 4" gold
]} [lancia {
view layout [
    size 240x240
    style dragbox box 40x40 font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [face/data: event/offset]
            if find [over away] action [
                face/offset: face/offset + event/offset - face/data
                show face
            ]
        ]
    ]
    dragbox "Box 1" navy
    dragbox "Box 2" teal
    dragbox "Box 3" maroon
    dragbox "Box 4" gold
]} ]

return text 100 {You can now drag any of the four boxes around. Notice that you can drag boxes under other boxes. The DRAGBOX style is defined with the new ENGAGE function that stores the starting position in the face's data field.
To pop the current face to the top, move it to the end of the window's face pane list when the down event occurs:}
return tooltip {view layout [
    size 240x240
    style dragbox box 40x40 font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [
                face/data: event/offset
                remove find face/parent-face/pane face
                append face/parent-face/pane face
            ]
            if find [over away] action [
                face/offset: face/offset + event/offset - face/data
            ]
            show face
        ]
    ]
    dragbox "Box 1" navy
    dragbox "Box 2" teal
    dragbox "Box 3" maroon
    dragbox "Box 4" gold
]} [lancia {
view layout [
    size 240x240
    style dragbox box 40x40 font-size 11 feel [
        engage: func [face action event] [
            if action = 'down [
                face/data: event/offset
                remove find face/parent-face/pane face
                append face/parent-face/pane face
            ]
            if find [over away] action [
                face/offset: face/offset + event/offset - face/data
            ]
            show face
        ]
    ]
    dragbox "Box 1" navy
    dragbox "Box 2" teal
    dragbox "Box 3" maroon
    dragbox "Box 4" gold
]}]

return text 100 "The example uses the parent-face field to access the window's pane list. You could also have assigned the window layout to a variable and used that to refer to the pane list."
return label "Keyboard Events"
return text 100 {To receive keyboard events, the face must be made the focus before they will be sent. Here is an example:}
return tooltip {view/new layout [
    the-box: box "A Box" forest feel [
        engage: func [face action event] [
            print [action event/key]
        ]
    ]
]
focus the-box
do-events}  [lancia {

view/new layout [
    the-box: box "A Box" forest feel [
        engage: func [face action event] [
            print [action event/key]
        ]
    ]
]
focus the-box
do-events} ]

return text 100 {When you type on the keyboard you will see a stream such as:

key a
key b
key c
key d

The event/key contains the keycode character for the key that was pressed.

If you press the function keys you will see:

key home
key end
key up
key down
key f1
key f5

However, these are not keycodes; they are words. In REBOL you do not need to decode the keyboard sequences. They are decoded for you. This makes it easy to write a key handler. Here is an example:}
return tooltip {view/new layout [
    the-box: box "A Box" forest feel [
        engage: func [face action event] [
            if action = 'key [
                either word? event/key [
                    print ["Special key:" event/key]
                ][
                    print ["Normal key:" mold event/key]
                ]
            ]
        ]
    ]
]
focus the-box
do-events}  [lancia {
view/new layout [
    the-box: box "A Box" forest feel [
        engage: func [face action event] [
            if action = 'key [
                either word? event/key [
                    print ["Special key:" event/key]
                ][
                    print ["Normal key:" mold event/key]
                ]
            ]
        ]
    ]
]
focus the-box
do-events}]

return text 100 {To detect if the control or shift keys are being held down you can write conditional tests such as:

if event/control [...]

if event/shift [...]

if event/control/shift [...]

And finally, if your system has a scroll wheel, its events will also occur as:

scroll-line

and if the control key is held down:

scroll-page

The amount of the scroll can be determined from the Y offset field of the event. Add this to one of the above examples.

if action = 'scroll-line [print event/offset/y]

The size of the Y offset is determined by the scroll-wheel sensitivity that has been set for your operating system.
Timer Events

Each face can have its own timer associated with it. When the timer expires, a TIME event will occur. Here is an example of a repeating time event that occurs every second:}
return tooltip {view layout [
    box "A Box" forest rate 1 feel [
        engage: func [face action event] [
            print action
        ]
    ]
]}  [lancia {
view layout [
    box "A Box" forest rate 1 feel [
        engage: func [face action event] [
            print action
        ]
    ]
]} ]

return text 100 {The rate can specify either the number of events per second or the period between events. If you used:

rate 10

then you would get ten events per second. If you wrote:

rate 0:00:10

then you would get a time event every ten seconds. Or,

rate 0:10

would send you a time event every 10 minutes.

Here is a digital clock that is based on time events:}
return tooltip {view layout [
    origin 0
    banner "00:00:00" rate 1 feel [
        engage: func [face act evt] [
            face/text: now/time
            show face
        ]
    ]
]}  [lancia {
view layout [
    origin 0
    banner "00:00:00" rate 1 feel [
        engage: func [face act evt] [
            face/text: now/time
            show face
        ]
    ]
]} ]

return text 100 {To create a "single shot" time event that occurs only once, you can disable the timer within the event:}
return tooltip {
ticks: 0
view layout [
    box "A Box" forest rate 0:00:10 feel [
        engage: func [face action event] [
            if action = 'time [
                if ticks > 0 [
                    face/rate: none
                    show face
                ]
                ticks: ticks + 1
                print now
            ]
        ]
    ]
]} [lancia {
ticks: 0
view layout [
    box "A Box" forest rate 0:00:10 feel [
        engage: func [face action event] [
            if action = 'time [
                if ticks > 0 [
                    face/rate: none
                    show face
                ]
                ticks: ticks + 1
                print now
            ]
        ]
    ]
]} ]

return text 100 {The first time event occurs immediately. (A bug in time events.) The TICKS variable keeps the count of how many times the event has occurred. To shut off the timer, the rate is set to NONE and SHOW is called on the face to update the timer internal values.}
return label "The Detect Feel"
return text 100 {The DETECT function is similar to ENGAGE, but has the ability to intercept events for all of its subfaces. DETECT can be used to process special events such as keyboard input, timers, or mouse events.
The DETECT function works as an event filter. When an event occurs, DETECT can decide how to handle the event. When it is done, the function can allow the event to continue to lower level faces, or stop it immediately.
DETECT should not be used if ENGAGE can deal with the event directly. DETECT is only needed when it is necessary to filter out events that are directed toward subfaces.
The DETECT function has the form:

detect face event

Where its arguments are:
-face	The face that has the event.
-event	The event that provides detailed information.

The DETECT function must return either:
-event	The same event that it was passed as an argument.
-none	When the event is not to be processed by subfaces.

Here is an example that will print every event that is received by the box face:}
return tooltip {print "Running.."
view layout [
    box 200x200 "A Box" navy feel [
        detect: func [face event] [
            print event/type
            event
        ]
    ]
]} [lancia {
print "Running.."
view layout [
    box 200x200 "A Box" navy feel [
        detect: func [face event] [
            print event/type
            event
        ]
    ]
]} ]

return text 100 {If the box is expanded to include a few faces within it, you can see how DETECT is used to filter events. In the example below, if you click on the "Lock Out" button, all events are locked out until you right click.}
return tooltip {lock-out: off
out: layout [
    the-box: box 240x140 teal feel [
        detect: func [face event] [
            if event/type = 'alt-down [
                lock-out: off
                vt/text: "Back to normal."
                show vt
            ]
            if not lock-out [return event]
            return none
        ]
    ]
]
out2: layout [
    space 0x8
    field "Type here"
    across
    button "Lock Out" [
        lock-out: on
        vt/text: trim/lines {Events are locked out.
            Right click to resume.}
        show vt
    ]
    button "Quit" [quit]
    return
    vt: vtext bold 200x30
]
the-box/pane: out2/pane
view out} [lancia {
lock-out: off
out: layout [
    the-box: box 240x140 teal feel [
        detect: func [face event] [
            if event/type = 'alt-down [
                lock-out: off
                vt/text: "Back to normal."
                show vt
            ]
            if not lock-out [return event]
            return none
        ]
    ]
]
out2: layout [
    space 0x8
    field "Type here"
    across
    button "Lock Out" [
        lock-out: on
        vt/text: trim/lines {Events are locked out.
            Right click to resume.}
        show vt
    ]
    button "Quit" [quit]
    return
    vt: vtext bold 200x30
]
the-box/pane: out2/pane
view out}]

return text 100 "Here the detect function only returns the event if the LOCK-OUT variable is set false. Otherwise it returns NONE and no events are passed down to the subfaces."
return label "Window Level Detect"
return text 100 {To use the DETECT function at the window level, you must set the DETECT feel function after the window VIEW has occurred, otherwise the VIEW function will override your FEEL. Here is an example:}
return tooltip {out: layout [banner "Testing"]
view/new out
out/feel: make out/feel [
    detect: func [face event] [...]
]} [lancia {
out: layout [banner "Testing"]
view/new out
out/feel: make out/feel [
    detect: func [face event] [...]
]} ]
return text 100 "It is better to use the INSERT-EVENT-FUNC function to set window event handlers. This function allows multiple handlers for each window. It will be discussed separately."
]]

;Draw guide
guida_DRAW: [
	heading "The DRAW dialect"	
	return
	text italic bold "You can click on the examples to see the results"
	return 
	scroll-panel 120x100 data [



return text 100 {DRAW commands are a dialect of REBOL.
DRAW blocks consist of a sequence of commands followed by arguments. DRAW commands may set attributes and modes that are used by commands that follow.
The DRAW block is not reduced, but word lookup is allowed. This is a change from prior versions of REBOL.
This change allows drawings that use the DRAW block to be embedded in messages (such as in View desktop icons, IOS conference, or AltME messages) without security concerns (because normal REBOL functions cannot be executed).
For example, this is allowed (because only words need to be evaluated):}
return tooltip {draw [pen color box offset margin]}

return text 100 {But this is not allowed (because block evaluation is needed):}
return tooltip {draw [pen color / 2  box offset offset + size]}

return text 100 {If you need that, you will need to perform REDUCE or COMPOSE yourself, prior to using the DRAW block:}
return tooltip{
reduce  ['pen color / 2  'box offset offset + size]
compose [pen (color / 2)  box offset (offset + size)]}

return label "Trying Examples"
return text 100 {To try any of the examples below, you can write a program as simple as this:}
return tooltip {view layout [box 400x400 black effect [draw [...]]]}
return text 100 {Just cut and paste the DRAW command into the ... block above. For example:}
return tooltip {view layout [box 400x400 black effect [draw [
    fill-pen 3 0x0 0 400 0 1 1 blue blue green red red
    box 0x0 400x400
]]]} [lancia {  
view layout [box 400x400 black effect [draw [
    fill-pen 3 0x0 0 400 0 1 1 blue blue green red red
    box 0x0 400x400
]]]}]
return text 100 "You can also create a simple test function like this:"
return tooltip {test: func [spec] [
    view layout [box 400x400 black effect [draw spec]]
]
test [fill-pen radial 0x0 0 400 0 1 1 blue green red red box]}    [lancia {  
test: func [spec] [
    view layout [box 400x400 black effect [draw spec]]
]
test [fill-pen radial 0x0 0 400 0 1 1 blue green red red box]} ]

return text 100 "Or add another level so you can just copy examples to the clipboard and read them automatically to run them:"

return tooltip {draw-test: does [test load read clipboard://]}    

return text 100 {Anywhere you specify a color, you can provide alpha channel information to control the transparency of the result. For example:}
return tooltip {pen navy fill-pen yellow
box 20x20 80x80
fill-pen 0.200.0.150
pen maroon
box 30x30 90x90}     [lancia {  view layout [box 400x400 black effect [draw [ 
                        pen navy fill-pen yellow
box 20x20 80x80
fill-pen 0.200.0.150
pen maroon
box 30x30 90x90]]]}]

return text "Or:"
return tooltip {image logo.gif 50x50 200x150 pen none line-width 0
fill-pen 200.0.0.128 box 50x50  100x150
fill-pen 0.200.0.128 box 100x50 150x150
fill-pen 0.0.200.128 box 150x50 200x150} [lancia {  view layout [box 400x400 black effect [draw [ 
image logo.gif 50x50 200x150 pen none line-width 0
fill-pen 200.0.0.128 box 50x50  100x150
fill-pen 0.200.0.128 box 100x50 150x150
fill-pen 0.0.200.128 box 150x50 200x150 
]]]}]

return  heading "Standard Commands"
return label "ANTI-ALIAS"
return text 100 {Turns anti-aliasing on or off; it is on by default}
return text  bold 100 {anti-alias on/off}
return text 100 {Notes and Examples
Compare this:}
return tooltip {anti-alias off  line-width 10  circle 200x200 100}  [lancia {  view layout [box 400x400 black effect [draw [ 
              anti-alias off  line-width 10  circle 200x200 100
     ]]]}]

return text "to this:"
     return tooltip {anti-alias on  line-width 10  circle 200x200 100}  [lancia {  view layout [box 400x400 black effect [draw [ 
              anti-alias on  line-width 10  circle 200x200 100
     ]]]}]
return text 100 {The ANTI-ALIAS command currently affects the entire DRAW effect; the last value you set it to is what will be used for all draw commands in the block. (TBD will be changing to keeping last setting in effect until changed)}

return label "ARC"
return text 100 { The ARC command draws a partial section of an ellipse (or circle).
arc  
-center [pair!]   The center of the circle
-radius [pair!]   The radius of the circle
-angle-begin [decimal!] The angle where the arc begins, in degrees
-angle-length [decimal!]  The length of the arc in degrees
-closed [word!]   Optional, must be the word closed. closed - close the arc
         
Notes and Examples
For angle-begin, 0 is to right of the center point, on the horizontal axis.
Arcs are drawn in a clockwise direction from the angle-begin point.
Simple open arcs, beginning at 0.}
return tooltip {arc 200x25  100x100 0  90
arc 200x125 100x100 0 135
arc 200x250 100x100 0 180}    [lancia {  view layout [box 400x400 black effect [draw [ 
arc 200x25  100x100 0  90
arc 200x125 100x100 0 135
arc 200x250 100x100 0 180
      ]]]}]

return text 100 "Simple open arcs, beginning at different angles, but all with the same length."
return tooltip {arc 200x25  100x100 0  120 
arc 200x125 100x100 45 120
arc 200x250 100x100 90 120}    [lancia {  view layout [box 400x400 black effect [draw [ 
arc 200x25  100x100 0  120 
arc 200x125 100x100 45 120
arc 200x250 100x100 90 120
     ]]]}]
     
return text 100 {A closed arc. The arc is closed by drawing lines to the center point of the circle that defines the arc.}
return tooltip {arc 100x100 100x100 0 90  closed
fill-pen red    arc 100x100 90x90 135 180
fill-pen green  arc 300x100 90x90 225 180
fill-pen blue   arc 100x300 90x90 45  180
fill-pen yellow arc 300x300 90x90 315 180
fill-pen red    arc 150x250 90x90 0   180
fill-pen green  arc 150x150 90x90 90  180
fill-pen blue   arc 250x150 90x90 180 180
fill-pen yellow arc 250x250 90x90 270 180}                [lancia {  view layout [box 400x400 black effect [draw [ 
                         arc 100x100 100x100 0 90  closed
fill-pen red    arc 100x100 90x90 135 180
fill-pen green  arc 300x100 90x90 225 180
fill-pen blue   arc 100x300 90x90 45  180
fill-pen yellow arc 300x300 90x90 315 180
fill-pen red    arc 150x250 90x90 0   180
fill-pen green  arc 150x150 90x90 90  180
fill-pen blue   arc 250x150 90x90 180 180
fill-pen yellow arc 250x250 90x90 270 180
	]]]}]

return text 100 "Closed arcs are an easy way to draw wedges for pie charts."
return tooltip {fill-pen red    arc 200x200 90x90 0   90 closed
fill-pen green  arc 200x200 90x90 90  90 closed
fill-pen blue   arc 200x200 90x90 180 90 closed
fill-pen yellow arc 200x200 90x90 270 90 closed}     [lancia {  view layout [box 400x400 black effect [draw [ 
   fill-pen red    arc 200x200 90x90 0   90 closed
fill-pen green  arc 200x200 90x90 90  90 closed
fill-pen blue   arc 200x200 90x90 180 90 closed
fill-pen yellow arc 200x200 90x90 270 90 closed
  ]]]}]

return text 100 "By changing the center point, you can draw exploded pie charts."
return tooltip {pen white line-width 2
fill-pen red    arc 204x204 150x150   0  90 closed
fill-pen green  arc 196x204 150x150  90  30 closed
fill-pen blue   arc 180x190 150x150 120 150 closed
fill-pen yellow arc 204x196 150x150 270  90 closed}  [lancia {  view layout [box 400x400 black effect [draw [
                  pen white line-width 2
fill-pen red    arc 204x204 150x150   0  90 closed
fill-pen green  arc 196x204 150x150  90  30 closed
fill-pen blue   arc 180x190 150x150 120 150 closed
fill-pen yellow arc 204x196 150x150 270  90 closed
    ]]]}]
    

return label "ARROW"

return text 100 {Set the arrow mode
arrow 
-arrow-mode [pair!] Possible numbers for combination in pair!
  0 - none
  1 - head
  2 - tail

Notes and Examples

Arrow marks are drawn at end-points, but not between the line that closes polygons, closed splines, etc.}
return tooltip {arrow 1x2  line 20x20 100x100
arrow 1x2  curve 50x50 300x50 50x300 300x300
arrow 1x2  spline 3 20x20 200x70 
150x200 50x300 80x300 200x200
arrow 1x2  spline closed 3 20x20 
200x70 150x200 50x300 80x300 200x200
arrow 1x2  polygon 20x20 200x70 150x200 50x300
arrow 1x2  box 20x20 150x200} [lancia {  view layout [box 400x400 black effect [draw [
                                       arrow 1x2  line 20x20 100x100
arrow 1x2  curve 50x50 300x50 50x300 300x300
arrow 1x2  spline 3 20x20 200x70 150x200 50x300 80x300 200x200
arrow 1x2  spline closed 3 20x20 200x70 150x200 50x300 80x300 200x200
arrow 1x2  polygon 20x20 200x70 150x200 50x300
arrow 1x2  box 20x20 150x200
 ]]]}]

return text 100 "Arrow is a stateful command; what you apply will be in effect until you change it again. You can reset it to no-head+no-tail with:"
return tooltip {arrow 0x0}

return label "BOX"

return text 100  {The BOX command provides a shortcut for a rectangular polygon. Only the upper-left and lower-right points are needed to draw the box.
box
-upper-left-point [pair!]   
-lower-right-point [pair!]
-corner-radius [decimal!]  Optional. Rounds corners

Notes and Examples

A solid fill-pen will fill the box with that color.}

return tooltip {fill-pen blue box 20x20 200x200}[lancia {  view layout [box 400x400 black effect [draw [
fill-pen blue box 20x20 200x200
      ]]]}]

return text 100 "An image used as the fill-pen will be repeated as the background."
return tooltip {fill-pen logo.gif  box 20x20 200x200}      [lancia {  view layout [box 400x400 black effect [draw [
fill-pen logo.gif  box 20x20 200x200
  ]]]}]

return text 100 "Boxes with rounded corners."
return tooltip {fill-pen blue box 20x20 380x380 30
fill-pen logo.gif  box 50x50 350x350 15} [lancia {  view layout [box 400x400 black effect [draw [
  fill-pen blue box 20x20 380x380 30
fill-pen logo.gif  box 50x50 350x350 15
   ]]]}]

return text 100 "line widths, patterns, joins, and rounded corners are fully supported."
return tooltip {pen red yellow
line-pattern 50 30
line-width 30
line-join round
box 50x50 350x350 
box 150x150 250x250 50} [lancia {  view layout [box 400x400 black effect [draw [
         pen red yellow
line-pattern 50 30
line-width 30
line-join round
box 50x50 350x350 
box 150x150 250x250 50
     ]]]}]

return label "CIRCLE"

return text 100 {Draws a circle or ellipse
circle
-center [Pair!]
-radius-x [decimal!] Used for both X and Y radii if radius-y isn't provided
-radius-y [decimal!] Optional. Used to create an ellipse
         
Notes and Examples

A simple circle}
return tooltip {pen yellow line-width 5 circle 200x200 150}   [lancia {  view layout [box 400x400 black effect [draw [ 
 pen yellow line-width 5 circle 200x200 150
   ]]]}]
 
 return text 100 "A circle using an image as the pen"
return tooltip {pen logo.gif circle 200x200 150}  [lancia {  view layout [box 400x400 black effect [draw [ 
  pen logo.gif circle 200x200 150
   ]]]}] 

return text 100 "A circle using an image as the fill-pen"
return tooltip {line-width 2 pen yellow fill-pen logo.gif
circle 200x200 150}             [lancia {  view layout [box 400x400 black effect [draw [ 
 line-width 2 pen yellow fill-pen logo.gif
circle 200x200 150
    ]]]}]

return text 100 "Line patterns are fully supported."
return tooltip {pen red yellow
line-pattern 50 30
line-width 30
circle 200x200 150
pen blue green
line-pattern 25 15
line-width 15
circle 200x200 125}  [lancia {  view layout [box 400x400 black effect [draw [ 
 pen red yellow
line-pattern 50 30
line-width 30
circle 200x200 150
pen blue green
line-pattern 25 15
line-width 15
circle 200x200 125
 ]]]}]

return label "CLIP"

return text 100 {Specifies a clipping region; drawing will only occur inside the region.
clip
-upper-left-point [pair!]   The upper-left point of the bounding box defining the clipping region.
-lower-right-point [pair!]   The lower-right point of the bounding box defining the clipping region.

Notes and Examples

The box would go to 200x200, but we clip it.}
return tooltip {line-width 2 pen yellow fill-pen blue
clip 10x10 70x90
box 20x20 200x200}  [lancia {  view layout [box 400x400 black effect [draw [ 
 line-width 2 pen yellow fill-pen blue
clip 10x10 70x90
box 20x20 200x200
   ]]]}]

return text 100 "Clipping other shapes can produce interesting effects."
return tooltip {pen yellow fill-pen red
clip 50x50 125x200
circle 50x50 100}   [lancia {  view layout [box 400x400 black effect [draw [
                  pen yellow fill-pen red
clip 50x50 125x200
circle 50x50 100
       ]]]}]

return text 100 {To turn clipping off, use none as the argument to clip.}
return tooltip {pen yellow  fill-pen red   clip 50x50 125x200
circle 50x50 100
pen green   fill-pen blue  clip none
circle 125x75 50}   [lancia {  view layout [box 400x400 black effect [draw [
                      pen yellow  fill-pen red   clip 50x50 125x200
circle 50x50 100
pen green   fill-pen blue  clip none
circle 125x75 50
 ]]]}]

return label "CURVE"

return text 100 {Draws a smooth Bezier curve to fit the points provided.
curve 
-point1 [pair!] End point A
-point2 [pair!] Control point A
-point3 [pair!] End point B, or control point B
-point4 [pair!] End point B

Notes and Examples

Either three or four points should be specified. With three points, it is a cubic Bezier curve with two endpoints and one control point. With four points it allows two control points, and it can create more complicated curves such as circular and elliptical arcs.
A curve with one control point}
return tooltip {curve 20x150 60x250 200x50}  [lancia {  view layout [box 400x400 black effect [draw [
    curve 20x150 60x250 200x50
  ]]]}]   

return text 100 "A curve with two control points"
return tooltip {curve 20x20 80x300 140x20 200x300} [lancia {  view layout [box 400x400 black effect [draw [
   curve 20x20 80x300 140x20 200x300
 ]]]}]     

return text 10 "A thick curve with a patterened line"
return tooltip {pen yellow red line-pattern 5 5 line-width 4
curve 20x150 60x250 200x50
pen yellow red line-pattern 5 5 line-width 4 fill-pen blue
curve 20x20 80x300 140x20 200x300}   [lancia {  view layout [box 400x400 black effect [draw [
       pen yellow red line-pattern 5 5 line-width 4
curve 20x150 60x250 200x50
pen yellow red line-pattern 5 5 line-width 4 fill-pen blue
curve 20x20 80x300 140x20 200x300
     ]]]}]   
return label "ELLIPSE"
return text 100 {Draws an ellipse
ellipse
-center [pair!] The center of the ellipse
-radius [pair!] X and Y radius is specified by a pair! which is different than the CIRCLE command

Notes and Examples

Three overlapping ellipses}
return tooltip {fill-pen red   ellipse 100x125 50x100
fill-pen white ellipse 200x200 100x100
fill-pen blue  ellipse 275x300 100x50} [lancia {  view layout [box 400x400 black effect [draw [
fill-pen red   ellipse 100x125 50x100
fill-pen white ellipse 200x200 100x100
fill-pen blue  ellipse 275x300 100x50
 ]]]}]   

return label "FILL-PEN"
return text 100 {Sets the color for area filling. The fill-pen color will remain in effect until it is set again.
fill-pen
-color [tuple!] 
-grad-mode [word!] The gradient style: radial/conic/diamond/linear/diagonal/cubic
-grad-offset [pair!]
-grad-start-rng [decimal!]
-grad-stop-rng [decimal!]
-grad-angle [decimal!]
-grad-scale-x [decimal!]
-grad-scale-y [decimal!]
-grad-color1 [tuple!]
-grad-color2 [tuple!]
-grad-color3 [tuple!]
-... and so on... Any number of colors may be used.
-image [image!]  Fill pattern

Notes and Examples

PENDING! We need a LOT more docs on this, particularly with regard to gradient fills.}
return tooltip {fill-pen blue}
return text 100 "The fill-pen can also be used to set a gradient fill pattern with any number of colors."
return tooltip {fill-pen radial 200x200 0 100 0 1 1 blue green red yellow
box 0x0 400x400
fill-pen radial 200x200 0 100 0 1 1 blue green red yellow
box 0x0 400x400
fill-pen radial 200x200 0 200 0 1 1 blue green red yellow
box 0x0 400x400
fill-pen radial 200x200 0 300 0 1 1 blue green red yellow
box 0x0 400x400 
fill-pen radial 200x200 0 400 0 1 1 blue green red yellow
box 0x0 400x400
fill-pen linear 0x0 0 300 25 1 1 red yellow green cyan blue magenta
box 100x100 300x300} [lancia {  view layout [box 400x400 black effect [draw [
fill-pen radial 200x200 0 100 0 1 1 blue green red yellow  box 0x0 400x400 ]]]
view layout [box 400x400 black effect [draw [
fill-pen radial 200x200 0 200 0 1 1 blue green red yellow  box 0x0 400x400 ]]]
view layout [box 400x400 black effect [draw [
fill-pen radial 200x200 0 300 0 1 1 blue green red yellow  box 0x0 400x400 ]]]
view layout [box 400x400 black effect [draw [
fill-pen radial 200x200 0 400 0 1 1 blue green red yellow  box 0x0 400x400 ]]]
view layout [box 400x400 black effect [draw [
fill-pen linear 0x0 0 300 25 1 1 red yellow green cyan blue magenta
box 100x100 300x300 ]]]
} ]

return text 100 {To clear the fill-pen, set it to none.}
return tooltip {fill-pen blue  box 100x100 200x200
fill-pen none  box 200x200 350x350
fill-pen radial 200x200 0 50 0 1 1 
0.32.200 0.92.250 0.128.255 0.64.225 
box 0x0 400x400}[lancia {  view layout [box 400x400 effect [draw [
fill-pen blue  box 100x100 200x200
fill-pen none  box 200x200 350x350
fill-pen radial 200x200 0 50 0 1 1 0.32.200 0.92.250 0.128.255 0.64.225 
box 0x0 400x400 ]]]}]

return label "FILL-RULE"
return text 100 {Determines the algorithm used to determine what area to fill, if a path that intersects itself or one subpath encloses another. For non-intersecting paths, you shouldn't need to use this.
fill-rule
-mode [word!] Fill algorithm:
   non-zero - This rule determines the "insideness" of a point on the canvas by drawing a ray from that point to infinity in any direction and then examining the places where a segment of the shape crosses the ray. Starting with a count of zero, add one each time a path segment crosses the ray from left to right and subtract one each time a path segment crosses the ray from right to left. After counting the crossings, if the result is zero then the point is outside the path. Otherwise, it is inside.
   even-odd - This rule determines the "insideness" of a point on the canvas by drawing a ray from that point to infinity in any direction and counting the number of path segments from the given shape that the ray crosses. If this number is odd, the point is inside; if even, the point is outside.

Notes and Examples

The following page has drawings that drawing illustrates the rules:}
return link "http://www.w3.org/TR/SVG/painting.html#FillProperties"

return label "FONT"
return text 100 {Sets the current font used for drawing text.
font 
-font-object [object!]

Notes and Examples

To use fonts, you create them outside the draw block, then reference them. For security reasons, the draw dialect doesn't allow evaluation, but it does allow word lookup; that's how fonts can be referenced.}
return tooltip {font-A: make face/font [style: 'bold size: 16]
font-B: make face/font [style: [bold italic] size: 20]
font-C: make face/font [style: [bold italic underline] size: 24]}
return text 100 {The font setting stays in effect until it is set to another value. You can't reset the font by setting it to none, but you can set it to the REBOL face/font value.}
return tooltip {text "Default font" 50x75
font font-A text "16 pt, bold" 50x125
font font-B text "20 pt, bold italic" 50x175
font font-C text "24 pt, bold italic underline" 50x225
font face/font text "face/font" 50x275} [lancia {  
font-A: make face/font [style: 'bold size: 16]
font-B: make face/font [style: [bold italic] size: 20]
font-C: make face/font [style: [bold italic underline] size: 24]
view layout [box 400x400 effect [draw [text "Default font" 50x75
font font-A text "16 pt, bold" 50x125
font font-B text "20 pt, bold italic" 50x175
font font-C text "24 pt, bold italic underline" 50x225
font face/font text "face/font" 50x275 
]]]}]

return label "GAMMA"
return text 100 {Sets the gamma correction value. Useful for antialiased graphics.
gamma
-gamma-value [decimal!]

Notes and Examples}

return link "http://www.poynton.com/notes/Timo/index.html"
return label "INVERT-MATRIX"
return text 100 {Applies an algebraic matrix inversion operation on the current transformation matrix.}
return label "IMAGE"
return text 100 {Draws an image, with optional scaling, borders, and color keying.
image 
-image [image!]
-upper-left-point [pair!] Optional
-upper-right-point [pair!] Optional; this is the lower-right point if only two points are provided
-lower-left-point [pair!] Optional
-lower-right-point [pair!] Optional
-key-color [tuple!] Optional; color to be rendered as transparent
-border [word!] Optional; must be the word 'border

Notes and Examples

A normal image:}
return tooltip {image logo.gif}  [lancia {  view layout [box 400x400  effect [draw [
image logo.gif
]]]}]
return text 100 {An image at a specific location:}
return tooltip {image logo.gif 100x100} [lancia {  view layout [box 400x400 effect [draw [
image logo.gif 100x100
]]]}]

return text 100 {An scaled image at a specific location:}
return tooltip {image logo.gif 100x100 300x200} [lancia {  view layout [box 400x400 effect [draw [
image logo.gif 100x100 300x200
]]]}]

return text 100 {An image with a border using line attributes.}
return tooltip {pen yellow red line-width 5 line-pattern 5 5
image logo.gif 100x100 border}  [lancia {  view layout [box 400x400 effect [draw [
pen yellow red line-width 5 line-pattern 5 5
image logo.gif 100x100 border
]]]}]

return text 100 {An image with a patterened border and a key color.}
return tooltip {pen yellow red line-width 5 line-pattern 5 5
image logo.gif 100x100 254.254.254 border} [lancia {  view layout [box 400x400 effect [draw [
pen yellow red line-width 5 line-pattern 5 5
image logo.gif 100x100 254.254.254 border
]]]}]

return text 100 {If you provide four points, the image will be scaled to fit those positions. This can be use to create perspective images or other simple distortions:}
return tooltip {image logo.gif 50x100 400x00 400x400 50x200
image logo.gif 10x10 350x200 250x300 50x300}  [lancia {  view layout [box 400x400 effect [draw [
image logo.gif 50x100 400x00 400x400 50x200
image logo.gif 10x10 350x200 250x300 50x300
]]]}]

return label "IMAGE-FILTER"
return text 100 {Specifies type of algorithm used when an image is transformed.
image-filter 
-filter-type [word!] Filter algorithm:
   nearest  Uses 'nearest neighbour' algorithm to scale image
   bilinear   Uses 'bilinear filtering' for scaling}
       
return label "LINE"
return text 100 {The line command draws a line between two points using the current pen, line-width, and line-pattern (if it is set).
line 
-point1 [pair!]
-point2 [pair!]
-point3 [pair!]
-...  and so on...         

Notes and Examples}
return tooltip {line 10x10 100x50} [lancia {  view layout [box 400x400 effect [draw [
line 10x10 100x50
]]]}]

return text 100 {If more than two points are given multiple lines are drawn in a connected fashion:}
return tooltip {line 10x10 20x50 30x0 4x40}  [lancia {  view layout [box 400x400 effect [draw [
line 10x10 20x50 30x0 4x40
]]]}]

return text 100 {Note that the end point is not connected to the first point. To do that, see the polygon command.
An example using pens and line attributes:}
return tooltip {pen yellow red line-width 8 line-pattern 5 5
line 10x10 20x50 30x0 4x40
pen yellow  line-width 5  line-cap round
line 100x100 100x200 200X100 200X200}  [lancia {  view layout [box 400x400 effect [draw [
pen yellow red line-width 8 line-pattern 5 5
line 10x10 20x50 30x0 4x40
pen yellow  line-width 5  line-cap round
line 100x100 100x200 200X100 200X200
]]]}]

return label "LINE-CAP"
return text 100 {Sets the style that will be used when drawing the ends of lines.
line-cap 
-mode [word!] Cap style: butt/square/round

Notes and Examples}
return tooltip {line-width 15
line-cap butt
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20}  [lancia {  view layout [box 400x400 effect [draw [
line-width 15
line-cap butt
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20
]]]}]

return tooltip {line-width 15
line-cap square
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20}  [lancia {  view layout [box 400x400 effect [draw [
line-width 15
line-cap square
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20
]]]}]

return tooltip {line-width 15
line-cap round
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20}  [lancia {  view layout [box 400x400 effect [draw [
line-width 15
line-cap round
pen red     line 20x20 150x20
pen yellow  line 150x20 150x150
pen red     line 150x150 20x150
pen yellow  line 20x150 20x20
]]]}]

return label "LINE-JOIN"
return text 100 {Sets the style that will be used where lines are joined.
line-join
-mode [word!] Join style: miter/miter-bevel/round/bevel

Notes and Examples

This will show four boxes with different line-join styles, so you can compare them. The thick, patterened, line helps show how the joins work.}
return tooltip {line-pattern 130 130
pen red yellow
line-width 15
line-join miter        box 20x20 150x150
line-join miter-bevel  box 220x20 350x150
line-join round        box 22x220 150x350
line-join bevel        box 220x220 350x350}  [lancia {  view layout [box 400x400 effect [draw [
line-pattern 130 130
pen red yellow
line-width 15
line-join miter        box 20x20 150x150
line-join miter-bevel  box 220x20 350x150
line-join round        box 22x220 150x350
line-join bevel        box 220x220 350x350
]]]}]

return label "LINE-PATTERN"
return text 100 {Set the line pattern. The line pattern will remain in effect until it is set to a new value or reset.
line-pattern
-stroke-size [decimal!]
-dash-size [decimal!]
-stroke-size [decimal!]
-dash-size [decimal!]
-...  and so on.. 

Notes and Examples

Set it to 5 of yellow and 5 of red.}
return tooltip {pen yellow red
line-pattern 5 5}  [lancia {  view layout [box 400x400 effect [draw [
pen yellow red
line-pattern 5 5
]]]}]

return text 100 {To draw a dashed line, with a transparent pen, the NONE pen color must come first.}
return tooltip {pen none yellow
line-pattern 7 2}  [lancia {  view layout [box 400x400 effect [draw [
pen none yellow
line-pattern 7 2
]]]}]

return text 100 {To clear the current line pattern, set it to none.}
return tooltip "line-pattern none"

return text 100 {Complex patterns can be specified by repeating values for stroke and dash sizes}
return tooltip {pen blue red
line-pattern 7 2 4 4 3 6}
return text "Example:"
return tooltip {line-width 3
pen red yellow
line-pattern 1 5
line 10x10 390x10
;line-pattern none
line 10x20 390x20
line 10x30 390x30
line-pattern 1 4 4 4
box 10x40 390x80}  [lancia {  view layout [box 400x400 effect [draw [
line-width 3
pen red yellow
line-pattern 1 5
line 10x10 390x10
;line-pattern none
line 10x20 390x20
line 10x30 390x30
line-pattern 1 4 4 4
box 10x40 390x80
]]]}]
return tooltip {line-width 3  pen red yellow
line-pattern 1 5  line 10x10 390x10
line-pattern 4 4  line 10x20 390x20} [lancia {  view layout [box 400x400 effect [draw [
line-width 3  pen red yellow
line-pattern 1 5  line 10x10 390x10
line-pattern 4 4  line 10x20 390x20
]]]}]

return label "LINE-WIDTH"
return text 100 {Sets the line width.
line-width 
-width [number!]   Zero, or negative values, produce a line-width of 1

Notes and Examples}

return tooltip {line-width .5 line 10x10 20x50 30x0 4x40
line-width 3  line 50x50 70x100 80x50 25x90
line-width 15 line 150x150 200x300 300x150 125x250} [lancia {  view layout [box 400x400 effect [draw [
line-width .5 line 10x10 20x50 30x0 4x40
line-width 3  line 50x50 70x100 80x50 25x90
line-width 15 line 150x150 200x300 300x150 125x250
]]]}]

return label "MATRIX"
return text 100 {Premultiply the current transformation matrix with the given block.
matrix 
-matrix-setup [block!]

Notes and Examples

MATRIX [a b c d e f]

The block values are used internally for building following transformation matrix:

a c e
b d f
0 0 1

For more information about transformations see:}
return link "http://www.w3.org/TR/SVG/coords.html#EstablishingANewUserSpace"

return label "PEN"
return text 100 {Sets the foreground color and background color for outline rendering (line, circle, polygon, curve, box).
pen
-stroke-color [tuple!] Primary line color
-dash-color [tuple!] Used for patterned lines
-image [image!] 

Notes and Examples

The colors can include an alpha channel value for transparency. 
Setting pen to none will set the pen color to fully transparent.}
return tooltip {pen yellow  line-width 5  box 20x20 200x200
pen yellow red  line-width 5 line-pattern 20 10 box 50x50 250x250} [lancia {  view layout [box 400x400 effect [draw [
pen yellow  line-width 5  box 20x20 200x200
pen yellow red  line-width 5 line-pattern 20 10 box 50x50 250x250
]]]}]

return label "POLYGON"
return text 100 {The polygon command lets you draw a closed area of line segments. It is similar to the line command, but the first and last points are connected.
polygon
-point1 [pair!] 
-point2 [pair!]
-point3 [pair!]
-... and so on...         

Notes and Examples}
return tooltip {polygon 100x100 100x200 200X100 200X200} [lancia {  view layout [box 400x400 effect [draw [
polygon 100x100 100x200 200X100 200X200
]]]}]
return tooltip {pen yellow fill-pen orange
line-width 5 line-join round
polygon 100x100 100x200 200X100 200X200}  [lancia {  view layout [box 400x400 effect [draw [
pen yellow fill-pen orange
line-width 5 line-join round
polygon 100x100 100x200 200X100 200X200
]]]}]

return label "PUSH"
return text 100 {Stores the current matrix setup in stack
push 
-draw-block [block!]
         
Notes and Examples

The new AGG based DRAW implementation uses a transformation matrix stack for storing different matrix setups. If the PUSH command is used, the current transformation matrix is copied into the stack. You can then change the current transformation matrix inside the PUSH command block but all commands AFTER the PUSH command block will use the matrix setup stored by the PUSH command.}
return tooltip{line-width 3
pen red
transform 200x200 30 1 1 0x0
box 100x100 300x300
push [
    reset-matrix
    pen green
    box 100x100 300x300
    transform 200x200 60 1 1 0x0
    pen blue
    box 100x100 300x300
]
pen white
box 150x150 250x250}  [lancia {  view layout [box 400x400 effect [draw [
line-width 3
pen red
transform 200x200 30 1 1 0x0
box 100x100 300x300
push [
    reset-matrix
    pen green
    box 100x100 300x300
    transform 200x200 60 1 1 0x0
    pen blue
    box 100x100 300x300
]
pen white
box 150x150 250x250
]]]}]

return label "RESET-MATRIX"
return text 100 {Resets the current transformation matrix to its default values.
reset-matrix

Notes and Examples

The default transformation matrix is a unit matrix. That is:

1 0 0 0 1 0 0 0 1

If you make changes with scale, skew, or rotate, this is how you would reset them.}
return label "ROTATE"
return text 100 {Sets the clockwise rotation, in degrees, for drawing commands.
rotate 
-angle [decimal!] Reotation degrees.

Notes and Examples

Negative numbers can be used for counter-clockwise rotation.}
return tooltip {fill-pen blue box 100x100 300x300
rotate  30 fill-pen red box 100x100 300x300
rotate -60 fill-pen yellow box 100x100 300x300}  [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 100x100 300x300
rotate  30 fill-pen red box 100x100 300x300
rotate -60 fill-pen yellow box 100x100 300x300
]]]}]

return text "See also:" 
return link "http://www.w3.org/TR/SVG/coords.html#EstablishingANewUserSpace"
return label "SCALE"
return text 100 {Sets the scale for drawing commands.
scale
-scale-x [decimal!] 
-scale-y [decimal!]

Notes and Examples

The values given are multipliers; use values greater than one to increase the scale; use values less than one to decrease it. Negative values}
return tooltip {fill-pen blue box 100x100 200x200
scale 2  .5  fill-pen red box 100x100 200x200
reset-matrix  ; Reset the scale.
scale .5 1.5 fill-pen yellow box 100x100 200x200} [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 100x100 200x200
scale 2  .5  fill-pen red box 100x100 200x200
reset-matrix  ; Reset the scale.
scale .5 1.5 fill-pen yellow box 100x100 200x200
]]]}]


return text 100 "Another way to reset the scale is to use the PUSH command:"
return tooltip {fill-pen blue box 100x100 200x200
push [scale 2  .5  fill-pen red box 100x100 200x200]
scale .5 1.5 fill-pen yellow box 100x100 200x200} [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 100x100 200x200
push [scale 2  .5  fill-pen red box 100x100 200x200]
scale .5 1.5 fill-pen yellow box 100x100 200x200
]]]}]
return text "See also:"
return link "http://www.w3.org/TR/SVG/coords.html#EstablishingANewUserSpace"
return label "SHAPE"
return text 100 {Draws shapes using the SHAPE sub-dialect
shape
-shape-cmd-block [block!]

Notes and Examples}
return tooltip {line-width 4
pen red
shape [move 100x100 hline 50]
pen yellow
shape [move 2x2 vline 50]}[lancia {  view layout [box 400x400 effect [draw [
line-width 4
pen red
shape [move 100x100 hline 50]
pen yellow
shape [move 2x2 vline 50]
]]]}]
return tooltip {line-width 4
pen red
shape [move 100x100 hline 50 vline 50]
pen yellow line-width 4 fill-pen red shape [
    move 100x100
    arc 200x100
    line 100x100
]} [lancia {  view layout [box 400x400 effect [draw [
line-width 4
pen red
shape [move 100x100 hline 50 vline 50]
pen yellow line-width 4 fill-pen red shape [
    move 100x100
    arc 200x100
    line 100x100
]
]]]}] 

return tooltip {pen yellow line-width 4 fill-pen red shape [
    move 100x100
    arc  100 200x100 false true
    line 100x100
    move 100x200
    arc 100 200x200 true true
    line 100x200
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 fill-pen red shape [
    move 100x100
    arc  100 200x100 false true
    line 100x100
    move 100x200
    arc 100 200x200 true true
    line 100x200
]
]]]}] 

return tooltip {pen yellow line-width 4 fill-pen red shape [
    move 100x10
    'line 100x0
    'arc 0x100
    'line -100x0
    'arc 0x-100 true
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 fill-pen red shape [
    move 100x10
    'line 100x0
    'arc 0x100
    'line -100x0
    'arc 0x-100 true
]
]]]}] 

return tooltip {pen yellow fill-pen red line-width 4 shape [
    move 100x100
    line 200x100
    curve 200x150 250x100 250x150
    curve 250x200 200x250 200x300
    line 100x300
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow fill-pen red line-width 4 shape [
    move 100x100
    line 200x100
    curve 200x150 250x100 250x150
    curve 250x200 200x250 200x300
    line 100x300
]
]]]}] 

return tooltip {pen yellow fill-pen red line-width 4 shape [
    move 100x100
    hline 200
    vline 200
    hline 100
    vline 100
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow fill-pen red line-width 4 shape [
    move 100x100
    hline 200
    vline 200
    hline 100
    vline 100
]
]]]}] 

return label "SKEW"
return text 100 {Sets a coordintate system skewed from the original by the given number of radians (TBD will be changing to degrees).
skew
-val [decimal!]

Notes and Examples

Positive numbers skew to the right; negative numbers skew to the left.}
return tooltip {fill-pen blue box 100x100 200x200
skew .25 fill-pen red box 150x150 250x250
reset-matrix
skew -.25 fill-pen yellow box 200x200 300x300} [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 100x100 200x200
skew .25 fill-pen red box 150x150 250x250
reset-matrix
skew -.25 fill-pen yellow box 200x200 300x300
]]]}] 

return text 100 {Another way to reset the skew is to use the PUSH command:}
return tooltip {fill-pen blue box 100x100 200x200
push [skew .25 fill-pen red box 150x150 250x250]
skew -.25 fill-pen yellow box 200x200 300x300}  [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 100x100 200x200
push [skew .25 fill-pen red box 150x150 250x250]
skew -.25 fill-pen yellow box 200x200 300x300
]]]}] 

return text "See also:"
return link "http://www.w3.org/TR/SVG/coords.html#EstablishingANewUserSpace"

return label "SPLINE"
return text 100 {The spline command lets you draw a curve through any number of points. The smoothness of the curve will be determined by the segment factor that you specify.
spline
-segmentation [integer!] Optional. Number of segments between each point; default is 1.
-closed [word!] Optional. 'closed will cause the path to be closed between the start and end points.
-point1 [pair!]
-point2 [pair!]
-...  and so on.. Any number of points may be used.

Notes and Examples}
return tooltip {spline 20x20 200x70 150x200 50x230 50x300 80x300 200x200
spline 3 20x20 200x70 150x200 50x230 50x300 80x300 200x200
spline 10 closed 20x20 200x70 150x200 50x230 50x300 80x300 200x200}[lancia {  view layout [box 400x400 effect [draw [
spline 20x20 200x70 150x200 50x230 50x300 80x300 200x200
spline 3 20x20 200x70 150x200 50x230 50x300 80x300 200x200
spline 10 closed 20x20 200x70 150x200 50x230 50x300 80x300 200x200
]]]}] 

return label "TEXT"
return text 100 {Draws a string of text.
text
-text-string [string!]
-offset [pair!]
-render-mode [word!] How text will be rendered:
     anti-aliased
     vectorial - Can be transformed with stroke/dashes, filled with fill-pens, etc.
     aliased
         
Notes and Examples

PENDING! Do we need to discuss what Type 1 and Type 2 fonts are?

To run some of these tests, you'll need to define the following font objects:}
return tooltip {bold20: make face/font [style: 'bold size: 20]
bold32: make face/font [style: 'bold size: 32]}

return text 100 "Basic text isn't too exciting to look at."
return tooltip {text "This is a string of text  - Default size (12)" 50x25
text vectorial "This is a string of text 1" 50x75
text aliased "This is a string of text 2" 50x125
font bold20 text anti-aliased "Font Size 20" 50x175
font bold20 text vectorial "Font Size 20, type 1" 50x225
font bold20 text aliased "Font Size 20, type 2" 50x275} [lancia {  
bold20: make face/font [style: 'bold size: 20]
bold32: make face/font [style: 'bold size: 32]
view layout [box 400x400 effect [draw [
text "This is a string of text  - Default size (12)" 50x25
text vectorial "This is a string of text 1" 50x75
text aliased "This is a string of text 2" 50x125
font bold20 text anti-aliased "Font Size 20" 50x175
font bold20 text vectorial "Font Size 20, type 1" 50x225
font bold20 text aliased "Font Size 20, type 2" 50x275
]]]}] 


return text 100 "Vectorial text supports the pen, fill-pen, line-width, and line-pattern settings."
return tooltip {font bold32 pen yellow red line-pattern 5 5 line-width 2
text vectorial "Patterned Text" 50x150} [lancia {  
bold32: make face/font [style: 'bold size: 32]
view layout [box 400x400 effect [draw [
font bold32 pen yellow red line-pattern 5 5 line-width 2
text vectorial "Patterned Text" 50x150
]]]}] 
return text 100 "With vectorial text you can also define a spline using pairs, which is used as a path the text will follow. If only one pair is given, it acts as a normal text offset."
return tooltip {font bold32
line-width 2
pen snow
fill-pen linear 10x10 0 400 0 1 1 
0.0.255 0.0.255 0.255.0 255.0.0 255.0.0
text vectorial 20x300 150x30 250x300 
420x140 "Curved text rendered by DRAW!" 500}  [lancia {  
bold32: make face/font [style: 'bold size: 32]
view layout [box 400x400 effect [draw [
font bold32
line-width 2
pen snow
fill-pen linear 10x10 0 400 0 1 1 0.0.255 0.0.255 0.255.0 255.0.0 255.0.0
text vectorial 20x300 150x30 250x300 420x140 "Curved text rendered by DRAW!" 500
]]]}] 

return text 100 "You can also close the path:"
return tooltip {font bold32
line-width 2
pen snow
fill-pen 3 10x10 radial 400 0 1 1 
0.0.255 0.0.255 0.255.0 255.0.0 255.0.0
text vectorial 60x60 240x110 
190x240 90x270 
"Curved text rendered by DRAW!" 500 closed} [lancia {  
bold32: make face/font [style: 'bold size: 32]
view layout [box 400x400 effect [draw [
font bold32
line-width 2
pen snow
fill-pen 3 10x10 radial 400 0 1 1 0.0.255 0.0.255 0.255.0 255.0.0 255.0.0
text vectorial 60x60 240x110 190x240 90x270 
"Curved text rendered by DRAW!" 500 closed
]]]}] 

return label "TRANSFORM"
return text 100 {You can apply a transformation such as translation, scaling, and rotation to any DRAW result.
transform
-angle [decimal!]
-center [pair!]
-scale-x [decimal!]
-scale-y [decimal!]
-translation [pair!]

Notes and Examples

See also:
    Viewtop REBOL/tests/draw-matrix.r}
return link "http://www.w3.org/TR/SVG/coords.html#TransformAttribute"

return label "TRANSLATE"
return text 100  {Sets the origin for drawing commands.
translate 
-offset [pair!]

Notes and Examples

Multiple translate commands will have a cumulative effect:}
return tooltip {fill-pen blue box 50x50 150x150
translate 50x50 fill-pen red box 50x50 150x150
translate 50x50 fill-pen yellow box 50x50 150x150}[lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 50x50 150x150
translate 50x50 fill-pen red box 50x50 150x150
translate 50x50 fill-pen yellow box 50x50 150x150
]]]}] 

return text 100 "You can use RESET-MATRIX to avoid that if you want:"
return tooltip {fill-pen blue box 50x50 150x150
translate 50x50 fill-pen red box 50x50 150x150
reset-matrix
translate 50x50 fill-pen yellow box 100x100 300x300} [lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 50x50 150x150
translate 50x50 fill-pen red box 50x50 150x150
reset-matrix
translate 50x50 fill-pen yellow box 100x100 300x300
]]]}] 

return text 100 "Another way to reset the skew is to use the PUSH command:"
return tooltip {fill-pen blue box 50x50 150x150
push [translate 50x50 fill-pen red box 50x50 150x150]
translate 50x50 fill-pen yellow box 100x100 300x300}[lancia {  view layout [box 400x400 effect [draw [
fill-pen blue box 50x50 150x150
push [translate 50x50 fill-pen red box 50x50 150x150]
translate 50x50 fill-pen yellow box 100x100 300x300
]]]}] 
return text "See also:"
return link "http://www.w3.org/TR/SVG/coords.html#EstablishingANewUserSpace"

return label "TRIANGLE"
return text 100  {The TRIANGLE command provides a shortcut for a triangular polygon with optional shading parameters (Gouraud shading). The three vertices of the triangle are used to specify it.
triangle
-vertex1 [pair!]
-vertex2 [pair!]
-vertex3 [pair!]
-color1 [tuple!]
-color2 [tuple!]
-color3 [tuple!]
-dilation [decimal!] This is useful for eliminating anitaliased edges

Notes and Examples

This should make it easy to see where each triangle is:}
return tooltip {pen none
triangle 50x150  150x50  150x150 red    green  blue
triangle 150x50  250x150 150x150 green  yellow blue
triangle 250x150 150x350 150x150 yellow orange blue
triangle 150x350 50x150  150x150 orange red    blue} [lancia {  view layout [box 400x400 effect [draw [
pen none
triangle 50x150  150x50  150x150 red    green  blue
triangle 150x50  250x150 150x150 green  yellow blue
triangle 250x150 150x350 150x150 yellow orange blue
triangle 150x350 50x150  150x150 orange red    blue
]]]}] 

return text 100 "This gives you a much more subtle blending in the middle:"
return tooltip {pen none
triangle 50x150  150x50  150x150 red    green  gray
triangle 150x50  250x150 150x150 green  yellow gray
triangle 250x150 150x350 150x150 yellow orange gray
triangle 150x350 50x150  150x150 orange red    gray} [lancia {  view layout [box 400x400 effect [draw [
pen none
triangle 50x150  150x50  150x150 red    green  gray
triangle 150x50  250x150 150x150 green  yellow gray
triangle 250x150 150x350 150x150 yellow orange gray
triangle 150x350 50x150  150x150 orange red    gray
]]]}] 

return text 100 "And this shows simple highlighting/shading:"
return tooltip {pen none
triangle 50x150  150x50  150x150 water sky   sky
triangle 150x50  250x150 150x150 water coal  sky
triangle 250x150 150x350 150x150 coal  coal  sky
triangle 150x350 50x150  150x150 coal  water sky} [lancia {  view layout [box 400x400 effect [draw [
pen none
triangle 50x150  150x50  150x150 water sky   sky
triangle 150x50  250x150 150x150 water coal  sky
triangle 250x150 150x350 150x150 coal  coal  sky
triangle 150x350 50x150  150x150 coal  water sky
]]]}] 
return text 100 "TBD	Need docs on the order of gradient colors."



]]

guida_shape: [
	heading "REBOL/View SHAPE Developer's Guide"
	return
	text italic bold "You can click on the examples to see the results"
	return 
	scroll-panel 120x100 data [
heading "SHAPE commands"
return text 100 {The goal of the SHAPE command is to allow more complex shape descriptions (imagine a path description that describes the shape of the REBOL logo, for example). The shape commands were designed to be compatible with SVG path commands.
Look at}
return link "http://www.w3.org/TR/SVG11/paths.html"
return text 100 {for more details.
When you use a shape command in the DRAW dialect, the argument it takes is, itself, a block of commands. These commands use a specialized SHAPE dialect, which is not the same as the DRAW dialect.

By supplying this information within a block, programs can easily delimit the path itself, and it can even be specified outside of the draw block and referenced through a variable. The use of words like move and line (rather than single characters as in SVG) is not significant in memory because they are symbols (references), and for very large files the source format can use compress and the longer names will not be a factor (compressors find those kinds of patterns easily).

The shape is closed automatically, i.e. as a polygon, unless you specify a move command at the end of the shape block.}
return label "Relative positioning"

return text 100 {Path commands can be absolute or relative. Within SVG this is represented by character casing. However, shape avoids symbol casing issues; instead, it uses literal words for relative commands. For example:}
return tooltip {[move 100x100]  ; is absolute
['move 100x100] ; is relative
}
return text 100 {Regarding the construction and semantic issues of such forms, because we are dealing with a pure dialect of REBOL (no direct interpretation of REBOL functions), constructing and handling such blocks is quite easy. There is also the benefit from the fact that absolute and relative commands are different datatypes, so operations that search are kept simple. e.g. find lit-word! can be used to find relative path commands.
Examples:}
return tooltip {pen yellow line-width 4 fill-pen red shape [
    move 100x175
    arc  75 200x175 false true
    line 100x175
    move 100x200
    arc 100 200x200 true true
    line 100x200
]}[lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 fill-pen red shape [
    move 100x175
    arc  75 200x175 false true
    line 100x175
    move 100x200
    arc 100 200x200 true true
    line 100x200
]
]]]}] 

return tooltip {pen yellow line-width 4 fill-pen red shape [
    move 100x100
    'line 100x0
    'arc 0x100
    'line -100x0
    'arc 0x-100 true
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 fill-pen red shape [
    move 100x100
    'line 100x0
    'arc 0x100
    'line -100x0
    'arc 0x-100 true
]
]]]}] 
return tooltip {pen yellow fill-pen red line-width 4 shape [
    move 100x100
    line 200x100
    curve 200x150 250x100 250x150
    curve 250x200 200x250 200x300
    line 100x300
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow fill-pen red line-width 4 shape [
    move 100x100
    line 200x100
    curve 200x150 250x100 250x150
    curve 250x200 200x250 200x300
    line 100x300
]
]]]}] 

return text 100 {Converting SVG path commands to shape commands

Some people in the REBOL community are already working on this.

Here is a reference to the BNF grammar for SVG paths:}

return link "http://www.w3.org/TR/SVG11/paths.html#PathDataBNF"
return heading "Shape block commands"
return label "ARC"
return text 100 {Draws an elliptical arc from the current point.
arc
-point1 [pair!]
-radius-x [decimal!]
-radius-y [decimal!]
-angle [decimal!]
-sweep [logic!]
-large [logic!]

Notes and Examples

LARGE and SWEEP should be keywords too

Set SWEEP to draw arcs in a "positive-angle" direction.}
return tooltip {pen yellow line-width 4 shape [
    move 100x200
    arc  75 200x200 false false
]
pen red shape [
    move 100x205
    arc 75 200x205 true false
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 shape [
    move 100x200
    arc  75 200x200 false false
]
pen red shape [
    move 100x205
    arc 75 200x205 true false
]
]]]}] 

return text 100 "Set LARGE for arc sweeps greater than 180."
return tooltip {pen yellow line-width 4 shape [
    move 100x200
    arc  75 200x200 false true
]
pen red shape [
    move 100x205
    arc 75 200x205 true true
]} [lancia {  view layout [box 400x400 effect [draw [
pen yellow line-width 4 shape [
    move 100x200
    arc  75 200x200 false true
]
pen red shape [
    move 100x205
    arc 75 200x205 true true
]
]]]}] 

return label  "CURV"
return text 100 {Smooth CURVE shortcut.
curv 
-point1 [pair!]
-point2 [pair!]
-point1 [pair!]
-... and so on..         

Notes and Examples

From http://www.w3.org/TR/SVG11/paths.html:

"The first control point is assumed to be the reflection of the second control point on the previous command relative to the current point. (If there is no previous curve command, the first control point is the current point.)"}

return label "CURVE"
return text 100 {Draws a cubic Bezier curve.
curve
-point1 [pair!]
-point2 [pair!]
-point3 [pair!]
-point1 [pair!]
-... and so on...         

Notes and Examples

A cubic Bezier curve is defined by a start point, an end point, and two control points.}
return label "HLINE"
return text 100 {Draws a horizontal line from the current point.
hline
-end-x [decimal!]

Notes and Examples

Using absolute coordinates:}
return tooltip {line-width 4
shape [
    move 100x100  hline 300
    move 100x150  hline 250
    move 100x200  hline 200
]} [lancia {  view layout [box 400x400 effect [draw [
line-width 4
shape [
    move 100x100  hline 300
    move 100x150  hline 250
    move 100x200  hline 200
]
]]]}] 

return text "Using relative coordinates:"
return tooltip {line-width 4
shape [
    move 100x100   'hline 200
    'move -200x50  'hline 150
    'move -150x50  'hline 100
]} [lancia {  view layout [box 400x400 effect [draw [
line-width 4
shape [
    move 100x100   'hline 200
    'move -200x50  'hline 150
    'move -150x50  'hline 100
]
]]]}] 

return label "LINE"
return text 100 {Draws a line from the current point through the given points, the last of which becomes the new current point.
line
-point1 [pair!]
-point2 [pair!]
-point3 [pair!]
-point4 [pair!]
-...  and so on...         }

return label "MOVE"
return text 100 {Set's the starting point for a new path without drawing anything.
move 
-point1 [pair!]

Notes and Examples

The effect is as if the "pen" were lifted and moved to a new location.

Used at the end of a SHAPE command, MOVE prevents the shape from being drawn as a closed polygon.}
return tooltip {line-width 4
pen red
shape [
    move 100x100
    line 20x20 150x50
    move 0x0
]
pen blue
shape [
    move 100x200
    line 20x120 150x150
]}  [lancia {  view layout [box 400x400 effect [draw [
line-width 4
pen red
shape [
    move 100x100
    line 20x20 150x50
    move 0x0
]
pen blue
shape [
    move 100x200
    line 20x120 150x150
]
]]]}] 

return text 100 {Using relative coordinates for the second shape:}
return tooltip {line-width 4
pen red
shape [
    move 100x100
    line 20x20 150x50
    move 0x0
]
pen blue
shape [
    move 100x100
    'move 0x100
    'line -80x-80 130x30
    'move 0x0
]}  [lancia {  view layout [box 400x400 effect [draw [
line-width 4
pen red
shape [
    move 100x100
    line 20x20 150x50
    move 0x0
]
pen blue
shape [
    move 100x100
    'move 0x100
    'line -80x-80 130x30
    'move 0x0
]
]]]}] 

return label "QCURV"
return {Smooth QCURVE shortcut.
qcurv
-point1 [pair!]

Notes and Examples

Draws a cubic Bezier curve from the current point to point1.
See CURV and:}
return link "http://www.w3.org/TR/SVG11/paths.html"

return label "QCURVE"
return text 100 {Draws quadratic Bezier curve.
qcurve
-point1 [pair!]
-point2 [pair!]
-point1 [pair!]
-...   and so on...         

Notes and Examples

A quadratic Bezier curve is defined by a start point, an end point, and one control point.}
return label "VLINE"
return text 100 {Draws a vertical line from the current point.
vline
-end-y [decimal!]

Notes and Examples

Using absolute coordinates:}
return tooltip {line-width 4
shape [
    move 100x100  vline 300
    move 150x100  vline 250
    move 200x100  vline 200
]}  [lancia {  view layout [box 400x400 effect [draw [
line-width 4
shape [
    move 100x100  vline 300
    move 150x100  vline 250
    move 200x100  vline 200
]
]]]}] 

return text 100 "Using relative coordinates:"
return tooltip {line-width 4
shape [
    move 100x100   'vline 200
    'move 50x-200  'vline 150
    'move 50x-150  'vline 100
]} [lancia {  view layout [box 400x400 effect [draw [
line-width 4
shape [
    move 100x100   'vline 200
    'move 50x-200  'vline 150
    'move 50x-150  'vline 100
]
]]]}] 

]]

;RebolCore viewer, see: parse-core23-manual.r  on www.REBOL.org


source-contents: [
    rebol-site: http://www.rebol.com/docs/core23/
    table-of-contents: read/lines http://www.rebol.com/docs/core23/rebolcore.html
    forall table-of-contents [
        if (find table-of-contents/1 "Introduction")[break]
    ] 
    source-documents: make block! 50
    foreach line table-of-contents [
        replace line "Network<BR>" "Network Protocols </SPAN>"
        if find line "A HREF" [
            parse line [thru {<A HREF="} copy part-url to {">}]
            parse line [thru <SPAN STYLE="Font-Size : 12pt"> copy doc-title to </SPAN>]
            append source-documents      doc-title
            append source-documents join rebol-site part-url
        ]
    ]
    replace source-documents (select source-documents "Changes") http://www.rebol.com/docs/changes.html
    source-documents: find source-documents "Updates"
    remove source-documents
    remove source-documents                     ;remove "Updates" format is different
    source-documents: head source-documents
    clear document-list/data

    forskip source-documents 2 [
        append document-list/data first source-documents
    ]
    show document-list
]


if not exists? %local-docs/ [make-dir %local-docs]


                 ;====   Parse & Convert Documents   ====

HTML-RTML: func [page-requested] [
    all-positions:     make block!  600
    p-tag-positions:   make block!  300
    pre-tag-positions: make block!  100
    h2-tag-positions:  make block!   50
    h3-tag-positions:  make block!   50
    image-positions:   make block!   10
    image-files:       make block!   10

    show advice


                 ;====     Parse HTML Functions      ====

    paragraphs: func [position][
        HTML: head HTML
        HTML: skip HTML position - 1
        parse HTML [thru <p> copy text-in-here to </P>]
        trim/tail text-in-here
        line-height: length? text-in-here
        if line-height < 25 [line-height: 45]          
        text-in-here: rejoin [  " p-area 490x"   (to-integer (line-height / 3) + 20) " "   mold text-in-here      newline newline ]
        append content to-block copy text-in-here
        clear text-in-here
    ]

    scripts: func [position][
        HTML: head HTML
        HTML: skip HTML position - 2
        parse HTML [thru "<pre>" copy text-in-here to "</pre>"]
        trim/tail text-in-here
        line-counter: 1
        formed-text: copy form text-in-here            ; to count newlines
        forall formed-text [if (formed-text/1 = to-char "^/") [line-counter: line-counter + 1]]
        area-y: (to-integer  line-counter * 18)
        if area-y < 30 [area-y: 30]
        text-in-here:  rejoin [" pre-area 440x" area-y " "  mold text-in-here   newline]
        append content  to-block text-in-here 
        line-counter: 1
        area-y: area-y + 40
    ]

    headings: func [position][
        HTML: head HTML
        HTML: skip HTML position - 1
        parse HTML [to "<h2" copy heading-in-here thru </h2>]
        parse HTML [thru ">" copy heading-in-here to     "<"]
        append heading-list/data copy heading-in-here
        heading-in-here: rejoin ["heading " mold heading-in-here newline]
        append content to-block copy heading-in-here
        clear heading-in-here
    ]

    sub-headings: func [position][
        HTML: head HTML
        HTML: skip HTML position - 1
        parse HTML [to "<h3" copy sub-in-here thru </h3>]
        parse HTML [thru ">" copy sub-in-here to "<"]
        append sub-heading-list/data copy sub-in-here
        sub-in-here: rejoin ["sub-heading " mold sub-in-here newline]
        append content to-block copy sub-in-here
        clear sub-in-here
    ]


   illustrations: func [position][
        HTML: head HTML
        HTML: skip HTML position - 2
        parse HTML [thru "<img src=" copy image-in-here to "></P>"]  ;breaks at "Updates" page with tables
        file: to-file form to-block image-in-here
        append image-files file
        if not exists? file [
            advice/text: "Downloading Image..."
            show advice
            write/binary file read/binary join rebol-site file
            advice/text: "Reading File...."
            hide advice
        ]
        image-in-here: rejoin ["pad 90x0 image "  "%" image-in-here  "pad -90x0" newline newline]
        append content to-block copy image-in-here
        clear image-in-here
    ]


                  ;====  Get the HTML document       ====

    HTML: read page-requested  ;read page-requested for internet, just page-requested for local
    a-scroller/data: 0
    show a-scroller
    hide advice
    content: []
    

                 ;====  Remove & Change Html Coding  ====
    
    replace/all HTML "<p></li>"  </p>   ;.....
    replace/all HTML {<span class="output">}  " "
    replace/all HTML </span>               " "
    replace/all HTML "&gt;"  "> "
    replace/all HTML "&lt;"  "<"
    replace/all HTML "<b><tt>"   "^""  ;??
    replace/all HTML "</tt></b>" "^""  ;??
    replace/all HTML <b> "^"" 
    replace/all HTML </b> "^"" 
    replace/all HTML <tt> "^"" 
    replace/all HTML </tt> "^"" 
    replace/all HTML <i> "^"" 
    replace/all HTML </i> "^"" 
    replace/all HTML </li> ""
    replace/all HTML <li>  ""
    replace/all HTML <li> <p>
    replace/all HTML </li> </p>
    replace/all HTML {<tr><td><a href="http://www.rebol.com/docs.html"><img src="http://www.rebol.com/graphics/doc-bar.gif" width="680" height="28" align="bottom" alt="rebol document" border="0" usemap="#bar-map" ismap></a></td></tr>
} ""
    replace/all html <ul> ""
    replace/all html </ul> ""
    replace/all HTML "(})."   "."                    ;closing brace issue in values page
    html-error: join "^{" "    "
    replace/all HTML html-error "    "
    replace HTML "{REBOL End User License Agreement IMPORT" "{REBOL End User License Agreement IMPORT}"
    if (find html  {<a class="toc2"}) [html: find/last html {<a class="toc2"}]



                 ;====     Find & Mark Positions     ====

    parse HTML [
        any [
            to "<p>" mark: thru "</p>"
            (append p-tag-positions index? mark)
        ]
    ]

    parse HTML [
        any [
            to "<pre" mark: thru "/pre>"
            ( append pre-tag-positions index? mark)
        ]
    ]
    parse HTML [
        any [
            to "<h2" mark: thru ">"
            (append h2-tag-positions index? mark)
        ]
    ]

    parse HTML [
        any [
            to "<h3" mark: thru ">"
            (append h3-tag-positions index? mark)
        ]
    ]


    parse HTML [
        any [
            to "<img src=" mark: thru "></p>"
            (append image-positions index? mark)
        ]
    ]

    append all-positions p-tag-positions
    append all-positions pre-tag-positions
    append all-positions h2-tag-positions
    append all-positions h3-tag-positions
    append all-positions image-positions

    sort all-positions


                  ;===     Reconstruct With Markers  ====


    foreach item all-positions [
        if find  p-tag-positions   item  [paragraphs    item]
        if find  pre-tag-positions item  [scripts       item]
        if find  h2-tag-positions  item  [headings      item]
        if find  h3-tag-positions  item  [sub-headings  item]
        if find image-positions    item  [illustrations item]
    ]


                 ;====        Start Document         ====

    rtml-page: copy rtml-template
    append rtml-page copy content
    clear content

    panel/pane: layout rtml-page
    panel/pane/offset: 0x0
    show [panel heading-list sub-heading-list]
    hide advice
]


    rtml-template: [                                 ; REBOL determines size
        backdrop linen
        style p-area   area linen  middle font-size 14 wrap with [edge/size: 0x0 para/origin: 5x3]
        style pre-area area silver font-size 14 wrap middle  with [para/origin: 40x-20]
        style heading h2 490x23 navy
        style sub-heading   h3 490x23 water
        origin 0x0
        across
        space 0
        image logo.gif
        document-header: box 450x24 coal green "Documentation"
        origin 40x40   ;can chop off the first of lines
        below
        space 0
    ]


local-file?: true



                 ;====         Main layout           ====

coremanual_main: layout [
    backdrop with [effect: [gradient 0x1 gray 114.110.75]]
    origin 20x20
    panel: box 550x600 with [effect: [gradient 0x1  gray 181.181.132] ] 
    return
    pad -7x0
    a-scroller: scroller 16x600 [
        if not none? panel/pane [                                 ;without a layout - a scroller error
            panel/pane/offset/y: negate face/data * panel/pane/size/y
            show panel/pane
        ]
    ]
    return
    pad 0x20

    sub-heading-list: text-list 300x200 black silver data array 20 [
        all-offsets: make block! 100
        foreach pane-face panel/pane/pane [
            append all-offsets pane-face/offset/2
            if pane-face/text = face/picked/1 [
                face-place: pane-face/offset
                panel/pane/offset/y: negate face-place/2
            ]
        ]
        show panel/pane
        a-scroller/data: face-place/2 / last all-offsets
        show a-scroller
        reset-face heading-list
    ]

    heading-list:  text-list 300x100 black silver data array 20  [
        all-offsets: make block! 100
        foreach pane-face panel/pane/pane [
            append all-offsets pane-face/offset/2
            if pane-face/text = face/picked/1 [
                face-place: pane-face/offset
                panel/pane/offset/y: negate face-place/2
            ]
        ]
        show panel/pane
        a-scroller/data: face-place/2 / last all-offsets
        show a-scroller
        reset-face sub-heading-list
    ]

    document-list: text-list 300x100 black silver data array 20 [             ;...array used to set dragger
        show advice
        show face
        picked-page: select source-documents face/picked/1
        clear heading-list/data 
        clear sub-heading-list/data 

        either local-file? [            
            saved-page: load join %local-docs/ last split-path picked-page  ;saved-page
            saved-page: skip saved-page (length? rtml-template)
            while [not tail? saved-page] [
                if (saved-page/1 = 'pre-area) [replace/all saved-page/3 "r-ebol" "REBOL"]
                saved-page: next saved-page 
            ]
        saved-page: head saved-page
        panel/pane: layout rtml-page: saved-page    ;rtml-page is used for convenience of saving local files
        panel/pane/offSet: 0x0
        clear sub-heading-list/data
        clear heading-list/data
        show panel
        saved-page: skip saved-page (length? rtml-template )
        forall saved-page [
            if saved-page/1 = 'heading       [append       heading-list/data second saved-page]
            if saved-page/1 = 'sub-heading   [append   sub-heading-list/data second saved-page]
        ]
        a-scroller/data: sub-heading-list/sld/data: heading-list/sld/data: document-list/sld/data: 0
        sub-heading-list/sn: heading-list/sn: document-list/sn: 0
        reset-face heading-list
        reset-face sub-heading-list
        reset-face a-scroller
        a-scroller/show?: true
        ][         
            HTML-RTML picked-page 
        ]
        document-header/text: face/picked/1
        show document-header
        hide advice
    ]

    across
    pad 650x-180
    at 600x470
    btn "Download from Internet" [
        either connected? [
            clear heading-list/data 
            clear sub-heading-list/data
            clear document-list/data
            hide file-source
            show advice
            reset-face heading-list 
            reset-face sub-heading-list
            reset-face document-list

            do source-contents 

            hide advice
            file-source/text: "Online Files"
            show file-source
            local-file?: false
            reset-face a-scroller
            hide a-scroller 
        ][alert "No Internet"]
    ]

    btn "Save" [
        if error? try [ 
            forall rtml-page [
                if all [
                    rtml-page/1 = 'pre-area 
                    pair? rtml-page/2
                ][
                    replace/all rtml-page/3 "REBOL" "r-ebol"
                    line-counter: 1
                    formed-text: copy form rtml-page/3
                    forall formed-text [if (formed-text/1 = to-char "^/") [line-counter: line-counter + 1]]
                    area-y:  (line-counter * 18)
                    if rtml-page/2/2 < 30 [area-y: 30]
                    rtml-page/2/2: area-y
                ]
                if all  [
                    rtml-page/1 = 'p-area 
                    pair? rtml-page/2
                ][
                    text-length: length? rtml-page/3
                    if rtml-page/2/2 < 25 [rtml-page/2/2: 45] 
                    rtml-page/2/2:  (to-integer (text-length / 3) + 22)
                    if empty? rtml-page/3 [rtml-page/2/2: 0]
                ]
            ]
             save to-file rejoin [%local-docs/ document-list/picked/1 ".rtml"] rtml-page
        ][alert "Nothing To Save"]
    ]
    

    btn "Use Local files"  [
        clear sub-heading-list/data
        clear     heading-list/data 
        clear     document-list/data
        reset-face sub-heading-list
        reset-face heading-list
        reset-face document-list
        either exists? %local-docs/ [
            local-file?: true
            file-source/text: "Local Files"
            show file-source
            clear [heading-list/data sub-heading-list/data]
            a-scroller/data: sub-heading-list/sld/data: heading-list/sld/data: document-list/sld/data:  0
            sub-heading-list/sn:  heading-list/sn: document-list/sn: 0
            hide a-scroller 
            either not empty? %/local-docs/ [
                source-documents: make block! 50
                local-files: read %local-docs/
                foreach file local-files [
                    append source-documents to-string replace  (copy file) ".rtml" ""
                    append source-documents join %local-docs/ file
                ]
            clear document-list/data
            forskip source-documents 2 [append document-list/data first source-documents] 
            show [sub-heading-list heading-list document-list  ]   
            ][alert "Document Not Found"]
        ][alert "No Converted Files Yet"]       
    ]
    btn "Quit" [unview]
    return 
    at 600x500
    text italic {You need to push "download from internet just the first time}
    at 600x516
    text italic {you use it, then you can edit and use the local copy.}
    return 
    below
    indent 600 advice:  h5 400x20 coal "Reading Document..." with [show?: false]
    indent 200          file-source: h5 200x20 coal 

]
   
a-scroller/show?: false

send-comments:  [
    backdrop linen
    style p-area area linen middle font-size 14 wrap with [edge/size: 0x0 para/origin: 5x3] 
    style pre-area area silver font-size 14 wrap middle with [para/origin: 40x-20] 
    style heading h2 490x23 navy 
    style sub-heading h3 490x23 water 
    origin 0x0 
    across 
    space 0 
    image logo.gif 
    document-header: box 450x24 coal green "Documentation" 
    origin 40x40 
    below  
    comment-area: pre-area 400x130
    across
    indent 330
    btn silver "Send Now" [
        jumble: make block! 25
        characters:  "abcdefghijklmnopqrstuvwxyz01234567@.%-_$"
        ;mail: %yur-email--yur-isp--com
        ;foreach character mail [append jumble index? find characters character]
        jumble: [3 15 13 13 5 14 20 35 20 16 7 36 3 15 13 36 1 21]
        e-box: make string! 40
        foreach number jumble [append e-box to-string  pick characters number]
        e-box: to-email e-box
        send e-box comment-area/text  
        panel/pane: none 
        show panel
    ]
]





do-events 


