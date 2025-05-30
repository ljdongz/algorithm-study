

def solution(phone_book):

    dict = {}
    
    for phone in sorted(phone_book):
        for i in range(len(phone)):
            if phone[:(i+1)] in dict:
                return False
        dict[phone] = True
        
    return True
                

