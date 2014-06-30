import re

def checkRegex():
    try:
        pattern = re.compile(raw_input('The regex pattern : '))
        return pattern
    except re.error:
        print('non-valid regex, try again')
        checkRegex()
    
def executeRegex():
    text = raw_input('Your text : ')
    pattern = checkRegex()
    catch = re.search(pattern,text)
    if catch is None:
        return 'No match has been found'
    else:
        return catch.group()

if __name__ == '__main__':
    print(executeRegex())

