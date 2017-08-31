# coding=utf8

class MaxLengthSubString:
    def __init__(self):
        self.substring = ''



# 获取最长子串
'''
    usage:
        substring = MaxLengthSubString()
        getMaxLengthSubStringBetween(0,0,str1, str2, 0,0,0, substring)
    :result
        substring.substring
'''
def getMaxLengthSubStringBetween(index1, index2, str1, str2, samelength, strbegin=0, strend=0, maxlength=MaxLengthSubString()):
    print index1, index2,str1, str2, strbegin, strend, samelength, maxlength.substring
    if index1 >= len(str1) or index2 >= len(str2):
        return samelength

    if strend-strbegin == samelength and len(maxlength.substring) < samelength:
        maxlength.substring = str1[strbegin:strend]

    if str1[index1] == str2[index2]:
        samelength += 1
        index1 += 1
        index2 += 1
        return getMaxLengthSubStringBetween(index1, index2, str1, str2, samelength,
                                            index1-samelength, index1, maxlength)
    else:

        return max(
            samelength,
            getMaxLengthSubStringBetween(index1+1, index2, str1, str2, 0,
                                         min(index1+1, index2+1), min(index1+1,index2+1), maxlength),
            getMaxLengthSubStringBetween(index1, index2+1, str1, str2, 0,
                                         min(index1,index2+1), min(index1,index2+1), maxlength),
        )


def test_getMaxLengthSubStringBetween():
    str1 = '12345667777'
    str2 = '12345664777'

    substring = MaxLengthSubString()

    print getMaxLengthSubStringBetween(0,0,str1, str2, 0, 0, 0, substring)
    print substring.substring




def main():
    test_getMaxLengthSubStringBetween()



if __name__ == '__main__':
    main()