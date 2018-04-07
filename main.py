from pracmln.mln.base import MLN
from pracmln.mln.database import Database
from pracmln.mln.inference.exact import EnumerationAsk
from pracmln.mln.inference.gibbs import GibbsSampler
import sys

# print(sys.path)
mln = MLN(logic='FirstOrderLogic', grammar='StandardGrammar', mlnfile='onenote.mln')
db = Database(mln, dbfile='onenote.db')
mrf = mln.ground(db)
# method = EnumerationAsk(mrf, ['Cancer', 'Smokes', 'Friends'])
method = GibbsSampler(mrf, chains=1, maxsteps=500, sample=True)
result = method.run()
result.write()
