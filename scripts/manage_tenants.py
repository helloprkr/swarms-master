import os
from swarms.config.tenant_config import TenantConfig, MultiTenantManager

def setup_tenant(
    tenant_id: str,
    api_key: str,
    model_name: str = "gpt-4",
    temperature: float = 0.7,
    max_agents: int = 10,
    rate_limit: int = 100
) -> TenantConfig:
    """Setup a new tenant configuration."""
    config = TenantConfig(
        tenant_id=tenant_id,
        api_key=api_key,
        model_config={
            "model_name": model_name,
            "temperature": str(temperature)
        },
        max_agents=max_agents,
        rate_limit=rate_limit,
        custom_settings={
            "max_loops": 1,
            "autosave": True
        }
    )
    return config

def main():
    """Main tenant management function."""
    manager = MultiTenantManager()
    
    # Example tenant setup
    tenant1 = setup_tenant(
        tenant_id="tenant1",
        api_key=os.getenv("TENANT1_API_KEY"),
        model_name="gpt-4"
    )
    
    tenant2 = setup_tenant(
        tenant_id="tenant2",
        api_key=os.getenv("TENANT2_API_KEY"),
        model_name="gpt-3.5-turbo",
        max_agents=5
    )
    
    # Register tenants
    manager.register_tenant(tenant1)
    manager.register_tenant(tenant2)
    
    return manager

if __name__ == "__main__":
    main() 