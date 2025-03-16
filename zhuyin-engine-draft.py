LONGEST_KEY = 1

simpleInitials = {
    "B": "ㄅ",
    "BDZ": "ㄆ",
    "GB": "ㄇ",
    "GBDZ": "ㄈ",
    "D": "ㄉ",
    "BD": "ㄊ",
    "GBD": "ㄋ",
    "GD": "ㄌ",
    "G": "ㄍ",
    "GDZ": "ㄎ",
    "DZ": "ㄏ",
    "Z": "ㄓ",
    "BZ": "ㄔ",
    "GZ": "ㄕ",
    "GBZ": "ㄖ",
    "": ""
}

palatalInitials = {
    "B": "ㄅ",
    "BDZ": "ㄆ",
    "GB": "ㄇ",
    "GBDZ": "ㄈ",
    "D": "ㄉ",
    "BD": "ㄊ",
    "GBD": "ㄋ",
    "GD": "ㄌ",
    "G": "ㄐ",
    "GDZ": "ㄑ",
    "DZ": "ㄒ",
    "Z": "ㄗ",
    "BZ": "ㄘ",
    "GZ": "ㄙ",
    "": ""
}

affricateInitials = {
    "Z": "ㄓ",
    "BZ": "ㄔ",
    "GZ": "ㄕ"
}

defaultRimes = {
    "B": "ㄅㄨ",
    "BDZ": "ㄆㄨ",
    "GB": "ㄇㄨ",
    "GBDZ": "ㄈㄨ",
    "D": "ㄉㄜ",
    "BD": "ㄊㄜ",
    "GBD": "ㄋㄜ",
    "GD": "ㄌㄜ",
    "G": "ㄍㄜ",
    "GDZ": "ㄎㄜ",
    "DZ": "ㄏㄜ",
    "GI": "ㄐㄧ",
    "GDZI": "ㄑㄧ",
    "DZI": "ㄒㄧ",
    "Z": "ㄓ",
    "BZ": "ㄔ",
    "GZ": "ㄕ",
    "GBZ": "ㄖ",
    "ZI": "ㄗ",
    "BZI": "ㄘ",
    "GZI": "ㄙ",
    "": ""
}

medials = {
    "I": "ㄧ",
    "U": "ㄨ",
    "IU": "ㄩ",
    "": ""
}

simpleRimes = {
    "A": "ㄚ",
    "O": "ㄨㄛ",
    "E": "ㄜ",
    "AE": "ㄞ",
    "ENO": "ㄟ",
    "AO": "ㄠ",
    "EO": "ㄡ",
    "AN": "ㄢ",
    "N": "ㄣ",
    "ANO": "ㄤ",
    "NO": "ㄥ",
    "EN": "ㄦ",
    "AEN": "ㄚㄦ",
    "": ""
}

irregularRimes = {
    "IE": "ㄧㄝ",
    "IUE": "ㄩㄝ",
    "UE": "ㄨㄟ",
    "UO": "ㄛ"
}

irregularSyllables = {
    "BE": "ㄅㄟ",
    "BDZE": "ㄆㄟ",
    "GBE": "ㄇㄟ",
    "GBDZE": "ㄈㄟ",
    "GBEN": "ㄇㄜ",
    "BO": "ㄅㄛ",
    "BDZO": "ㄆㄛ",
    "GBO": "ㄇㄛ",
    "GBDZO": "ㄈㄛ",
    "DE": "ㄉㄟ",
    "BDE": "ㄊㄟ",
    "GBDE": "ㄋㄟ",
    "GDE": "ㄌㄟ",
    "GE": "ㄍㄟ",
    "GDZE": "ㄎㄟ",
    "DZE": "ㄏㄟ",
    "ZIUE": "ㄗㄨㄟ",
    "BZIUE": "ㄘㄨㄟ",
    "GZIUE": "ㄙㄨㄟ",
    "ZIU": "ㄗㄨ",
    "BZIU": "ㄘㄨ",
    "GZIU": "ㄙㄨ",
    "ZIUO": "ㄗㄛ",
    "BZIUO": "ㄘㄛ",
    "GZIUO": "ㄙㄛ",
    "ZIE": "ㄗㄜ",
    "BZIE": "ㄘㄜ",
    "GZIE": "ㄙㄜ"
}

tones = {
    "D": "ˉ",
    "G": "ˊ",
    "GB": "ˇ",
    "B": "ˋ",
    "Z": "˙"
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
    lh = ""
    rh = ""
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
            if i in "IUAENO":
                c += 1  # move on if you hit a medial
            else:
                kls += i  # otherwise add key to left start
        if c == 2:
            if i in "I":
                klmi += i  # add I to klmi
            elif i in "U":
                klmu += i  # add U to klmu
            else:
                c += 1  # move on
        if c == 3:
            if i in "-*":
                c += 1  # if you find a syllable marker, move on
            else:
                kle += i  # add rime to left ending
        if c == 4:
            if i in "-*":
                mid += i  # add middle symbol
            else:
                c += 1  # and then move on
        if c == 5:
            if i in "IU":
                c += 1  # move on if you hit a medial
            else:
                krs += i  # otherwise add key to right start
        if c == 6:
            if i in "I":
                krmi += i  # add I to krmi
            else:
                c += 1  # move on
        if c == 7:
            if i in "U":
                krmu += i  # add U to krmu
            else:
                c += 1  # move on
        if c == 8:
            kre += i  # add remaining keys to right ending

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
            elif klmi != "":
                if kls in affricateInitials:
                    if kle == "":
                        ph = defaultRimes[klf] + tones[krf]
                    elif klr in irregularRimes:
                        ph = palatalInitials[kls] + irregularRimes[klr] + tones[krf]
                    else:
                        ph = palatalInitials[kls] + medials[klmu] + simpleRimes[kle] + tones[krf]
                elif klr in irregularRimes:
                    ph = palatalInitials[kls] + irregularRimes[klr] + tones[krf]
                else:
                    ph = palatalInitials[kls] + medials[klm] + simpleRimes[kle] + tones[krf]
            elif kle == "":
                ph = defaultRimes[klf] + tones[krf]
            elif klr in irregularRimes:
                ph = palatalInitials[kls] + irregularRimes[klr] + tones[krf]
            else:
                ph = simpleInitials[kls] + medials[klm] + simpleRimes[kle] + tones[krf]
        else:
            raise KeyError

    if krf != "":
        if krf in irregularSyllables:
            rh += irregularSyllables[krf]
        elif krmi != "":
            if krs in affricateInitials:
                if kre == "":
                    rh += defaultRimes[krf]
                elif krr in irregularRimes:
                    rh += palatalInitials[krs]
                    rh += irregularRimes[krr]
                else:
                    rh += palatalInitials[krs]
                    rh += medials[krmu]
                    rh += simpleRimes[kre]
            elif krr in irregularRimes:
                rh += palatalInitials[krs]
                rh += irregularRimes[krr]
            else:
                rh += palatalInitials[krs]
                rh += medials[krm]
                rh += simpleRimes[kre]
        elif krr == "":
            rh = defaultRimes[krf]
        elif krr in irregularRimes:
            rh = simpleInitials[krs] + irregularRimes[krr]
        else:
            if krs != "":
                rh += simpleInitials[krs]
            if krmu != "":
                rh += medials[krmu]
            if kle != "":
                rh += simpleRimes[kre]

    if klf != "":
	    if klf in irregularSyllables:
		    lh = irregularSyllables[klf]
	    elif klmi != "":
		    if kls in affricateInitials:
			    if kle == "":
				    lh = defaultRimes[klf]
			     elif klr in irregularRimes:
				     lh = palatalInitials[kls] + irregularRimes[klr]
			     else:
				     lh = palatalInitials[kls] + medials[klmu] + simpleRimes[kle]
		    elif klr in irregularRimes:
			    lh += palatalInitials[kls]
			    lh += irregularRimes[klr]
		    else:
			    lh += palatalInitials[kls]
			    lh += medials[klm]
			    lh += simpleRimes[kle]
	    elif klr == "":
		    lh = defaultRimes[klf]
	    elif klr in irregularRimes:
		    lh = simpleInitials[kls] + irregularRimes[klr]
	    else:
		    if kls != "":
			    lh += simpleInitials[kls]
		    if klmu != "":
			    lh += medials[klmu]
		    if kle != "":
			    lh += simpleRimes[kle]
    
    ph = lh + rh

    return " ".join(ph.split())
