user_words = 'is it going to be cold weather today'.split(' ')
faq_question = 'what day is it today'.split(' ')

intersect = [] #in both
union = [] #in either

for uw in user_words:
    if uw in faq_question and uw not in intersect:
        #no duplicates
        intersect.append(uw)
    if uw not in union:
        union.append(uw)

for word in faq_question:
    if word not in union:
        union.append(word)

print(intersect)
print(union)
score = len(intersect)/len(union)

print("Score is {:.2f}".format(score))