import logging
logging.basicConfig(filename="test1.log",level=logging.INFO,format='%(asctime)s %(message)s %(name)s %(levelname)s')
logging.info("we are inside the main log")


class list_s:
    logging.info("we are inside the list log")
    #try to extract the list entity from list
    def extract_list(self,l):
        self.l=l
        logging.info("we are inside class list and inside extract list function")
        try:
            for i in l:
                if type(i)==list:
                    logging.info("the number is %s",i)
        except Exception as e:
            logging.exception(e)
            return e
    # Try to summ all the int values from list
    def summation_values(self,l):
       self.l=l
       try:
           n=0
           for i in l:
               for j in i:
                   if type(j)==int:
                       n=n+j
           return n
           logging.info("logging after getting summation values",n)
       except Exception as e:
           logging.exception(e)
           return e
#Try to filter out all the odd values out of all numeric data which is part of list
   def odd_list(self,l):
       self.l=l
       logging.info("We are inside class list and checking odd number from list")
       try:
           for i in n:
               if i%2!=0:
                   return i
                   logging.info("here are the odd numbers from list", l1)
       except Exception as e:
       logging.exception(e)
       return e
#Try to find out alphanum from list
   def alnum_list(self,l):
       self.l=l
       logging.info("we are inside class list and alnum function")
       try:
           for i in l:
               if type(i)==str:
                   if i.isalnum():
                       return i
                       logging.info("Here are alnum from list", l1)
       except Exception as e:
       logging.exception(e)
       return e

    #Try to unwrape all the collection inside collection and create a flat list
    def flat_list(self,l):
        self.l=l
        logging.info("Inside a list class and flat_list function")
        try:
            l1=[]
            for i in l:
                for j in i:
                    l1.append(j)
            return l1
            logging.info("Here are the flat list",l1)
        except Exception as e:
            logging.exception(e)
            return e

    #write a function which will take multiple list as a input and give me concatnation of all the element as and output
    def conc_list(self,l):
        logging.info("we are inside concationation function")
        try:
            l1 = []
            for i in range(len(l)):
                l1 = l1 + l[i]
            return l1
            logging.info("here are the cancationation list",l1)
        except Exception as e:
            logging.exception(e)
            return e




l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"Sudh","k2":"ineuron","k3":"kumar",3:6,7:8},['ineuron','data science']]
"""obj_list=list_s()
obj_list.extract_list(l)
obj_list.summation_values(l)
obj_list.odd_list(l)
obj_list.alnum_list(l)
obj_list.flat_list(l)
obj_list.conc_list(l)"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Tuple-Task3&4   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class tuple_s:
    logging.info("We are inside tuple class for task 3")
    #Try to extract all the tuple entity
    def extract_tuple(self,l):
        self.l=l
        logging.info("we are inside extract_tuple function and tuple_s class")
        try:
            for i in l:
                if type(i) == tuple:
                    print(i)
                    logging.info("we have extracted the tuple",i)

        except Exception as e:
            logging.exception(e)
            return e


     #Try to extract "ineuron" out of the data
    def extract_data(self,l):
        self.l=l
        logging.info("we are inside extract_data function")
        l1=[]
        try:
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l1.append(j)
                if type(i) == dict:
                    for k in i.items():
                        for g in k:
                            if g == 'ineuron':
                                l1.append(g)
        return l1
        logging.info("We have extracted ineuron from l",l1)
        except Exception as e:
            logging.exception(e)
            return e

    #Try to extract all the tuple entity
    def tuple_entity(self,l):
        self.l=l
        try:
            for i in l:
                if type(i)==tuple:
                    print(i)
                    logging.info("we got all the tuple entity from list",i)

        except Exception as e:
            logging.exception(e)
            return e


"""obj_tuple=tuple_s()
obj_tuple.extract_tuple(l)
obj_tuple.extract_data(l)
obj_tuple.tuple_entity(l)"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ String-Task 3 and 4 $$$$$$$$$$$$$$$$$$$$

class string_s:
    logging.info("we are inside string class")
    #Try to filter out all the vowels:
    def check_vowels(self,s,vowels):
        self.s=s
        self.vowels=vowels
        try:
            for i in s:
                if i in vowels:
                    print(i)
                    logging.info("here are vowels",i)
        except Exception as e:
        logging.exception(e)
        return e
"""vowels="AaEeIiOoUu"
check_vowels(s,vowels)"""


"""s=Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.[32]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[33][34]

Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[35] Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.[36]

Python consistently ranks as one of the most popular programming languagesc"""


   #you have to write a fun which will take string and return a len of it without using a inbuilt fun len
   def len_str(self,s):
       self.s=s
       logging.info("we are inside str class and to find len_str function")
       try:
           n=0
           for i in s:
               n+=1
               print("length of s",n)
               logging.info("we are inside try and we got len",n)

       except Exception as e:
           logging.exception(e)
           return e
"""obj_str=string_s()
obj_str.len_str(l)"""

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Dict-Task3 and task4 $$$$$$$$$$$$$$$$$$$$$$

class dic_s:
    #Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work .
    d = {'k1': "value", "k2": "values ", "k3": {"k12": "sudh", "k13": "gafasd"}}

    def dic_to_list(self,d):
        self.d=d
        logging.info("we are inside dict class and dic_to_list function")
        l=[]
        try:
            for i in d.values():
                if type(i) != dict:
                    l.append(i)
                if type(i) == dict:
                    for j in i.values():
                        l.append(j)
        return l
        except Exception as e:
        logging.exception(e)
        return e
"""obj_dict=dic_s()
obj_dict.dic_to_list(d)"""


    #Try to extract all the numerical data it may be a part of dict keys and values
    #l=[[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,45,4,4,5,45,45,4,5]),{'k1':"Sudh","k2":"ineuron","k3":"kumar",3:6,7:8},['ineuron','data science']]
    def dict_num(self,l):
        self.l=l
        try:
            for i, j in l[4].items():  # this is wrong
                if type(i) == int:
                    print(i, ":", j)
        except Exception as e:
        logging.exception(e)
        return e
"""obj_dict=dict_s()
obj_dict.dict_num(l)"""

   #Try to extract all the dict entity
   def dict_extract(self,l):
       self.l=l
       try:
           for i in l:
               if type(i)==dict:
                   print(i)
                   logging.info("we have extracted data from l",i)

       except Exception as e:
           logging.exception(e)
           return e 

"""obj_dict=dict_s()
obj_dict.dict_extract(l)"""       