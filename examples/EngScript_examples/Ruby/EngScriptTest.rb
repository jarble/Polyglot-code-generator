
module EngScriptTest
    for i in 1..2
        1
    end
    for i in 1..2
        1
    end
    engScript_a[i]
    (engScript_a + engScript_a)
    engScript_foo.length
    engScript_derp.length
    (3**10)
    (3 + 3)
    engScript_j = 5
    #"These functions are intended to be used in the EngScript compiler"
    engScript_j = 1
    (3 * 4)
    (3 + 5)
    (3 / 7)
    (q and a)
    def engScript_derp(engScript_wow)
        while engScript_a do
            a
        end
        hello
    end
    def engScript_lol(engScript_thing)
        if engScript_a then
            a
        else
            guh
    end
    def engScript_randomStringGenerator()
        return
        ([1,3,5,3][Random.new.rand(((0 - 1)+1)..([1,3,5,3].length-1))])
    end
    puts(Random.new.rand((2+1)..(5-1)))
    puts(Random.new.rand((2+1)..(7-1)))
    puts(Random.new.rand((2+1)..(5-1)))
    if engScript_a then
        b
    elsif engScript_v
        d
    else
        d
    end
    #"The next line uses the string concatenation operator"
    (engScript_str1 + engScript_str2)
    #"The next line uses the array concatenation operator"
    (engScript_arr1 + engScript_arr2)
    def engScript_openingTag(engScript_theTag)
        return ("<" + engScript_theTag + ">")
    end
    def engScript_closingTag(engScript_theTag)
        return ("</" + engScript_theTag + ">")
    end
    def engScript_surroundWithTag(engScript_theString, engScript_theTag)
        return (engScript_openingTag(engScript_theTag) + engScript_theString + engScript_closingTag(engScript_theTag))
    end
    def engScript_boldText(engScript_str1)
        return engScript_surroundWithTag(engScript_str1,"b")
    end
    def engScript_italicText(engScript_str1)
        return engScript_surroundWithTag(engScript_str1,"i")
    end
    def engScript_boldWikiText(engScript_str1)
        return ("'''" + engScript_str1 + "'''")
    end
    def engScript_italicWikiText(engScript_str1)
        return ("''" + engScript_str1 + "''")
    end
    def engScript_wikiLink(engScript_pageTitle, engScript_linkText)
        return ("[[" + engScript_pageTitle + "|" + engScript_linkText + "]]")
    end
    def engScript_markdownLink(engScript_theURL, engScript_linkText)
        return ("[" + engScript_linkText + "](" + engScript_theURL + ")")
    end
    "hello".length
    engScript_a[2..5]
    ("derp" + "herp")
    (3 > 4)
    (3 < 4)
    (3 >= 4)
    (3 <= 4)
    puts(engScript_lawz)
    Ruby
        derp
    end
    #"Hello World!"
    ("common " + " lisp")
    def engScript_helloWorld(engScript_a, engScript_b)
        if engScript_a then
            return (3 - (((1 * 1) + 2) / 4))
        elsif engScript_b
            return 2
        else
            return 3
        end
    end
end