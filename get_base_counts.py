import pandas as pd

dna = "TCTCGATCGACACATGTGGGGATCATCATCGTGATGCTTA"

# To create counts of individual bases in a sequence
# This function does not take into account any bad inputs--bases other than A, T, C, and G.
def get_base_counts(dna):
    counts = {}
    for base in dna:
        if base in counts:
            counts[base] += 1
        else:
            counts[base] = 1
    return counts
print("Sequence: ",dna,'\n',get_base_counts(dna))


