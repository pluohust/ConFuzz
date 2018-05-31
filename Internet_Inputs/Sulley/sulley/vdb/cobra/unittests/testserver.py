
import cobra

cobra.verbose = True

class woot:

    def printwoot(self, x):
        print 'WOOT',x
        return 'DID WOOT'

d = cobra.CobraDaemon()
d.shareObject(woot(), 'woot', doref=True)
d.serve_forever()
