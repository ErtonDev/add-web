# add-web
Discord server related website and other important scripts related to the project.

## Database server credentials
Host        `ec2-54-73-68-39.eu-west-1.compute.amazonaws.com`

Database    `d2qnnn465f5n23`

User        `zinavvopoesljt`

Password    `e9acadc681b670392c65be283556f2b67f34875f6fbbc56d4055114f4f39dff9`

Port        `5432`

## Previous database files classification
New server database must store this information:

user_id     (discord id)  |
user_name   (discord username) |
user_pt     (profile points) |
user_cr     (profile credits) |
user_lvl    (profile level) |
user_{e1/4} (profile stock e) |
user_{n1/2} (profile stock n) |
user_mul    (profile "ficha.txt") * optional |
cr_{e1/4}   (bot stock cr e) |
cr_{n1/2}   (bot stock cr n) |
cant_{e1/4} (bot stock cant e) |
cant_{n1/2} (bot stock cant n) |

... more files should be transfered later

## Note
char length shoud be around 30 in db
