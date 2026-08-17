# test_secrets.py

# Trigger 1: recognized variable name pattern
password = "SuperSecretPassw0rd!"
BROKER_TOKEN="po258ef1-34d5-1234-y65e-p612461f1123c"
CLIENT_TOKEN="we234ef1-34d8-4156-r55e-e52461f1123c"

# Trigger 2: known provider key format (AWS Access Key ID pattern)
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"

# Trigger 3: hardcoded secret passed as a function parameter
def connect_to_db():
    return mysqli_connect("10.0.0.1", "admin", "pass123", "production_db")
