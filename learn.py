from pracmln.mln.base import MLN
from pracmln.mln.database import Database
from pracmln.mln.learning.bpll import BPLL

mln = MLN(logic='FirstOrderLogic', grammar='StandardGrammar', mlnfile='onenote.mln')
# mln.fixweights = [True, False]
db = Database(mln, dbfile='onenote-train.db')
mrf = mln.ground(db)
method = BPLL(mrf, prior_stdev=1, verbose=True)
result = method.run()
for w in result:
    print('{:.3f}'.format(w))
