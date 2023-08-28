l=["Hello", "World", "Sayan", 'Dhoni']
#vowel and consonant counter
vc=0
cc=0
for i in l:
    for j in i:
        if j in "aeiouAEIOU":
            vc+=1 #increment vowel count by 1 when a vowel is encountered.
        else:
            cc+=1 #increment consonant count by 1 when a consonat is eencountered.
print(f"vowel is {vc} and cosonant is {cc}")
