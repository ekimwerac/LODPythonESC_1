class Person:

   def __init__ (self, name, gender):
       self.__name = name
       self.__gender = gender.upper()
       
   def __str__ (self):
       return "Name: "+self.__name+ \
              " Gender: "+self.__gender
       
   #string get_name() const { return name; }
   #void change_name(const string &);
   
