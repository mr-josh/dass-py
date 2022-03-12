from datetime import datetime
from pathlib import Path


das = {
    "d": 0,
    "a": 0,
    "s": 0,
}

questions = [
    ("I found it hard to wind down", "s"),
    ("I was aware of dryness of my mouth", "a"),
    ("I couldn't seem to experience any positive feeling at all", "d"),
    ("I experienced breathing difficulty (eg, excessively rapid breathing, breathlessness in the absence of physical exertion)", "a"),
    ("I found it difficult to work up the initiative to do things", "d"),
    ("I tended to over-react to situations", "s"),
    ("I experienced trembling (eg, in the hands)", "a"),
    ("I felt that I was using a lot of nervous energy", "s"),
    ("I was worried about situations in which I might panic and make a fool of myself", "a"),
    ("I felt that I had nothing to look forward to", "d"),
    ("I found myself getting agitated", "s"),
    ("I found it difficult to relax", "s"),
    ("I felt down-hearted and blue", "d"),
    ("I was intolerant of anything that kept me from getting on with what I was doing", "s"),
    ("I felt I was close to panic", "a"),
    ("I was unable to become enthusiastic about anything", "d"),
    ("I felt I wasn't worth much as a person", "d"),
    ("I felt that I was rather touchy", "s"),
    ("I was aware of the action of my heart in the absence of physical exertion (eg, sense of heart rate increase, heart missing a beat)", "a"),
    ("I felt scared without any good reason", "a"),
    ("I felt that life was meaningless", "d")
]

Path("recordings/").mkdir(parents=True, exist_ok=True)
with open(f"recordings/{datetime.now().isoformat()}.csv", "w") as f:
    for quest in questions:
        resp = input(f"{quest[0]}: ")
        das[quest[1]] += int(resp)
        f.write(f"{quest[0]},{resp}\n")
    f.write(f"totals,D:{das['d']} A:{das['a']} S:{das['s']}")


print(f"D:{das['d']} A:{das['a']} S:{das['s']}")
