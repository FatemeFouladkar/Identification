# Identification
A Library to help you identify you users using Zibal API

## Usage

```python
from zibal_api import ZibalClient

# Initialize the client
client = ZibalClient(api_token="your-token-here")

# Check if user is identified
is_identified = client.is_user_identified(
    mobile="1234567890",
    national_code="1234567890"
)

# Get user identity
identity, status_code = client.get_user_identity(
    birthday="1990/01/01",
    national_code="1234567890"
)
```
