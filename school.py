import csv
def w_file(i):
    with open('s_f.csv','a') as file:
        w=csv.writer(file)
        if file.tell()==0:
            w.writerow(['name','age','phone','mail'])
        w.writerow(i)
if __name__ == '__main__':
    c=True
    s=1
    while (c):
        s_info=input('enter the student{} details name,age,phone,mail:'.format(s))
        s_info_l=s_info.split(',')
        print("\n The entered is: \n name:{} age:{} \n phone:{} \n mail:{}\n".format(s_info_l[0],s_info_l[1],s_info_l[2],s_info_l[3]))
        x=input('\nif the entered info is correct press y of press n:')
        if x=='y':
            w_file(s_info_l)
            ask=input('\nenter y or n if u want to continue:')
            if ask=='y':
                s+=s
                continue
            elif ask=='n':
                break
        elif x=='n':
            print('\nenter the info agian')
