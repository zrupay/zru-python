
# ZRU Python SDK

## Overview

The ZRU Python SDK provides easy access to the ZRU API, allowing developers to manage transactions, products, plans, taxes, subscriptions, and notifications seamlessly.

[![Coverage Status](https://coveralls.io/repos/github/zru/zru-python/badge.svg?branch=master)](https://coveralls.io/github/zru/zru-python?branch=master)

## Installation

Install the SDK via pip:

```bash
pip install --upgrade zru-python
```

Alternatively, you can use `easy_install`:

```bash
easy_install --upgrade zru-python
```

To install from the source, run:

```bash
python setup.py install
```

## Migration Guide for Versions Prior to 1.x.x

If you're upgrading from a version earlier than 1.x.x, you will need to update your import statements to reflect the transition from `mc2p` to `zru`. Here's a guide to help with this transition:

### Updating Import Statements

Replace any imports from the `mc2p` module with `zru`.

#### Example:

Before:
```python
from mc2p.errors import InvalidRequestError
```
After:
```python
from zru.errors import InvalidRequestError
```

### Updating the Client Class

Replace instances of `MC2PClient` with `ZRUClient`.

#### Example:

Before:
```python
client = MC2PClient(...)
```

After:
```python
client = ZRUClient(...)
```

### Steps to Update Your Code

1. **Search and Replace**: Use an IDE or text editor to search for `mc2p` and replace it with `zru`.
2. **Verify Imports**: Ensure all import statements now reference `zru`.
3. **Run Tests**: Test your code to ensure everything functions correctly after the migration.

## Summary

Following these steps will help you migrate your project from versions prior to 1.x.x, ensuring compatibility with the new `zru` module naming convention.

## Quick Start Example

```python
from zru import ZRUClient

zru = ZRUClient('API_KEY', 'SECRET_KEY')

# Create a transaction
transaction = zru.Transaction({
    "currency": "EUR",
    "products": [{
        "amount": 1,
        "product_id": "PRODUCT-ID"
    }]
})

# Create a transaction with product details
transaction = zru.Transaction({
    "currency": "EUR",
    "products": [{
        "amount": 1,
        "product": {
            "name": "Product",
            "price": 5
        }
    }]
})
transaction.save()

# Get payment URLs
print('Payment URL:', transaction.pay_url)     # URL for user to complete the payment
print('Iframe URL:', transaction.iframe_url)  # URL for embedding in an iframe

# List available plans
plans_paginator = zru.Plan.list()
print('Plan Count:', plans_paginator.count)
print('Plan Results:', plans_paginator.results)    # List of plans
plans_paginator.get_next_list()  # Fetch next set of plans

# Get a product, update its price, and save changes
product = zru.Product.get("PRODUCT-ID")
product.price = 10
product.save()

# Create and delete a tax
tax = zru.Tax({
    "name": "Tax",
    "percent": 5
})
tax.save()
tax.delete()

# Check if a transaction is paid
transaction = zru.Transaction.get("TRANSACTION-ID")
is_paid = transaction.status == 'D'  # 'D' stands for 'Paid'
print('Transaction Paid:', is_paid)

# Create a subscription
subscription = zru.Subscription({
    "currency": "EUR",
    "plan_id": "PLAN-ID",
    "note": "Note example"
})

# Create a subscription with plan details
subscription = zru.Subscription({
    "currency": "EUR",
    "plan": {
        "name": "Plan",
        "price": 5,
        "duration": 1,
        "unit": "M",
        "recurring": True
    },
    "note": "Note example"
})
subscription.save()

# Get subscription payment URLs
print('Subscription Payment URL:', subscription.pay_url)     # URL for user to complete the subscription payment
print('Subscription Iframe URL:', subscription.iframe_url)  # URL for embedding in an iframe

# Handling notifications
notification_data = zru.NotificationData(JSON_DICT_RECEIVED_FROM_ZRU)
is_paid = notification_data.is_status_done   # Check if payment is completed
print('Notification Payment Status:', is_paid)
transaction = notification_data.transaction  # Get the transaction details
sale = notification_data.sale                # Get the sale details
```

## Handling Exceptions

```python
from zru.errors import InvalidRequestError

# Example of incorrect data
shipping = zru.Shipping({
    "name": "Normal shipping",
    "price": "text"  # Price must be a number
})

try:
    shipping.save()
except InvalidRequestError as e:
    print("Error:", e._message)      # Status code of the error
    print("Details:", e.json_body)   # JSON response from the server
    print("Resource:", e.resource)   # The resource involved in the error
    print("Resource ID:", e.resource_id)  # The resource ID that caused the error
```