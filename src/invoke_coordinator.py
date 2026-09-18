from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient


# Microsoft Foundry project endpoint
endpoint = "https://agentathon-level3-resource.services.ai.azure.com/api/projects/agentathon-level3"

# Connect to the Foundry project using Azure authentication
project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

# Deployed Campus Support Coordinator
agent_name = "campus-support-coordinator"
agent_version = "4"

openai_client = project_client.get_openai_client()

# Send a request to the coordinator agent
response = openai_client.responses.create(
    input=[
        {
            "role": "user",
            "content": "Tell me what you can help with."
        }
    ],
    extra_body={
        "agent_reference": {
            "name": agent_name,
            "version": agent_version,
            "type": "agent_reference"
        }
    },
)

print("Campus Support Coordinator Response:")
print(response.output_text)
