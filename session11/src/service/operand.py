class Operand():

    DEFAULT_PARAM1 = 0
    DEFAULT_PARAM2 = 0
    DEFAULT_PARAM3 = "PLUS1"

    def __init__(self, param1:int = DEFAULT_PARAM1, param2: int = DEFAULT_PARAM2, param3: str =DEFAULT_PARAM3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
   
    @staticmethod
    def func(param1,param2,param3):
        try:
            if(str.upper(param3) == "PLUS1"):
                return Operand.fnc_plus1(param1,param2)
            elif(str.upper(param3) == "KUADRAT"):
                return Operand.fnc_kuadrat(param1,param2)
            elif(str.upper(param3) == "FIBONACCI"):
                return Operand.fnc_fibonacci(param1,param2)
            else:
                return "Menu doesn't exists"
        except:
            return "Please input valid parameter (int, int, str)"

    def fnc_plus1(param1, param2):
        list_plus1=[]
        # list_plus1 = list(range(param1,param2+1)) #CaraCepatPlus1
        try:
            for plus in range(param1, param2+1):
                # print("Ke {}".format(plus))
                if(plus == param1):
                    list_plus1.append(param1)
                else:
                    param1=param1+1
                    if(param1<=param2):
                        list_plus1.append(param1)
            return list_plus1            
        except TypeError:
            return "Please input valid integer"
        # print("Plus 1 : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_plus1))

    def fnc_kuadrat(param1, param2):
        list_exponent=[]
        kuadrat_result = 0
        iteration = 1
        try:
            while(kuadrat_result<=param2):
                kuadrat_result=param1**iteration
                print("Ke {}, Kuadrat: {}".format(iteration, kuadrat_result))
                if(kuadrat_result<=param2):
                    list_exponent.append(kuadrat_result)
                iteration = iteration+1
            return list_exponent
        except TypeError:
            return "Please input valid integer"
        # print("Kuadrat : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_exponent))

    def fnc_fibonacci(param1, param2):
        list_fbnc=[]
        curr_val = 0
        prev_val = 1
        stt=0
        #0,1,1,2,3,5,8,13,21,34
        try:
            while(stt<=param2):
                if(stt>=param1):
                    list_fbnc.append(stt)
                curr_val=stt+prev_val
                prev_val=stt
                stt=curr_val
            return list_fbnc
            # print("Fibonacci : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_fbnc))
        except TypeError:
            return "Please input valid integer"