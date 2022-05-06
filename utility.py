from multiprocessing.connection import answer_challenge
import spacy
import difflib
nlp = spacy.load("en_core_web_lg")



def make_quiz(original_doc:str) -> str:
    answer_key : dict[int,str] = dict()
    doc = nlp(original_doc)
    print(doc.noun_chunks)

    problem_num = 1

    #今どこまでの文字を見ているか。
    next_index = 0
    for chunk in doc.noun_chunks:
        chunk_before = str(chunk)
        chunk_after = f' (Q{problem_num}) '+str(chunk)

        print(chunk,chunk[0].pos_)

        if chunk[0].pos_ in ['PRON']:
            next_index = next_index + len(str(chunk))
            continue

        
        if str(chunk[0]) in ['The','the','A','a','An','an']:
            chunk_after = f' (Q{problem_num}) '+str(chunk[1:])
        elif str(chunk[0]) in ["All","all","Both","both"]:
            chunk_after = str(chunk[0]) + f' (Q{problem_num}) '+str(chunk[1:])
        elif chunk[0].pos_ in ['DET']:
            continue



        left_index = original_doc[next_index:].find(chunk_before)
        right_index = left_index + len(chunk_before)

        original_doc = original_doc[:next_index + left_index] + chunk_after + original_doc[next_index + right_index:]
        next_index = next_index + left_index + len(str(chunk_after))

        print(original_doc)
        problem_num += 1



    
    return original_doc



if __name__ == "__main__":
    document = """We created our Travel Restrictions Today visualization to look at the latest global news and determine travel bans, lockdowns, and border closures. We found datasets already cleaned and classified but they were either limited or not free of charge. So, we decided to start with the Humanitarian Data Exchange's COVID-19 Global Travel Restrictions and Airline Information dataset and create our own dataset.
"""

    s = input()
    if s:
        document = s
    print(make_quiz(document))

    




