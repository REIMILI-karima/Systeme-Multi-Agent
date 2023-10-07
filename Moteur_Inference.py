class MoteurInference():
    def __init__(self,rule_base,fact_base):
        self.rule_base = rule_base
        self.fact_base = fact_base
        self.activable_rules = []
        self.premisses=[]
        self.conclusions=[]
    
    def get_fact_base(self):
        return self.fact_base
    
    def forward_chain(self):
        
        #on initialise une variable qui va nous permettre de savoir si on a appliqué une règle (pour savoir si on doit recommencer)
        
        new_fact = True
        
        #tant qu'on a appliqué une règle, on recommence
        
        while new_fact :
        
            #on met la variable à False
            new_fact=False
            
            #on parcout toutes les règles
            #si la règle est activable et qu'elle est applicable, on ajoute les conclusions à la base de faits et on désactive la règle
            for rule in self.rule_base:
                if rule.is_activable() and rule.is_applicable(self.fact_base):
                
                #on ajoute la Rules dans une liste de Ruless activables pour gerer les conflits 
                    self.activable_rules.append(rule)                
            
            #si on a pas de Ruless activables, on arrete
            if len(self.activable_rules)==0:
                break
            
            #on doit gerer les conflits (si on a deux règles ou + activables et applicables, on ne peut pas les appliquer toutes)
            #on a 2 politiques possibles :
            #1) on applique la Rules avec le plus de premisses
            #2) on applique la Rules avec l'indice le plus petit dans la base de Ruless

            
            if len(self.activable_rules)>1:

                #on va appliquer la 1ere politique
                #on va parcourir la liste des Ruless activables et on va garder la Rules avec le plus de premisses
                max_length_premisses= max(len(rule.get_premisses()) for rule in self.activable_rules)
                self.activable_rules=[rule for rule in self.activable_rules if len(rule.get_premisses())==max_length_premisses]
                
                #on applique la 2eme politique si on a toujours plusieurs Ruless activables
                if len(self.activable_rules) >1 :
                    
                    self.activable_rules=[rule for rule in self.activable_rules if self.rule_base.index(rule)==min(self.rule_base.index(rule) for rule in self.activable_rules)]
            
            #get index of the rule in the rule base
            index = self.rule_base.index(self.activable_rules[0])
            rule=self.rule_base[index]
            print("\n activable_rules",index," : ",str(rule.get_premisses()),"->",str(rule.get_conclusions()))
            self.premisses.append(str(rule.get_premisses()))
            self.conclusions.append(str(rule.get_conclusions()))
            self.fact_base.append(rule.get_conclusions())
            rule.disable_rule()
            new_fact=True
            self.activable_rules = []
    def get_conl(self):
        return self.conclusions
    def get_prem(self):
        return self.premisses

        
        