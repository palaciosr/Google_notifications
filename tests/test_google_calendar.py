import re 


def check_email_is_valid():

    email = 'palaciosr080@gmail.com'

    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if(re.search(regex,email)): 
        return True

    else:
        return False

assert check_email_is_valid() == True 

def check_cred_json():


    with open('credentials.json') as cred:

        if not cred:
            print("fail")
        else:

            print('pass')

            cred.close()
#need to check paths exists where google keys are being stored