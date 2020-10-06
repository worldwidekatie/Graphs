# Print out all of the strings in the following array in alphabetical order, each on a separate line.
strings = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
'Cha Cha'
'Foxtrot'
'Jive'
'Paso Doble'
'Rumba'
'Samba'
'Tango'
'Viennese Waltz'
'Waltz'
# You may use whatever programming language you'd like.
#Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

strings.sort()
for i in strings:
    print(i)


"""Stretch Goal"""
# Print out all of the strings in the following array in alphabetical order s
# orted by the middle letter of each string, each on a separate line. 
# If the word has an even number of letters, choose the later letter, 
# i.e. the one closer to the end of the string.
strings = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
#The expected output is:
'Cha Cha'
'Paso Doble'
'Viennese Waltz'
'Waltz'
'Samba'
'Rumba'
'Tango'
'Foxtrot'
'Jive'
#You may use whatever programming language you'd like.
#Verbalize your thought process as much as possible before writing any code. 
# Run through the UPER problem solving framework while going through your thought process.