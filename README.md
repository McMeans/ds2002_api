# API Project - Current Time in a Capital
IP ADDRESS: `34.69.63.91`. See below to call upon the exact URL, which should automatically be live via `nohup`.

The secret token remains the same as out tutorial: `supersecrettoken123`

Using this secret token, we can use the following command to execute...
>`curl -H "Authorization: Bearer supersecrettoken123" http://34.69.63.91:5000/api/capital-time/{NAME}`

Where {NAME} is one of the following capitals in the database (case-sensitive)...
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
