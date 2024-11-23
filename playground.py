from time import perf_counter_ns

#### loops --> repeat certain action ??
print('n' in 'nohA')
name = "Abdelkader"
# get brief version of it ?? --> remove char [a,e,i,o,u]
# generate brief version --> new place --> to the chars
briefname= ""
for char in name:
    print(f"char = {char}")
    if not(char in 'aeiou'):
        briefname += char

print(briefname)


################# ?





