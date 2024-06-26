import copy
class Country:

    index = {'name':0,'population':1,'capital':2,'citypop':3,'continent':4,
             'ind_date':5,'currency':6,'religion':7,'language':8}
    
    def __init__(self, row):
        self.__attr = row.split(',')
        
        # Added to support + and -
        self.__attr[Country.index['population']] = \
            int(self.__attr[Country.index['population']])
        
    def print(self):
        print(self.__attr[Country.index['name']])
    
    # Overloaded stringification
    def __str__(self):
        #return self._attr[Country.index['name']]
        #return self.name
        return "{0:<32} {1}".format(self.name, self.population)
    
    # Overloaded + and -
    def __add__(self,amount):    
        retn = copy.deepcopy(self)
        retn.__attr[Country.index['population']] += amount
        return retn
    
    def __sub__(self, amount):
        """ Added exception for context manager testing """    
        
        if amount >  self.__attr[Country.index['population']]:
            raise ValueError(("Population would be zero",
                  Country.index['population'], amount))
    
        self.__attr[Country.index['population']] -= amount
        return self
    
    # Overloaded == (for index search)
    def __eq__(self,key):
        return (key == self.name)
    
    # Getter methods
    @property
    def name(self):
        return self.__attr[Country.index['name']]
    
    @property
    def population(self):
        return int(self.__attr[Country.index['population']])
    
    @name.setter
    def name(self,name):
        self.__attr[0]=name
        
    