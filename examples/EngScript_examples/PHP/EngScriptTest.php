

function engScript_randomStringGenerator(){
    return;
    (array(1,3,5,3)[rand((0 - 1)+1, count(array(1,3,5,3))-1)]);
}
print(rand(2+1, 5-1))
print(rand(2+1, 7-1))
print(rand(2+1, 5-1))
if($engScript_a){
    b;
}
elseif($engScript_v){
    d;
}
else {
    d;
}
//"The next line uses the string concatenation operator"
$engScript_str1 . $engScript_str2
//"The next line uses the array concatenation operator"
array_merge($engScript_arr1, $engScript_arr2)
function engScript_openingTag($engScript_theTag){
    return "<" . $engScript_theTag . ">";
}
function engScript_closingTag($engScript_theTag){
    return "</" . $engScript_theTag . ">";
}
function engScript_surroundWithTag($engScript_theString, $engScript_theTag){
    return engScript_openingTag($engScript_theTag) . $engScript_theString . engScript_closingTag($engScript_theTag);
}
function engScript_boldText($engScript_str1){
    return engScript_surroundWithTag($engScript_str1,"b");
}
function engScript_italicText($engScript_str1){
    return engScript_surroundWithTag($engScript_str1,"i");
}
function engScript_boldWikiText($engScript_str1){
    return "'''" . $engScript_str1 . "'''";
}
function engScript_italicWikiText($engScript_str1){
    return "''" . $engScript_str1 . "''";
}
function engScript_wikiLink($engScript_pageTitle, $engScript_linkText){
    return "[[" . $engScript_pageTitle . "|" . $engScript_linkText . "]]";
}
function engScript_markdownLink($engScript_theURL, $engScript_linkText){
    return "[" . $engScript_linkText . "](" . $engScript_theURL . ")";
}
strlen("hello")
substr($engScript_a,2,5)
"derp" . "herp";
(3 > 4)
(3 < 4)
(3 >= 4)
(3 <= 4)
print($engScript_lawz)
foreach ($engScript_b as $engScript_a){
    derp
}
//"Hello World!"
"common " . " lisp"
function engScript_helloWorld($engScript_a, $engScript_b){
    if($engScript_a){
        return (3 - (((1 * 1) + 2) / 4));
    }
    elseif($engScript_b){
        return 2;
    }
    else {
        return 3;
    }
}