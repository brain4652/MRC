def add_stopwords(filename:str,input:str):
    
    fileName = filename     

    with open(fileName, 'r') as f:
        words_list = f.read().split(',\n')
        f.close()
    
    if input in words_list:
        print("already Exists!")
        return 0
    else:
        with open(fileName, 'a') as f:
            f.write(input+',\n')
            f.close()