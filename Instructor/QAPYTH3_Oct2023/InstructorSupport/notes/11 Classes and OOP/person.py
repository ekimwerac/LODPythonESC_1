class Person:

   def __init__ (self, name, gender):
       self.__name = name
       self.__gender = gender.upper()
       self.public = name + gender
       self.stuff = 'Person stuff'
       
   def __str__ (self):
       return "Name: "+self.__name+ \
              " Gender: "+self.__gender
       
   def get_name (self):
       self.__some_name()
       return self.stuff
   
   def __some_name (self):
       print("some_name",self.__class__.__name__)
   
   #string get_name() const { return name; }
   #void change_name(const string &);
   
