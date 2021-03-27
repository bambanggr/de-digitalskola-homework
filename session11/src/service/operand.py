class Operand():

    DEFAULT_PARAM1 = 0
    DEFAULT_PARAM2 = 0
    DEFAULT_PARAM3 = "PLUS1"

    def __init__(self, param1:int = DEFAULT_PARAM1, param2: int = DEFAULT_PARAM2, param3: str =DEFAULT_PARAM3):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        if(str.upper(self.param3)=="PLUS1"):
            Operand.fnc_plus1(self)
        elif(str.upper(self.param3)=="KUADRAT"):
            Operand.fnc_kuadrat(self)
        elif(str.upper(self.param3)=="FIBONACCI"):
            Operand.fnc_fibonacci(self)
        else:
            return "Please input valid function"

    # def transform(self, string):
    #     return f"{self.prefix}_{string}_{self.suffix}"

    def fnc_plus1(self):
        param1=self.param1
        param2=self.param2
        param3=self.param3
        list_plus1=[]
        # list_plus1 = list(range(param1,param2+1)) #CaraCepatPlus1
        for plus in range(param1, param2+1):
            # print("Ke {}".format(plus))
            if(plus == param1):
                list_plus1.append(param1)
            else:
                param1=param1+1
                if(param1<=param2):
                    list_plus1.append(param1)            
        print("Plus 1 : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_plus1))

    def fnc_kuadrat(self):
        param1=self.param1
        param2=self.param2
        param3=self.param3
        list_exponent=[]
        val_start = param1
        while(param1<=param2):
            if(val_start==param1):
                list_exponent.append(param1)
                param1=param1*2
            else:
                list_exponent.append(param1)
                param1=param1*2
        # return list_exponent
        print("Kuadrat : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_exponent))

    def fnc_fibonacci(self):
        param1=self.param1
        param2=self.param2
        param3=self.param3

        list_fbnc=[]
        curr_val = 0
        prev_val = 1
        stt=0
        #0,1,1,2,3,5,8,13,21,34
        while(stt<=param2):
            if(stt>=param1):
                list_fbnc.append(stt)
            curr_val=stt+prev_val
            prev_val=stt
            stt=curr_val
        # return list_fbnc
        print("Fibonacci : function ({},{},'{}') -> {}".format(self.param1,self.param2,self.param3,list_fbnc))