
class Date:
    
    def __init__ (self, day=0, month=0, year=0):
        self.__day   = day
        self.__month = month
        self.__year  = year
        Date.__count += 1
        
    def __str__ (self):
        return str(self.__day)   + '/' + \
               str(self.__month) + '/' + \
               str(self.__year)
               
    def __add__ (this, value):
        this.__day = this.__day + value
        this.__validate_date()
        return this
        
   #             J  F  M  A  M  J  J  A  S  O  N  D     
    __months = (31,28,31,30,31,30,31,31,30,31,30,31)
    
    def __validate_date(self):
        mday = Date.__months[self.__month-1]
        
        if self.__day > mday:
            self.__day -= mday
            self.__month += 1
            
        if self.__month > 12:
            self.__year += 1
            self.__month -= 12
            
            
    __count = 0
    
    def get_count():
        return Date.__count
        
    @property
    def mday(self):
        return self.__day
        
    @mday.setter
    def mday(self, day):
        self.__day = day
        
        