LONGEST_KEY = 1

single = {
"BA":"ㄅㄚ",
"BUE":"ㄅㄛ",
"BAE":"ㄅㄞ",
"BE":"ㄅㄟ",
"BAW":"ㄅㄠ",
"BAN":"ㄅㄢ",
"BN":"ㄅㄣ",
"BANW":"ㄅㄤ"
}

double = {
"BA*D":"ㄅㄚˉ",
"BUE*D":"ㄅㄛˉ",
"BAE*D":"ㄅㄞˉ",
"BE*D":"ㄅㄟˉ",
"BAW*D":"ㄅㄠˉ",
"BAN*D":"ㄅㄢˉ",
"BN*D":"ㄅㄣˉ",
"BANW*D":"ㄅㄤˉ"
}



def lookup(key):
    assert len(key) <= LONGEST_KEY

    ks = ""
    km = ""
    ke = ""
    kf = ""
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
                c += 1  # move on if you hit "-" or "*"
            else:
                ks += i  # otherwise add the key to the starting half
        if c == 2:
            if i not in "-*":
                c += 1  # if you find something that isn't "-" or "*", move on
            else:
                km += i  # add "-*" to middle
        if c == 3:
            ke += i  # add remaining keys to ending

	kf = ks + km + ke
	
    if nm == 1:  # if chord has # for number
        raise KeyError
    elif kf in double:
    	ph += double[kf]
    else:
        if ks in single:
            ph += single[ks]  # add left side if found in starters
        elif ks == "": 
        	ph += ""
        else: 
        	raise KeyError
        if ke in single:
            ph += single[ke]  # if found right side in enders, add
        elif ke == "":
        	ph += ""
        else:
            raise KeyError

    return " ".join(ph.split())
