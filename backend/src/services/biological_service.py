# backend/src/services/biological_service.py

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def transcribe_dna_to_rna(dna_sequence):
    dna = Seq(dna_sequence, IUPAC.unambiguous_dna)
    rna = dna.transcribe()
    return str(rna)
