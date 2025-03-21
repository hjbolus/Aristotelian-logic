from itertools import product

class Proposition:
    first: str
    second: str
    terms: tuple
    quantifier: str

    def __init__(self, first: str, quantifier: str, second: str):
        self.first = first
        self.second = second
        self.terms = (first, second)
        assert quantifier in {'a','e', 'i', 'o'}, print(f'Invalid quantifier "{quantifier}"')
        self.quantifier = quantifier

    def __repr__(self):
        if self.quantifier == 'a':
            return f'Everything that is a(n) {self.first} is a(n) {self.second}'
        elif self.quantifier == 'e':
            return f'Nothing that is a(n) {self.first} is a(n) {self.second}'
        elif self.quantifier == 'i':
            return f'Some things that are a(n) {self.first} are a(n) {self.second}'
        else:
            return f'Not all things that are a(n) {self.first} are a(n) {self.second}'

    def __eq__(self, other):
        return isinstance(other, Proposition) and str(self) == str(other)

    def contrary(self):
        if self.quantifier == 'a':
            quantifier = 'e'
        elif self.quantifier == 'e':
            quantifier = 'a'
        elif self.quantifier == 'i':
            quantifier = 'o'
        else:
            quantifier = 'i'
        return Proposition(self.first, quantifier, self.second)

    def contradiction(self):
        if self.quantifier == 'a':
            quantifier = 'o'
        elif self.quantifier == 'e':
            quantifier = 'i'
        elif self.quantifier == 'i':
            quantifier = 'e'
        else:
            quantifier = 'a'
        return Proposition(self.first, quantifier, self.second)

    def subaltern(self):
        if self.quantifier == 'a':
            quantifier = 'i'
        elif self.quantifier == 'e':
            quantifier = 'o'
        elif self.quantifier == 'i':
            quantifier = 'a'
        else:
            quantifier = 'e'
        return Proposition(self.first, quantifier, self.second)

class Syllogism:
    major: Proposition
    minor: Proposition
    conclusion: Proposition
    subject: str
    predicate: str
    middle_term: str
    figure: str
    mood: str
    lines: list

    figure1 = {
    ('a', 'a', 'a'): 'barbara',
    ('e', 'a', 'e'): 'celarent',
    ('a', 'i', 'i'): 'darii',
    ('e', 'i', 'o'): 'ferio',
    ('a', 'a', 'i'): 'barbari',
    ('e', 'a', 'o'): 'celaront'}
    figure2 = {
    ('e', 'a', 'e'): 'cesare',
    ('a', 'e', 'e'): 'camestres',
    ('e', 'i', 'o'): 'festino',
    ('a', 'o', 'o'): 'baroco',
    ('e', 'a', 'o'): 'cesaro',
    ('a', 'e', 'o'): 'camestros'}
    figure3 = {
    ('a', 'i', 'i'): 'datisi',
    ('i', 'a', 'i'): 'disamis',
    ('e', 'i', 'o'): 'ferison',
    ('o', 'a', 'o'): 'bocardo',
    ('e', 'a', 'o'): 'felapton',
    ('a', 'a', 'i'): 'darapti'}
    figure4 = {
    ('a', 'e', 'e'): 'calemes',
    ('i', 'a', 'i'): 'dimatis',
    ('e', 'i', 'o'): 'fresison',
    ('a', 'e', 'o'): 'calemos',
    ('e', 'a', 'o'): 'fesapo',
    ('a', 'a', 'i'): 'bamalip'}

    moods = {'barbara': ('1', ('a', 'a', 'a')),
    'celarent': ('1', ('e', 'a', 'e')),
    'darii': ('1', ('a', 'i', 'i')),
    'ferio': ('1', ('e', 'i', 'o')),
    'barbari': ('1', ('a', 'a', 'i')),
    'celaront': ('1', ('e', 'a', 'o')),
    'cesare': ('2', ('e', 'a', 'e')),
    'camestres': ('2', ('a', 'e', 'e')),
    'festino': ('2', ('e', 'i', 'o')),
    'baroco': ('2', ('a', 'o', 'o')),
    'cesaro': ('2', ('e', 'a', 'o')),
    'camestros': ('2', ('a', 'e', 'o')),
    'datisi': ('3', ('a', 'i', 'i')),
    'disamis': ('3', ('i', 'a', 'i')),
    'ferison': ('3', ('e', 'i', 'o')),
    'bocardo': ('3', ('o', 'a', 'o')),
    'felapton': ('3', ('e', 'a', 'o')),
    'darapti': ('3', ('a', 'a', 'i')),
    'calemes': ('4', ('a', 'e', 'e')),
    'dimatis': ('4', ('i', 'a', 'i')),
    'fresison': ('4', ('e', 'i', 'o')),
    'calemos': ('4', ('a', 'e', 'o')),
    'fesapo': ('4', ('e', 'a', 'o')),
    'bamalip': ('4', ('a', 'a', 'i'))}

    def __init__(self, major: Proposition, minor: Proposition, conclusion=None):
        self.major = major
        self.minor = minor

        #determine figure
        if major.first == minor.second:
            self.figure = '1'
            self.subject = minor.first
            self.predicate = major.second
            self.middle_term = major.first

        elif major.second == minor.second:
            self.figure = '2'
            self.subject = minor.first
            self.predicate = major.first
            self.middle_term = major.second

        elif major.first == minor.first:
            self.figure = '3'
            self.subject = minor.second
            self.predicate = major.second
            self.middle_term = major.first

        else:
            self.figure = '4'
            self.subject = minor.second
            self.predicate = major.first
            self.middle_term = major.second

        if conclusion:
            self.conclusion = conclusion
        else:
            print('Pick a conclusion from the following:')
            for quantifier in ['a', 'e', 'i', 'o']:
                print(f'{quantifier}: {Proposition(self.subject, quantifier, self.predicate)}')
            quantifier = str(input())
            assert quantifier in {'a', 'e', 'i', 'o'}, print('invalid quantifier')
            self.conclusion = Proposition(self.subject, quantifier, self.predicate)

        self.lines = (self.major, self.minor, self.conclusion)

        #determine mood
        self.quantifiers = (self.major.quantifier, self.minor.quantifier, self.conclusion.quantifier)
        if self.figure == '1':
            if self.quantifiers in Syllogism.figure1:
                self.mood = Syllogism.figure1[self.quantifiers]
            else:
                self.mood = ''.join([self.figure, *[line.quantifier for line in self.lines]])
        elif self.figure == '2':
            if self.quantifiers in Syllogism.figure2:
                self.mood = Syllogism.figure2[self.quantifiers]
            else:
                self.mood = ''.join([self.figure, *[line.quantifier for line in self.lines]])
        elif self.figure == '3':
            if self.quantifiers in Syllogism.figure3:
                self.mood = Syllogism.figure3[self.quantifiers]
            else:
                self.mood = ''.join([self.figure, *[line.quantifier for line in self.lines]])
        elif self.figure == '4':
            if self.quantifiers in Syllogism.figure4:
                self.mood = Syllogism.figure4[self.quantifiers]
            else:
                self.mood = ''.join([self.figure, *[line.quantifier for line in self.lines]])

    def __repr__(self):
        return f"{self.major},\n{self.minor},\n\tTherefore,\n{self.conclusion}."

    def __eq__(self, other):
        if isinstance(other, Syllogism):
            return self.major == other.major and self.minor == other.minor and self.conclusion == other.conclusion
        return False

    def is_valid(self):
        if self.mood in Syllogism.moods:
            if self.figure == '1':
                return self.major.first == self.minor.second and self.major.second == self.conclusion.second and self.minor.first == self.conclusion.first
            elif self.figure == '2':
                return self.major.second == self.minor.second and self.major.first == self.conclusion.second and self.minor.first == self.conclusion.first
            elif self.figure == '3':
                return self.major.first == self.minor.first and self.major.second == self.conclusion.second and self.minor.second == self.conclusion.first
            else:
                return self.major.first == self.conclusion.second and self.major.second == self.minor.first and self.minor.second == self.conclusion.first
        return False

    def from_terms_figure_and_quantifiers(subject='S', middle_term='M', predicate='P', figure='1', quantifiers=('a','a','a')):
        assert figure in {'1','2','3','4'}
        assert len(quantifiers) == 3 and all(i in {'a','e','i','o'} for i in quantifiers)
        if figure == '1':
            major = Proposition(middle_term, quantifiers[0], predicate)
            minor = Proposition(subject, quantifiers[1], middle_term)

        elif figure == '2':
            major = Proposition(predicate, quantifiers[0], middle_term)
            minor = Proposition(subject, quantifiers[1], middle_term)

        elif figure == '3':
            major = Proposition(middle_term, quantifiers[0], predicate)
            minor = Proposition(middle_term, quantifiers[1], subject)

        else:
            major = Proposition(predicate, quantifiers[0], middle_term)
            minor = Proposition(middle_term, quantifiers[1], subject)

        conclusion = Proposition(subject, quantifiers[2], predicate)
        return Syllogism(major, minor, conclusion)

    def from_terms_and_mood(subject, middle_term, predicate, mood):
        assert mood.lower() in Syllogism.moods
        figure, quantifiers = Syllogism.moods[mood.lower()]
        return Syllogism.from_terms_figure_and_quantifiers(subject, middle_term, predicate, figure, quantifiers)

    def from_m_and_f(mood_and_figure):
        if mood_and_figure.lower() in Syllogism.moods:
            figure, quantifiers = Syllogism.moods[mood_and_figure.lower()]
        else:
            assert len(mood_and_figure) == 4
            if mood_and_figure[0].isnumeric():
                assert mood_and_figure[1:].isalpha()
                figure = mood_and_figure[0]
                quantifiers = list(mood_and_figure[1:])
            elif mood_and_figure[-1].isnumeric():
                assert mood_and_figure[:-1].isalpha()
                figure = mood_and_figure[-1]
                quantifiers = list(mood_and_figure[:-1])
        return Syllogism.from_terms_figure_and_quantifiers('S', 'M', 'P', figure, quantifiers)

    def to_propositional_logic(self):
        pass

    def to_predicate_logic(self):
        pass

    def major_contraposition(self):
        conclusion = self.conclusion.contradiction()

        major = self.major.contradiction()
        if major.second in self.minor.terms:
            major_contraposition = Syllogism(self.minor, conclusion, major)
        else:
            assert major.second in conclusion.terms
            major_contraposition = Syllogism(conclusion, self.minor, major)

        return major_contraposition

    def minor_contraposition(self):
        conclusion = self.conclusion.contradiction()

        #minor_contraposition
        minor = self.minor.contradiction()
        if minor.second in self.major.terms:
            minor_contraposition = Syllogism(self.major, conclusion, minor)
        else:
            assert minor.second in self.conclusion.terms
            minor_contraposition = Syllogism(conclusion, self.major, minor)

        return minor_contraposition

    def contrapositions(self):
        conclusion = self.conclusion.contradiction()

        #major_contraposition
        major = self.major.contradiction()
        if major.second in self.minor.terms:
            major_contraposition = Syllogism(self.minor, conclusion, major)
        else:
            assert major.second in conclusion.terms
            major_contraposition = Syllogism(conclusion, self.minor, major)

        #minor_contraposition
        minor = self.minor.contradiction()
        if minor.second in self.major.terms:
            minor_contraposition = Syllogism(self.major, conclusion, minor)
        else:
            assert minor.second in self.conclusion.terms
            minor_contraposition = Syllogism(conclusion, self.major, minor)

        return major_contraposition, minor_contraposition

    def converse(self):
        new_lines = []
        #premises
        for line in (self.major, self.minor):
            if line.quantifier in {'e','i'}:
                new_lines.append(Proposition(line.second, line.quantifier, line.first))
            else:
                new_lines.append(line)

        #conclusion
        if self.conclusion.quantifier in {'e', 'i'}:
            #exchange the premises
            new_lines = new_lines[::-1]
            new_lines.append(Proposition(self.conclusion.second, self.conclusion.quantifier, self.conclusion.first))
        else:
            new_lines.append(self.conclusion)
        return Syllogism(*new_lines)

    def obverse(self):
        if self.major.second == self.minor.second:
            major = self.major.contrary()
            minor = self.minor.contrary()
            return Syllogism(major, minor, self.conclusion)
        elif self.major.second == self.conclusion.second:
            major = self.major.contrary()
            conclusion = self.conclusion.contrary()
            return Syllogism(major, self.minor, conclusion)
        else:
            return self
