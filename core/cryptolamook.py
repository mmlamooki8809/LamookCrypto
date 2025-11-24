import random as rd


equivalent_text_dict = {
    '743' : '1',
    '745' : '2',
    '747' : '3',
    '749' : '4',
    '750' : '5',
    '753' : '6',
    '757' : '7',
    '762' : '8',
    '771' : '9',
    '780' : '0',
    '101' : 'A',
    '102' : 'B',
    '105' : 'C',
    '107' : 'D',
    '112' : 'E',
    '124' : 'F',
    '110' : 'G',
    '120' : 'H',
    '109' : 'I',
    '114' : 'J',
    '115' : 'K',
    '137' : 'L',
    '154' : 'M',
    '181' : 'N',
    '173' : 'O',
    '192' : 'P',
    '144' : 'Q',
    '132' : 'R',
    '157' : 'S',
    '161' : 'T',
    '199' : 'U',
    '149' : 'V',
    '175' : 'W',
    '196' : 'X',
    '159' : 'Y',
    '103' : 'Z',
    '501' : 'a',
    '502' : 'b',
    '505' : 'c',
    '507' : 'd',
    '512' : 'e',
    '524' : 'f',
    '510' : 'g',
    '520' : 'h',
    '509' : 'i',
    '514' : 'j',
    '515' : 'k',
    '537' : 'l',
    '554' : 'm',
    '581' : 'n',
    '573' : 'o',
    '592' : 'p',
    '544' : 'q',
    '532' : 'r',
    '557' : 's',
    '561' : 't',
    '599' : 'u',
    '549' : 'v',
    '575' : 'w',
    '596' : 'x',
    '559' : 'y',
    '503' : 'z',
    '251' : '!',
    '262' : '?',
    '273' : '@',
    '263' : '$',
    '256' : '/',
    '241' : '_',
    '206' : '#',
    '207' : ':',
    '291' : "'",
    '264' : '"',
    '201' : '.',
    '243' : ';',
    '299' : ',',
    '296' : '`',
    '367' : '+',
    '321' : '-',
    '309' : '*',
    '372' : '=',
    '305' : '%',
    '355' : '^',
    '407' : '(',
    '412' : ')',
    '415' : '[',
    '456' : ']',
    '471' : '{',
    '462' : '}',
    '446' : '<',
    '409' : '>',
    '666' : ' ',
    '655' : '\n',
    '606' : '\t',
    '687' : '\r',
    '624' : '\b',
    '678' : '\a',
    '640' : '\v'
}

equivalent_crypto_dict = {
    '1': '743',
    '2': '745',
    '3': '747',
    '4': '749',
    '5': '750',
    '6': '753',
    '7': '757',
    '8': '762',
    '9': '771',
    '0': '780',
    'A': '101',
    'B': '102',
    'C': '105',
    'D': '107',
    'E': '112',
    'F': '124',
    'G': '110',
    'H': '120',
    'I': '109',
    'J': '114',
    'K': '115',
    'L': '137',
    'M': '154',
    'N': '181',
    'O': '173',
    'P': '192',
    'Q': '144',
    'R': '132',
    'S': '157',
    'T': '161',
    'U': '199',
    'V': '149',
    'W': '175',
    'X': '196',
    'Y': '159',
    'Z': '103',
    'a': '501',
    'b': '502',
    'c': '505',
    'd': '507',
    'e': '512',
    'f': '524',
    'g': '510',
    'h': '520',
    'i': '509',
    'j': '514',
    'k': '515',
    'l': '537',
    'm': '554',
    'n': '581',
    'o': '573',
    'p': '592',
    'q': '544',
    'r': '532',
    's': '557',
    't': '561',
    'u': '599',
    'v': '549',
    'w': '575',
    'x': '596',
    'y': '559',
    'z': '503',
    '!': '251',
    '?': '262',
    '@': '273',
    '$': '263',
    '/': '256',
    '_': '241',
    '#': '206',
    ':': '207',
    "'": '291',
    '"': '264',
    '.': '201',
    ';': '243',
    ',': '299',
    '`': '296',
    '+': '367',
    '-': '321',
    '*': '309',
    '=': '372',
    '%': '305',
    '^': '355',
    '(': '407',
    ')': '412',
    '[': '415',
    ']': '456',
    '{': '471',
    '}': '462',
    '<': '446',
    '>': '409',
    ' ': '666',
    '\n': '655',
    '\t': '606',
    '\r': '687'
    }


class CryptoGraphy:
    def __init__(self):
        self.cdict = equivalent_crypto_dict
        self.tdict = equivalent_text_dict
        
        
    def textTocrypto(self, text):
        crypto_text = ''
        crypto_key1 = rd.randint(0, 7)
        crypto_key2_doter = rd.randint(1, 5)
        crypto_key2_starter = rd.randint(100, 151)
        crypto_key2_end = rd.randint(crypto_key2_starter, 301)
        crypto_key2 = (crypto_key2_starter + crypto_key2_end) // 2
        crypto_key2_end = crypto_key2_end * crypto_key2_doter
        crypto_text = f'{crypto_key1}{crypto_key2_doter}{crypto_key2_starter}{crypto_key2_end}'
        
        key = crypto_key2-crypto_key1
        for i in text:
            key_pluse = str(int(self.cdict[i]) + key)
            crypto_text = f'{crypto_text}{key_pluse}'
        
        return crypto_text
    
    def cryptoTotext(self, crypto):
        text = ''
        crypto_key = crypto[0:8]
        
        crypto_key1 = int(crypto[0])
        
        crypto_key2_doter = int(crypto[1])
        crypto_key2_starter = int(crypto[2:5])
        crypto_key2_end = int(crypto[5:8])
        crypto_key2_end = crypto_key2_end // crypto_key2_doter
        crypto_key2 = (crypto_key2_starter + crypto_key2_end) // 2
        
        key = crypto_key2-crypto_key1
        crypto = crypto[8:]
        cryptolen = len(crypto)//3
        
        for i in range(1, cryptolen+1):
            ne = 3*i
            n1 = ne - 3
            
            crypt = str(int(crypto[n1:ne]) - key)
            convert = self.tdict[crypt]
            text = f'{text}{convert}'
            
        return text    