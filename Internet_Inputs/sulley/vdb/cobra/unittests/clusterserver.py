

import cobra
import cobra.cluster as c_cluster

c = c_cluster.ClusterServer('woot')
c.setClusterQueen('127.0.0.1')

for i in xrange(2):
    c.addWork( c_cluster.ClusterWork() )

c.runServer()

