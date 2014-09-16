import englishToPython
countDownTimer = englishToPython.englishToPython + [
    [["(remind|tell|ask|instruct|prompt|command) me to <<bar>> every <<baz>> minutes for the next <<foo>> minutes", "for(| the next) <<foo>> minutes (remind|tell|ask|instruct|prompt|command) me to <<bar>> every <<baz>> minutes"], "SpeakingCountdownTimer.countDown{<<foo>>, <<bar>>, <<baz>>}"],
    [["for(| the next) <<foo>> minutes(,|) ((remind|tell|ask|instruct|prompt|command) me to|I (should|must|will)) <<bar>>", "(|(I (will|should|must)|(remind|tell|ask|instruct|prompt|command) me to) )<<bar>> for the next <<foo>> minutes"], "remind me to <<bar>> every 2 minutes for the next <<foo>> minutes"],
    [["for(| the next) <<foo>> minutes(|,) <<bar>>"], "<<bar>> for the next <<foo>> minutes"],
    [["<<foo>> for <<bar>> minutes"], "<<foo>> for the next <<bar>> minutes"],
    [["do (|all of )these for <<foo>> minutes : <<bar>>", "do(| ((each|every|all)(| one)(| of))) these(| things) for <<foo>> minutes: <<bar>>"], 'for each current in <<bar>> : (current for <<foo>> minutes)'],
    [["do this for <<foo>> minutes : <<bar>>"], "<<bar>> for <<foo>> minutes"],
    [["<<bar>> for <<foo>> minutes each", "for <<foo>> minutes each : <<bar>>", "for <<foo>> minutes do (|(each|all)( | of ))these : <<bar>>"], "do these for <<foo>> minutes: <<bar>>"],
    [["for <<bar>> minutes each do these in a random order : <<foo>>", "do these in a random order for <<bar>> minutes each : <<foo>>", "<<foo>> in a random order for <<bar>> minutes"], "do all of these for <<bar>> minutes : (<<foo>> rearranged randomly)"],
    [["<<foo>> times : <<bar>>"], "do this <<foo>> times: <<bar>>"],
]