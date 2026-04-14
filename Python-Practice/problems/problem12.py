#wapp to fill in a etter template given below with name and date
# letter = '''
#        Dear <|NAME|>,
#        You are selected!
#        <|Date|>
#        '''

letter = '''
       Dear <|NAME|>,
       You are selected!
       <|Date|>
       '''


print(letter.replace("<|NAME|>", "Harry").replace("<|Date|>", "14th April 2026"))