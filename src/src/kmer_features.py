from collections import Counter


def get_kmers(sequence, k=3):
    """
    Extract overlapping k-mers from a DNA sequence.
    """
    return [
        sequence[i:i+k]
        for i in range(len(sequence) - k + 1)
    ]


def kmer_frequency(sequence, k=3):
    """
    Count the frequency of each k-mer in a DNA sequence.
    """
    kmers = get_kmers(sequence, k)
    return Counter(kmers)
