# Method 1:

import keyword


def keyword_list():
    word=input("Enter any word: ")
    kw_list=keyword.kwlist
    if word in kw_list:
        return "Yes"
    else: 
        return "No"

    
print(keyword_list())

def again():
    again()