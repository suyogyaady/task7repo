list = [23,45,18,90]

new_list = set(list)
new_list.remove(max(new_list))
new_list.remove(max(new_list))

a=max(new_list)


print("third highest number is :",a)
