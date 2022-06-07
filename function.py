from copyreg import dispatch_table


def swapfiledata():
    filename=input("Enter the file name: ")

    file1=data_a
    
    with open(file1,'r') as a:
        data_a = a.read()

    with open(file1,'w') as a:
        a.write(data_b)

swapfiledata()

