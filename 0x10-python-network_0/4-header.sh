#!/bin/bash
# The script takes URL as an argument, GET request to the URL, and displays the body of the response. A header variable X-HolbertonSchool-User-Id must be sent with the value 98.
curl -sX GET -H "X-School-User-Id: 98" "$1"
