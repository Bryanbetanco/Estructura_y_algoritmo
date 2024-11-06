# Implement an Array data structure as a simplified type of list.
class Array(object):
    def __init__(self, initialSize): # Constructor
        self.__a = [None] * initialSize # The array stored as a list
        self.__nItems = 0 # No items in array initially
    
    def __len__(self): # Special def for len() func
        return self.__nItems # Return number of items
    
    def get(self, n): # Return the value at index n
        if 0 <= n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n] # only return item if in bounds
    
    def set(self, n, value): # Set the value at index n
        if 0 <= n < self.__nItems: # Check if n is in bounds, and
            self.__a[n] = value # only set item if in bounds
    
    def insert(self, item): # Insert item at end
        self.__a[self.__nItems] = item # Item goes at current end
        self.__nItems += 1 # Increment number of items
    
    def find(self, item): # Find index for item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found,
                return j # then return index to item
        return -1 # Not found -> return -1
    
    def search(self, item): # Search for item
        return self.get(self.find(item)) # and return item if found
    
    def delete(self, item): # Delete first occurrence of an item
        for j in range(self.__nItems): # Among current items
            if self.__a[j] == item: # If found,
                self.__nItems -= 1 # One fewer at end
                for k in range(j, self.__nItems): # Move items from
                    self.__a[k] = self.__a[k + 1] # right over 1
                return True # Return success flag
        return False # Made it here, so couldn't find the item
    
    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems): # and apply a function
            function(self.__a[j])
    
    def getMaxNum(self): # New method to find the maximum number
        max_num = None
        for item in self.__a[:self.__nItems]:
            if isinstance(item, (int, float)):
                if max_num is None or item > max_num:
                    max_num = item
        return max_num

    
    def getAverageNum(self):
        sum_nums = 0
        count_nums = 0
        for item in self.__a[:self.__nItems]:
            if isinstance(item, (int, float)):
                sum_nums += item
                count_nums += 1
        return sum_nums / count_nums if count_nums != 0 else 

    def parImpar1(self): # New method to find the maximum number
        par = 0
        impar = 0
        for item in self.__a[:self.__nItems]:
            if isinstance(item, (int, float)):
                if intem%2 == 0 
                    par += 1
                else
                    impar +=1 
        return par , impar


        def parImpar(self, tipo): # New method to find the maximum number
        par = 0
        impar = 0
        for item in self.__a[:self.__nItems]:
           
            if isinstance(item, (int, float)):
                if intem%2 == 0:
                    par += 1
                else
                    impar +=1 
            if tipo = 0:
                return print ("Par", par)
            else 
                return print ("Impar"; impar)
        return 0
    

