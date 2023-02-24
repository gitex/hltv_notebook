from settings import Settings

from .download import DownloadMatchesContainer
from .analyze import AnalyzeMatchesContainer


analyze_container = AnalyzeMatchesContainer()
analyze_container.config.from_pydantic(Settings())
analyze_container.wire(modules=[__name__])
