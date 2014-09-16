from EngScript import syntaxRules
from EngScript import outputString
from EngScript import grammar
import speakingCountdownTimer

timerScript = grammar + [
    [["say <<x>>"], "speakingCountdownTimer.say{<<x>>}"],
    [["do this <<foo>> times(| ): <<bar>>", "<<bar>> <<foo>> times"], "for _ in range{<<foo>>} (<<bar>>)"],
    [["<<x>> for <<y>> minute(s|)", "(|do this )for <<y>> minute(s|)(| ): <<x>>"], "speakingCountdownTimer.countDown{(timeInMinutes = <<y>>), (toSay = <<x>>), (interval = 5)}"],
    [["(do|(work|focus|concentrate) on)(| (each|all|(each|every) one)(| of)) these(| tasks) for <<x>> minute(|s) each(| ): <<y>>", "do( |(each|all) of) these for <<x>> minute(|s): <<y>>"], "for current in <<y>> (current for <<x>> minutes)"],
]

firstTimerScript = syntaxRules.testMacro(timerScript, '''
module
    #say "The instructions on this list should be limited to reading assignments";
    do this 10 times:
        do all of these tasks for 10 minutes each:
            ["Add citation URLs to draft 2 of the essay", "Put the URLs into MLA format"];
        #Submit the in-class assignment for the first draft of the essay, Read essay assignment on Blackboard, Check Nova email, Email questions about the essay assignment, Search for newspaper articles for the annotated bibligraphy, Write down questions about the annotated bibliography";
        #["Ask Facebook friends about weekend plans", "Try to find headphones", "Ask Vicky White for disability accommodations", "Ask which assignments are due"]
    do this 4 times:
        "End of countdown timer" for 2 minutes;
''')

#raise Exception(firstTimerScript)

timerScriptToEval = outputString("Python", firstTimerScript)

#raise Exception(timerScriptToEval)
exec timerScriptToEval