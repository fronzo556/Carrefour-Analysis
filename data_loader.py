"""
Data loader module to load purchase transactions from CSV files.
"""
import csv
from datetime import datetime
from typing import List
from purchase_models import PurchaseTransaction


class PurchaseDataLoader:
    """Loads purchase transaction data from CSV files."""
    
    @staticmethod
    def load_from_csv(filepath: str) -> List[PurchaseTransaction]:
        """
        Load purchase transactions from a CSV file.
        
        Args:
            filepath: Path to the CSV file
            
        Returns:
            List of PurchaseTransaction objects
        """
        transactions = []
        
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = PurchaseTransaction(
                    transaction_id=row['transaction_id'],
                    timestamp=datetime.fromisoformat(row['timestamp']),
                    cashier_id=row['cashier_id'],
                    department=row['department'],
                    product_category=row['product_category'],
                    amount=float(row['amount']),
                    items_count=int(row['items_count']),
                    customer_id=row.get('customer_id', None)
                )
                transactions.append(transaction)
        
        return transactions
    
    @staticmethod
    def save_to_csv(transactions: List[PurchaseTransaction], filepath: str):
        """
        Save purchase transactions to a CSV file.
        
        Args:
            transactions: List of PurchaseTransaction objects
            filepath: Path to save the CSV file
        """
        if not transactions:
            return
            
        fieldnames = [
            'transaction_id', 'timestamp', 'cashier_id', 'department',
            'product_category', 'amount', 'items_count', 'customer_id'
        ]
        
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for transaction in transactions:
                row = transaction.to_dict()
                row['timestamp'] = row['timestamp'].isoformat()
                writer.writerow(row)
