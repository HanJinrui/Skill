sea_sick = lambda s: ['No Problem', 'Throw Up'][s.count('~_') + s.count('_~') > 0.2 * len(s)]
