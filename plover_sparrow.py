KEYS = (
    '#',
    '、', '？', '。', '：', 'B', 'G', 'D', 'Z', 'H', 'L',
    '*',
    'I', 'U', 'A', 'E', 'N', 'O', '2', '4',
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
        'B': 'e',
        'G': 'd',
        'D': 'r',
        'Z': 'f',
        'H': 'c',
        'L': 'v',
        
        '*': ('t', 'g', 'y', 'h'),

        'I': 'n',
        'U': 'm',
        'A': 'u',
        'E': 'j',
        'N': 'i',
        'O': 'k',
        '2': 'o',
        '4': 'l',
        '#': ('p', ';'),

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C', '-D', '-Z'),

        '、': 'S1-',
        '？': 'S2-',
        '。': 'T-',
        '：': 'K-',
        'B': 'P-',
        'G': 'W-',
        'D': 'H-',
        'Z': 'R-',
        'H': 'A-',
        'L': 'O-',
        
        '*': ('*1', '*2', '*3', '*4'),

        'I': '-E',
        'U': '-U',
        'A': '-F',
        'E': '-R',
        'N': '-P',
        'O': '-B',
        '2': '-L',
        '4': '-G',
        '#': ('-T', '-S'),

        'no-op': ('res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = 'asset:plover_sparrow:dictionaries'
DEFAULT_DICTIONARIES = (
	'sparrow-1char.json', 
	'sparrow-2char.json', 
	'sparrow-commands.json')
