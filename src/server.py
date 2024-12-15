"""FastAPI server for Swarms deployment."""
from fastapi import FastAPI, HTTPException, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from swarms.config.tenant_config import MultiTenantManager, TenantConfig
from swarms import Agent
from swarms.models import OpenAIChat
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Swarms Multi-Tenant API",
    description="API for Swarms AI Agent Framework",
    version="0.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tenant_manager = MultiTenantManager()

async def get_tenant_id(x_tenant_id: str = Header(...)) -> str:
    """Validate tenant ID from request header."""
    try:
        tenant_manager.get_tenant_config(x_tenant_id)
        return x_tenant_id
    except ValueError:
        raise HTTPException(status_code=403, detail="Invalid tenant ID")

@app.get("/")
async def root():
    """Root endpoint."""
    return {"status": "ok", "message": "Swarms API is running"}

@app.post("/api/{tenant_id}/run_agent")
async def run_agent(
    tenant_id: str,
    task: str,
    system_prompt: str = "You are a helpful AI assistant.",
    x_tenant_id: str = Depends(get_tenant_id)
):
    """Run an agent for a specific tenant."""
    try:
        config = tenant_manager.get_tenant_config(tenant_id)
        
        # Initialize model with tenant-specific settings
        model = OpenAIChat(
            openai_api_key=config.api_key,
            model_name=config.model_config.get("model_name", "gpt-4"),
            temperature=float(config.model_config.get("temperature", "0.7"))
        )
        
        # Create agent with tenant configuration
        agent = Agent(
            agent_name=f"tenant-{tenant_id}-agent",
            system_prompt=system_prompt,
            llm=model,
            max_loops=config.custom_settings.get("max_loops", 1),
            verbose=True
        )
        
        # Run the task
        response = agent.run(task)
        return {"response": response, "tenant_id": tenant_id}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"} 