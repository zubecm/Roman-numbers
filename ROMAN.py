class RomanNumerals:

    def to_roman(val):
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thous = ["", "M", "MM", "MMM", "MMMM"]

        t = thous[val // 1000]
        h = hunds[val // 100 % 10]
        te = tens[val // 10 % 10]
        o = ones[val % 10]
        return t + h + te + o

    def from_roman(roman):
        sum = 0
        a = 10000
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in roman:
            if dic[i] > a:
                a = -2 * a
                sum = dic[i] + sum + a
                a = dic[i]
            else:
                sum = dic[i] + sum
                a = dic[i]
        return sum