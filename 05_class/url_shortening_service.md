Functional Requirements:

1. Given a URL, our service should generate a shorter and unique alias of it. This is called a short link.
2. When users access a short link, our service should redirect them to the original link.
3. Links will expire after a standard default timespan. Users should also be able to specify
   the expiration time.

Non-Functional Requirements:

1. The system should be highly available.
2. URL redirection should happen in real-time with minimal latency.
3. 500M new URL shortenings per month
4. 100:1 read/write ratio
5. Default timespan is 5 years
6. URL object size is 500 bytes