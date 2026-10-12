username = "admin"
logged_in = True
is_banned = False
is_verified = False
has_token = True
security_level = 5
verification_code = None

if logged_in and not is_banned:
    if (username == "admin" and security_level >= 5) and (is_verified or has_token):
        
        if is_verified and verification_code != None:
            print("Full access")
        else:
            print("Conditional access")
    elif (has_token and security_level >= 4) and not is_banned:
        print("Temporary access")
    elif not is_verified and not has_token:
        print("Verification denied")
    else:
        print("Limited access")
else:
    print("Login rejected")