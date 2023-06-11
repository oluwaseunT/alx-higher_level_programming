#!/usr/bin/python3
'''
Displays the body response of a URL
'''
if __name__ == '__main__':
    import sys
    import urllib.request
    
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(f'Body response:')
        print(f'- type: {type(res.read())}')
        print(f'- content: {res.read()}')
        print(f'- utf8 content: {res.read().decode("utf-8")}')

