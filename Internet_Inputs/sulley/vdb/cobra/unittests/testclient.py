
import cobra

cobra.verbose = True

p = cobra.CobraProxy('cobra://localhost/woot')
print p.printwoot('blah')
