Functional Requirements:

1. Users should be able to post new tweets.
2. Users should be able to follow other users.
3. The service should be able to create and display user’s timeline consisting of top tweets from all the people the
   user follows.
4. Users should be able to mark tweets favorite.
5. Tweets can contain photos and videos.

Non-Functional Requirements:

1. Service needs to be highly available.
2. Acceptable latency is 200ms for timeline generation.
3. Consistency can take a hit (in the interest of availability). If a user doesn’t see a tweet for a while, it should be
   fine.
4. 1B users
5. 200M daily active users.
6. 100M new tweets every day.
7. Each user follows 200 users on average.