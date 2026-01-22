"""
Data models for personnel management.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict


@dataclass
class EmployeePerformance:
    """Represents employee performance metrics derived from purchase data."""
    employee_id: str
    employee_name: str
    department: str
    period_start: datetime
    period_end: datetime
    total_transactions: int
    total_revenue: float
    avg_transaction_value: float
    transactions_per_hour: float
    efficiency_score: float
    
    def to_dict(self):
        """Convert to dictionary for reporting."""
        return {
            'employee_id': self.employee_id,
            'employee_name': self.employee_name,
            'department': self.department,
            'period_start': self.period_start,
            'period_end': self.period_end,
            'total_transactions': self.total_transactions,
            'total_revenue': self.total_revenue,
            'avg_transaction_value': self.avg_transaction_value,
            'transactions_per_hour': self.transactions_per_hour,
            'efficiency_score': self.efficiency_score
        }


@dataclass
class StaffingRequirement:
    """Represents staffing requirements based on purchase patterns."""
    department: str
    date: datetime
    hour: int
    required_staff: int
    expected_transactions: int
    expected_revenue: float
    
    def to_dict(self):
        """Convert to dictionary for reporting."""
        return {
            'department': self.department,
            'date': self.date,
            'hour': self.hour,
            'required_staff': self.required_staff,
            'expected_transactions': self.expected_transactions,
            'expected_revenue': self.expected_revenue
        }


@dataclass
class PersonnelReport:
    """Complete personnel management report."""
    report_date: datetime
    employee_performances: List[EmployeePerformance]
    staffing_requirements: List[StaffingRequirement]
    summary: Dict[str, any]
    
    def to_dict(self):
        """Convert to dictionary for reporting."""
        return {
            'report_date': self.report_date,
            'employee_performances': [ep.to_dict() for ep in self.employee_performances],
            'staffing_requirements': [sr.to_dict() for sr in self.staffing_requirements],
            'summary': self.summary
        }
