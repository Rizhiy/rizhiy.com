# CHANGELOG

## v0.14.0 (2024-08-22)

### Feature

* feat(wishlist): indicate reserved wishes a bit better ([`9332a11`](https://github.com/Rizhiy/rizhiy.com/commit/9332a11aa45f48d5d1e169ccafc66687a2efe87a))

## v0.13.0 (2024-08-21)

### Feature

* feat(wishlist): add message about remaining wishes ([`bec853a`](https://github.com/Rizhiy/rizhiy.com/commit/bec853ade7dfb48f446ddeab4087a7500a922ac6))

## v0.12.0 (2024-08-20)

### Feature

* feat(auth): limit pre_login memory to 5 minutes and remember page before logout ([`60a7045`](https://github.com/Rizhiy/rizhiy.com/commit/60a70452cb83a1d968cb7edbcb8976e4a9d97e39))

## v0.11.4 (2024-08-20)

### Fix

* fix: re-order title template ([`47d372d`](https://github.com/Rizhiy/rizhiy.com/commit/47d372d75ae6abfba2d5d1a4e6cfa560c0f2f280))

## v0.11.3 (2024-08-20)

### Fix

* fix(wishlist): add text to clarify which items were reserved by the person ([`d38f340`](https://github.com/Rizhiy/rizhiy.com/commit/d38f3401421422c8e25109bb865c7da758ebd814))

### Test

* test: add retry for test_get_url_title ([`888f3c5`](https://github.com/Rizhiy/rizhiy.com/commit/888f3c5361c6b244a720d9a1a6a8202c950ecdb2))

## v0.11.2 (2024-08-20)

### Chore

* chore: force update during update_prod ([`d2c4722`](https://github.com/Rizhiy/rizhiy.com/commit/d2c47223357192813234c02664633065dcad15a0))

* chore: restart nginx when updating prod ([`fd26f8f`](https://github.com/Rizhiy/rizhiy.com/commit/fd26f8f2f22c62b808cd9181405c6126e4cab804))

* chore: adjust navbar color and add link to register on login ([`7ec8131`](https://github.com/Rizhiy/rizhiy.com/commit/7ec8131bd313ec3aa446df747be112b5322e6349))

### Fix

* fix(wishlist): allow to reserve upto 3 wishes and add success message ([`486d0b2`](https://github.com/Rizhiy/rizhiy.com/commit/486d0b299a55c29d1bc0542a3a041511fc23a0d9))

## v0.11.1 (2024-08-19)

### Fix

* fix(auth): fix prev_url for prod ([`a3d4d54`](https://github.com/Rizhiy/rizhiy.com/commit/a3d4d54337a04528f31ea76853a928d40cfe42ba))

## v0.11.0 (2024-08-19)

### Feature

* feat(auth): login on register and remember last request before login ([`b231a1d`](https://github.com/Rizhiy/rizhiy.com/commit/b231a1dde5fec956de1c0189c1870cbc060acda4))

## v0.10.1 (2024-08-19)

### Fix

* fix: make navbar sticky and reduce top margin ([`b22338c`](https://github.com/Rizhiy/rizhiy.com/commit/b22338c3439101f312ab493e78ad6104679176c6))

* fix(wishlist): fix multiline description ([`a7bb97c`](https://github.com/Rizhiy/rizhiy.com/commit/a7bb97c87f6c66b6fea2e72ab31f296e42ff7ab2))

* fix(wishlist): fix display when user is unknown ([`03e5005`](https://github.com/Rizhiy/rizhiy.com/commit/03e5005d655d57a003206a1fc2775efe54fb2061))

## v0.10.0 (2024-08-19)

### Chore

* chore(utils): add special case for Ebay ([`19e3851`](https://github.com/Rizhiy/rizhiy.com/commit/19e38519bd632f6c2dfe2f211c53713b24ea4b1b))

* chore(wishlist): sort by price asc ([`dafd67e`](https://github.com/Rizhiy/rizhiy.com/commit/dafd67ec2c0bb48f81cb20ec851fa2d55d8de348))

### Feature

* feat(wishlist): add function to create image thumbnails ([`7fd25ef`](https://github.com/Rizhiy/rizhiy.com/commit/7fd25ef1242eb1e1c8f1e226946653b78af131e2))

### Fix

* fix: add pillow to dependencies ([`5343bae`](https://github.com/Rizhiy/rizhiy.com/commit/5343bae2629d2b2a0f132d36c015a6b3c5bfbb60))

## v0.9.0 (2024-08-19)

### Feature

* feat(wishlist): add links to index ([`514cc15`](https://github.com/Rizhiy/rizhiy.com/commit/514cc1510837e0ca4bef5e957f92f746a64e6168))

## v0.8.1 (2024-08-19)

### Chore

* chore: add dotenv ([`a8f6655`](https://github.com/Rizhiy/rizhiy.com/commit/a8f6655c59bb92fa370f65dbded13c0854929924))

### Fix

* fix(navbar): fix profile picture alignment ([`c77e98b`](https://github.com/Rizhiy/rizhiy.com/commit/c77e98b7f5cc909dca0190d6bc62bda797a9632a))

## v0.8.0 (2024-08-19)

### Feature

* feat(wishlist): add basic functionality ([`5f91d12`](https://github.com/Rizhiy/rizhiy.com/commit/5f91d1263d64862f9952295d6f1ba98938a340a9))

### Fix

* fix(wishlist): fix wishlist on mobile devices ([`e392733`](https://github.com/Rizhiy/rizhiy.com/commit/e392733d2f8e54b72ac66f10fccbdf1de91c37ef))

* fix(wishlist): fix unreserved use-case ([`1209d56`](https://github.com/Rizhiy/rizhiy.com/commit/1209d56bfc6bd935e751bac52a364aa5f3d37834))

### Style

* style: format ([`7ae3ac4`](https://github.com/Rizhiy/rizhiy.com/commit/7ae3ac403702f7896d8c99c84ea6101ef21bb1a4))

### Test

* test: add replete[testing] ([`7377be8`](https://github.com/Rizhiy/rizhiy.com/commit/7377be8a031739e3cec551003cfd3c0e61a1bcb9))

* test: fix ([`7a6d3d7`](https://github.com/Rizhiy/rizhiy.com/commit/7a6d3d75167fada538817b51ffd8a2502a7a031c))

## v0.7.1 (2024-08-17)

### Fix

* fix: fix url resolution on prod ([`dd07278`](https://github.com/Rizhiy/rizhiy.com/commit/dd072785108c4cf90c377fc301ff93f1796ba32c))

## v0.7.0 (2024-08-17)

### Feature

* feat: add google auth ([`1d33670`](https://github.com/Rizhiy/rizhiy.com/commit/1d33670e3bbfe015bc6a47dbf2afedd266ffcc01))

### Test

* test: fix auth tests ([`3ba9bd2`](https://github.com/Rizhiy/rizhiy.com/commit/3ba9bd2aebbe0d644cffac33c8bc2720c8177eb1))

## v0.6.0 (2024-08-16)

### Feature

* feat: add https ([`41381e3`](https://github.com/Rizhiy/rizhiy.com/commit/41381e36011f780535872e7b5fb67a37294381ff))

## v0.5.1 (2024-08-16)

### Fix

* fix: fix min-width ([`d366d30`](https://github.com/Rizhiy/rizhiy.com/commit/d366d3068028ff38cceee1e30cdd3769841ac0ff))

## v0.5.0 (2024-08-16)

### Feature

* feat: simplify auth pages and add social links ([`fa69f86`](https://github.com/Rizhiy/rizhiy.com/commit/fa69f86418628551fa854648302ee4c86dcc9ad4))

## v0.4.2 (2024-08-15)

### Fix

* fix: adjust for dark mode 2 ([`70ac0d7`](https://github.com/Rizhiy/rizhiy.com/commit/70ac0d7c7180cbbdc51ca5a00bc9b04654c92483))

## v0.4.1 (2024-08-14)

### Fix

* fix: adjust for dark mode ([`366e6dc`](https://github.com/Rizhiy/rizhiy.com/commit/366e6dc71874db965f7e2d245b86c8c5f6dd8a2f))

## v0.4.0 (2024-08-14)

### Chore

* chore: fix script to update prod ([`0ebbcf0`](https://github.com/Rizhiy/rizhiy.com/commit/0ebbcf091b184aaa71b679aaf2fafb2d9e3b16fb))

* chore: add script to update prod ([`573cc14`](https://github.com/Rizhiy/rizhiy.com/commit/573cc14a3b486c233c7fd880f24d80e00364bfb2))

### Feature

* feat: add auth back and add navbar ([`003ffa3`](https://github.com/Rizhiy/rizhiy.com/commit/003ffa3cb56b8a3b1429bcf60bc0cb974614d960))

## v0.3.0 (2024-08-14)

### Feature

* feat: add basic main page ([`830a985`](https://github.com/Rizhiy/rizhiy.com/commit/830a985581d111ebb0898020a1387d60032edf6d))

### Test

* test: disable most tests for now ([`b74c35f`](https://github.com/Rizhiy/rizhiy.com/commit/b74c35f6a2bd1ab10eb480eb36fa3469ca0a5367))

## v0.2.0 (2024-08-12)

### Feature

* feat: add scripts to setup prod ([`15fc94e`](https://github.com/Rizhiy/rizhiy.com/commit/15fc94e60e6224c2324b00625d828f587f5a24ee))

## v0.1.0 (2024-08-11)

### Feature

* feat: setup tutorial flask project ([`103a1cc`](https://github.com/Rizhiy/rizhiy.com/commit/103a1cc325613386217dbddf1b73a3a4c833a187))

### Fix

* fix: update min python version ([`8f08f75`](https://github.com/Rizhiy/rizhiy.com/commit/8f08f7541191bfa457a756be0e8a3604edf050fd))

### Test

* test: update code to fix format ([`b5cc928`](https://github.com/Rizhiy/rizhiy.com/commit/b5cc92853d3a3813612b0f554297c56aa7672acb))

### Unknown

* Initial commit ([`17d448e`](https://github.com/Rizhiy/rizhiy.com/commit/17d448e89027e99aada9e746480c59b4a61f72fa))
