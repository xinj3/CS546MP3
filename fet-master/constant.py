PAD = '<<<$PAD$>>>'
UNK = '<<<$UNK$>>>'
EOS = '<<<$EOS$>>>'
SOS = '<<<$SOS$>>>'
PAD_INDEX = 0       # Padding symbol index
UNK_INDEX = 1       # Unknown token index
SOS_INDEX = 2       # Start-of-sentence symbol index
EOS_INDEX = 3       # End-of-sentence symbol index
CHAR_PADS = [
    (PAD, PAD_INDEX),
    (UNK, UNK_INDEX),
]
TOKEN_PADS = [
    (PAD, PAD_INDEX),
    (UNK, UNK_INDEX),
    (SOS, SOS_INDEX),
    (EOS, EOS_INDEX),
]
TOK_REPLACEMENT = {
    '-LRB-': '(',
    '-RRB-': ')',
    '-LSB-': '[',
    '-RSB-': ']',
    '-LCB-': '{',
    '-RCB-': '}',
    '``': '"',
    '\'\'': '"',
    '/.': '.',
    '/?': '?'
}

ELMO_MAX_CHAR_LEN = 50