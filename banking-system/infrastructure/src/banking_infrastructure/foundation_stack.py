import aws_cdk as cdk
from constructs import Construct


class FoundationStack(cdk.Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        project_name: str,
        environment_name: str,
        **kwargs: object,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        cdk.Tags.of(self).add("Project", project_name)
        cdk.Tags.of(self).add("Environment", environment_name)
        cdk.Tags.of(self).add("ManagedBy", "cdk")

        cdk.CfnOutput(
            self,
            "ProjectName",
            value=project_name,
            description="Project name for shared resource naming.",
        )

        cdk.CfnOutput(
            self,
            "EnvironmentName",
            value=environment_name,
            description="Deployment environment name.",
        )
