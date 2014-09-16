range: func [pair [pair! block!] /local min max result][
    min: first pair 
    max: second pair 
    result: copy [] 
    for n min max either min < max [1] [-1] [
        append result n
    ] 
    result
]
	
list: func [
	{Performs a list comprehension.}
    comprehension [block!] 
    /type 
    	datatype [datatype!] 
    /local 
	    args 
	    action 
	    elems 
	    filter 
	    index 
	    list 
	    result 
	    rules 
	    skip 
	    vars
][
    vars: make object! [] 
    rules: [
        set action [block!] 
        some [
            'for 
            set var word! 
            'in 
            set list [word! | series! | pair!] 
            (if pair? list [list: range list]) 
            (vars: make vars reduce [to-set-word var either paren? list [do list] [list]])
        ] 
        opt [
            'where 
            set filter [block!]
        ]
    ] 
    unless parse comprehension rules [
        make error! "The list comprehension was not valid."
    ] 
    action: func copy at first vars 2 action 
    filter: func copy at first vars 2 either found? filter [filter] [[true]] 
    elems: 1 
    foreach field at first vars 2 [
        unless found? result [
            result: make either type [datatype] [type? vars/(field)] none
        ] 
        elems: elems * (length? vars/(field))
    ] 
    for n 0 (elems - 1) 1 [
        skip: elems 
        args: copy [] 
        foreach field at first vars 2 [
            list: vars/(field) 
            skip: skip / length? list 
            index: (mod to-integer (n / skip) length? list) + 1 
            append args list/(index)
        ] 
        if do compose [filter (args)] [
            append/only result do compose [action (args)]
        ]
    ] 
    result
]
