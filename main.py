from ActionDebianSpeakOpenPage import ActionDebianSpeakOpenPage
from Item import Item

items = [Item.from_url('https://www.komputronik.pl/product/700067/asus-geforce-rtx-3080-strix-gaming-10gb-oc.html'),
         Item.from_url('https://www.komputronik.pl/product/702274/gigabyte-geforce-rtx-3080-aorus-master-10g.html'),
         Item.from_url('https://www.komputronik.pl/product/700075/gigabyte-geforce-rtx-3080-gaming-oc-10g.html'),
         Item.from_url('https://www.komputronik.pl/product/699241/asus-geforce-rtx-3080-tuf-gaming-10gb-oc.html'),
         Item.from_url('https://www.komputronik.pl/product/699084/asus-geforce-rtx-3080-tuf-gaming-10gb.html'),
         Item.from_url('https://www.komputronik.pl/product/700429/msi-geforce-rtx-3080-gaming-x-trio-10g.html'),
         Item.from_url('https://www.euro.com.pl/karty-graficzne/msi-karta-gragiczna-msi-rtx-3080-gaming-x-tr.bhtml'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-asus-geforce-rog-strix-rtx-3080-o10g-gaming'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-asus-geforce-tuf-rtx-3080-o10g-gaming'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-asus-geforce-rog-strix-rtx-3080-10g-gaming'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-msi-geforce-rtx-3080-gaming-x-trio-10g'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-asus-geforce-tuf-rtx-3080-10g-gaming'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-vga-gigabyte-aorus-geforce-rtx-3080-master-10g-10gb-gddr6x-320bit-3xhdmi-3xdp-pcie4-0'),
         Item.from_url('https://www.mediaexpert.pl/komputery-i-tablety/podzespoly-komputerowe/karty-graficzne/karta-graficzna-gigabyte-geforce-rtx-3080-gaming-oc-10g'),
         Item.from_url('https://www.morele.net/karta-graficzna-gigabyte-aorus-geforce-rtx-3080-master-10gb-gddr6x-gv-n3080aorus-m-10gd-5944486/'),
         Item.from_url('https://www.nvidia.com/pl-pl/shop/geforce/gpu/?page=1&limit=9&locale=pl-pl&category=GPU&manufacturer=NVIDIA&gpu=RTX%203080'),
         Item.from_url('https://www.nvidia.com/pl-pl/shop/geforce/gpu/?page=1&limit=9&locale=pl-pl&category=GPU&manufacturer=NVIDIA&gpu=RTX%203090'),
         ]

for item in items:
    item.run(5, ActionDebianSpeakOpenPage)
