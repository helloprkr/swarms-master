from typing import Dict, Optional
from pydantic import BaseModel

class TenantConfig(BaseModel):
    """Tenant configuration settings."""
    tenant_id: str
    api_key: str
    model_config: Dict[str, str]
    max_agents: int = 10
    rate_limit: int = 100
    custom_settings: Optional[Dict] = None

class MultiTenantManager:
    """Manages multi-tenant configurations and routing."""
    
    def __init__(self):
        self.tenants: Dict[str, TenantConfig] = {}
        
    def register_tenant(self, config: TenantConfig):
        """Register a new tenant."""
        self.tenants[config.tenant_id] = config
        
    def get_tenant_config(self, tenant_id: str) -> TenantConfig:
        """Get tenant configuration."""
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant {tenant_id} not found")
        return self.tenants[tenant_id] 