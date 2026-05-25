from dagster import define_asset_job, op, Out, job

main_job = define_asset_job(
    name="main_job",
    selection="*"
)

@op()
def extract_data(context):
    response =boto3.list_objects('incoming')

    data = [1,2,3,4]
    context.log.info(f'Extracted {len(data)} records')
    return data

@op
def load_data(context, transformed):
    context.log.info(f'Load {len(transformed)} records')

@op
def transform_data(data):
    return [x*x for x in data]

@job
def my_job(context):
    raw = extract_data()
    transform_data(raw)
    load_data(raw)

