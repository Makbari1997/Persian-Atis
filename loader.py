import os

def format1_loader(path:str):
    """
    This function is to load the Format 1 of ATIS dataset

    Args:
    --------
    path : str - path to the .txt file

    Returns:
    --------
    (sentences, slots, intents)
    """
    sentences, slots, intents = [], [], []

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        _slots, _sentences = [], []
        for line in lines:
            _line = line.split(',')
            if _line[0] == '#BOS':
                intents.append(_line[-1].split()[0])
            elif _line[0] == '#EOS':
                slots.append(_slots)
                sentences.append(_sentences)
                _slots, _sentences = [], []
            else:
                _sentences.append(_line[0])
                _slots.append(_line[1].split()[0])
    return sentences, slots, intents

def format2_loader(path:str):
    """
    This function is to load the Format 2 of ATIS dataset
    
    Args:
    ---------
    path : str - path to the folder that contains label, seq.in, and seq.out files

    Returns:
    --------
    (sentences, slots, intents)
    """
    sentences, slots, intents = [], [], []
    
    with open(os.path.join(path, 'label'), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            intents.append(line.split()[0])
    
    with open(os.path.join(path, 'seq.in'), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            sentences.append(line.split())
    
    with open(os.path.join(path, 'seq.out'), 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            slots.append(line.split())
    
    return sentences, slots, intents
    
    