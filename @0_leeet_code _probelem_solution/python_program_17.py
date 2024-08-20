#17  to find flatten a nested list


def flatten(flatte):
    flatten_list=[]
    for nums in flatte:
        if isinstance(nums,list):
            flatten_list.extend(flatten(nums))
        else:
            flatten_list.append(nums)
    return flatten_list

print(flatten([3,2,[1,2]]))

                