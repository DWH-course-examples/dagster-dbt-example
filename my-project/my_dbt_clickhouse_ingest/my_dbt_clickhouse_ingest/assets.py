from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import clickhouse_starschema_project


@dbt_assets(manifest=clickhouse_starschema_project.manifest_path)
def clickhouse_starschema_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    