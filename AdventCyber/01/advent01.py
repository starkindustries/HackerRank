import logging

logging.basicConfig(level=logging.INFO)

keypadChars = [
    " 0",  # define N7110_KEYPAD_ZERO_ABC_CHARS  " 0"
    ".,'?!\"1-()@/:",  # define N7110_KEYPAD_ONE_ABC_CHARS ".,'?!\"1-()@/:"
    "abc2",  # define N7110_KEYPAD_TWO_ABC_CHARS   "abc2"
    "def3",  # define N7110_KEYPAD_THREE_ABC_CHARS "def3"
    "ghi4",  # define N7110_KEYPAD_FOUR_ABC_CHARS  "ghi4"
    "jkl5",  # define N7110_KEYPAD_FIVE_ABC_CHARS  "jkl5"
    "mno6",  # define N7110_KEYPAD_SIX_ABC_CHARS   "mno6"
    "pqrs7",  # define N7110_KEYPAD_SEVEN_ABC_CHARS "pqrs7"
    "tuv8",  # define N7110_KEYPAD_EIGHT_ABC_CHARS "tuv8"
    "wxyz9",  # define N7110_KEYPAD_NINE_ABC_CHARS  "wxyz9"
    "@/:_;+&%*[]{}",  # define N7110_KEYPAD_STAR_ABC_CHARS  "@/:_;+&%*[]{}"
]  # define N7110_KEYPAD_HASH_CHARS N7110_IME_METHODS


# date: 1999-11-23 03:01:10
# to: 00611015550117
# text: rudolf where are you brrr
def convertT9toChar(keycode, count):
    if keycode >= len(keypadChars):
        logging.error(f"Error: keycode index [{keycode}] out of bounds.")
        return "#"
    if count >= len(keypadChars[keycode]):
        newCount = count % len(keypadChars[keycode])
        logging.info(f"Count [{count}] out of bounds for keycode [{keycode}]. New count: {newCount}. Char: {keypadChars[keycode][newCount]}")
        count = newCount
    return keypadChars[keycode][count]


def parseKeylog(lines):
    phoneNumberDigits = 14
    tapThreshold = 1000
    smsString = ""
    keycodeCount = 0
    lastKeycode = None
    lastTapTime = lines[0][0]
    for i in range(len(lines) - phoneNumberDigits):
        time, keycode = lines[i][0], lines[i][1]
        tapTime = time - lastTapTime
        if keycode > 10:
            logging.debug(f"keycode: {keycode}")
        elif lastKeycode is None:
            lastKeycode = keycode
            lastTapTime = time
        elif lastKeycode != keycode:
            smsString += convertT9toChar(lastKeycode, keycodeCount)
            lastKeycode = keycode
            keycodeCount = 0
        elif lastKeycode == keycode and tapTime > tapThreshold:
            smsString += convertT9toChar(keycode, keycodeCount)
            keycodeCount = 0
        elif lastKeycode == keycode:
            keycodeCount += 1
        else:
            logging.error(f"ERROR: unexpected keycode condition: {keycode}")
        logging.debug(f"raw time: {time}, key: {keycode}, time: {time - lastTapTime}, string: {smsString}")
        lastTapTime = time
    if keycodeCount > 0:
        smsString += convertT9toChar(keycode, keycodeCount)
    return smsString


def testParseKeylog(i):
    print("===================================")
    # Grab the decoded text message from the txt file
    sms = []
    textFile = f"sms{i}.txt"
    textMessage = None
    try:
        with open(textFile, 'r') as handle:
            for line in handle:
                sms.append(line)
        textMessage = sms[2][6:].strip()
    except FileNotFoundError:
        logging.info(f"File {textFile} not found.")

    # Parse the csv file
    lines = []
    with open(f"sms{i}.csv", 'r') as handle:
        for line in handle:
            lines.append([int(x) for x in line.strip().split(',')])
    logging.debug(lines)
    result = parseKeylog(lines)

    if result == textMessage:
        print(f"SUCCESS! {result}")
    else:
        print(f"Test failed")
        print(f"Expected: {textMessage}")
        print(f"  Result: {result}")


if __name__ == "__main__":
    for i in range(1, 5):
        testParseKeylog(i)
    # testParseKeylog(4)
