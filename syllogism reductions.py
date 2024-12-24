from syllogisms import *
from itertools import product
import copy

end_points = ['barbara', 'darapti', 'darii', 'barbari']

def reduce_syllogism(syllogism, chain: list):
    for transformation in (Syllogism.obverse, Syllogism.converse, Syllogism.major_contraposition, Syllogism.minor_contraposition):
        if not (syllogism.mood, transformation) in chain:
            chain.append((syllogism.mood, transformation))
            new_syllogism = transformation(syllogism)
            
            if new_syllogism.mood in end_points:
                chain.append((new_syllogism.mood, True))
                return chain
            else:
                chain = reduce_syllogism(new_syllogism, chain)
                if chain[-1][1] == True:
                    return chain
    return chain
    
valid_chains = []
invalid_chains = []
for figure in ['1','2','3','4']:
    for copulae in product(['a','e','i','o'], repeat=3):
        syllogism =  Syllogism.from_terms_figure_and_copulae('S','M','P', figure, copulae)
        if syllogism.mood in end_points:
            result = [(syllogism.mood, True)]
        else:
            result = reduce_syllogism(syllogism, [])
        if result[-1][1] == True:
            valid_chains.append([i[0] for i in result])
        else:
            result[-1] = (result[-1][0], False)
            invalid_chains.append([i[0] for i in result])
        print(syllogism.mood, result[-1][1])

# ['barbara']
# ['barbari']
# ['darii']
# ['darapti']
# ['celarent', 'barbara']
# ['celaront', 'barbari']
# ['ferio', 'darii']
# ['felapton', 'darapti']
# ['bamalip', 'bamalip', 'barbari']
# ['disamis', 'bocardo', 'disamis', 'darii']
# ['fesapo', 'fesapo', 'felapton', 'darapti']
# ['fresison', 'fresison', 'ferio', 'darii']
# ['camestres', 'cesare', 'camestres', 'celarent', 'barbara']
# ['cesaro', 'camestros', 'cesaro', 'celaront', 'barbari']
# ['bocardo', 'disamis', 'bocardo', 'bocardo', 'barbara']
# ['camestros', 'cesaro', 'camestros', 'calemos', 'calemos', 'camestros', 'felapton', 'darapti']
# ['datisi', 'ferison', 'datisi', 'dimatis', 'dimatis', 'datisi', 'ferio', 'darii']
# ['ferison', 'datisi', 'ferison', 'festino', 'baroco', 'festino', 'ferison', 'darii']
# ['baroco', 'festino', 'baroco', 'baroco', 'bocardo', 'disamis', 'bocardo', 'bocardo', 'barbara']
# ['calemes', 'calemes', 'cesare', 'camestres', 'cesare', 'calemes', 'fresison', 'fresison', 'ferio', 'darii']
# ['calemos', 'calemos', 'camestros', 'cesaro', 'camestros', 'calemos', 'fesapo', 'fesapo', 'felapton', 'darapti']
# ['festino', 'baroco', 'festino', 'ferison', 'datisi', 'ferison', 'festino', 'disamis', 'bocardo', 'disamis', 'darii']
# ['cesare', 'camestres', 'cesare', 'calemes', 'calemes', 'cesare', 'datisi', 'ferison', 'datisi', 'dimatis', 'dimatis', 'datisi', 'ferio', 'darii']
# ['dimatis', 'dimatis', 'datisi', 'ferison', 'datisi', 'dimatis', 'calemes', 'calemes', 'cesare', 'camestres', 'cesare', 'calemes', 'fresison', 'fresison', 'ferio', 'darii']
