###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiou"
vowel_count = 0
cnt=0

# Count vowels in the text
while(cnt < len(text)):
    if  text[cnt].lower() in vowels:
        vowel_count += 1
    cnt += 1
# for char in text:
#     if char in vowels:
#         vowel_count += 1

print(f"The number of vowels in the text is: {vowel_count}")
