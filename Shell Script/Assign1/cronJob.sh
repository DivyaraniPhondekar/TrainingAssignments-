#!/bin/bash
chmod +x /any.sh
0 14 * * 1-5 /any.sh
0 8-20/3 * * * / any.sh
0 0 */2 2-12/2 * / any.sh


# *     *     *     *     *  Command to be executed
# -     -     -     -     -
# |     |     |     |     |
# |     |     |     |     +----- Day of week (0-7)
# |     |     |     +------- Month (1 - 12)
# |     |     +--------- Day of month (1 - 31)
# |     +----------- Hour (0 - 23)
# +------------- Min (0 - 59)
