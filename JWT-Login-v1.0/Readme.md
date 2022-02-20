# JWT Login v1.0

Challenge:

Field: Username
CTA: Login

We have a python file, which creates a Flask environment

This html has a class class="pin-prompt" which has display:none;

It requires the PIN to unlock the console.


It generates a token, the token is saved in a domain,

It is really useful this tool: https://github.com/ticarpi/jwt_tool

The tool allows to know the flag:

$ python3 jwt_tool/jwt_tool.py -t https://jwt-login-v1.sexy-allpacks.com/ -rc "jwt=<token>;anothercookie=test" -rh "Origin: null" -cv "Welcome" -M er

The tool shows:

Decoded Token Values:

Where Token payload values has the Flag!  {^^}


