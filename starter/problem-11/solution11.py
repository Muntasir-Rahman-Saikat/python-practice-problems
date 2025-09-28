rhyme = 'Twinkle, twinkle, little stars. How I wonder what you are!'

repeat=[]
previous_count=0
max_count=0
max_index=0
rhyme=rhyme.replace(" ","").lower()

for first in range(len(rhyme)):
    if rhyme[first] in repeat: #this is used to stop repeation in loop
        continue

    count = 0
    for second in range(first+1,len(rhyme)):
        if rhyme[first]==rhyme[second]:
            count+=1
            if count>max_count:
                max_count=count
                max_index=first
        # else:
        #     print(f"{rhyme[first]} is not equal to {rhyme[second]}")
    repeat.append(rhyme[first])
print("most frequent character is",rhyme[max_index],max_count+1)
