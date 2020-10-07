# freezeout
Ever been totally frozen out of a domain? Can't even get a lousy userlist from the DC? On a dead segment with nothing to grab or relay?

Stupid authentication. Make your own list!

## what is this?
Notes on user enumeration, password spraying, a list of last names and a script to generate usernames.

## OSINT's cool and all..
..and it's definitely useful, but, it probably won't yield the raw number of accounts needed to get lucky with lateral spraying. 

What's the interpid pentester to do before they freeze to death and the wolves decend?

## Kerberos to the rescue
This is not a new thing, but I did some work on an engagement that I thought I'd pack up and ship to hopefully save someone some time if they end up in the predicamant I was in.

Kerberos will allow for username queries with no penalties (no chance of lockouts, and likely not logged). You can blast the DC with hundreds of thousands of queries, and it will helpfully tell you if it's a valid name or not.

Nmap has a script for this, as well as metasploit (gather/kerberos_enumusers). I prefered the MSF modulule as it so graciously logged everything and seemed more reliable than the nmap script. Quite a bit more reliable actually. I found another tool, kerbrute, that is faster, more reliable, and more feature rich than either of those: kerbrute. Recommended!!
- [kerbrute](https://github.com/ropnop/kerbrute)  << Recommended! 
- [MSF](https://www.rapid7.com/db/modules/auxiliary/gather/kerberos_enumusers)
- [nmap](https://nmap.org/nsedoc/scripts/krb5-enum-users.html)


## Cool story bro, so what?
OK, OK, chill. Once you have a list of actual usernames, you can proceed to lateral spray passwords to hopefully get some real creds up in the joint.

'Winter2019' **IS ALIVE AND WELL.** Really.

## da code
Along with this salty readme, you'll find a list of about 36K last names and a script that will generate a userlist by looping through and prepending a letter (first initial + lastname style). 

It'll be about 8megs, with 944040 candidates. It'll take awhile to run through kerberos, but if you're that locked out, *anything* is a step in the right direction. More productive than crying anyways.

## How do I spray?
There are so many options, I can't (won't) get into it, but here's a couple bones:

- MSF has a module, although I think it's likely to lockout everyone if not kept on a short leash.
- CME will enumerate as well, but again, it'll lock everyone out.

I slapped together a simple shell script (slowride.sh) that let CME do the user loop and gave it a single password, then slept for 15 minutes. 

Lockout rules can be pretty different between domains, so tread with caution.

## Yea, but but what for where I the pw?
Easy champ. Start with the cheesy ones (there's always some of THOSE people), Password01, Summer2019!, crap like that. [SecLists](https://github.com/danielmiessler/SecLists) has a lot of good inspiration.

Will this work? Not guaranteed at all. But it might. What else you got going on?

### Good luck, and stay warm!
