import core
import core.help as help
import asyncio
import sys


async def make_git_ignore(*args: str) -> None:
    """Builds the file."""
    try:
        core.check_if_file_exists()
        files = await core.get_gitignore_list(*args)
        
        print("Creating .gitignore file...")
        with open(r".gitignore", "w") as f:
            for file in files:
                f.write(file + "\n")

        print("Done!")
    except Exception as e:
        print(e, file=sys.stderr)


async def main(*args: str) -> None:
    """Main function."""
    if not args or args[0] in ("-h", "--help"):
        help.help()

    elif args[0] in ("-v", "--version"):
        print("Python AIOGitIgnore package version ", help.VERSION)

    else:
        await make_git_ignore(*[arg for arg in args if not arg.startswith("-")])


if __name__ == "__main__":
    asyncio.run(main(*(sys.argv[1:])))
