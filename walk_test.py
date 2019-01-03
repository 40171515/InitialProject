
# edit made within second branch

import os
for root, dirs, files in os.walk("/home/patch_of_scotland/Documents/Code/PyCharmProjects/MiG_based_prototype/auld_lang_syne", topdown=False):
    for name in files:
        print(os.path.join(root, name))

print('')

for root, dirs, files in os.walk("/home/patch_of_scotland/Documents/Code/PyCharmProjects/MiG_based_prototype/auld_lang_syne", topdown=False):
    for name in files:
        print(os.path.join(root, name))

# edit made within second branch