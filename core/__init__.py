import asyncio
import sys
import aiohttp
import async_lru

URL = r"https://www.toptal.com/developers/gitignore/api/"


@async_lru.alru_cache(maxsize=1024)
async def get_gitignore(language: str) -> str:
    """Get the `.gitignore` file for the selected language.

    Args:
        language (str): language.

    Returns:
        str: Git ignore file.
    """
    url = URL + language
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_gitignore_list(*args) -> list[str]:
    """Gets the files associated to the languages.

    Returns:
        list[str]: list of files.
    """
    return await asyncio.gather(
        *[get_gitignore(lang) for lang in (args or sys.argv[1:]) if not lang.startswith("-")]
    )
