#!/usr/bin/env python3

import argparse

from {{ cookiecutter.repo_name | replace('-', '_') }} import {{ cookiecutter.repo_name | replace('-', '') }}


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()


if __name__ == '__main__':
    main()
