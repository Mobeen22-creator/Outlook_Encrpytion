from outlook_encryption import* 

password="" # Password to encrypt
key="" # Scrape it from signup page
randomNum=""# Scrape it from signup page
SKI="" # Scrape it from signup page
encrpyted_password = ctx.call('Encrypt',"", "","newpwd",password,key,randomNum,SKI)
