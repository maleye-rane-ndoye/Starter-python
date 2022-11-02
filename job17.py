def myFuntion( *params ):
    list = []

    for item in params:
        if isinstance(item,(int)):
            list,append(item)
        else:
            print("error item unknown as numeric")

    for item in list:
        if item % 7 == 0:
           print (item)