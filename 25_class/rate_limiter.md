Functional Requirements:

1. Limit the number of requests that some entity can send to API within a time window (e.g. 15 requests per second).
2. API is accessible through a cluster, so the rate limit should be considered across different servers.
   The user should get an error message whenever the defined threshold
   is crossed within a single server or across a combination of servers.

Non-Functional Requirements:

1. The system should be highly available.
   The rate limiter should always work since it protects our service from external attacks.
2. Rate limiter should not introduce substantial latencies affecting the user experience.