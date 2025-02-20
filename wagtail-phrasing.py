LONGEST_KEY = 1

starters = {
    "BDA": "他",
    "BDIU": "她",
    "BDE": "它",
    "BDIW": "牠",
    "BDN": "祂",
    "UE": "我",
    "BDEN": "他們",
    "GZW": "是"
}

enders = {
    "IEW": "有",
    "D": "的",
    "ZW": "知道",
    "GDZAN": "看",
    "GZW": "是"
}

number = {
    "I": "一",
    "GBEW": "某"
}

classifier = {
    "Z": "隻",
    "G": "個"
}

preadj = {
    "DZN": "很",
    "DZAW": "好",
    "BDAE": "太",
    "GBDZENW": "非常",
    "BZAW": "超",
    "ZIUEW": "最",
    "BIUA": "比較",
    "GEW": "夠",
    "IUAE": "越來越"
}

adj = {
    "BUE": "薄",
    "BAE": "白",
    "BAW": "飽",
    "BN": "笨",
    "BANW": "棒",
    "BIAN": "扁",
    "BINW": "冰",
    "B": "不",
    "BDZA": "怕",
    "BDZUE": "破",
    "BDZE": "配",
    "BDZANW": "胖",
    "BDZNW": "澎",
    "BDZIAW": "漂",
    "BDZINW": "平",
    "BDZ": "普",
    "GBENW": "美",
    "GBAW": "毛",
    "GBAN": "慢",
    "GBN": "悶",
    "GBANW": "忙",
    "GBNW": "猛",
    "GBI": "密",
    "GBIAW": "妙",
    "GBIEW": "謬",
    "GBDZUE": "佛",
    "GBDZE": "肥",
    "GBDZAN": "煩",
    "GBDZN": "粉",
    "GBDZANW": "方",
    "GBDZNW": "瘋",
    "GBDZ": "富",
    "DA": "大",
    "D": "的"
}

ordinal = {
    "DI": "第"
}

name = {
    "GDI*GB": "李"
}

def lookup(key):
    assert len(key) <= LONGEST_KEY

    ks = ""
    km = ""
    ke = ""
    kf = ""
    ph = ""
    c = 0
    d = 0
    nm = 0

    for i in key[0]:  # Assuming key is a string
        if c == 0:
            if i == "#":
                nm += 1  # check if chord is a number phrase
            else:
                c += 1  # move on otherwise
        if c == 1:
            if i in "-*":
                c += 1  # move on if you hit "-" or "*"
            else:
                ks += i  # otherwise add the key to the starting half
        if c == 2:
            if not i in "-*":
                c += 1  # if you find something that isn't "-" or "*", move on
            elif i in "-*":
                km += i  # add "-*" to middle
        if c == 3:
            ke += i  # add remaining keys to ending
            
    if nm == 1:  # if chord has # for number
    	if km == "*":
    		kf += ks+km+ke
    		if kf in name:
    			ph += name[kf]
    		else:
    			raise KeyError
        elif ks in number:
            ph += number[ks]  # if can find start in number, add to phrase
        elif ks == "":
            ph += ""
        else:
            raise KeyError
        if ke in classifier:
            ph += classifier[ke]  # if can find end in classifier, add
        elif ke == "":
            ph += ""
        else:
            raise KeyError

    elif ks in preadj:  # if chord has preadj starter
        ph += preadj[ks]  # if can find start in preadj, add to phrase
        if ke in adj:
            ph += adj[ke]  # if can find end in adj, add
        elif ke in enders:
            ph += enders[ke]  # if can find end in enders, add to phrase
        else:
            raise KeyError

    else:
        if ks in starters:
            ph += starters[ks]  # add left side if found in starters
        elif ks in number:
            ph += number[ks]  # check in numbers; add if found
        else:
            raise KeyError
        if ke in enders:
            ph += enders[ke]  # if found right side in enders, add
        elif ke in classifier:
            ph += classifier[ke]  # check classifiers; add if found
        else:
            raise KeyError

    return " ".join(ph.split())
