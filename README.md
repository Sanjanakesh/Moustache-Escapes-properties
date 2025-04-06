

1. Initial Thought Process and Problem Breakdown
When I first read the problem statement, I understood that the core requirement was to build a robust backend API capable of identifying Moustache Escapes properties within a 50km radius of a customer-specified location. The solution had to handle spelling errors, ensure real-time responsiveness, and calculate geographical proximity using latitude and longitude data.
Input Normalization: Accept a free-form textual query (with potential spelling mistakes) and map it to the correct geographical location.
Geolocation Resolution: Convert the location string into accurate latitude and longitude coordinates.
Distance Calculation: Compute the distance between this geolocation and all known property coordinates.
Filtering: Return all properties within a 50km radius or an appropriate fallback message.
Performance: Ensure the response time is within 2 seconds, suitable for real-time tele-calling operations.

2. Tools, Libraries, and Online Resources Used
To develop an efficient and accurate solution, I leveraged the following tools and technologies:
Language: Python – Chosen for its extensive library support, rapid prototyping capability, and community-driven ecosystem for geospatial work.

Geocoding API:
OpenCage Geocoder or Google Maps Geocoding API – Used to convert user-input location names to latitude/longitude. These services provide tolerance to spelling errors and fuzzy matching capabilities, which directly address the input normalization challenge.
Distance Calculation:
Haversine Formula via the geopy.distance or haversine library – For accurate geographic distance calculations between two sets of coordinates.
FastAPI:
A modern, asynchronous Python web framework used to build the API – chosen for its performance, fast development cycles, and automatic documentation (Swagger UI).

3. Key Challenge and How It Was Solved
The biggest challenge was handling inaccurate or misspelled input locations in a way that remained both accurate and performant. Typographical errors like "delih" or "bangalre" could have caused the geocoding services to fail or return incorrect coordinates.
To tackle this:
I implemented a two-layered input resolution system:
Fuzzy matching against a known list of Indian cities/regions to autocorrect or suggest close alternatives.
Once corrected, the input was passed to the geocoding API to retrieve accurate latitude/longitude.
This hybrid approach ensured high input resilience without sacrificing speed.

4. Future Improvements and Alternative Approaches
With more time, I would make the system faster and smarter. I’d use an AI model trained on Indian place names to better understand user input. To speed things up, I’d add caching (like Redis) for repeated searches and pre-calculate distances between cities. I’d also improve spell correction using tools like SymSpell or AI-based suggestions. These changes would make the system more reliable, scalable, and perfect for real-time use in tele-calling or customer support.

Final Result
The result is a highly responsive backend API that:
Corrects misspelled location queries.
Accurately geolocates the input.
Identifies properties within a 50km radius.
Returns real-time responses within 2 seconds.
