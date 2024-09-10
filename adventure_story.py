# Ethan Lawrence
# september 10, 2024
# f-String Adventure Story

'''
Directions:

1. Update the comment block at the top of this script.

2. Use the Python `input( )` function to prompt (ask) the user for three pieces of information:

     - the hero's first name
     - the setting of the story (e.g., forest, desert, cave system)
     - the object the hero finds while on his/her adventure

3. Assign each piece of information collected to a variable with a short, specific name.

4. Declare (create) a variable named `story` and assign to it the `f-string` that is your adventure story

5. Use the `print( )` function to display your adventure story on the screen.

6. Execute (run) your script in Visual Studio Code and correct any errors.
'''

firstName = input('What is the hero\'s name? example: Dax \n')
setting = input('What is the setting of this story? example: the kingdom of newest york\n')
gameObject = input('What will the hero find on their journey? example: a mysterous purple cube with anchent engravings\n')

story = (f'{firstName} Is a hero of great legend. in their time of adventuring they retreved {gameObject} from a extrodenarily dangerous {setting}. they then used the {gameObject} to defeat the great evil and banish them from {setting} freeing it\'s people from peril.')
print(story)