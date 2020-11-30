import random

#secret_santa = {'Alexi': '', 'Rene': '', 'Sabrina': '', 'Philippe': '', 'Erin': '', 'Dario': '', 'Papi': '', 'Ela': ''}
secret_santa = {'Alexi': '', 'Rene': '', 'Sabrina': '', 'Philippe': '', 'Erin': '', 'Dario': '', 'Ela': ''}

def secretsanta():
    global secret_santa
    #pool = ['Alexi', 'Rene', 'Sabrina', 'Philippe', 'Erin', 'Dario', 'Papi', 'Ela']
    pool = ['Alexi', 'Rene', 'Sabrina', 'Philippe', 'Erin', 'Dario', 'Ela']

    success = False

    while(not success):
        mismatch = False
        random.shuffle(pool)
        randomized = pool
        print(randomized)

        if (randomized[0] == 'Alexi' or randomized[0] == 'Ela'):
            mismatch = True
            continue
        
        if (randomized[1] == 'Rene' or randomized[1] == 'Ela'):
            mismatch = True
            continue

        if (randomized[2] == 'Sabrina' or randomized[2] == 'Philippe'):
            mismatch = True
            continue

        if (randomized[3] == 'Sabrina' or randomized[3] == 'Philippe'):
            mismatch = True
            continue

        if (randomized[4] == 'Erin' or randomized[4] == 'Dario'):
            mismatch = True
            continue


        if (randomized[5] == 'Erin' or randomized[5] == 'Dario'):
            mismatch = True
            continue

        if (randomized[6] == 'Ela'):
            mismatch = True
            continue

      
        # if (randomized[7] == 'Papi' or randomized[7] == 'Ela'):
        #     print(8)
        #     mismatch = True
        #     continue


        if (not mismatch):
            secret_santa['Alexi'] = randomized[0]
            secret_santa['Rene'] = randomized[1]
            secret_santa['Sabrina'] = randomized[2]
            secret_santa['Philippe'] = randomized[3]
            secret_santa['Erin'] = randomized[4]
            secret_santa['Dario'] = randomized[5]
            #secret_santa['Papi'] = randomized[6]
            secret_santa['Ela'] = randomized[6]
            success = True
    
    print(secret_santa)

    for name in secret_santa:
        f = open("{}.rst".format(name), 'w')
        nameLen = len(name)
        underline = "="*nameLen
        recipient = secret_santa[name]
        rst_file = "{}\n{}\nYou will be the secret santa for: {}".format(name, underline, recipient)
        print(rst_file)
        f.write(rst_file)
        f.close()


secretsanta()
