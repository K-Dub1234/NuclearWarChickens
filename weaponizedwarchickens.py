def start():
  import b18918291658374

def main():
  from PIL import Image
  img = Image.open('/Weaponized war chickens/assets/weaponizedwarchickensload.png')
  img.show()
  print('The creators of this software have no liability whatsoever over the destruction of anything by this software.')
  print('Are you sure you want to continue? This program may harm any device it has access to. (Y/N)')
  ipt = input()
  if ipt == 'Y' or ipt == 'yes' or ipt == 'YES' or ipt == 'y':
    start()
  if ipt == 'N' or ipt == 'no' or ipt == 'NO' or ipt == 'n':
    print('We understand. Disarming...')
    img = Image.open('/Weaponized war chickens/assets/weaponizedwarchickensdisarming.png')
    img.show()
  if ipt != 'Y' or ipt == 'yes' or ipt == 'YES' or ipt == 'y' or 'N' or ipt == 'no' or ipt == 'NO' or ipt == 'n':
    print('We dont understand the command. It was a simple yes or no question.')
main()
