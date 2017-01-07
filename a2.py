def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    if len(dna1) > len(dna2):
        return True
    else:
        return False
    


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    
    num_nuc = 0

    for char in dna:
        if char == nucleotide:
            num_nuc = num_nuc + 1

    return num_nuc


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    
    if dna2 in dna1 :
        return True
    else:
        return False


def is_valid_sequence(dna):
    """(str) -> bool

    Return True is and only if DNA sequence is valid.

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('aTCgcc')
    False
    
    """
    
    seq_num = 0

    for char in dna:
        if char not in "ATCG":
            seq_num = seq_num + 1

        if seq_num > 0:
            return False
        else:
            return True

def insert_sequence(dna1, dna2, index):
    """(str,str,int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    into the first DNA sequence at the given index.

    >>>insert_sequence('CGAT', 'AC', 2)
    'CGACAT'
    >>>insert_sequence('GGCC', 'TT', -1)
    'GGCTTC'
    """

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """(str) -> str

    Return the nucleotide's complement.

    >>> get_complement('A')
    'T'
    >>> get_complement('G')
    'C'
    >>> get_complement('r')
    'Not a nucleotide'
    """

    for char in nucleotide:
        if char in 'ACGT':
            if char == 'A':
                return 'T'
            if char == 'C':
                return 'G'
            if char == 'G':
                return 'C'
            if char == 'T':
                return 'A'
        else:
            return 'Not a nucleotide'


def get_complementary_sequence(dna):
    
    """(str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GA')
    'CT'
    >>> get_complementary_sequence('aa')
    'Not a nucleotide''Not a nucleotide'
    """

    for char in dna:
        if get_complement(dna[0]) and get_complement(dna[1]):
            return get_complement(dna[0]) + get_complement(dna[1])
       
        
    
