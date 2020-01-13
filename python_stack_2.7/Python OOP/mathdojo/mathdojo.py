# part 1
class MathDojo(object):
    def __init__(self):
        self.equals = 0
   
    def add(self, *args):
        for add_int in args:
            self.equals += add_int
        return self

    def subtract(self, *args):
        for sub_int in args:
            self.equals -= sub_int
        return self
    
    def result(self):
        print self.equals
        return self


md = MathDojo()
md.add(2).add(2,5).subtract(3,2).result()

# part 2
class MathDojoModify1(MathDojo):
    def __init__(self):
        super(MathDojoModify1, self).__init__()

    def add(self, *args):
        for add_int in args:
            if type(add_int) == list:
                add_list_equals = 0
                for add_list_int in add_int:
                    add_list_equals += add_list_int
                self.equals += add_list_equals
                add_list_equals = 0
            else:    
                super(MathDojoModify1, self).add(add_int)
        return self

    def subtract(self, *args):
        for sub_int in args:
            if type(sub_int) == list:
                sub_list_equals = 0
                for sub_list_int in sub_int:
                    sub_list_equals -= sub_list_int
                self.equals += sub_list_equals
                sub_list_equals = 0
            else:
                super(MathDojoModify1, self).subtract(sub_int)
        return self


md1 = MathDojoModify1()
md1.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).result()

class MathDojoModify2(MathDojoModify1, MathDojo):
    def __init__(self):
        super(MathDojoModify2, self).__init__()

    def add(self, *args):
        for add_int in args:
            if type(add_int) == tuple:
                for add_key, add_value in enumerate(add_int):
                    add_list_equals = 0
                    if type(add_value) == list:
                        for add_individual_value in add_value:
                            add_list_equals += add_individual_value
                        self.equals += add_list_equals
                    elif type(add_value) == tuple:
                        for add_value_key, add_value_value in enumerate(add_value):
                            add_value_list_equals = 0
                            if type(add_value_value) == list:
                                for add_value_individual_value in add_value_value:
                                    add_value_list_equals += add_value_individual_value
                                self.equals += add_value_list_equals
                            else:
                                super(MathDojoModify2, self).add(add_value)
                    else:
                        super(MathDojoModify2, self).add(add_value)
            else:
                super(MathDojoModify2, self).add(add_int)
        return self

    def subtract(self, *args):
        for sub_int in args:
            if type(sub_int) == tuple:
                for sub_key, sub_value in enumerate(sub_int):
                    sub_list_equals = 0
                    if type(sub_value) == list:
                        for sub_individual_value in sub_value:
                            sub_list_equals -= sub_individual_value
                        self.equals += sub_list_equals
                    elif type(sub_value) == tuple:
                        for sub_value_key, sub_value_value in enumerate(sub_value):
                            sub_value_list_equals = 0
                            if type(sub_value_value) == list:
                                for sub_value_individual_value in sub_value_value:
                                    sub_value_list_equals -= sub_value_individual_value
                                self.equals += sub_value_list_equals
                            else:
                                super(MathDojoModify2, self).subtract(sub_value)
                    else:
                        super(MathDojoModify2, self).subtract(sub_value)
            else:
                super(MathDojoModify2, self).subtract(sub_int)
        return self

md2 = MathDojoModify2()
md2.add([1],3,4).add([3,5,7,8],[2,4.3,1.25]).subtract(2,[2,3],[1.1,2.3]).subtract(([1,1,1],[1,1])).add(([1,1],([1,1,1]))).result()


    # def add1(self, *args):
    #     for add1_int in args:
    #         if type(add1_int) == list:
    #             add1_list_equals = 0
    #             for add1_list_int in add1_int:
    #                 add1_list_equals += add1_list_int
    #             self.equals += add1_list_equals
    #         elif type(add1_int) == int or type(add1_int) == float:
    #             self.equals += add1_int
    #         else:
    #             print "This is not a valid entry type"
    #     return self
    
    # def sub1(self, *args):
    #     for sub1_int in args:
    #         if type(sub1_int) == list:
    #             sub1_list_equals = 0
    #             for sub1_list_int in sub1_int:
    #                 sub1_list_equals -= sub1_list_int
    #             self.equals += sub1_list_equals
    #         elif type(sub1_int) == int or type(sub1_int) == float:
    #             self.equals -= sub1_int
    #         else:
    #             print "This is not a valid entry type"
    #     return self

