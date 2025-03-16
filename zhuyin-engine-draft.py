LONGEST_KEY = 1

simpleInitials = {
    "B":"ㄅ",
    "BDZ":"ㄆ",
    "GB":"ㄇ",
    "GBDZ":"ㄈ",
    "D":"ㄉ",
    "BD":"ㄊ",
    "GBD":"ㄋ",
    "GD":"ㄌ",
    "G":"ㄍ",
    "GDZ":"ㄎ",
    "DZ":"ㄏ",
    "Z":"ㄓ",
    "BZ":"ㄔ",
    "GZ":"ㄕ",
    "GBZ":"ㄖ",
    "":""
}

palatalInitials = {
    "B":"ㄅ",
    "BDZ":"ㄆ",
    "GB":"ㄇ",
    "GBDZ":"ㄈ",
    "D":"ㄉ",
    "BD":"ㄊ",
    "GBD":"ㄋ",
    "GD":"ㄌ",
    "GI":"ㄐ",
    "GDZI":"ㄑ",
    "DZI":"ㄒ",
    "ZI":"ㄗ",
    "BZI":"ㄘ",
    "GZI":"ㄙ",
    "":""
}

affricateInitials = {
    "Z":"ㄓ",
    "BZ":"ㄔ",
    "GZ":"ㄕ"
}

defaultRimes = {
    "B":"ㄅㄨ",
    "BDZ":"ㄆㄨ",
    "GB":"ㄇㄨ",
    "GBDZ":"ㄈㄨ",
    "D":"ㄉㄜ",
    "BD":"ㄊㄜ",
    "GBD":"ㄋㄜ",
    "GD":"ㄌㄜ",
    "G":"ㄍㄜ",
    "GDZ":"ㄎㄜ",
    "DZ":"ㄏㄜ",
    "GI":"ㄐㄧ",
    "GDZI":"ㄑㄧ",
    "DZI":"ㄒㄧ",
    "Z":"ㄓ",
    "BZ":"ㄔ",
    "GZ":"ㄕ",
    "GBZ":"ㄖ",
    "ZI":"ㄗ",
    "BZI":"ㄘ",
    "GZI":"ㄙ",
    "":""
}

medials = {
    "I":"ㄧ",
    "U":"ㄨ",
    "IU":"ㄩ",
    "":""
}

simpleRimes = {
    "A":"ㄚ",
    "O":"ㄛ",
    "E":"ㄜ",
    "AE":"ㄞ",
    "ENO":"ㄟ",
    "AO":"ㄠ",
    "EO":"ㄡ",
    "AN":"ㄢ",
    "N":"ㄣ",
    "ANO":"ㄤ",
    "NO":"ㄥ",
    "EN":"ㄦ",
    "":""
}

irregularRimes = {
    "IE":"ㄧㄝ",
    "IUE":"ㄩㄝ"
}

irregularSyllables = {
    "BE":"ㄅㄟ",
    "BDZE":"ㄆㄟ",
    "GBE":"ㄇㄟ",
    "GBDZE":"ㄈㄟ",
    "GBEN":"ㄇㄜ",
    "DE":"ㄉㄟ",
    "BDE":"ㄊㄟ",
    "GBDE":"ㄋㄟ",
    "GDE":"ㄌㄟ",
    "GE":"ㄍㄟ",
    "GDZE":"ㄎㄟ",
    "DZE":"ㄏㄟ"
}

tones = {
    "D":"ˉ",
    "G":"ˊ",
    "GB":"ˇ",
    "B":"ˋ",
    "Z":"˙"
}

def lookup(key):
    assert len(key) <= LONGEST_KEY

    kls = ""
    klm = ""
    klmi = ""
    klmu = ""
    kle = ""
    krs = ""
    krm = ""
    krmi = ""
    krmu = ""
    kre = ""
    klf = ""
    krf = ""
    mid = ""
    ph = ""
    c = 0
    nm = 0

    for i in key[0]:  # Assuming key is a string
        if c == 0:
            if i == "#":
                nm += 1  # check if chord is a number phrase
            else:
                c += 1  # move on otherwise
        if c == 1:
            if i in "IU":
                c += 1  # move on if you hit a medial
            else:
                kls += i  # otherwise add key to left start
        if c == 2:
            if i in "I":
                klmi += i # add I to klmi
            else:
                c += 1 # move on
        if c == 3:
            if i in "U":
                klmu += i # add U to klmu
            else: 
                c += 1 # move on
        if c == 4:
            if i in "-*":
                c += 1  # if you find a syllable marker, move on
            else:
                kle += i  # add rime to left ending
        if c == 5:
            if i in "-*":
                mid += i # add middle symbol
            else:
                c += 1 # and then move on
        if c == 6:
            if i in "IU":
                c += 1  # move on if you hit a medial
            else:
                krs += i  # otherwise add key to right start
        if c == 7:
            if i in "I":
                krmi += i # add I to krmi
            else:
                c += 1 # move on
        if c == 8:
            if i in "U":
                krmu += i # add U to krmu
            else: 
                c += 1 # move on
        if c == 9:
            kre += i # add remaining keys to right ending

    klm = klmi + klmu
    krm = krmi + krmu
    klr = klm + kle
    krr = krm + kre
    klf = kls + klm + kle
    krf = krs + krm + kre

    if nm == 1:  # if chord has # for number
        raise KeyError
    if mid == "*":
        if krf in tones:
            if klf in irregularSyllables:
                ph = irregularSyllables[klf] + tones[krf]
            elif klmi == "I":
                if kls in affricateInitials:
                	if kle = "":
                		ph = defaultRimes[klf]
                	else:
                		ph = palatalInitials[kls] + medials[klmu] + simpleRimes[kle] + tones[krf]
                elif klr in irregularRimes:
                    ph = palatalInitials[kls] + irregularRimes[klr] + tones[krf]
                else:
                    ph = palatalInitials[kls] + medials[klm] + simpleRimes[kle] + tones[krf]
            elif kle == "":
                ph = defaultRimes[klf] + tones[krf]
            else:
                ph = simpleInitials[kls] + medials[klm] + simpleRimes[kle] + tones[krf]
        else:
        	raise KeyError
    elif klf in irregularSyllables:
        ph = irregularSyllables[klf]
    elif klmi == "I":
        if "Z" in kls:
            ph += palatalInitials[kls]
            ph += medials[klmu]
            ph += simpleRimes[kle]
        elif klr in irregularRimes:
            ph += palatalInitials[kls] 
            ph += irregularRimes[klr]
        else:
            ph += palatalInitials[kls] 
            ph += medials[klm]
            ph += simpleRimes[kle]
    elif kle == "":
        ph = defaultRimes[klf]
    else:
    	if kls not == "":
    		ph += simpleInitials[kls]
    	if klm not == "":
    		ph += medials[klm] 
    	if kle not == "":
    		ph += simpleRimes[kle]

    return " ".join(ph.split())
