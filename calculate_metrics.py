# import...

def compute_precision(ref, candidate):
    """
    Same as Rouge-1 Precision.
    Compute the percentage of the words in the candidate summary 
    that are also present in the reference summary.

    Input:
        ref: String
        candidate: String

    Return: float
    
    Ignore non-words like <q>, \n, period, comma...

    Example:
    ref: the cat was under the bed
    candidate: the cat was found under the bed

    Result: 6/7=0.86
    """
    pass

def compute_recall(ref, candidate):
    """
    Same as Rouge-1 Recall, or simply Rouge-1.
    Compute the percentage of the words in the reference summary 
    that are also present in the candidate summary.

    Input:
        ref: String
        candidate: String

    Return: float
    
    Ignore non-words like <q>, \n, period, comma...

    Example:
    ref: the cat was under the bed
    candidate: the cat was found under the bed

    Result: 1.0
    """
    pass

def compute_f1(ref, candiate):
    recall = compute_recall(ref, candidate)
    precision = compute_precision(ref, candidate)
    return 2. * recall * precision / (recall + precision)

def compute_rouge2_precision(ref, candidate):
    """
    Compute the percentage of the 2-grams words in the candidate summary 
    that are also present in the reference summary.

    Input:
        ref: String
        candidate: String

    Return: float
    
    Ignore non-words like <q>, \n, period, comma...

    Example:
    ref: the cat was under the bed
    candidate: the cat was found under the bed

    Result: 0.67
    """
    pass

def compute_rouge2_recall(ref, candidate):
    """
    Compute the percentage of the 2-grams words in the reference summary 
    that are also present in the candidate summary.

    Input:
        ref: String
        candidate: String

    Return: float
    
    Ignore non-words like <q>, \n, period, comma...

    Example:
    ref: the cat was under the bed
    candidate: the cat was found under the bed

    Result: 0.8
    """
    pass

def compute_rouge2_f1(ref, candiate):
    recall = compute_rouge2_recall(ref, candidate)
    precision = compute_rouge2_precision(ref, candidate)
    return 2. * recall * precision / (recall + precision)
