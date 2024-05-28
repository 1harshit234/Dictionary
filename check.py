sample_dict = {'a': 100, 'b': 200, 'c': 300}
for i in sample_dict:
    y = sample_dict[i]
    if y == 200:
        print("it is present")
    else:
        print("it is not present")

#jaha per direct values use nhi ho patah hai waha per yeh use hota ahi jaha hamne direct values() likeh dete hai
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in a dict')