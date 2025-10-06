from setuptools import find_packages, setup

setup(
    name="my_dbt_clickhouse_ingest",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "my_dbt_clickhouse_ingest": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-clickhouse<1.9",
        "dbt-clickhouse<1.9",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)