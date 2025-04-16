import random

def simulate_trading(initial_capital, days, min_return=-0.01, max_return=0.01):
    """
    Simulates crypto trading with 3 trades per day.
    
    Parameters:
        initial_capital (float): Starting money
        days (int): Number of days to simulate
        min_return (float): Minimum return rate per trade (e.g. -0.01 for -1%)
        max_return (float): Maximum return rate per trade (e.g. 0.01 for +1%)
        
    Returns:
        final_capital (float): Capital after all trades
    """
    capital = initial_capital
    total_trades = 3 * days

    for _ in range(total_trades):
        # Simulate a return rate for each trade
        # trade_return = random.uniform(min_return, max_return)
        capital += capital * max_return

    return round(capital, 2)

# Example usage
initial_capital = 500 # Starting with $1,000
days = 30  # Trading for 30 days
# min_return = -2/100  # -2% per trade
max_return = 1/100   # +3% per trade
print(max_return) #, min_return)

final_capital = simulate_trading(initial_capital, days, -0.02, max_return)
print(f"After {days} days of trading, your capital would be approximately: ₹{final_capital}")
