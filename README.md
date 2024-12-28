# pyident
A Library to help you identify you users using Zibal API

# Usage


### .env
```python
ZIBAL_TOKEN=your-token
```

### identification.py
```python
from pyident.zibal import ZibalClient

# Initialize the client
client = ZibalClient()

# Check if user is identified
is_identified: bool = client.is_user_identified(
    mobile="1234567890",
    national_code="1234567890"
)

# Get user identity
identity: dict, status_code: int = client.get_user_identity(
    birthday="1990/01/01",
    national_code="1234567890"
)
```



# Contributing to the Project

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Here's a list of `types` you can use for your commit message:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes
- **style**: Code style changes (like formatting)
- **refactor**: Code changes that neither fix a bug nor add a feature
- **test**: Adding or modifying tests
- **chore**: Routine tasks, such as dependencies updates

Commit message example:
```
feat(auth): add login API endpoint
feat(lang): add Polish language
```