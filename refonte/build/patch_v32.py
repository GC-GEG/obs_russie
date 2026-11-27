# Passe 32 : apostrophe droite dans toute la méthodologie, à la place de l'apostrophe courbe (décision de Marin du 27/11/2026). IT et ES : scripts/i18n.py et refonte/i18n/i18n_production.py.
_i = t.find('const METHODE = [')
_j = t.find('\n];', _i)
if _i < 0 or _j < 0:
    sys.exit('PASSE 32 : méthodologie introuvable')
_n = t[_i:_j].count('’')
if _n != 71:
    sys.exit('PASSE 32 : %d apostrophes courbes dans la méthodologie, 71 attendues' % _n)
t = t[:_i] + t[_i:_j].replace('’', "'") + t[_j:]
