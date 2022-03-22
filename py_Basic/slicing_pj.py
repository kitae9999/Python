address="https://gall.dcinside.com/mgallery"
dot=address.index(".")
address1=address[8:dot]
address2=address1[0:3]+str(dot-8)+str(address1.count("e"))+"!"

print(address2)