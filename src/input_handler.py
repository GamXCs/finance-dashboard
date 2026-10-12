
def get_initial_investment_collection() -> float:
    while True:
        try:
            investement = round(float(input("Enter Your Initial Investment: ")), 2)
            if investement <= 0:
                print("Investment must be greater than 0")
                continue

            
            print("Investment:$",investement, "\n")
            return investement
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_rate_of_return_collection() -> float:
    while True:
        try:
            rate_of_return = round(float(input("Enter Your Rate of Return: ")), 2) / 100
            if rate_of_return <= 0:
                print("Rate of Return must be positive or Greater than Zero")
                continue

            print("Rate of Return:%",rate_of_return, "\n")
            return rate_of_return
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_length_of_time_collection() -> int:
    while True:
        try:
            length_time = round(int(input("Enter Length of Time of Investment as Years: ")), 0)
            if length_time < 0:
                print("Length of Time Must Be Positive")
                continue
            
            print("Length of Time of Investment:", length_time,"Years", "\n")
            return length_time
        except ValueError as ve:
            print(f"Value Error: {ve}")


def get_contribute_monthly() -> int:
    while True:
        try:
            monthly = int(input("How much would you contribute monthly: $"))
            if monthly < 0:
                print("Monthly Contribution must be greater than 0")
                continue

            print("Monthly Contributions: $", monthly, "\n")
            return monthly
        except ValueError as ve:
            print(f"Value Error: {ve}")


def main():
   pass

if __name__ == "__main__":
    main()