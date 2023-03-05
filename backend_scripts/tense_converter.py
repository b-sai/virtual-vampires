
import os
import pandas as pd


df = pd.read_csv("data/dict.tsv", header=None, sep="\t")

verbs = df[1].tolist()

print(verbs)

def to_past(verb):
    if len(verb.split(" ")) > 1:
        return to_past(verb.split(" ")[0]) + " " + " ".join(verb.split(" ")[1:])
    if verb.startswith("be "):
        return verb.replace("be ", "was ")
    if verb.startswith("put on"):
        return verb

    if verb in tense_exceptions:
        return tense_exceptions[verb]
    if verb.endswith("e"):
        return verb + "d"
    elif verb.endswith("y"):
        return verb[:-1] + "ied"
    elif verb.endswith("d"):
        return verb[:-1] + "t"
    else:
        return verb+"ed"
    
    
def to_future(verb):
    return "will " + verb

def get_past_participle(verb):
    if verb in participle_exceptions:
        return participle_exceptions[verb]
    elif verb.endswith("e"):
        return verb + "d"
    elif len(verb) > 2 and verb.endswith("y") and verb[-2] not in "aeiou":
        return verb.replace("y", "ied")
    else:
        return verb+"ed"
    
        

# build a dictionary of exceptions when converting to past tense
tense_exceptions = {
    "go": "went",
    "come": "came",
    "do": "did",
    "have": "had",
    "be": "was",
    "see": "saw",
    "make": "made",
    "take": "took",
    "get": "got",
    "know": "knew",
    "think": "thought",
    "say": "said",
    "tell": "told",
    "see": "saw",
    "come": "came",
    "give": "gave",
    "find": "found",
    "tell": "told",
    "feel": "felt",
    "fall": "fell",
    "need": "needed",
    "leave": "left",
    "become": "became",
    "begin": "began",
    "hear": "heard",
    "run": "ran",
    "hold": "held",
    "bring": "brought",
    "write": "wrote",
    "sit": "sat",
    "stand": "stood",
    "lose": "lost",
    "pay": "paid",
    "meet": "met",
    "set": "set",
    "lead": "led",
    "understand": "understood",
    "speak": "spoke",
    "read": "read",
    "grow": "grew",
    "win": "won",
    "add": "added",
    "clad": "clad",
    "shred": "shredded",
    "build": "built",
    "hold": "held",
    "yield": "yielded",
    "end": "ended",
    "bend": "bent",
    "send": "sent",
    "bid": "bidded",

}

for verb in verbs:
    past_verb = to_past(verb)
    print(f"{verb:<20} | {past_verb:<20} | {to_future(verb):<20}")
