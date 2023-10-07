class Regles : 
    def __init__(self,premisses,conclusions):
       self.premisses = premisses
       self.conclusions = conclusions
       self.activable = True
    
    def __str__(self):
       return str(self.premisses) + " -> " + str(self.conclusions)

    def get_premisses(self):
       return self.premisses
    
    def get_conclusions(self):
       return self.conclusions

    def disable_rule(self):
       self.activable = False
    
    def is_activable(self):
         return self.activable


    def is_applicable(self, facts):
       for fact in self.premisses:
           if fact not in facts:
               return False
       return True    