So this is basically a dict-building state machine.

It stays in one state until a line is provided that matches the state. Then it continues.

Some sections repeat, so there is also an exit condition. If the file ends, or if there is a match for the next line after the section, this section ends and the next begins.

Looking for section[reqs], line[REQ...]

Create variable reqs. Key is provided, so variable is dictionary.

1: No match
2: No match
3: No match
4: Match found. reqs[ADAMES] = {}. reqs[ADAMES][Mnemonic] = ADAMES. Move to next line.
5: Match found. reqs[ADAMES][Description] = ADAMES. Move to next line.
6: Match found. reqs[ADAMES][Department] = 01.173. Move to next line.

Next is section. Create variable stocks. Enter section. 

7: No match
8: No match
9: No match
10: No match
11: No match
12: Match found. stocks[0] = {Line: 1, Item: 018159, Description: ALCOHOL..., PackagingString: EA}. Move to next line.
End of section. Section repeats, so return to the beginning of this section. 
Set exit condition to the next line. End of section. Section repeats, so return to the beginning of this section.


Really, we just need to define an exit condition for the repeating sections that will skip to the next section.

