"""TABLES STRUCT
    :          users
    :               - id   - bigint      > ID
    :               - tid  - bigint      > UID from user
    :               - name - varchar(30) > name of  user
    :               - age  - smallint    > age  of  user
    :               
    :        classes
    :               - id       - bigint      > ID
    :               - name     - varchar(30) > name of class
    :               - password - varchar(30) > password of class
    :
    : classesOfUsers
    :               - uid      - bigint > ID of user  from table:users
    :               - cid      - bigint > ID of class from table:classes    
    :               - status   - bool   > is user admin of group            
    :
    ? foreign keys
    ?       table:classesOfUsers:uid ? table:users:id
    ?       table:classesOfUsers:cid ? table:classes:id
"""

import asyncpg

from dotenv import load_dotenv
from os     import path, getenv, getcwd

class Database:
    def __init__(self) -> None:
        load_dotenv(path.join(getcwd(), '.env'))
        self.conn: asyncpg.Connection = None

    async def __aenter__(self):
        self.conn = await asyncpg.connect(
            
            database = getenv('database'),
            user     = getenv('user'),
            password = getenv('password'),
            host     = getenv('host'),
            port     = getenv('port')
        
        )

        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.conn.close()
