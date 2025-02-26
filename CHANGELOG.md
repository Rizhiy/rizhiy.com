# CHANGELOG


## v0.17.0 (2025-02-26)

### Features

- Improve style with the help of AI
  ([`e69828f`](https://github.com/Rizhiy/rizhiy.com/commit/e69828f20ee454d03222aec6d39078e707a12833))


## v0.16.0 (2025-02-22)

### Code Style

- **utils**: Format
  ([`f9bff82`](https://github.com/Rizhiy/rizhiy.com/commit/f9bff8249ed99750cea50da6eee5b0a1f057804a))

### Features

- **wishlist**: Add ability to edit links for a wish and add tests
  ([`d54f90c`](https://github.com/Rizhiy/rizhiy.com/commit/d54f90ca0bda31796443a2b13f83c1b46ec1ebb8))

### Testing

- Improve retry
  ([`b65d168`](https://github.com/Rizhiy/rizhiy.com/commit/b65d1689200bd1aab48bab638b7737bc67f84f25))


## v0.15.0 (2024-08-22)

### Features

- **auth**: Add logo to google sign in
  ([`482d6bb`](https://github.com/Rizhiy/rizhiy.com/commit/482d6bbbd80ac4989c01f58e8a68760ea2e32655))


## v0.14.2 (2024-08-22)

### Bug Fixes

- **wishlist**: Fix line-through for price on mobile
  ([`8607ff9`](https://github.com/Rizhiy/rizhiy.com/commit/8607ff9110fd44d00ad47a671506e623942c5b32))

### Performance Improvements

- Load font-awesome only on main page
  ([`9b34c8e`](https://github.com/Rizhiy/rizhiy.com/commit/9b34c8eb9b4aa38d85c5d6e009bdc5afd64d84c7))


## v0.14.1 (2024-08-22)

### Bug Fixes

- **wishlist**: Improve text a bit
  ([`e319dd1`](https://github.com/Rizhiy/rizhiy.com/commit/e319dd137f820137e48efd71f8a0b9eb321f1ce8))


## v0.14.0 (2024-08-22)

### Features

- **wishlist**: Indicate reserved wishes a bit better
  ([`9332a11`](https://github.com/Rizhiy/rizhiy.com/commit/9332a11aa45f48d5d1e169ccafc66687a2efe87a))


## v0.13.0 (2024-08-21)

### Features

- **wishlist**: Add message about remaining wishes
  ([`bec853a`](https://github.com/Rizhiy/rizhiy.com/commit/bec853ade7dfb48f446ddeab4087a7500a922ac6))


## v0.12.0 (2024-08-20)

### Features

- **auth**: Limit pre_login memory to 5 minutes and remember page before logout
  ([`60a7045`](https://github.com/Rizhiy/rizhiy.com/commit/60a70452cb83a1d968cb7edbcb8976e4a9d97e39))


## v0.11.4 (2024-08-20)

### Bug Fixes

- Re-order title template
  ([`47d372d`](https://github.com/Rizhiy/rizhiy.com/commit/47d372d75ae6abfba2d5d1a4e6cfa560c0f2f280))


## v0.11.3 (2024-08-20)

### Bug Fixes

- **wishlist**: Add text to clarify which items were reserved by the person
  ([`d38f340`](https://github.com/Rizhiy/rizhiy.com/commit/d38f3401421422c8e25109bb865c7da758ebd814))

### Testing

- Add retry for test_get_url_title
  ([`888f3c5`](https://github.com/Rizhiy/rizhiy.com/commit/888f3c5361c6b244a720d9a1a6a8202c950ecdb2))


## v0.11.2 (2024-08-20)

### Bug Fixes

- **wishlist**: Allow to reserve upto 3 wishes and add success message
  ([`486d0b2`](https://github.com/Rizhiy/rizhiy.com/commit/486d0b299a55c29d1bc0542a3a041511fc23a0d9))

### Chores

- Adjust navbar color and add link to register on login
  ([`7ec8131`](https://github.com/Rizhiy/rizhiy.com/commit/7ec8131bd313ec3aa446df747be112b5322e6349))

- Force update during update_prod
  ([`d2c4722`](https://github.com/Rizhiy/rizhiy.com/commit/d2c47223357192813234c02664633065dcad15a0))

- Restart nginx when updating prod
  ([`fd26f8f`](https://github.com/Rizhiy/rizhiy.com/commit/fd26f8f2f22c62b808cd9181405c6126e4cab804))


## v0.11.1 (2024-08-19)

### Bug Fixes

- **auth**: Fix prev_url for prod
  ([`a3d4d54`](https://github.com/Rizhiy/rizhiy.com/commit/a3d4d54337a04528f31ea76853a928d40cfe42ba))


## v0.11.0 (2024-08-19)

### Features

- **auth**: Login on register and remember last request before login
  ([`b231a1d`](https://github.com/Rizhiy/rizhiy.com/commit/b231a1dde5fec956de1c0189c1870cbc060acda4))


## v0.10.1 (2024-08-19)

### Bug Fixes

- Make navbar sticky and reduce top margin
  ([`b22338c`](https://github.com/Rizhiy/rizhiy.com/commit/b22338c3439101f312ab493e78ad6104679176c6))

- **wishlist**: Fix display when user is unknown
  ([`03e5005`](https://github.com/Rizhiy/rizhiy.com/commit/03e5005d655d57a003206a1fc2775efe54fb2061))

- **wishlist**: Fix multiline description
  ([`a7bb97c`](https://github.com/Rizhiy/rizhiy.com/commit/a7bb97c87f6c66b6fea2e72ab31f296e42ff7ab2))


## v0.10.0 (2024-08-19)

### Bug Fixes

- Add pillow to dependencies
  ([`5343bae`](https://github.com/Rizhiy/rizhiy.com/commit/5343bae2629d2b2a0f132d36c015a6b3c5bfbb60))

### Chores

- **utils**: Add special case for Ebay
  ([`19e3851`](https://github.com/Rizhiy/rizhiy.com/commit/19e38519bd632f6c2dfe2f211c53713b24ea4b1b))

- **wishlist**: Sort by price asc
  ([`dafd67e`](https://github.com/Rizhiy/rizhiy.com/commit/dafd67ec2c0bb48f81cb20ec851fa2d55d8de348))

### Features

- **wishlist**: Add function to create image thumbnails
  ([`7fd25ef`](https://github.com/Rizhiy/rizhiy.com/commit/7fd25ef1242eb1e1c8f1e226946653b78af131e2))


## v0.9.0 (2024-08-19)

### Features

- **wishlist**: Add links to index
  ([`514cc15`](https://github.com/Rizhiy/rizhiy.com/commit/514cc1510837e0ca4bef5e957f92f746a64e6168))


## v0.8.1 (2024-08-19)

### Bug Fixes

- **navbar**: Fix profile picture alignment
  ([`c77e98b`](https://github.com/Rizhiy/rizhiy.com/commit/c77e98b7f5cc909dca0190d6bc62bda797a9632a))

### Chores

- Add dotenv
  ([`a8f6655`](https://github.com/Rizhiy/rizhiy.com/commit/a8f6655c59bb92fa370f65dbded13c0854929924))


## v0.8.0 (2024-08-19)

### Bug Fixes

- **wishlist**: Fix unreserved use-case
  ([`1209d56`](https://github.com/Rizhiy/rizhiy.com/commit/1209d56bfc6bd935e751bac52a364aa5f3d37834))

- **wishlist**: Fix wishlist on mobile devices
  ([`e392733`](https://github.com/Rizhiy/rizhiy.com/commit/e392733d2f8e54b72ac66f10fccbdf1de91c37ef))

### Code Style

- Format
  ([`7ae3ac4`](https://github.com/Rizhiy/rizhiy.com/commit/7ae3ac403702f7896d8c99c84ea6101ef21bb1a4))

### Features

- **wishlist**: Add basic functionality
  ([`5f91d12`](https://github.com/Rizhiy/rizhiy.com/commit/5f91d1263d64862f9952295d6f1ba98938a340a9))

### Testing

- Add replete[testing]
  ([`7377be8`](https://github.com/Rizhiy/rizhiy.com/commit/7377be8a031739e3cec551003cfd3c0e61a1bcb9))

- Fix
  ([`7a6d3d7`](https://github.com/Rizhiy/rizhiy.com/commit/7a6d3d75167fada538817b51ffd8a2502a7a031c))


## v0.7.1 (2024-08-17)

### Bug Fixes

- Fix url resolution on prod
  ([`dd07278`](https://github.com/Rizhiy/rizhiy.com/commit/dd072785108c4cf90c377fc301ff93f1796ba32c))


## v0.7.0 (2024-08-17)

### Features

- Add google auth
  ([`1d33670`](https://github.com/Rizhiy/rizhiy.com/commit/1d33670e3bbfe015bc6a47dbf2afedd266ffcc01))

### Testing

- Fix auth tests
  ([`3ba9bd2`](https://github.com/Rizhiy/rizhiy.com/commit/3ba9bd2aebbe0d644cffac33c8bc2720c8177eb1))


## v0.6.0 (2024-08-16)

### Features

- Add https
  ([`41381e3`](https://github.com/Rizhiy/rizhiy.com/commit/41381e36011f780535872e7b5fb67a37294381ff))


## v0.5.1 (2024-08-16)

### Bug Fixes

- Fix min-width
  ([`d366d30`](https://github.com/Rizhiy/rizhiy.com/commit/d366d3068028ff38cceee1e30cdd3769841ac0ff))


## v0.5.0 (2024-08-16)

### Features

- Simplify auth pages and add social links
  ([`fa69f86`](https://github.com/Rizhiy/rizhiy.com/commit/fa69f86418628551fa854648302ee4c86dcc9ad4))


## v0.4.2 (2024-08-15)

### Bug Fixes

- Adjust for dark mode 2
  ([`70ac0d7`](https://github.com/Rizhiy/rizhiy.com/commit/70ac0d7c7180cbbdc51ca5a00bc9b04654c92483))


## v0.4.1 (2024-08-14)

### Bug Fixes

- Adjust for dark mode
  ([`366e6dc`](https://github.com/Rizhiy/rizhiy.com/commit/366e6dc71874db965f7e2d245b86c8c5f6dd8a2f))


## v0.4.0 (2024-08-14)

### Chores

- Add script to update prod
  ([`573cc14`](https://github.com/Rizhiy/rizhiy.com/commit/573cc14a3b486c233c7fd880f24d80e00364bfb2))

- Fix script to update prod
  ([`0ebbcf0`](https://github.com/Rizhiy/rizhiy.com/commit/0ebbcf091b184aaa71b679aaf2fafb2d9e3b16fb))

### Features

- Add auth back and add navbar
  ([`003ffa3`](https://github.com/Rizhiy/rizhiy.com/commit/003ffa3cb56b8a3b1429bcf60bc0cb974614d960))


## v0.3.0 (2024-08-14)

### Features

- Add basic main page
  ([`830a985`](https://github.com/Rizhiy/rizhiy.com/commit/830a985581d111ebb0898020a1387d60032edf6d))

### Testing

- Disable most tests for now
  ([`b74c35f`](https://github.com/Rizhiy/rizhiy.com/commit/b74c35f6a2bd1ab10eb480eb36fa3469ca0a5367))


## v0.2.0 (2024-08-12)

### Features

- Add scripts to setup prod
  ([`15fc94e`](https://github.com/Rizhiy/rizhiy.com/commit/15fc94e60e6224c2324b00625d828f587f5a24ee))


## v0.1.0 (2024-08-11)

### Bug Fixes

- Update min python version
  ([`8f08f75`](https://github.com/Rizhiy/rizhiy.com/commit/8f08f7541191bfa457a756be0e8a3604edf050fd))

### Features

- Setup tutorial flask project
  ([`103a1cc`](https://github.com/Rizhiy/rizhiy.com/commit/103a1cc325613386217dbddf1b73a3a4c833a187))

### Testing

- Update code to fix format
  ([`b5cc928`](https://github.com/Rizhiy/rizhiy.com/commit/b5cc92853d3a3813612b0f554297c56aa7672acb))
