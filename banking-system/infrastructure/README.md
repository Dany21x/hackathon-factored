# Infrastructure

AWS CDK infrastructure for the banking system.

Phase 1 starts with a minimal CDK foundation. It does not deploy AgentCore,
Secrets Manager, IAM roles, DynamoDB, API Gateway, Cognito, Lambda, or Amplify
yet.

## AWS Profile

Use PowerShell as the standard shell for project AWS commands.

Configure the development profile if it does not already exist:

```powershell
aws configure --profile bedrock-dev-user
```

Verify the profile and selected account:

```powershell
aws sts get-caller-identity --profile bedrock-dev-user
```

Set the default region for the current PowerShell session:

```powershell
$env:AWS_PROFILE = "bedrock-dev-user"
$env:CDK_DEFAULT_REGION = "us-east-1"
```

## Local Development

Install dependencies:

```powershell
cd banking-system/infrastructure
uv sync
```

Run local checks:

```powershell
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

Synthesize the CDK app:

```powershell
npx aws-cdk@latest synth --profile bedrock-dev-user
```

The CDK app uses non-sensitive context from `cdk.json`. Secrets must not be
stored in CDK code, context, local files, or source control.

## Deployment

Do not deploy this stack until the corresponding phase explicitly requires it.

When deployment is required, use an explicit profile:

```powershell
npx aws-cdk@latest deploy --profile bedrock-dev-user
```

## Runtime Configuration

- Development AWS region: `us-east-1`
- Development AWS profile: `bedrock-dev-user`
- Sensitive values: AWS Secrets Manager, introduced in a later Phase 1 block
- Non-sensitive values: CDK context, safe defaults, or documented local config
