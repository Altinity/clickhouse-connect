from setuptools import setup, find_packages


setup(
    name='clickhouse-connect',
    version='0.0.1',
    author='ClickHouse Inc.',
    author_email='clickhouse-connect@clickhouse.com',
    packages=find_packages(exclude=['tests*']),
    python_requires="~=3.7",
    install_requires=[
        'requests',
        'pytz'
    ],
    test_requires=[
        'sqlalchemy>1.3.21, <1.4'
        'apache_superset>=1.4.1'
    ],
    extras_requires={
        'sqlalchemy': ['sqlalchemy>1.3.21, <1.4'],
        'superset': ['apache_superset>=1.4.1', 'sqlalchemy>1.3.21, <1.4']
    },
    entry_points={
        'sqlalchemy.dialects': ['clickhousedb.connect=clickhouse_connect.sqlalchemy.dialect:ClickHouseDialect'],
        'superset.db_engine_specs': ['clickhousedb=clickhouse_connect.superset.engine:ClickHouseEngineSpec']
    }
)