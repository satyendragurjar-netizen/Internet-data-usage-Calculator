#Internet data usage calculator
print("=" * 60)
print("              INTERNET DATA USAGE CALCULATOR")
print("=" * 60)
# data
name = input("Enter your name: ")
plan_name = input("Enter your data plan name: ")
monthly_limit = float(input("Enter monthly data limit (GB): "))
used_data = float(input("Enter data already used (GB): "))
days_used = int(input("Enter number of days used: "))
# Calculation
remaining_data = monthly_limit - used_data
usage_percentage = (used_data / monthly_limit) * 100
average_daily_usage = used_data / days_used
# monthly usage
estimated_monthly_usage = average_daily_usage * 30
estimated_remaining_data = monthly_limit - estimated_monthly_usage
# Extra data calculation
extra_data = estimated_monthly_usage - monthly_limit
# Exa. extra data cost
cost_per_gb = float(input("Enter extra data cost per GB (₹): "))
extra_data_cost = extra_data * cost_per_gb
# Output
print("\n" + "=" * 60)
print("                    DATA USAGE REPORT")
print("=" * 60)
print(f"Name                    : {name}")
print(f"Data Plan               : {plan_name}")
print(f"Monthly Data Limit      : {monthly_limit:.2f} GB")
print(f"Data Used               : {used_data:.2f} GB")
print(f"Data Remaining          : {remaining_data:.2f} GB")
print(f"Days Used               : {days_used}")
print(f"Average Daily Usage     : {average_daily_usage:.2f} GB")
print(f"Current Usage           : {usage_percentage:.2f}%")
print(f"Estimated Monthly Usage : {estimated_monthly_usage:.2f} GB")
print(f"Estimated Extra Data    : {extra_data:.2f} GB")
print(f"Extra Data Cost         : ₹{extra_data_cost:.2f}")
print("=" * 60)
print("             THANK YOU FOR USING THE PROGRAM")
print("=" * 60)
