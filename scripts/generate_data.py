# import pandas as pd
# import random
# from datetime import datetime, timedelta
# def generate_nigerian_sales(num_records=20000):
#     """Generate realistic Nigerian e-commerce data"""
    
#     # Nigerian context
#     products = {
#         'Electronics': ['Samsung Galaxy', 'iPhone', 'HP Laptop', 'LG TV', 'JBL Speaker'],
#         'Fashion': ['Ankara Dress', 'Senator Outfit', 'Nike Sneakers', 'Gucci Bag', 'Wristwatch'],
#         'Home': ['Cooking Pot', 'Blender', 'Rice Cooker', 'Table Lamp', 'Rug'],
#         'Beauty': ['Makeup Kit', 'Hair Extension', 'Perfume', 'Skincare Set', 'Nail Polish']
#     }
    
#     nigerian_cities = ['Lagos', 'Abuja', 'Port Harcourt', 'Kano', 'Ibadan', 'Enugu']
    
#     data = []
#     start_date = datetime(2023, 1, 1)
    
#     for i in range(num_records):
#         category = random.choice(list(products.keys()))
#         product = random.choice(products[category])
        
#         quantity = random.randint(1, 5)
#         unit_price = round(random.uniform(5000, 500000), 2)  # Naira prices
#         revenue = round(quantity * unit_price, 2)
        
#         record = {
#             'transaction_id': f'TXN{i+1:06d}',
#             'order_date': start_date + timedelta(days=random.randint(0, 730)),
#             'product_name': product,
#             'category': category,
#             'quantity': quantity,
#             'unit_price': unit_price,
#             'revenue': revenue,
#             'city': random.choice(nigerian_cities),
#             'payment_method': random.choice(['Card', 'Transfer', 'USSD', 'Cash']),
#             'delivery_status': random.choice(['Delivered', 'Pending', 'Cancelled'])
#         }
        
#         data.append(record)
    
#     df = pd.DataFrame(data)
#     df = df.sort_values('order_date').reset_index(drop=True)
#     return df

# if __name__ == "__main__":
#     print("Generating 20,000 Nigerian e-commerce records...")
#     df = generate_nigerian_sales(20000)
#     df.to_csv('data/raw/sales_data.csv', index=False)


"""Clean and prepare sales data"""
import pandas as pd

def clean_sales_data():
    print("Loading data...")
    df = pd.read_csv('data/raw/sales_data.csv')
    print(f"Loaded: {len(df):,} records")
    
    # Convert date
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # Remove any nulls
    df = df.dropna()
    
    # Add time features
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['month_name'] = df['order_date'].dt.strftime('%B')
    df['quarter'] = df['order_date'].dt.quarter
    
    # Sort by date
    df = df.sort_values('order_date').reset_index(drop=True)
    
    # Save
    df.to_csv('data/processed/sales_clean.csv', index=False)
    print(f"✅ Cleaned: {len(df):,} records")
    print(f"Date range: {df['order_date'].min().date()} to {df['order_date'].max().date()}")
    print(f"Total revenue: ₦{df['revenue'].sum():,.2f}")

if __name__ == "__main__":
    clean_sales_data()