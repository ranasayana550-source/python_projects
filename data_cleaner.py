# PORTFOLIO PROJECT: CUSTOMER DATA CLEANER
raw_data = [
    {"name": "Alice", "spent": 150.00},
    {"name": "Bob", "spent": 45.50},
    {"name": "Alice", "spent": 150.00},  
    {"name": "Charlie", "spent": -20.00}, 
    {"name": "David", "spent": 85.00}
]

def clean_and_filter_data(customer_list):
    clean_list = []      
    seen_names = set()   
    
    for customer in customer_list:
        name = customer["name"]
        spent = customer["spent"]
    
        if name in seen_names:
            print(f"Skipping duplicate: {name}")
            continue
            
        if spent < 0:
            print(f"Skipping invalid data (negative spent): {name}")
            continue 
            
        seen_names.add(name)
        clean_list.append(customer)
        
    return clean_list


print("--- STARTING DATA CLEANING ---")
final_clean_data = clean_and_filter_data(raw_data)

print("\n--- FINAL CLEANED DATA FOR THE CLIENT ---")
for customer in final_clean_data:
    print(f"Customer Name: {customer['name']} | Total Spent: ${customer['spent']:.2f}")
