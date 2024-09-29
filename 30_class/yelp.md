Functional Requirements:

1. Users should be able to add, delete, update places.
2. Given their location (longitude/latitude),
   users should be able to find all nearby places within a given radius.
3. Users should be able to add feedback about a place.

Non-Functional Requirements:

1. Users should have real-time search experience with minimum latency.
2. Our service should support a heavy search load.
   There will be a lot of search requests compared to adding a new place.
3. Total number of places is 500M.
4. Search queries are 100K per second.