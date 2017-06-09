# Generate string permutations with no repetitions or mirrors of the same string (if ab then not ba)

perms = set()
def generate_perms(str):
    generate_perms_helper("", str)

def generate_perms_helper(prefix, str):
    if str is "":
        if prefix[::-1] not in perms:
            perms.add(prefix)
        return
    
    for i in range(0, len(str)):
        generate_perms_helper(prefix + str[i], str[:i] + str[i+1:])


generate_perms("abc")

for i in perms:
    print(i)