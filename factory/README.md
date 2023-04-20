
# Explanation

- The factory pattern is used when you need to create objects of different classes based on a common interface or base class. The factory pattern encapsulates the object creation logic in a separate class, which makes it easier to maintain and modify. The factory pattern is useful when you have a fixed set of object types that you need to create, and when the object creation logic is complex or may change frequently.

### Code example explanation

- This implementation uses a try block to safely extract the "topic" key from the request body. If the key is missing or invalid, it returns None. Otherwise, it looks up the corresponding WebHook class in the WEBHOOKS dictionary using the topic as the key. If the topic is unknown, it also returns None.

- Note that this implementation returns None instead of a default WebHook if the topic is missing or unknown. This is because it's better to handle these cases explicitly, rather than silently falling back to a default behavior. This way, you can log or notify the user of the issue and take appropriate action.