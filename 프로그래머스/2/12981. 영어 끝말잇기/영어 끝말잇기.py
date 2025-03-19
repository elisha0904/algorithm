def check_wrong(w1:str, w2:str):
    if w1[-1] == w2[0]:
        return True
    else:
        return False

def solution(n, words):
    unique = []
    
    for i, word in enumerate(words):

        if i == 0:
            unique.append(word)
        elif check_wrong(words[i-1], words[i]) and word not in unique:
            unique.append(word)
        else:
            ord, idx = divmod(i, n)
            return [idx+1, ord+1]
                
    return [0, 0]