# with open('test_file.txt','w') as wt:
#     wt.write('3.1415926535')

while True:
    name=input('please input you name:')
    with open('name_list','a') as name_object:
        name_object.write("hello"+name + '\n')