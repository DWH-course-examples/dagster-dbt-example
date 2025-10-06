from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import clickhouse_starschema_dbt_assets
from .project import clickhouse_starschema_project
from .schedules import schedules

defs = Definitions(
    assets=[clickhouse_starschema_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=clickhouse_starschema_project),
    },
)