# Sephora Crawler

## Usage
Requires Python 3.x
```bash
$ pip3 install -r requirements.txt
$ ./main.py givenchy
Brand name: Givenchy
Brand URL: https://www.sephora.com/brand/givenchy
Current offer in banner: {color:white}{font-size:12px}[THE WEEKLY WOW JUST DROPPED! AVAILABLE IN STORE AND ONLINE WHILE SUPPLIES LAST. +SHOP NOW+ | https://www.sephora.com/beauty-offers?icid=persistentbanner2_belowthenav_justdropped_weeklywow_112918_m_us-ca_markdown]{color}{font-size}
Number of products: 96
Listing first 10 products:
 - Le Rouge Lipstick (P377755) https://www.sephora.com/product/le-rouge-P377755
 - Prisme Libre Loose Powder (P390722) https://www.sephora.com/product/prisme-libre-loose-powder-P390722
 - Le Rouge Lipstick - Spring Limited Edition (P440025) https://www.sephora.com/product/le-rouge-lipstick-spring-limited-edition-P440025?skuId=2185486
 - Le Rouge Perfecto Beautifying Lip Balm (P410769) https://www.sephora.com/product/le-rouge-perfecto-beautifying-lip-balm-P410769
 - Le Rouge Perfecto - Spring Limited Edition (P440026) https://www.sephora.com/product/le-rouge-perfecto-spring-limited-edition-P440026?skuId=2185494
 - Le Rouge Lipstick Lunar New Year Edition (P439638) https://www.sephora.com/product/le-rouge-lunar-new-year-edition-P439638
 - Prisme Libre Lunar New Year Edition (P439637) https://www.sephora.com/product/prisme-libre-lunar-new-year-edition-P439637
 - Photo’Perfexion Fluid Foundation SPF 20 (P235346) https://www.sephora.com/product/photo-perfexion-fluid-foundation-spf-20-pa-P235346
 - Rouge Interdit Satin Lipstick (P181912) https://www.sephora.com/product/rouge-interdit-satin-lipstick-P181912
 - Rouge Interdit Vinyl Color Enhancing Lipstick (P405231) https://www.sephora.com/product/rouge-interdit-vinyl-color-enhancing-lipstick-P405231
```

## Documentation
```bash
$ ./main.py -h
usage: main.py brand

Download metadata and products about a brand featured on sephora.com

positional arguments:
  brand       The slug brand name such as "givenchy" or "guerlain"
```
