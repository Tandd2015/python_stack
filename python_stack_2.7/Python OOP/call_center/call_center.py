import datetime
from operator import attrgetter

class Call(object):
    call_logger_id = 0
    def __init__(self, caller_name, caller_phone_number, reason_for_call):
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = datetime.datetime.now()
        self.reason_for_call = reason_for_call
        self.unique_id = Call.call_logger_id

        Call.call_logger_id += 1


    def display(self):
        for attribute, value in self.__dict__.iteritems():
            new_attribute_name = attribute.replace("_", " ")
            if attribute == "time_of_call":
                print new_attribute_name + ":  " + value.strftime("%I:%M %p")
            else:
                print new_attribute_name + ": " + str(value)
        return self

# call1 = Call("Daniel Beatty", 15673410262, "Assignment call")
# call1.display()

class CallCenter(Call):
    new_self_calls = []
    call_in = False
    call_counter = 0
    def __init__(self, caller_name, caller_phone_number, reason_for_call):
        self.calls = []
        self.queue_size = self.get_que_size()
        super(CallCenter, self).__init__(caller_name, caller_phone_number, reason_for_call)

    def get_que_size(self):
        return len(self.calls)

    def remove(self):
        CallCenter.delete_call = self
        CallCenter.call_counter -= 1
        self.calls.remove(CallCenter.delete_call)
        return self
    
    def add(self):
        self.call_center_unique_id = self.queue_size
        CallCenter.call_counter += 1
        CallCenter.new_call = self
        self.calls.append(CallCenter.new_call)
        return self

    def info(self):
        for i in range(len(self.calls)):
            for attribute, value in self.calls[i].__dict__.iteritems():
                new_attribute_name = attribute.replace("_", " ")
                if attribute == "time_of_call":
                    converted_time = new_attribute_name + ":  " + value.strftime("%I:%M %p")
                    print "length of queue: " + str(CallCenter.call_counter)
                elif attribute == "caller_name":
                    print new_attribute_name + ":  " + str(value)
                elif attribute == "caller_phone_number":
                    print new_attribute_name + ":  " + str(value)
                    print " "
                else:
                    pass
        return self

    def ninja_level(self):
        search_call_number = 0
        for index in range(len(self.calls)):
            for key, value in self.calls[index].__dict__.iteritems():
                if key == "caller_phone_number":
                    search_call_number = value
                    if value == search_call_number:
                        self.calls.remove(self.calls[index])
                        CallCenter.call_counter -= 1
                else:
                    pass
        return self
    
    def hacker_level(self):
        for index in range(len(self.calls)):
            print index
            for k, v in self.calls[index].__dict__.iteritems():
                if k == "time_of_call":
                    # converted_time_handler = v.strftime("%Y-%m-%d %H:%M:%S.%f")
                    time = v.strftime("%H%M%S.%f")
                    hour = int(v.strftime("%H"))
                    minute = int(v.strftime("%M"))
                    second = float(v.strftime("%S.%f"))
                    print hour, minute, second, time
                    CallCenter.new_self_calls.append(self)
                    print CallCenter.new_self_calls
                    print self.calls
                # print converted_time_handle
        return self
        
call2 = CallCenter("Daniel Beatty", 15673410262, "Super class Assignment call2")
call3 = CallCenter("Christina Trevino", 15673410251, "Super class Assignment call3")
call4 = CallCenter("Harlow Grace Beatty", 9333666999, "Super class Assignment call4")
call5 = CallCenter("Ava Ryan", 3693693693, "Super class Assignment call5")

call3.add().hacker_level()
call4.add().hacker_level()
call2.add().hacker_level()
call5.add().hacker_level()

            # print CallCenter.call_counter
            # print index
            # print self.queue_size
        # for attribute, value in self.__dict__.iteritems():
        #     new_attribute_name = attribute.replace("_", " ")
        #     if attribute == "time_of_call":
        #         new_time_of_call = new_attribute_name + ": " + value.strftime("%I:%M %p")
        #     elif attribute == "caller_name":
        #         new_caller_name = new_attribute_name + ": " + str(value)
        #     elif attribute == "queue_size":
        #         new_queue_size = new_attribute_name + ": " + str(value)
        #     else:
        #         continue
            
        # def info_printer(*args):
        #     for index in args:
        #         print index
        # info_printer(new_time_of_call, new_caller_name, new_queue_size)

                
        # delete_call = self
        # queue_call_number = self.caller_phone_number
        # for key, val in self.__dict__.iteritems():
        #     if key == "caller_phone_number":
        #         if val == queue_call_number:
        #             print "hello world"
        #             print delete_call
        #             # self.calls.remove(delete_call)
        #         else:
        #             continue
        #     else:
        #         continue
        # print queue_call_number
        