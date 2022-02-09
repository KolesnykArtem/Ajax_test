def deletes(file_name):
    out_line = ''
    all_file = open(file_name, 'r')
    for line in all_file:
        if 'HUB' in line:
            line.strip()
            line = line.replace(' ','')
            out_line = out_line + line
    all_file.close()

    all_file = open(file_name, 'w')
    all_file.write(out_line)  
    all_file.close()

deletes('test.log')
