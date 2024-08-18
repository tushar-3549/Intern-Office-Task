'''
import pandas as pd
df = pd.read_csv("all_subtypes.csv")
# print(df)

def check_dup(sub_type):
    if isinstance(sub_type, str):
        words = [word.strip() for word in sub_type.split(',')]
        print(words)
        length = int(len(words))
        print(length)
        # l = len(set(words))
        # print(l)
        
        # int(len(words) != len(set(words))) 
        # 1 -> duplicate, 0 -> not duplicate 
    else:
        return 0
df['status'] = df['sub_type'].apply(check_dup)
print(df['status'])
'''
# Step 1:
'''
import pandas as pd

df = pd.read_csv("all_subtypes.csv")
print(df)

def check_dup(sub_type):
    if isinstance(sub_type, str):
        words = [word.strip() for word in sub_type.split(',')]
        return int(len(words) != len(set(words)))
    else:
        return 0

df['status'] = df['sub_type'].apply(check_dup)
df.to_csv("check_allSubTypes.csv", index=False)

print("Successful")
'''
# Step 2:
'''
import pandas as pd
df = pd.read_csv('check_allSubTypes.csv')
# print(df)
def remove_dup(sub_type):
    if isinstance(sub_type, str):
        words = [word.strip() for word in sub_type.split(',')]
        # print(words)
        uni_word = set(words)
        # print(uni_word)
        # return uni_word
        return ", ".join(uni_word)
    else:
        return sub_type
df['remove_duplicate'] = df['sub_type'].apply(remove_dup)
# print(df['remove_duplicate'])
df.to_csv("remove_dup_allSubtypes.csv", index=False)
print("Done")
'''

# Step 3:
'''
import pandas as pd
df = pd.read_csv("remove_dup_allSubtypes.csv")
# print(df)
# print(df['remove_duplicate'])
def up_low_check(text):
    if isinstance(text, str):
        ans = [word.capitalize() for word in text.split()]
        # print(ans)
        return ' '.join(ans)
    else:
        return text
df['correct'] = df['remove_duplicate'].apply(up_low_check)
# print(df['correct'])
df.to_csv("updated_allSubtypes.csv", index=False)
print("Done")
'''

# Step 4:
import pandas as pd
df = pd.read_csv('up_allsubtypes.csv')
# print(df['correct'])
def to_sort(text):
    if isinstance(text, str):
        words = [word.strip() for word in text.split(', ')]
        words.sort()
        return ", ".join(words)
    else:
        return text
df['after_sort'] = df['correct'].apply(to_sort)
# print(df['after_sort'])
df.to_csv("sort_allsubtypes.csv", index=False)
print("Done")


    
    



