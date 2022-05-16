"""
How to use decorator
Born time: 2022.5.15
Latest update: 2022.5.16
Creator: ZHX
"""


def test_dec(call_back):  # 1st visited
    def inner_func(me):
        print(me)
        print("I am a decorator.")

    call_back(100)  # 2nd visited
    return inner_func  # 3rd visited


@test_dec  # test_dec(decorated_func())
def decorated_func(data):
    print("Normal:{}".format(data))


decorated_func(me=18)
