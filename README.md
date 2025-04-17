# API Project - Current Time in a Capital
The IP Address used is the same as the GCP tutorial from a few weeks ago: `34.27.14.14`. See below to call upon the exact URL.

The secret token remains the same as out tutorial: `supersecrettoken123`

Using this secret token, we can use the following command to execute...
>`curl -H "Authorization: Bearer supersecrettoken123" http://34.27.14.14:5000/api/capital-time/{NAME}`

Where {NAME} is one of the following capitals in the databse...
- Washington
- London
- Paris
- Tokyo
- Sydney
- Moscow
- Beijing
- Berlin
- Rome
- Madrid
- New Delhi
- Buenos Aires
- Cairo
- Nairobi
- Ottawa

It will return the following data...
- City Name
- Local Time
- Timezone
- UTC Offset
