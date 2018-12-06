from webbot import Browser
web = Browser()
web.go_to('https://172.22.2.6/PortalMain')
web.click('Username')
web.type('17ucc063',id = 'LoginUserPassword_auth_username')
web.click('Password')
web.type('YxgV5662*')
web.click('Login',id = 'LoginUserPassword_auth_password')
web.click('Log In',tag = 'span')