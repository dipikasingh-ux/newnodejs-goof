# test_secrets.py

# Trigger 1: recognized variable name pattern
password = "SuperSecretPassw0rd!"
BROKER_TOKEN="ty248ef1-7t68-4145-r55e-f123461f1123c"
CLIENT_TOKEN="po256ef1-45d8-9875-t65e-k12461f1234c"

# Trigger 2: known provider key format (AWS Access Key ID pattern)
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"

# Trigger 3: hardcoded secret passed as a function parameter
def connect_to_db():
    return mysqli_connect("10.0.0.1", "admin", "pass123", "production_db")
