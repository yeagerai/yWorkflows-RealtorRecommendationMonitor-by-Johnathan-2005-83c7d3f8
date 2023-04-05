
# UserInfoExtractor

Extracts user information (first and last name) from the Facebook post. Requires the post's JSON data as input from the 'NewPostDetector' node.

## Initial generation prompt
description: Extracts user information (first and last name) from the Facebook post.
  Requires the post's JSON data as input from the 'NewPostDetector' node.
name: UserInfoExtractor


## Transformer breakdown
- Step 1: Access the user's name using the specified 'user_name_key' from the post_data JSON input.
- Step 2: Extract the first and last name from the user's name string.
- Step 3: Return the extracted user information (first and last name).

## Parameters
[{'name': 'user_name_key', 'default_value': 'user_name', 'description': "The key to access the user's name (first and last) in the post's JSON data.", 'type': 'string'}]

        