import os
import json

from app import config
from app.services.department import _parse_department_names, _is_ministry_or_subordinate_thereof


def test_department_names_parses() -> None:
    with open(os.path.join(config.PROJECT_DIR, config.DEPARTMENTS_JSON_FILENAME)) as f:
        departments = json.load(f).get('departments')
        department_names = [name for name in _parse_department_names(departments)]
        assert len(department_names) == 30
        assert department_names[0] == "Auswärtiges Amt"
        assert department_names[1] == "Bundesministerium der Justiz"
        assert department_names[2] == "Deutsches Patent- und Markenamt"
        assert department_names[3] == "Bundesamt für Justiz"
        assert department_names[4] == "Bundesministerium der Finanzen"


def test_is_ministry_or_subordinate_thereof() -> None:
    known_ministries_and_subordinates = [
        'Auswärtiges Amt',
        'Bundesministerium der Justiz',
        'Deutsches Patent- und Markenamt',
        'Bundesamt für Justiz',
        'Bundesministerium der Finanzen',
        'Bundeszentralamt für Steuern',
        'Generalzolldirektion',
        'ITZ-Bund',
        'Bundesministerium der Verteidigung',
        'Bundesministerium des Innern',
        'Bundesinstitut für Bau-, Stadt- und Raumforschung (BBSR) im Bundesamt für '
        'Bauwesen und Raumordnung (BBR)',
        'Bundesausgleichsamt',
        'Bundesverwaltungsamt',
        'Statistisches Bundesamt',
        'Bundesministerium für Arbeit und Soziales',
        'Bundesanstalt für Arbeitsschutz und Arbeitsmedizin ',
        'Bundesministerium für Bildung und Forschung',
        'Bundesministerium für Familie, Senioren, Frauen und Jugend',
        'Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung',
        'Bundesministerium für Wirtschaft und Energie',
        'Bundesamt für Wirtschaft und Ausfuhrkontrolle',
        'Bundesanstalt für Materialforschung und -prüfung ',
        'Bundesministerium für Ernährung und Landwirtschaft',
        'Bundesamt für Verbraucherschutz und Lebensmittelsicherheit',
        'Bundessortenamt',
        'Max Rubner-Institut',
        'Bundesministerium für Gesundheit',
        'Bundesamt für Soziale Sicherung',
        'Bundesministerium für Verkehr und digitale Infrastruktur',
        'mCLOUD',
    ]
    department_names_from_api = [
        'Bundesministerium für Bildung und Forschung',
        'Bundesministerium für Ernährung und Landwirtschaft',
        'Bundesministerium für Familie, Senioren, Frauen und Jugend',
        'Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung',
        'Bundesministerium für Wirtschaft und Klimaschutz',  # MISSING - should be found by keyword
        'Bundessortenamt',
        'Bundesversicherungsamt',
        'Bundesverwaltungsamt',
        'Bundeszentralamt für Steuern',
        'Der Bundesbeauftragte für den Datenschutz und die Informationsfreiheit',
        'Deutsche Nationalbibliothek',
        'Deutsches Patent- und Markenamt',
        'Die Beauftragte der Bundesregierung für Kultur und Medien',
        'Freistaat Sachsen',
        'Friedrich-Loeffler-Institut',
        'GDI-DE',
        'Generalzolldirektion',
        'ITZ-Bund',
        'Land Brandenburg',
        'Landeshauptstadt München',
        'Bundesanstalt für Materialforschung und -prüfung (BAM)',  # MISSING - should be found by keyword
    ]
    ministries_and_subordinates_from_api = [dep for dep in department_names_from_api if
                                            _is_ministry_or_subordinate_thereof(dep, known_ministries_and_subordinates)]
    assert 'Bundesministerium für Wirtschaft und Klimaschutz' in ministries_and_subordinates_from_api
    assert 'Bundesanstalt für Materialforschung und -prüfung (BAM)' in ministries_and_subordinates_from_api
