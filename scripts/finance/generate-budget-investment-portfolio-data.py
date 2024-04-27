import random
from datetime import datetime, timedelta

# List of assets code
assets = [
    "BCA-MCARD-ISTRI", "BNI-MCARD-ISTRI", "JEN-MCARD-MAS", "JEN-ECARD-MAS",
    "JEN-FSE-MAS", "JEN-MS-MAS", "BIBIT-EMERGENCY", "BIBIT-RETIRE",
    "BAREKSAMM-BNIAM", "BAREKSAMM-MANDIRI", "BAREKSAMM-MAYBANK",
    "BAREKSAMM-SUCOR", "BAREKSAS-SIMAS", "BAREKSAS-SUCOR",
    "BAREKSAS-SUCORSHARIA", "EMONEY-GOPAY-MAS", "EMONEY-GOPAY-ISTRI"
]

# Function to generate random date within the year 2024
def random_date():
    start_date = datetime(2028, 1, 1)
    end_date = datetime(2028, 12, 30)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

# Function to generate random transaction data
def generate_data(action):
    asset = random.choice(assets)
    transaction_date = random_date().strftime("%d/%m/%Y")
    month = random_date().strftime("%B")
    year = random_date().strftime("%Y")
    # action = random.choice(["BUY","SELL"])
    amount = random.randint(100000, 1000000)
    quantity = "{:.2f}".format(random.uniform(0.1, 10.0))
    note = random.choice(["-"])

    return f"{asset}\t{transaction_date}\t{month}\t{year}\t{action}\t{amount}\t{quantity}\t{note}"

# Generate 50 data entries
data_entries = []
for _ in range(30):
    data_entries.append(generate_data("BUY"))

for _ in range(6):
    data_entries.append(generate_data("SELL"))

# Print the generated data
for i, entry in enumerate(data_entries, start=1):
    print(f"{i}\t{entry}")
