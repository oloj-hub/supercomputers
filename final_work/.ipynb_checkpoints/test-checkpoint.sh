#!/bin/bash
token=1677496628:AAEEavk7MpcbNTwOC0SE0whKNMwOVV-ZG7w
id=460001441
curl -s -X POST "https://api.telegram.org/bot${token}/sendPhoto?chat_id=${id}" -F photo="@ENG.png" -F caption="TheImage" 

