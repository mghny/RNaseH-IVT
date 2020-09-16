#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

n = 600

# raw_rna = """
# AGGGCCACAUCCCACUGCCA
# """.strip()

raw_rna = """
CGUCACCCUCCUCAAGUAUACUUCAAAGGACAUUUAACUAAAACCCCUACGCAUUUAUAUAGAGGAGACAAGUCG
""".strip()

seq_rna = Seq(raw_rna, IUPAC.unambiguous_rna)
seq_dna = seq_rna.back_transcribe()

A = "taatacgactcactatagggaga"
E = ""
B = seq_dna[-8:]
D = seq_dna[0:4]
C = Seq('')

# parts = [A, B, C, D, E]
# template = sum(parts, Seq(""))
template = Seq("")

while (len(template) + len(seq_dna) <= n):
    C += seq_dna
    # parts = [A, B, C, D, E]
    # template = sum(parts, Seq(""))
    template = sum([A, B, C, D, E], Seq(""))

print("DNA Template (5' - 3'):")
# print(len(template))
print(template.upper())
print()

# Cleavage Guide
# prime5Flank = D.complement().transcribe()[::-1]
prime5Flank = D.reverse_complement().transcribe()
# center = B[4:].complement()[::-1]
center = B[4:].reverse_complement()
# prime3Flank = B[:4].complement().transcribe()[::-1]
prime3Flank = B[:4].reverse_complement().transcribe()

print("Cleavage Guide (5' - 3'):")
print(' '.join(["m" + nt for nt in prime5Flank]))
print(' '.join(center.lower()))
print(' '.join(["m" + nt for nt in prime3Flank]))
print()

# print(D.complement().transcribe()[::-1])
# print(D.reverse_complement().transcribe())
# print()

# print(B[4:].complement()[::-1])
# print(B[4:].reverse_complement())
# print()

# print(B[:4].complement().transcribe()[::-1])
# print(B[:4].reverse_complement().transcribe())

# if __name__ == "__main__":
  # dna_template = construct_dna_template()
  # cleavage_guide = construct_cleavage_guide()
  #
  # print("DNA Template (5' - 3'):")
  # print(dna_template)
  # print()
  # print("Cleavage Guide (5' - 3'):")
  # print(cleavage_guide)
  # print()

