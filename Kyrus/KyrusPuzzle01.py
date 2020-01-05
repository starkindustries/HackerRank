import requests
import re
import timeit
import hashlib


def decrypteMD5Hash(hashValue):
    url = "https://hashtoolkit.com/reverse-hash/?hash=" + hashValue

    responseText = requests.get(url).text
    try:
        decryptedSpan = re.search('<span title="decrypted md5 hash">.*<\/span>', responseText).group(0)
        # remove the html tags
        finalValue = decryptedSpan[33:-7]
        return finalValue
    except AttributeError:
        pass

    return '[no match]'


if __name__ == "__main__":
    # lines for testing
    # lines = [
    #     "d41d8cd98f00b204e9800998ecf8427e",
    #     "61e9c06ea9a85a5088a499df6458d276",
    #     "0cde1252d73b5bb4352e9287f281cca4",
    #     "4ee972120bcda675f75222c87cb9d356",
    # ]

    filename = 'KyrusPuzzle01_input.txt'
    lines = []
    with open(filename, 'r') as fileHandle:
        for line in fileHandle:
            lines.append(line.strip())

    # startingLine = 12561
    # outputFile = open('KyrusPuzzle01_output.txt', 'a')
    # for i in range(startingLine, len(lines)):
    #     start = timeit.default_timer()
    #     hashValue = lines[i]
    #     result = decrypteMD5Hash(hashValue)
    #     if result != "[no match]":
    #         print(f"{i}: [{hashValue} : {result}]")
    #     print(f"{hashValue}: {result}", file=outputFile)
    #     stop = timeit.default_timer()
    #     print(f"{i}, time: {stop - start}")
    # outputFile.close()

    # https://www.rapidtables.com/convert/number/hex-to-ascii.html
    # hexString = "57686f2064657369676e656420626f74682052433520616e64204d44353f0a"
    # The above hex string is ASCII for "Who designed both RC5 and MD5?"
    # print(f"{len(hexString)}")

    m = hashlib.md5()
    # m.update(b"Who designed both RC5 and MD5?")
    # m.update(b"$HEX[57686f2064657369676e656420626f74682052433520616e64204d44353f0a]")

    s1 = "Rivest"
    # s2 = "Who designed both RC5 and MD5?"
    s1 = s1
    m.update(s1.encode())
    digest = m.hexdigest()
    print(f"digest {digest} exists: {digest in lines}")
