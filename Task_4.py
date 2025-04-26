def wordreversal(): #declared function
    word = str(input("Enter a word to reverse: ")) #user input
    reverse_word = " " #give word to be reversed 
    for i in word: #make a loop for reversing word
        reverse_word = i + reverse_word #add each character in reverse
    print(reverse_word) 
wordreversal() #call function