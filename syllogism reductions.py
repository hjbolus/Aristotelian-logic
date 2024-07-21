from syllogisms import *
from itertools import product
import copy

end_points = ['Barbara', 'Darapti', 'Darii', 'Barbari']

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
for figure in ['1','2','3', '4']:
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

# ['Barbara']
# ['Barbari']
# ['Darii']
# ['Darapti']
# ['Datisi', 'Datisi', 'Darii']
# ['Bocardo', 'Bocardo', 'Bocardo', 'Barbara']
# ['Felapton', 'Felapton', 'Fesapo', 'Fesapo', 'Felapton', 'Barbari']
# ['Celaront', 'Celaront', 'Cesaro', 'Camestros', 'Cesaro', 'Celaront', 'Darapti']
# ['Cesaro', 'Camestros', 'Cesaro', 'Celaront', 'Celaront', 'Cesaro', 'Darapti']
# ['Ferison', 'Ferison', 'Festino', 'Baroco', 'Festino', 'Ferison', 'Darii']
# ['Ferio', 'Ferio', 'Fresison', 'Fresison', 'Ferio', 'Datisi', 'Datisi', 'Darii']
# ['Baroco', 'Festino', 'Baroco', 'Baroco', 'Bocardo', 'Bocardo', 'Bocardo', 'Barbara']
# ['Cesare', 'Camestres', 'Cesare', 'Celarent', 'Celarent', 'Cesare', 'Datisi', 'Datisi', 'Darii']
# ['Camestros', 'Cesaro', 'Camestros', 'Calemos', 'Calemos', 'Camestros', 'Felapton', 'Felapton', 'Fesapo', 'Fesapo', 'Felapton', 'Barbari']
# ['Camestres', 'Cesare', 'Camestres', 'Calemes', 'Calemes', 'Camestres', 'Ferison', 'Ferison', 'Festino', 'Baroco', 'Festino', 'Ferison', 'Darii']
# ['Bamalip', 'Bamalip', 'Bamalip', 'Camestros', 'Cesaro', 'Camestros', 'Calemos', 'Calemos', 'Camestros', 'Felapton', 'Felapton', 'Fesapo', 'Fesapo', 'Felapton', 'Barbari']
# ['Fesapo', 'Fesapo', 'Felapton', 'Felapton', 'Fesapo', 'Bamalip', 'Bamalip', 'Bamalip', 'Camestros', 'Cesaro', 'Camestros', 'Calemos', 'Calemos', 'Camestros', 'Felapton', 'Barbari']
# ['Calemos', 'Calemos', 'Camestros', 'Cesaro', 'Camestros', 'Calemos', 'Fesapo', 'Fesapo', 'Felapton', 'Felapton', 'Fesapo', 'Bamalip', 'Bamalip', 'Bamalip', 'Camestros', 'Felapton', 'Barbari']
# ['Celarent', 'Celarent', 'Cesare', 'Camestres', 'Cesare', 'Celarent', 'Disamis', 'Disamis', 'Dimatis', 'Dimatis', 'Disamis', 'Celarent', 'Festino', 'Baroco', 'Festino', 'Ferison', 'Ferison', 'Festino', 'Disamis', 'Festino', 'Ferison', 'Darii']
# ['Festino', 'Baroco', 'Festino', 'Ferison', 'Ferison', 'Festino', 'Disamis', 'Disamis', 'Dimatis', 'Dimatis', 'Disamis', 'Celarent', 'Celarent', 'Cesare', 'Camestres', 'Cesare', 'Celarent', 'Disamis', 'Festino', 'Celarent', 'Cesare', 'Darii']
# ['Disamis', 'Disamis', 'Dimatis', 'Dimatis', 'Disamis', 'Celarent', 'Celarent', 'Cesare', 'Camestres', 'Cesare', 'Celarent', 'Disamis', 'Festino', 'Baroco', 'Festino', 'Ferison', 'Ferison', 'Festino', 'Festino', 'Celarent', 'Ferison', 'Darii']
# ['Dimatis', 'Dimatis', 'Disamis', 'Disamis', 'Dimatis', 'Calemes', 'Calemes', 'Camestres', 'Cesare', 'Camestres', 'Calemes', 'Fresison', 'Fresison', 'Ferio', 'Ferio', 'Fresison', 'Dimatis', 'Fresison', 'Calemes', 'Ferio', 'Datisi', 'Datisi', 'Darii']
# ['Fresison', 'Fresison', 'Ferio', 'Ferio', 'Fresison', 'Dimatis', 'Dimatis', 'Disamis', 'Disamis', 'Dimatis', 'Calemes', 'Calemes', 'Camestres', 'Cesare', 'Camestres', 'Calemes', 'Fresison', 'Calemes', 'Dimatis', 'Camestres', 'Ferio', 'Datisi', 'Datisi', 'Darii']
