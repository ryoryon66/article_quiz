import spacy
import difflib
nlp = spacy.load("en_core_web_lg")



def make_quiz(original_doc:str) -> str:
    original_doc = original_doc
    doc = nlp(original_doc)
    print(doc.noun_chunks)

    #今どこまでの文字を見ているか。
    next_index = 0
    for chunk in doc.noun_chunks:
        chunk_before = str(chunk)
        chunk_after = ' (Q) '+str(chunk)

        print(chunk,chunk[0].pos_)

        if chunk[0].pos_ in ['PRON']:
            next_index = next_index + len(str(chunk))
            continue

        
        if str(chunk[0]) in ['The','the','A','a','An','an']:
            chunk_after = ' (Q) '+str(chunk[1:])
        elif chunk[0].pos_ in ['DET']:
            continue



        left_index = original_doc[next_index:].find(chunk_before)
        right_index = left_index + len(chunk_before)

        original_doc = original_doc[:next_index + left_index] + chunk_after + original_doc[next_index + right_index:]
        next_index = next_index + left_index + len(str(chunk_after))

        print(original_doc)



    
    return original_doc


def print_diff_hl(ground_truth, target):
    """
    文字列の差異をハイライト表示する
    """
    color_dic = {
        'red':'\033[31m',
        'yellow':'\033[43m',  
        'end':'\033[0m'
    }

    d = difflib.Differ()
    diffs = d.compare(ground_truth, target)

    result = ''
    for diff in diffs:
        status, _, character = list(diff)
        if status == '-':
            character = color_dic['red'] + character + color_dic['end']
        elif status == '+':
            character = color_dic['yellow'] + character + color_dic['end']
        else:
            pass
        result += character

    print(f"ground truth : {ground_truth}")
    print(f"target string: {target}")
    print(f"diff result  : {result}")



print_diff_hl('aaa','aba')


if __name__ == "__main__":
    document = """We created our Travel Restrictions Today visualization to look at the latest global news and determine travel bans, lockdowns, and border closures. We found datasets already cleaned and classified but they were either limited or not free of charge. So, we decided to start with the Humanitarian Data Exchange's COVID-19 Global Travel Restrictions and Airline Information dataset and create our own dataset.
"""

s = input()
if s:
    document = s
print(make_quiz(document))



print_diff_hl(document,make_quiz(document))
