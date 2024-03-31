# Write a function to convert numbers to text numerals

def text_numeral(num):
    """ Converts numbers to its respective work form """
    
    NUM_WORDS = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    
    num_str = str(num)
    num = num_str.replace('(', '')
    num = num.replace(')', '')
    num = num.replace('.', '')
    num = int(num)
    
    valid = True
    x = 0
    
    if 90 < num < 100:
        x = num - 90
        num = 90
    elif 80 < num < 90:
        x = num - 80
        num = 80
    elif 70 < num < 80:
        x = num - 70 
    elif 60 < num < 70:
        x = num - 60
        num = 60
    elif 50 < num < 60:
        x = num - 50
        num = 50
    elif 40 < num < 50:
        x = num - 40
        num = 40
    elif 30 < num < 40:
        x = num - 30
        num = 30
    elif 20 < num < 30:
        x = num - 20 
        num = 20
    if valid and  x != 0: 
        return (NUM_WORDS[num] + ' ' + NUM_WORDS[x])
    else:
        return (NUM_WORDS[num])
            


    
        
