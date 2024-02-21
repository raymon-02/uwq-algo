Functional Requirements:

1. Users should be able to upload/download/view photos.
2. Users can perform searches based on photo/video titles.
3. Users can follow other users.
4. The system should be able to generate and display a user’s News Feed consisting of
   top photos from all the people the user follows.

Non-Functional Requirements:

1. Our service needs to be highly available.
2. Consistency can take a hit (in the interest of availability), if a user doesn’t see a photo
   for a while, it should be fine.
3. The system should be highly reliable, any uploaded photo or video should never be
   lost.
4. 500M total users.
5. 1M daily active users.
6. 2M new photos every day.
7. Average photo file size is 200KB.
8. The acceptable latency of the system is 200ms for News Feed generation.