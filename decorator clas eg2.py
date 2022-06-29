def decorator(original):
    def frosting():
        print("all cake has frosting")
        return original()
    return frosting

def cake():
    print("choclate cake")
decorated_cake=decorator(cake)
#decorated_test()
decorated_cake()