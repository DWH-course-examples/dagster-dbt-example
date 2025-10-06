from pathlib import Path

from dagster_dbt import DbtProject

clickhouse_starschema_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "..", "dbt_clickhouse_lab").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
clickhouse_starschema_project.prepare_if_dev()