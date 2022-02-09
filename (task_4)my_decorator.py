def assertion_decorator(name_original_fn):
    def the_wrapper():
        for i in range (1, 4):
            try:
                name_original_fn()
                break
            except NameError as error:
                print(error)
    return the_wrapper()

def test():
    print(ghjkk)

assertion_decorator(test)



