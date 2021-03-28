import boto3
import click

@click.command()
@click.option("--cluster", help="Name of the ECS cluster", required=True)
@click.option("--service", help="Name of the ECS service", required=True)
def deploy(cluster, service):
    client = boto3.client("ecs")

    container_definitions = []
    response = get_current_task_definition(client, cluster, service)
    for container_definition in response["taskDefinition"]["containerDefinitions"]:
        new_def = container_definition.copy()
        container_definitions.append(new_def)

    response = client.register_task_definition(
        family=response["taskDefinition"]["family"],
        volumes=response["taskDefinition"]["volumes"],
        containerDefinitions=container_definitions,
    )
    new_task_arn = response["taskDefinition"]["taskDefinitionArn"]

    response = client.update_service(
        cluster=cluster, service=service, taskDefinition=new_task_arn,
    )
