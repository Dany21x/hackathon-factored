# Product Specification

## Product

AI-first Card Emergency Support for a synthetic LATAM bank.

The system behaves as a banking service capable of safely completing
customer-service workflows, not merely as a conversational chatbot.

## Problem

Customers experiencing lost or stolen cards, suspicious transactions,
or possible identity impersonation need immediate assistance.

Traditional customer service can require waiting for a human agent even
when part of the workflow can be safely automated.

The system should automate safe steps while recognizing when it should not
act and when human intervention is required.

## Primary Demo Scenario

Customer:

> "Me robaron la billetera y veo una compra que no hice."

Expected system behavior:

1. Understand the incident.
2. Identify the affected card.
3. Perform step-up identity verification.
4. Retrieve recent transactions.
5. Ask whether suspicious transactions are recognized.
6. Ask for explicit confirmation before blocking.
7. Block the card through a deterministic banking tool.
8. Verify that the card is actually blocked.
9. If fraud or impersonation is suspected, create an urgent support case.
10. Provide a structured human handoff.

## Secondary Capabilities

- check card balance
- check card status
- retrieve recent transactions
- answer card policies using RAG
- lost or stolen card support
- suspicious transaction support
- human escalation

## Safety Boundary

The AI agent may decide which capability is needed, but it does not authorize
sensitive banking actions.

Authorization, identity verification, card ownership validation and action
preconditions are enforced deterministically by banking services/tools.

Security questions are simulated step-up verification for the prototype and
should not be presented as production-grade MFA.

## Human Handoff

When the system cannot safely complete a workflow, it should provide the
human agent with structured context.

Example:

```json
{
  "case_id": "...",
  "customer_verified": true,
  "intent": "stolen_card",
  "card_last_four": "4821",
  "card_blocked": true,
  "suspicious_transactions": [],
  "actions_taken": [],
  "risk_reason": "...",
  "unresolved_questions": []
}