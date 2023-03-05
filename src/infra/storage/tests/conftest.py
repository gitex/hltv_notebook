from pathlib import Path
from uuid import uuid4

import pytest
import pandas as pd

from infra.storage import HtmlRepository, DataType
from infra.storage.structs import Filename
from infra.hltv_client.http_client import Response, Html
from infra.stubs import CSV
from infra.storage.constants import CSV_DELIMITER


@pytest.fixture(scope='session')
def matches_html() -> Html:
    return Html(
        """
        <html>
        <head>
            <title>Matches - HLTV.org</title>
        </head>
        <body>
        
            <table>
                <thead>
                    <tr>
                        <th>Match id</th>
                        <th>Event</th>
                        <th>Map</th>
                        <th>Team 1</th>
                        <th>Team 2</th>
                        <th>Result</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="matchstats-id"><a href="/matches/2342497/heroic-vs-g2-blast-premier-spring-showdown-2021"><span class="match-id" data-zonedgrouping-entry-unix="1619594400000">2342497</span></a></td>
                        <td><a href="/events/5812/blast-premier-spring-showdown-2021"><img src="https://static.hltv.org/images/eventLogos/000/005/812/medium/BUcXrJ7VIAE6rD_.png" title="BLAST Premier Spring Showdown 2021"></a></td>
                        <td><a href="/maps/19235/nuke">Nuke</a></td>
                        <td class="team-cell"><a href="/team/7175/heroic"><img src="https://static.hltv.org/images/team/logo/7175" alt="Heroic" title="Heroic" class="logo"></a></td>
                        <td class="team-cell"><a href="/team/5995/g2"><img src="https://static.hltv.org/images/team/logo/5995" alt="G2" title="G2" class="logo"></a></td>
                        <td><div class="won">16-14</div></td>
                    </tr>
                    <tr>
                        <td class="matchstats-id"><a href="/matches/2342494/liquid-vs-virtuspro-iem-summer-2021-north-america-qualifier"><span class="match-id" data-zonedgrouping-entry-unix="1619578200000">2342494</span></a></td>
                        <td><a href="/events/5833/iem-summer-2021-north-america-qualifier"><img src="https://static.hltv.org/images/eventLogos/000/005/833/medium/PypzbZb.png" title="IEM Summer 2021 North America Qualifier"></a></td>
                        <td><a href="/maps/19235/nuke">Nuke</a></td>
                        <td class="team-cell"><a href="/team/5973/liquid"><img src="https://static.hltv.org/images/team/logo/5973" alt="Liquid" title="Liquid" class="logo"></a></td>
                        <td class="team-cell"><a href="/team/5378/virtuspro"><img src="https://static.hltv.org/images/team/logo/5378" alt="Virtus.pro" title="Virtus.pro" class="logo"></a></td>
                        <td><div class="lost">7-16</div></td>
                    </tr>
                    <tr>
                        <td class="matchstats-id"><a href="/matches/2342493/liquid-vs-virtuspro-iem-summer-2021-north-america-qualifier"><span class="match-id" data-zonedgrouping-entry-unix="1619578200000">2342493</span></a></td>
                        <td><a href="/events/5833/iem-summer-2021-north-america-qualifier"><img src="https://static.hltv.org/images/eventLogos/000/005/833/medium/PypzbZb.png" title="IEM Summer 2021 North America Qualifier"></a></td>
                        <td><a href="/maps/19235/nuke">Nuke</a></td>
                        <td class="team-cell"><a href="/team/5973/liquid"><img src="https://static.hltv.org/images/team/logo/5973" alt="Liquid" title="Liquid" class="logo"></a></td>
                        <td class="team-cell"><a href="/team/5378/virtuspro"><img src="https://static.hltv.org/images/team/logo/5378" alt="Virtus.pro" title="Virtus.pro" class="logo"></a></td>
                        <td><div class="lost">7-16</div></td>
                    </tr>
                </tbody>
            </table>
        </body>
        </html>                         
        """.strip('\n').strip()
    )


@pytest.fixture
def matches_response(matches_html) -> Response:
    return Response(
        ok=True,
        status_code=200,
        data={},
        content=Html(matches_html),
    )


@pytest.fixture(scope='session')
def data_dir(tmp_path_factory) -> Path:
    return tmp_path_factory.mktemp("data")


@pytest.fixture(scope='session')
def html_dir(data_dir) -> Path:
    path = data_dir / 'html'
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture(scope='session')
def matches_dir(html_dir) -> Path:
    path = html_dir / 'matches'
    path.mkdir(exist_ok=True)
    return path


@pytest.fixture(scope='session')
def make_html_files_of_matches(matches_dir, matches_html) -> list[Path]:
    html_files: list[Path] = []

    for _ in range(5):
        path = matches_dir / Filename.generate_on_current_datetime('html').as_str()
        html_files.append(path)
        path.write_text(matches_html)

    return html_files


@pytest.fixture(scope='session')
def matches_html_repository(data_dir) -> HtmlRepository:
    return HtmlRepository(context=data_dir, data_type=DataType.MATCHES)


@pytest.fixture
def mock_repository(mocker):
    return mocker.Mock()


@pytest.fixture
def secret_code() -> str:
    return str(uuid4())


@pytest.fixture(scope='session')
def csv_headers() -> list:
    return ['a', 'b', 'c']


@pytest.fixture(scope='session')
def csv_values() -> list[list]:
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@pytest.fixture(scope='session')
def csv(csv_headers, csv_values) -> CSV:
    df = pd.DataFrame(csv_values, columns=csv_headers)

    return CSV(df.to_csv(index=False, sep=',', encoding='utf-8', header=True))
