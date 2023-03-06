from pathlib import Path
from pydantic import BaseSettings


class PathSettings(BaseSettings):
    root: Path = Path(__file__).parent.parent
    data: Path = root / 'data'
    html: Path = data / 'html'
    csv: Path = data / 'csv'
    csv_matches: Path = csv / 'matches'
    original_csv_matches: Path = csv_matches / 'original'
    split_by_teams_csv_matches: Path = csv_matches / 'split_by_teams.csv'


class HLTVSettings(BaseSettings):
    base_url: str = 'https://www.hltv.org'

    class Config:
        env_prefix = 'hltv_'


class Settings(BaseSettings):
    dirs: PathSettings = PathSettings()
    hltv: HLTVSettings = HLTVSettings()


settings = Settings()
