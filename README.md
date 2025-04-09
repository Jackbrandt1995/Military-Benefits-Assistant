# VA Benefits Assistant

This is a Vercel-ready OpenAI-powered assistant that helps users access and apply for military education benefits.

## Setup

1. Add the following Environment Variables in Vercel:
   - `OPENAI_API_KEY`
   - `OPENAI_ORG_ID`
   - `SERPER_API_KEY`

2. Deploy the project via GitHub or upload ZIP directly.

3. Frontend can call the assistant via:
   POST /api/chat
   Body: { "user_input": "How do I apply for Tuition Assistance?" }

## Features
- GPT-4o-mini assistant
- Real-time web search via Serper.dev
- Form fill + simulated submit tools
- SOC-2/HIPAA-conscious handling
