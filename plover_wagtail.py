KEYS = (
    '#',
    'G-', 'B-', 'D-', 'Z-', 'I-', 'U-', 'A-', 'E-', 'N-', 'W-',
    '*',
    '-G', '-B', '-D', '-Z', '-I', '-U', '-A', '-E', '-N', '-W',
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

        'N-': 'q',
        'W-': 'a',
        'A-': 'w',
        'E-': 's',
        'I-': 'e',
        'U-': 'd',
        'D-': 'r',
        'Z-': 'f',
        'B-': 'c',
        'G-': 'v',
        
        '*': ('t', 'g', 'y', 'h'),

        '-G': 'n',
        '-B': 'm',
        '-D': 'u',
        '-Z': 'j',
        '-I': 'i',
        '-U': 'k',
        '-A': 'o',
        '-E': 'l',
        '-N': 'p',
        '-W': ';',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C', '-D', '-Z'),

        'N-': 'S1-',
        'W-': 'S2-',
        'A-': 'T-',
        'E-': 'K-',
        'I-': 'P-',
        'U-': 'W-',
        'D-': 'H-',
        'Z-': 'R-',
        'B-': 'A-',
        'G-': 'O-',
        
        '*': ('*1', '*2', '*3', '*4'),

        '-G': '-E',
        '-B': '-U',
        '-D': '-F',
        '-Z': '-R',
        '-I': '-P',
        '-U': '-B',
        '-A': '-L',
        '-E': '-G',
        '-N': '-T',
        '-W': '-S',

        'no-op': ('res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = 'asset:plover_wagtail:dictionaries'
DEFAULT_DICTIONARIES = (
	'wagtail-lightning.json', 
	'wagtail-adorned.json', 
	'wagtail-commands.json', 
	'wagtail-briefs.json')
