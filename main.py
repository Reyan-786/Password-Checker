import sys
import checkmypass as cmp
# main function->
def main(args):
    for password in args:
        count = cmp.pwned_api_check(password)
        if count:
            print(f"\n{password} was found {count} times...,you should probably change it before you get hacked ::: <===;;;===> :::\n")
        else :
            print(f"\n{password} was not found!!! everything is safe for now!!!\n")
    print('done') 
main(sys.argv[1:])
