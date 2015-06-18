import logging
import sys
import argparse

logging.basicConfig(filename="snippets.log", level= logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associated name.

    Returns the name of the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})",format(name, snippet))
    return name, snippet

def get(name):
    """Retrieve the snippet with a given name.

    If there is no such snippet...

    Return the snippet.
    """
    logging.error("FIXME: Unimplemented - put({!r}",format(name))
    return name

def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retreive snippets of text")
    arguments= parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()
