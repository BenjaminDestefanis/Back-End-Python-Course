# word-replacement. El programa se encarga de reemplazar los valores que le digamos por los valores que le pasemos.
# el string que sera alterado sera la sentencia

sentece = input('Enter your sentence please:')
print('your sentence is: ' + sentece)

word1 = input('Enter word to replace: ')
word2 = input('Enter the word to replace it with: ')

print(sentece.replace(word1, word2))