preklad = open("f200_20003_eubergesetzt_de_sk - 7618.txt", "r", encoding="utf-8")
original = open("f200_20003_de_sk - kópia.xlf", "r", encoding="utf-8")
loaded = open("f200_20003_de_sk - loaded.xlf", "w", encoding="utf-8")

lines = preklad.readlines()

vals = []
dict = {}

for i in range(len(lines)): 
    line = lines[i].strip()
    if line != "":
        vals.append(line)

for i in range(0, len(vals) - 1, 2):
    if not vals[i] in dict.keys():
        dict[vals[i]] = vals[i+1]
    else:
        print(f"String {vals[i]} is already present in dict.keys()!")

lines = original.readlines()

for i in range(1, len(lines)):
    if lines[i].startswith(('<target>', "</target>")):
        l = lines[i].strip()[8:-9]
        l = l.lstrip()
        if l in dict.keys():
            print(f"Writing translation: [{l}]  -->  [{dict[l]}]")
            lines[i] = f"<target>{dict[l]}</target>\n"
            
        else:
            print(f"Translation for {l} not in dictionary, skipping...")

print("\nFinished :)")
loaded.writelines(lines)