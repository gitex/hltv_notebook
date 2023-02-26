import click
from dependency_injector.wiring import Provide, inject

from api.containers import DownloadMatchesContainer
from api.services import DownloadMatchesService
from settings import Settings


@click.command()
@click.option('--page', default=1, help='Page on HLTV')
@inject
def download_page_of_matches(
        page: int,
        service: DownloadMatchesService = Provide[DownloadMatchesContainer.service]
):
    service.download_matches_by_page(page)
    click.echo(f'Page {page} stored!')


if __name__ == '__main__':
    download_matches_container = DownloadMatchesContainer()
    download_matches_container.config.from_pydantic(Settings())
    download_matches_container.wire(modules=[__name__])

    download_page_of_matches()
