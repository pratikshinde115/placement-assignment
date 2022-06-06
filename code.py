def change_file_content():

    with open('sample.txt', 'r') as file :
        filedata = file.read()

    filecontent = filedata.replace('placement', 'screening')

    with open('sample.txt', 'w') as file:
        file.write(filecontent)


change_file_content()