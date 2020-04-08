import os
fname=input('Enter file name:')
if os.path.isfile(fname):
    print('File exists!!!',fname)
    with open(fname,'r') as f:
        lcount=wcount=ccount=0
        for line in f:
            if f.readline!='':
                lcount=lcount+1
            no_of_words_in_current_line=len(line.split())
            wcount=wcount+no_of_words_in_current_line
            no_of_char_in_current_line=len(line)
            ccount=ccount+no_of_char_in_current_line
        print('No of lines in file is:',lcount)
        print('No of words in file are:',wcount)
        print('No of characters in file are:',ccount)
else:
    print("file doesn't exists",fname)
