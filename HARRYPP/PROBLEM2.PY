letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>
'''

print(letter.replace("<|NAME|>", "krishan").replace("<|DATE|>", "12/12/2024"))