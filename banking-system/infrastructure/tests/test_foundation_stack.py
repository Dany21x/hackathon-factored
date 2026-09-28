import aws_cdk as cdk
from aws_cdk import assertions

from banking_infrastructure.foundation_stack import FoundationStack


def test_foundation_stack_outputs_project_and_environment() -> None:
    app = cdk.App()
    stack = FoundationStack(
        app,
        "test-foundation",
        project_name="banking-system",
        environment_name="dev",
    )

    template = assertions.Template.from_stack(stack)

    template.has_output(
        "ProjectName",
        {
            "Value": "banking-system",
            "Description": "Project name for shared resource naming.",
        },
    )
    template.has_output(
        "EnvironmentName",
        {
            "Value": "dev",
            "Description": "Deployment environment name.",
        },
    )
