import requests
from datetime import datetime, timedelta

import db


class Match:
    def __init__(self, match_dict: dict):
        self.id = match_dict['id']
        self.competition = match_dict['competition']['code']
        self.status = match_dict['status']

        try:
            self.start_time = datetime.strptime(match_dict['utcDate'], '%Y-%m-%dT%H:%M:%SZ')
        except:
            self.start_time = None

        if match_dict['homeTeam']['name']:
            # one Dutch team has unencoded ' in their name
            self.home_team = match_dict['homeTeam']['name'].replace("'", "\'")
        else:
            # For schedule matches with undetermined teams
            self.home_team = "TBD"

        if match_dict['awayTeam']['name']:
            # one Dutch team has unencoded ' in their name
            self.away_team = match_dict['awayTeam']['name'].replace("'", "\'").replace('"', '\"')
        else:
            # For schedule matches with undetermined teams
            self.away_team = "TBD"

        try:
            self.last_updated = datetime.strptime(match_dict['lastUpdated'], '%Y-%m-%dT%H:%M:%SZ')
        except:
            self.last_updated = None

    def __str__(self):
        return f"{match.id}: {match.home_team} vs {match.away_team}"


def add_match(match: Match):
    if None in (match.home_team, match.away_team, match.start_time):
        return

    query = f'INSERT INTO matches(id, competiton, start_date_time, home_team, away_team, status, last_updated) ' \
                    f'VALUES({match.id}, "{match.competition}", "{match.start_time.strftime("%Y-%m-%d %H:%M:%S")}", ' \
                    f'"{match.home_team}", "{match.away_team}", "{match.status}", ' \
                    f'"{match.last_updated.strftime("%Y-%m-%d %H:%M:%S")}")'
    db.execute_commit(query)


def update_match(match: Match):
    if None in (match.home_team, match.away_team, match.start_time):
        return

    query = f'UPDATE matches set start_date_time = "{match.start_time.strftime("%Y-%m-%d %H:%M:%S")}", ' \
                f'status = "{match.status}", last_updated = "{match.last_updated}" WHERE id = {match.id}'
    db.execute_commit(query)


if __name__ == '__main__':
    # get known matches in database
    result = db.execute_query('SELECT id, last_updated FROM matches')
    known_matches = dict(result.fetchall())

    # date range: yesterday - one year from today
    # using yesterday in case of matches that didn't get updated yet
    date_from = datetime.today() - timedelta(days=1)
    date_to = date_from + timedelta(days=366)

    str_date_from = date_from.strftime('%Y-%m-%d')
    str_date_to = date_to.strftime('%Y-%m-%d')

    base_uri = 'https://api.football-data.org/v4/competitions'
    headers = {
        'X-Auth-Token': '81d39002fe874c15bba784f712906fa8'
    }

    # query tracked leagues
    result = db.execute_query('SELECT code FROM competitions')
    competitions = result.fetchall()

    # get matches for all 10 leagues (competitions)
    for comp in competitions:
        try:
            code = comp[0]
            # query API
            uri = base_uri + f'/{code}/matches?dateFrom={str_date_from}&dateTo={str_date_to}'

            response = requests.get(uri, headers=headers)

            matches = response.json()['matches']
            for match_dict in matches:
                match = Match(match_dict)

                if match.id not in known_matches.keys():
                    add_match(match)

                elif match.last_updated and match.last_updated > datetime.strptime(known_matches[match.id], '%Y-%m-%d %H:%M:%S'):
                    update_match(match)

        except Exception as e:
            print(f"{e}: {match_dict}\n")
