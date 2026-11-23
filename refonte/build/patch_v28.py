# Passe 28 (23/11/2026) : date de mise à jour d'un événement (colonne Q « Date mise à jour », champ « maj » des données,
# règle F5). Décision de Marin du 23/11/2026, libellés validés le même jour.
# - « N derniers événements » / « Ajoutés depuis le … » : inchangés, fondés sur la Date entrée seule (FRESH).
# - Date « Mise à jour » de l'ouverture : la plus récente des Dates entrée et des Dates mise à jour.
# - Fiche : ligne « Mis à jour le … » sous la ligne date - lieu quand « maj » est rempli.
# Chronologie, constat « Dernière semaine », moyennes et compteur total : inchangés (Date événement ou sans date).
# Champ « maj » absent (anciennes données) : traité comme vide.

sub("lastUpdate: D ? fDot(lastEntry) : '…',",
    "lastUpdate: D ? fDot(EV.reduce((m, e) => (e.maj && e.maj > m ? e.maj : m), lastEntry)) : '…',")

sub("dateLong: fLong(s.date), entree: fLong(s.entree),",
    "dateLong: fLong(s.date), entree: fLong(s.entree), majOn: !!s.maj, maj: s.maj ? 'Mis à jour le ' + fLong(s.maj) : '',")
sub("dateLong: '', entree: '',",
    "dateLong: '', entree: '', majOn: false, maj: '',")

sub('{{sel.dateLong}} - {{sel.lieu}}</span>\n            <sc-if value="{{sel.passe}}"',
    '{{sel.dateLong}} - {{sel.lieu}}</span>\n'
    '            <sc-if value="{{sel.majOn}}" hint-placeholder-val="{{false}}">\n'
    '              <span class="fiche-m" style="font-size: 13px; line-height: 1.3; color: #a3a09a; margin-top: -4px;">{{sel.maj}}</span>\n'
    '            </sc-if>\n'
    '            <sc-if value="{{sel.passe}}"')
