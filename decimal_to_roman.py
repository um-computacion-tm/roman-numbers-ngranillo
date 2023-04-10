def decimal_to_roman(decimal):
    roman = ""
    if decimal == 1000:
        roman = "M"
        decimal -= 1000
    if decimal >= 100:
        centesima = decimal // 100
        decimal -= 100 * centesima
        if centesima <= 3:
            roman += "C" * centesima
        elif centesima == 4:
            roman += "CD"
        elif centesima == 5:
            roman += "D"
        elif 8 >= centesima >= 6:
            I = centesima - 5
            roman += "D" + ("C" * I)
        elif centesima == 9:
            roman += "CM"
    if decimal >= 10:
        decena = decimal // 10
        decimal -= 10 * decena
        if decena <= 3:
            roman += "X" * decena
        elif decena == 4:
            roman += "XL"
        elif decena == 5:
            roman += "L"
        elif 8 >= decena >= 6:
            I = decena - 5
            roman += "L" + ("X" * I)
        elif decena == 9:
            roman += "XC"
    if decimal <= 3:
        roman += "I" * decimal
    elif decimal == 4:
        roman += "IV"
    elif decimal == 5:
        roman += "V"
    elif 8 >= decimal >= 6:
        I = decimal - 5
        roman += "V" + ("I" * I)
    elif decimal == 9:
        roman += "IX"

    return roman

