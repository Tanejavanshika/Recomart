import pandas as pd
import os

RAW_PATH = "data/raw"
VALIDATED_PATH = "data/validated"

def get_latest_raw_folder():
    folders = [f for f in os.listdir(RAW_PATH) if os.path.isdir(os.path.join(RAW_PATH, f))]
    folders.sort()
    return os.path.join(RAW_PATH, folders[-1]) if folders else None

def validate_user_interactions(df):
    report = {}

    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicate_rows"] = df.duplicated().sum()

    required_columns = ["user_id", "product_id", "event_type", "timestamp"]
    report["schema_valid"] = all(col in df.columns for col in required_columns)

    return report

def validate_transactions(df):
    report = {}

    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicate_rows"] = df.duplicated().sum()
    report["positive_quantity"] = (df["quantity"] > 0).all()
    report["positive_price"] = (df["price"] > 0).all()

    return report

def validate_external_signals(df):
    report = {}

    report["missing_values"] = df.isnull().sum().to_dict()
    report["duplicate_rows"] = df.duplicated().sum()
    report["valid_popularity_range"] = df["popularity_score"].between(0,1).all()

    return report

def find_csv_file(base_path, pattern):
    """Find CSV file matching pattern in subdirectories"""
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if pattern in file.lower() and file.endswith('.csv'):
                return os.path.join(root, file)
    return None

def run_validation():
    latest_folder = get_latest_raw_folder()
    
    if not latest_folder:
        print("No raw data folder found!")
        return

    print("Validating data from:", latest_folder)

    os.makedirs(VALIDATED_PATH, exist_ok=True)

    # Find CSV files in subdirectories
    interactions_path = find_csv_file(latest_folder, "interactions")
    transactions_path = find_csv_file(latest_folder, "transactions")
    
    if not interactions_path or not transactions_path:
        print(f"Error: Could not find required CSV files!")
        print(f"  Interactions: {interactions_path}")
        print(f"  Transactions: {transactions_path}")
        return

    # Load data
    interactions = pd.read_csv(interactions_path)
    transactions = pd.read_csv(transactions_path)
    
    # Validate
    interactions_report = validate_user_interactions(interactions)
    transactions_report = validate_transactions(transactions)

    # Save validated copies
    interactions.to_csv(os.path.join(VALIDATED_PATH, "user_interactions.csv"), index=False)
    transactions.to_csv(os.path.join(VALIDATED_PATH, "transactions.csv"), index=False)

    print("\n--- Data Quality Report ---")
    print("User Interactions:", interactions_report)
    print("Transactions:", transactions_report)

if __name__ == "__main__":
    run_validation()
