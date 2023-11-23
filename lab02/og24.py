sample_dict = {}
num=int(input("Enter the dictionary list size"))
for i in range(num):
    name = input("Enter dictionary name: ")
    size = input("Enter dictionary size: ")

    sample_dict[name] = size


sorted_dict_keys_asc = dict(sorted(sample_dict.items()))
print("Ascending order:", sorted_dict_keys_asc)

sorted_dict_keys_desc = dict(sorted(sample_dict.items(), reverse=True))
print("Descending order:", sorted_dict_keys_desc)
