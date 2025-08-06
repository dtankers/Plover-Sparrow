KEYS = (
    '#',
    '壹', '貳', '叄', '肆', 'G', 'Z', 'B', 'D', 'L', 'H',
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

        '壹': 'q',
        '貳': 'a',
        '叄': 'w',
        '肆': 's',
        'G': 'e',
        'Z': 'd',
        'B': 'r',
        'D': 'f',
        'L': 'c',
        'H': 'v',
        
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

        '壹': 'S1-',
        '貳': 'S2-',
        '叄': 'T-',
        '肆': 'K-',
        'G': 'P-',
        'Z': 'W-',
        'B': 'H-',
        'D': 'R-',
        'L': 'A-',
        'H': 'O-',
        
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
