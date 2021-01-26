#!/usr/bin/env python3

import argparse

from {{ cookiecutter.repo_name }} import {{ cookiecutter.script_name }}


def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()


if __main__ == '__main__':
    main()
