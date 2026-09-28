# Architecture

## Development Architecture

During early development, the application uses a hybrid local/AWS architecture.

Local:

- Next.js frontend
- FastAPI backend
- EDA / DuckDB
- unit and integration tests

AWS Dev:

- Bedrock AgentCore Runtime
- Amazon Bedrock models
- AgentCore Gateway and Lambda tools when required
- DynamoDB development data when required
- Bedrock Knowledge Base when RAG is introduced
- Secrets Manager
- CloudWatch / AgentCore Observability

Development flow:

Next.js (localhost)
    ↓
FastAPI (localhost)
    ↓
Bedrock AgentCore Runtime (AWS)
    ↓
AgentCore Gateway
    ↓
Lambda Tools
    ↓
DynamoDB

AgentCore should be integrated and tested against AWS from the beginning.

Frontend hosting, Cognito, API Gateway and FastAPI Lambda deployment are
introduced after the core workflows are validated locally.

---

## Target Architecture

User
 ↓
Next.js / AWS Amplify
 ↓
Amazon Cognito
 ↓
API Gateway
 ↓
FastAPI / Lambda
 ↓
Bedrock AgentCore Runtime
 ↓
AgentCore Gateway
 ├── read banking tools
 ├── identity verification
 ├── card actions
 └── escalation tools
        ↓
    DynamoDB

Supporting systems:

S3
    → raw hackathon dataset

Snowflake
    → data engineering
    → curated analytical models
    → exploratory analysis
    → baseline analysis
    → evaluation metrics

DynamoDB
    → operational banking simulation
    → cards
    → security facts
    → support tickets

Bedrock Knowledge Base
    → banking policies

Secrets Manager
    → sensitive application and integration configuration

CloudWatch / AgentCore Observability
    → logs, metrics and traces

---

## Responsibilities

### Frontend

Responsible for:

- authentication UI
- banking UI
- AI conversation UI
- customer confirmation

Not responsible for authorization.

### FastAPI

Responsible for:

- authenticated API
- session context
- API contracts
- invocation of AgentCore
- conventional application endpoints

### Agent

Responsible for:

- intent understanding
- conversation orchestration
- deciding which tool is needed
- clarification
- escalation reasoning

Not responsible for authorization.

### Banking Tools

Responsible for:

- retrieving trusted banking information
- enforcing business rules
- authorization
- performing actions
- verifying action results
- returning structured deterministic results

Sensitive actions must validate their own preconditions independently of
the agent.

### RAG

Responsible only for banking knowledge and policy retrieval.

RAG must never authorize banking actions or act as the source of truth for
customer-specific banking data.

### Data Platforms

DuckDB is used for local exploratory analysis.

S3 stores the raw hackathon dataset.

Snowflake is used for data engineering, analytics, baselines and evaluation.

DynamoDB is used for the operational banking simulation.

---

## Infrastructure

AWS infrastructure is managed using AWS CDK under:

`banking-system/infrastructure/`

The infrastructure project uses AWS CDK with Python.

Infrastructure is introduced incrementally as required.

Initial infrastructure should focus on:

- AgentCore
- required IAM permissions
- Secrets Manager

Additional resources such as DynamoDB, RAG infrastructure, API Gateway,
Cognito and application hosting are added when their corresponding
workflows require them.

Avoid manual AWS Console configuration when the resource can reasonably be
managed through CDK.
