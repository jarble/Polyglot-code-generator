Rebol [] "press ctrl+d to save this file."

print "Hi!"

"how to get type of variable:"

"how to generate a file:"

"how to  replace a word in a list"


make-dir %sampleFolder
write %sampleFolder/derp.txt "hi"


theArr: [[goo goo bar]]

print (type? theArr) = block!

foreach theIndex theArr [theArr/theIndex: to-string pick theIndex theArr]

print pick theArr 1

print type? "hello"

print 'hello == "hello"

print '_goo

Ask "Type any key to continue."