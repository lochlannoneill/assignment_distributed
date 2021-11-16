PROJECT BRIEF:
-COMPLETE-  The player is provided with 7 letters (never including an S).
-DOING-     One of the letters is the centre letter which must be included in all submitted words.
-COMPLETE-  Any of the 7 letters can be the centre letter
-COMPLETE-  You can use any of the 7 letters as many times as you like.
-COMPLETE-  A valid word must be at least 4 letters long
-COMPLETE?- A 4 letter word scores 1 point
-COMPLETE?- For all words of 5 letters and above the score is the number of letters, e.g. a 7-letter word score 7 points
-COMPLETE?- If the submitted word contains all 7 letters (a pangram), a bonus is applied of 7 points. E.g. in the image below, AUTOCRACY is 9 letters long and contains all 7 letters, therefore scores 16 points. Usually there is only 1 pangram, but I have seen 2 or 3 in a game also.


BUGS:
-URGENT-    client stopped working when i tried to request the required letter
            when this bug is fixed
                - add 'string str' to spellingb.proto
                - uncomment code in server.py VerifyWord()
                - remove while look from client.py ask_input()

-SMALL-     the pangram returned to the client is of length 8 for some reason. len 7 is required



Fixed Bugs:
