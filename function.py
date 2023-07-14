'''  default argument...! '''

def fun1 (department ,  no = 1 , name = "admin"  ):
    print("\nmy number is :- " , no ," \nname is :-" ,name, "\ndepartmengt is :-" , department )

fun1("it")
fun1("cse",2,"devloper")

'''  keyword argument...! '''

fun1(no=3 , name= "jay" ,  department = "hostel")

'''  required argument  ''' 

def  fun2 ( fname , mname , lname  ):
    print (fname , mname , lname)


fun2("\nmeet" , "mukeshbhai","vaghasiya" )


'''  arbitary arguamnet  '''

def fun3 (*name):
    print("\n",name[0],name[1],name[2],name[3]) 

fun3("meet","jay","ishwar", "bhumil")


def fun4 (**name):
    print("\n",name[0],name[1],name[2],name[3]) 

fun4("meet","jay","ishwar", "bhumil")
