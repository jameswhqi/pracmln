from pracmln.mln.base import MLN
from pracmln.mln.database import Database
from pracmln.mln.inference.exact import EnumerationAsk
from pracmln.mln.inference.gibbs import GibbsSampler
from pracmln.mln.inference.mcsat import MCSAT
from pracmln.mln.constants import ALL

mln = MLN(logic='FirstOrderLogic', grammar='StandardGrammar', mlnfile='onenote.mln')
db = Database(mln, dbfile='onenote-infer.db')
mrf = mln.ground(db)
# method = EnumerationAsk(mrf, queries=ALL)
# method = GibbsSampler(mrf, chains=1, maxsteps=50, sample=True)
method = MCSAT(mrf, chains=10, maxsteps=500, sample=True)
result = method.run()
result.write()
