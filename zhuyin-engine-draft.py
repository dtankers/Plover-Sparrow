LONGEST_KEY = 1

simpleInitials = {
    "B": "ㄅ",
    "BH": "ㄆ",
    "BL": "ㄇ",
    "BHL": "ㄈ",
    "D": "ㄉ",
    "DH": "ㄊ",
    "DL": "ㄋ",
    "L": "ㄌ",
    "G": "ㄍ",
    "GH": "ㄎ",
    "H": "ㄏ",
    "Z": "ㄓ",
    "ZH": "ㄔ",
    "ZL": "ㄕ",
    "HL": "ㄖ",
    "": ""
}

palatalInitials = {
    "B": "ㄅ",
    "BH": "ㄆ",
    "BL": "ㄇ",
    "BHL": "ㄈ",
    "D": "ㄉ",
    "DH": "ㄊ",
    "DL": "ㄋ",
    "L": "ㄌ",
    "G": "ㄐ",
    "GH": "ㄑ",
    "H": "ㄒ",
    "Z": "ㄗ",
    "ZH": "ㄘ",
    "ZL": "ㄙ",
    "": ""
}

affricateInitials = {
    "Z": "ㄓ",
    "ZH": "ㄔ",
    "ZL": "ㄕ"
}

defaultRimes = {
    "B": "ㄅㄨ",
    "BH": "ㄆㄨ",
    "BL": "ㄇㄨ",
    "BHL": "ㄈㄨ",
    "D": "ㄉㄜ",
    "DH": "ㄊㄜ",
    "DL": "ㄋㄜ",
    "L": "ㄌㄜ",
    "G": "ㄍㄜ",
    "GH": "ㄎㄜ",
    "H": "ㄏㄜ",
    "GI": "ㄐㄧ",
    "GHI": "ㄑㄧ",
    "HI": "ㄒㄧ",
    "Z": "ㄓ",
    "ZH": "ㄔ",
    "ZL": "ㄕ",
    "HL": "ㄖ",
    "ZI": "ㄗ",
    "ZHI": "ㄘ",
    "ZLI": "ㄙ",
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
    "BHE": "ㄆㄟ",
    "BLE": "ㄇㄟ",
    "BHLE": "ㄈㄟ",
    "BLEN": "ㄇㄜ",
    "BO": "ㄅㄛ", #兼容碼
    "BHO": "ㄆㄛ", #兼容碼
    "GLO": "ㄇㄛ", #兼容碼
    "BHLO": "ㄈㄛ", #兼容碼
    "BUO": "ㄅㄛ",
    "BHUO": "ㄆㄛ",
    "GLUO": "ㄇㄛ",
    "BHLUO": "ㄈㄛ",
    "DE": "ㄉㄟ",
    "DHE": "ㄊㄟ",
    "DLE": "ㄋㄟ",
    "LE": "ㄌㄟ",
    "GE": "ㄍㄟ",
    "GHE": "ㄎㄟ",
    "HE": "ㄏㄟ",
    "ZIUE": "ㄗㄨㄟ",
    "ZHIUE": "ㄘㄨㄟ",
    "ZLIUE": "ㄙㄨㄟ",
    "ZIU": "ㄗㄨ",
    "ZHIU": "ㄘㄨ",
    "ZLIU": "ㄙㄨ",
    "ZIUO": "ㄗㄛ",
    "ZHIUO": "ㄘㄛ",
    "ZLIUO": "ㄙㄛ",
    "ZIE": "ㄗㄜ",
    "ZHIE": "ㄘㄜ",
    "ZLIE": "ㄙㄜ"
}

tones = {
    "D": "ˉ",
    "2": "ˊ",
    "24": "ˇ",
    "4": "ˋ",
    "Z": "˙"
}

def lookup(key):
    assert len(key) <= LONGEST_KEY

    syllableInitial = ""
    syllableRime = ""
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
			if i in "-*":
				c += 1 # if you find a middle marker, move on
			else:
				syllableInitial += i # add to syllableInitial
		if c == 2:
			if i in "-*":
				mid += i
			else:
				c += 1
		if c == 3:
			if i in "I":
				syllableMedialI += i #add I to syllableMedial (palatal)
			elif i in "U":
				syllableMedialU += i # add U to syllableMedial (rounded)
			else:
				c += 1 # move on otherwise
		if c == 4:
			if i in "24": 
				c += 1 # if you find a tone number, move on
			else:
				syllableEnding += i #add keys to syllableEnding
		if c == 5:
			syllableTone += i #add any remaining keys to syllableTone
	

    syllableMedial = syllableMedialI + syllableMedialU
    syllableRime = syllableMedial + syllableEnding
    syllableFull = syllableInitial + syllableMedial + syllableEnding

    if nm == 1:  # if chord has # for number
        raise KeyError
    if mid == "*":
        raise KeyError

    if syllableFull in irregularSyllables:
        ph += irregularSyllables[krf]
    elif syllableMedialI != "":
        if syllableInitial in affricateInitials:
            if syllableEnding == "":
                ph += defaultRimes[syllableFull]
            elif syllableRime in irregularRimes:
                ph += palatalInitials[syllableInitial]
                ph += irregularRimes[syllableRime]
            else:
                ph += palatalInitials[syllableInitial]
                ph += medials[syllableMedialU]
                ph += simpleRimes[syllableEnding]
        elif syllableRime in irregularRimes:
            ph += palatalInitials[syllableInitial]
            ph += irregularRimes[syllableRime]
        else:
            ph += palatalInitials[syllableInitial]
            ph += medials[syllableMedial]
            ph += simpleRimes[syllableEnding]
    elif syllableRime == "":
        ph = defaultRimes[syllableFull]
    elif syllableRime in irregularRimes:
        ph = simpleInitials[syllableInitial] + irregularRimes[syllableRime]
    else:
        if syllableInitial != "":
            ph += simpleInitials[syllableInitial]
        if syllableMedialU != "":
            ph += medials[syllableMedialU]
        if kle != "":
            ph += simpleRimes[syllableEnding]

    return " ".join(ph.split())
