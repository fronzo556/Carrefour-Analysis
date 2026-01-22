"""
Data models for purchase transactions.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class PurchaseTransaction:
    """Represents a single purchase transaction at Carrefour."""
    transaction_id: str
    timestamp: datetime
    cashier_id: str
    department: str
    product_category: str
    amount: float
    items_count: int
    customer_id: Optional[str] = None
    
    def to_dict(self):
        """Convert to dictionary for easier processing."""
        return {
            'transaction_id': self.transaction_id,
            'timestamp': self.timestamp,
            'cashier_id': self.cashier_id,
            'department': self.department,
            'product_category': self.product_category,
            'amount': self.amount,
            'items_count': self.items_count,
            'customer_id': self.customer_id
        }
