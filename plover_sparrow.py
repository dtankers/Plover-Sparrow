KEYS = (
    '#',
    '、', '？', '。', '：', 'ㄅ', 'ㄍ', 'ㄉ', 'ㄓ', 'ㄏ', 'ㄌ',
    '*',
    'ㄧ', 'ㄨ', 'ㄚ', 'ㄜ', 'ㄣ', 'ㄛ', 'ˋ', 'ˊ',
)

IMPLICIT_HYPHEN_KEYS = ('*')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

FERAL_NUMBER_KEY = False

UNDO_STROKE_STENO = "*"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'x'),

        '、': 'q',
        '？': 'a',
        '。': 'w',
        '：': 's',
        'ㄅ': 'e',
        'ㄍ': 'd',
        'ㄉ': 'r',
        'ㄓ': 'f',
        'ㄏ': 'c',
        'ㄌ': 'v',
        
        '*': ('t', 'g', 'y', 'h'),

        'ㄧ': 'n',
        'ㄨ': 'm',
        'ㄚ': 'u',
        'ㄜ': 'j',
        'ㄣ': 'i',
        'ㄛ': 'k',
        '2': 'o',
        'ˋ': 'l',
        'ˊ': ('p', ';'),

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C', '-D', '-Z'),

        '、': 'S1-',
        '？': 'S2-',
        '。': 'T-',
        '：': 'K-',
        'ㄅ': 'P-',
        'ㄍ': 'W-',
        'ㄉ': 'H-',
        'ㄓ': 'R-',
        'ㄏ': 'A-',
        'ㄌ': 'O-',
        
        '*': ('*1', '*2', '*3', '*4'),

        'ㄧ': '-E',
        'ㄨ': '-U',
        'ㄚ': '-F',
        'ㄜ': '-R',
        'ㄣ': '-P',
        'ㄛ': '-B',
        'ˋ': '-L',
        'ˊ': '-G',
        '#': ('-T', '-S'),

        'no-op': ('res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = 'asset:plover_sparrow:dictionaries'
DEFAULT_DICTIONARIES = (
	'sparrow-1char.json', 
	'sparrow-2char.json', 
	'sparrow-numbers.json',
	'sparrow-commands.json')
