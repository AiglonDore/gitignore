import core
import core.help as help
import asyncio
import sys


async def main() -> None:
    """Main function."""
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        help.help()
        return

    if args[0] in ("-v", "--version"):
        print("Python GigIgnore package version ", help.VERSION)
        return

    print("Creating .gitignore file...")
    files = await core.get_gitignore_list()

    print("Writing .gitignore file...")
    with open(r".gitignore", "w") as f:
        for file in files:
            f.write(file + "\n")
    
    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
