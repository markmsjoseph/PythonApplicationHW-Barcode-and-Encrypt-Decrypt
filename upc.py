# mark joseph
"""
upc.py
=====
Implement the following two functions as specified in the docstrings:

1. generate_bar_widths(s)
2. valid_barcode(s)

Some resources that may help with your implementation:

* https://en.wikipedia.org/wiki/Universal_Product_Code#Encoding
* http://electronics.howstuffworks.com/gadgets/high-tech-gadgets/upc3.htm
* http://www.adams1.com/upccode.html

"""
def generate_bar_widths(s):
    barcode ="111"
    for ch in s:
        if (len(barcode) == 27):
            barcode = barcode + "11111"

        if (ch == "0"):
            barcode = barcode + "3211"
        if (ch == "1"):
            barcode = barcode + "2221"
        if (ch == "2"):
            barcode = barcode + "2122"
        if (ch == "3"):
            barcode = barcode + "1411"
        if (ch == "4"):
            barcode = barcode + "1132"
        if (ch == "5"):
            barcode = barcode + "1231"
        if (ch == "6"):
            barcode = barcode + "1114"
        if (ch == "7"):
            barcode = barcode + "1312"
        if (ch == "8"):
            barcode = barcode + "1213"
        if (ch == "9"):
            barcode = barcode + "3112"

        if(len(barcode)==56):
            barcode = barcode + "111"
            break

    return barcode

def valid_barcode(s):
    """Determines whether a barcode is valid or not based on length and
    the check digit. A "UPC-A" barcode consists of 12 digits, with the
    last digit being the check digit. Some examples:

    valid_barcode('036000291452') # --> True
    valid_barcode('036000291450') # --> False
    valid_barcode('075678164125') # --> True
    valid_barcode('')            # --> False

    :param s: barcode number
    :type s: str
    :return: true if the barcode is valid, false otherwise
    :rtype: bool
    """
    #check for length of barcode
    if(len(s) != 12):
        return False
    #put stuff in an index so mod can be calculated easier
    barcode = []
    for ch in s:
        barcode.append(ch)

    odds = 0
    #do calculations from wikipedia page about checkdigit
    #chedk odd indexes
    for i in range(len(barcode)):
        if i%2 == 0:
            odds = odds + int(barcode[i])
    odds = odds*3

    #check even indexes
    for i in range(len(barcode)-1):
        if i%2 == 1:
            odds = odds + int(barcode[i])

    mod = odds%10

    checkDigit = 10 - mod

    if(int(s[11]) == checkDigit):
        return True
    else:
        return False

if __name__ == '__main__':
    print(generate_bar_widths("684730294856"))
    print(valid_barcode(""))