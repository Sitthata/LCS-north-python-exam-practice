discount_map = {
    "CASH": 0.05,
    "BIRTHDAY": 0.1,
    "COVID": 0.3
}


def main():
    try:
        # Prompt for the number of customers
        customer_count_input = input('Input (Number of customers): ').strip()
        customer_count = int(customer_count_input)
    except ValueError:
        print('Invalid customer count')
        return

    # Validate the number of customers
    if customer_count < 1:
        print('Invalid customer count')
        return

    # Prompt for the discount code (can be blank)
    discount_code_input = input('Input (Discount code): ').strip()

    # Determine the discount rate based on the discount code
    discount_rate = discount_map.get(discount_code_input.upper(), 0.0)

    # Get the price per person based on the number of customers
    price_per_person = get_price(customer_count)
    if price_per_person == 0:
        print('Invalid number of customers')
        return

    # Calculate the subtotal
    subtotal = customer_count * price_per_person

    # Calculate the actual price after applying the discount
    actual_price = apply_discount(subtotal, discount_rate)

    # Calculate the discount percentage for display
    discount_percentage = int(discount_rate * 100)

    # Print the outputs in the required format
    print(f'{customer_count} person{"s" if customer_count > 1 else ""} x {price_per_person:.2f} baht')
    print(f'A subtotal price is {subtotal:.2f} baht')
    print(f'On-top discount {discount_percentage}%')
    print(f'A total price is {actual_price:.2f} baht')


def apply_discount(price: float, discount_rate: float) -> float:
    """
    Applies the discount to the given price.

    :param price: The original price before discount.
    :param discount_rate: The discount rate as a decimal.
    :return: The price after applying the discount.
    """
    return price - (price * discount_rate)


def get_price(n: int) -> float:
    """
    Determines the price per person based on the number of customers.

    :param n: Number of customers.
    :return: Price per person.
    """
    if 1 <= n <= 3:
        return 399.00
    elif 4 <= n <= 6:
        return 499.00
    elif n > 6:
        return 599.00
    else:
        return 0.00  # This case should not occur due to prior validation


if __name__ == '__main__':
    main()
