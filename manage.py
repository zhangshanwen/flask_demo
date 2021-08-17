#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(repository='migrations', url='mysql+mysqlconnector://root:123456@127.0.0.1:3306/ya', debug='False')
