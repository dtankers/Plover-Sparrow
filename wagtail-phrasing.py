LONGEST_KEY = 3

number = {
"#GH*I": "{&7}",
"#GH*IAN": "{&000}",
"#GHI": "七",
"#GHIAN": "千",
"#G*IEO24": "{&9}",
"#GIEO24": "九",
"#ZL*IAN": "{&3}",
"#ZL*I4": "{&4}",
"#ZL*2": "{&10}",
"#ZLIAN": "三",
"#ZLI4": "四",
"#ZL2": "十",
"#ZAO4": "兆",
"#B*A": "{&8}",
"#B*AE24": "{&00}",
"#BA": "八",
"#BAE24": "百",
"#L*IEO4": "{&6}",
"#L*INO2": "{&0}",
"#LIEO4": "六",
"#LINO2": "零",
"#*I": "{&1}",
"#*UAN4": "{&0000}",
"#*U24": "{&5}",
"#*EN4": "{&2}",
"#I": "一",
"#I4": "億",
"#UAN4": "萬",
"#U24": "五",
"#EN4": "二",
"G4": "各",
"BLEO24": "某"
}

classifier = {
"B":"部",
"B":"步",
"BA24":"把",
"BAN":"班",
"BAN4":"瓣",
"BANO":"幫",
"BAO":"包",
"DHAE2":"台",
"DHANO2":"堂",
"DHANO24":"趟",
"DHAO4":"套",
"DHEO2":"頭",
"DHI2":"題",
"DHIAN":"天",
"DHIAO2":"條",
"DHIE":"帖",
"DHINO24":"挺",
"DHUAN2":"團",
"DHUO2":"坨",
"DHUNO":"通",
"BHAE2":"排",
"BHAE4":"派",
"BHAN2":"盤",
"BHAO4":"泡",
"BHEO2":"抔",
"BHI":"批",
"BHI24":"匹",
"BHIAN4":"片",
"BHIAN":"篇",
"BHINO2":"瓶",
#"BHINO2":"坪", # need to add graphical key
"BE":"杯",
"BE4":"輩",
"BI24":"筆",
"BIAN4":"遍",
"BN24":"本",
"ZH24":"尺",
"ZHANO24":"場",
"ZHI4":"次",
"ZHE4":"冊",
"ZHINO2":"層",
"ZHIUN4":"寸",
"ZHU":"齣",
"ZHUAN4":"串",
#"ZHUANO2":"床", need to add graphical key
"ZHUANO2":"幢",
"ZHIUO":"撮",
"DA24":"打",
"DAE4":"袋",
"DAO4":"道",
"DAO":"刀",
"DEO24":"斗",
"DI4":"地",
"DI":"滴",
"DIAN24":"點",
"DINO24":"頂",
"DU24":"堵",
"DUAN4":"段",
"DUO24":"朵",
"DUE4":"對",
"DUE":"堆",
"DUN4":"頓",
#"DUN4":"噸", #need to add graphical key
"DUNO4":"棟",
"H2":"盒",
"HANO2":"行",
"HAO4":"號",
"HI2":"席",
"HIA4":"下",
"HIANO4":"項",
"HU4":"戶",
"HU2":"壺",
"HUO24":"伙",
"HUE2":"回",
"G":"個",
"GAN24":"桿",
"DLIAN2":"年",
"BHLA":"發",
"BHLAN":"番",
"BHLANO":"方",
"BHLN":"分",
"BHLN4":"份",
"BHLNO":"封",
"BHL2":"服",
"BHL4":"副",
"BLE2":"枚",
"BLI24":"米",
"BLIAN4":"面",
"BLIAO24":"秒",
"BLINO2":"名",
"BLN2":"門",
"HL4":"日",
"LE4":"類",
"LI24":"里",
"LI4":"粒",
"LIA24":"倆",
"LIANO24":"兩",
"LIANO4":"輛",
"LIE4":"列",
"LIEO24":"綹",
"LIU24":"縷",
"LUO4":"摞",
"LUN2":"輪",
"GH4":"克",
#"GH4":"刻", #add graphical code
"GH":"顆",
#"GH":"棵", #add graphical code
"GHEO24":"口",
"GHI2":"期",
"GHI24":"起",
"GHIANO":"腔",
"GHIUN2":"群",
"GHUAE4":"塊",
"GHUN4":"捆",
"GI4":"記",
"GI24":"幾",
#"GI":"劑", #add graphical code
"GIA":"家",
"GIA4":"架",
"GIAN":"間",
"GIAN4":"件",
"GIAO24":"腳",
"GIE2":"節",
"GIE4":"屆",
"GIN":"斤",
"GIU4":"句",
"GDZIUAN24":"卷",
"GN":"根",
"GU24":"股",
"GUAN24":"管",
"GUAN4":"罐",
"ZL2":"時",
"ZLAN4":"扇",
#"ZLEO24":"手", # add graphical code
"ZLEO24":"首",
"ZLIAO":"艘",
"ZLIUO24":"所",
"ZLIUE4":"歲",
#"ZLNO":"聲", # add graphical code to this or 升
"ZLNO":"升",
"ZLU4":"束",
"ZLUANO":"雙",
"ZLUE24":"水",
"IANO4":"樣",
"IUAN2":"元",
"UAN24":"碗",
"UO":"窩",
"UE4":"位",
#"UE":"味", # add graphical code
"UE24":"尾",
"Z":"隻",
"ZAN24":"盞",
"ZANO":"張",
"ZIA":"匝",
"ZIAE4":"載",
"ZIE2":"則",
"ZIU24":"組",
"ZIUO4":"座",
"ZIUN":"尊",
"ZN4":"陣",
"ZU4":"柱",
"ZU":"株",
#"ZU4":"炷", #add graphical code
"ZUNO24":"種",
#"Z":"只", #add graphical code
#"Z":"支", #add graphical code
"DU4":"度",
"HLN4":"任",
"ZEO":"週",
}

ordinal = {
    "DI": "第"
}

def lookup(key):
    assert len(key) <= LONGEST_KEY

    ks = ""
    km = ""
    ke = ""
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

    kf = ks + km + ke # concatenate all key parts
    
    if ((nm == 1) and (kf in ordinal)): # if chord has # and ordinal
        if k in number:
            ph = ordinal[ks] + number[ke]
        else:
            raise KeyError           
    elif nm == 1:
    	if ks in number:
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
