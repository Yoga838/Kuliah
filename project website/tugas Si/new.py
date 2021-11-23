unsort_list = ['Goliath', 'Oligoxystre', 'Cobalt', 'Chilean', 'Aphonopelma', 'Grammostola','Chromatopelma', 'Avicularia', 'Brachypelma', 'Psalmopoeus']

sort_list = []

# while unsort_list:
#     smallest = min(unsort_list)
#     sort_list.append(smallest)
#     unsort_list.pop(unsort_list.index(smallest))

for i in range(len(unsort_list)):
    smallest = min(unsort_list)
    sort_list.append(smallest)
    # unsort_list.pop(unsort_list.index(smallest))

print (sort_list)

# for i in range (len(unsort_list)):
#     for j in range (i+1, len(unsort_list)):
#         if len(unsort_list[i])> len(unsort_list[j]):
#             unsort_list[i], unsort_list[j] = unsort_list[j], unsort_list[i]
# print (unsort_list)
