def generate_unique_id(existing_ids, prefix='ITEM'):
    """
    Generates a unique ID for a new library item

    Args: 
        existing_ids (list): List of existing item IDs.
        prefix (str): Prefix for the ID.

    Returns:
        str: A unique item ID.
    """
    number = 1
    while True:
        new_id = f"{prefix}{number:04d}"
        if new_id not in existing_ids:
            return new_id
        number += 1

def validate_email(email):
    """
    Simple email validation

     Args: 
        email (str): the email address to validate

    Returns:
        bool; True if valid, False otherwise
    """
    return "@" in email and "." in email