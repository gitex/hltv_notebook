from pathlib import Path
from pydantic import BaseSettings, validator, BaseModel


class PathSettings(BaseSettings):
    root: Path = Path(__file__).parent.parent
    data: Path = root / 'data'
    html: Path = data / 'html'


class HLTVSettings(BaseSettings):
    base_url: str = 'https://www.hltv.org'


class Settings(BaseSettings):
    dirs: PathSettings = PathSettings()
    hltv: HLTVSettings = HLTVSettings()
