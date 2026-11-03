# Dá»± Ãn: Chuá»™t MÃ¡y TÃ­nh TÃ­ch Há»£p Vi DÃ²ng Äiá»‡n (Microcurrent Mouse)

## 1. Giá»›i thiá»‡u tá»•ng quan
Dá»± Ã¡n phÃ¡t triá»ƒn má»™t thiáº¿t bá»‹ ngoáº¡i vi mÃ¡y tÃ­nh (chuá»™t cÃ´ng thÃ¡i há»c - Ergonomic Mouse) tÃ­ch há»£p cÃ´ng nghá»‡ **vi dÃ²ng Ä‘iá»‡n (Microcurrent Therapy - MENS)** nháº±m má»¥c tiÃªu:
- **TÄƒng tuáº§n hoÃ n mÃ¡u & kÃ­ch thÃ­ch sáº£n sinh ATP:** GiÃºp phá»¥c há»“i mÃ´, giáº£m cÄƒng cá»©ng cÆ¡ bÃ n tay vÃ  cá»• tay khi lÃ m viá»‡c vÄƒn phÃ²ng liÃªn tá»¥c.
- **Giáº£m nguy cÆ¡ há»™i chá»©ng á»‘ng cá»• tay (Carpal Tunnel Syndrome):** Há»— trá»£ xoa dá»‹u cÃ¡c bÃ³ cÆ¡ vÃ  dÃ¢y tháº§n kinh vÃ¹ng bÃ n tay.
- **NÃ¢ng cao kháº£ nÄƒng táº­p trung:** NghiÃªn cá»©u cÆ¡ cháº¿ kÃ­ch thÃ­ch tháº§n kinh nháº¹ nhÃ ng (tÆ°Æ¡ng tá»± vi kÃ­ch thÃ­ch Cranial/Peripheral) káº¿t há»£p cÃ¡c chu ká»³ lÃ m viá»‡c (nhÆ° Pomodoro).

---

## 2. Cáº¥u trÃºc thÆ° má»¥c dá»± Ã¡n

```text
microcurrent-mouse/
â”œâ”€â”€ docs/                      # TÃ i liá»‡u nghiÃªn cá»©u, phÃ¡p lÃ½ vÃ  Ä‘áº·c táº£ ká»¹ thuáº­t
â”‚   â”œâ”€â”€ current-conduction-principles/ # NguyÃªn lÃ½ truyá»n dáº«n dÃ²ng Ä‘iá»‡n trong mÃ´ & giáº£i pháº«u há»c
â”‚   â”‚   â”œâ”€â”€ current-path-and-tissue-penetration.md  # PhÃ¢n tÃ­ch Ä‘Æ°á»ng Ä‘i dÃ²ng Ä‘iá»‡n, Ä‘á»™ sÃ¢u & vá»‹ trÃ­ Ä‘iá»‡n cá»±c
â”‚   â”‚   â”œâ”€â”€ local-vs-systemic-effects.md            # ÄÃ¡nh giÃ¡ tÃ¡c dá»¥ng cá»¥c bá»™ bÃ n tay vs. toÃ n thÃ¢n
â”‚   â”‚   â””â”€â”€ skin-impedance-and-efficacy.md          # CÆ¡ cháº¿ sinh há»c tÄƒng ATP & mÃ´ hÃ¬nh trá»Ÿ khÃ¡ng da
â”‚   â”œâ”€â”€ research/              # TÃ i liá»‡u y sinh, cÆ¡ cháº¿ vi dÃ²ng Ä‘iá»‡n, tÃ¡c Ä‘á»™ng ATP
â”‚   â”‚   â”œâ”€â”€ core-keywords.md   # Tá»« khÃ³a trá»ng tÃ¢m (DOMS, Sub-sensory, Lipolysis, Muscle Thickness)
â”‚   â”‚   â”œâ”€â”€ hand-nerve-anatomy-and-mouse-correlation.md # Giáº£i pháº«u 3 dÃ¢y tháº§n kinh tay & á»©ng dá»¥ng vÃ o chuá»™t
â”‚   â”‚   â””â”€â”€ PMC9941239-summary.md # TÃ³m táº¯t bÃ i bÃ¡o nghiÃªn cá»©u ná»n táº£ng (Eur J Appl Physiol 2023)
â”‚   â”œâ”€â”€ safety-standards/      # TiÃªu chuáº©n an toÃ n Ä‘iá»‡n sinh há»c (IEC 60601-1, ngÆ°á»¡ng vi dÃ²ng)
â”‚   â””â”€â”€ specifications/        # ThÃ´ng sá»‘ ká»¹ thuáº­t cá»§a thiáº¿t bá»‹ (Specs)
â”œâ”€â”€ hardware/                  # Thiáº¿t káº¿ pháº§n cá»©ng & Ä‘iá»‡n tá»­
â”‚   â”œâ”€â”€ schematics/            # SÆ¡ Ä‘á»“ máº¡ch nguyÃªn lÃ½ (KiCad / Proteus / EasyEDA)
â”‚   â”œâ”€â”€ pcb/                   # Báº£n váº½ máº¡ch in & Gerber files
â”‚   â”œâ”€â”€ bom/                   # Báº£ng danh má»¥c linh kiá»‡n & chi phÃ­ (BOM)
â”‚   â””â”€â”€ datasheets/            # Datasheet cÃ¡c linh kiá»‡n chÃ­nh (MCU, Op-Amp, DAC,...)
â”œâ”€â”€ mechanical-cad/            # Thiáº¿t káº¿ cÆ¡ khÃ­ & vá» ngoÃ i (3D Modeling)
â”‚   â”œâ”€â”€ 3d-models/             # File CAD (.step, .stl, file gá»‘c Fusion360/SolidWorks)
â”‚   â”œâ”€â”€ electrodes/            # Thiáº¿t káº¿ & vá»‹ trÃ­ cÃ¡c Ä‘iá»‡n cá»±c tiáº¿p xÃºc da
â”‚   â””â”€â”€ renders/               # HÃ¬nh áº£nh 3D mÃ´ phá»ng
â”œâ”€â”€ firmware/                  # Láº­p trÃ¬nh nhÃºng cho vi Ä‘iá»u khiá»ƒn
â”‚   â”œâ”€â”€ src/                   # Source code C/C++ Ä‘iá»u khiá»ƒn xung, Ä‘á»c cáº£m biáº¿n, USB/BLE HID
â”‚   â”œâ”€â”€ include/               # Header files
â”‚   â””â”€â”€ tests/                 # Code test pháº§n cá»©ng, hiá»‡u chuáº©n dÃ²ng Ä‘iá»‡n
â”œâ”€â”€ software/                  # Pháº§n má»m á»©ng dá»¥ng Ä‘i kÃ¨m (Desktop / Web Companion)
â”‚   â””â”€â”€ companion-app/         # á»¨ng dá»¥ng Ä‘iá»u chá»‰nh thÃ´ng sá»‘, háº¹n giá», theo dÃµi sá»©c khá»e
â”œâ”€â”€ tests-and-logs/            # Káº¿t quáº£ Ä‘o kiá»ƒm & nháº­t kÃ½ thá»­ nghiá»‡m
â”‚   â”œâ”€â”€ oscilloscope-captures/ # áº¢nh chá»¥p dáº¡ng sÃ³ng thá»±c táº¿ trÃªn dao Ä‘á»™ng kÃ½
â”‚   â””â”€â”€ test-reports/          # BÃ¡o cÃ¡o Ä‘o kiá»ƒm táº£i giáº£ & thá»­ nghiá»‡m thá»±c táº¿
â””â”€â”€ assets/                    # HÃ¬nh áº£nh, sÆ¡ Ä‘á»“ minh há»a
```

---

## 3. CÃ¡c giai Ä‘oáº¡n phÃ¡t triá»ƒn (Roadmap)

### Giai Ä‘oáº¡n 1: NghiÃªn cá»©u kháº£ thi & An toÃ n (Feasibility & Safety)
- [ ] XÃ¡c Ä‘á»‹nh dáº£i dÃ²ng Ä‘iá»‡n an toÃ n ($10\,\mu\text{A} - 500\,\mu\text{A}$) vÃ  dáº£i táº§n sá»‘ kÃ­ch thÃ­ch ($0.5\,\text{Hz} - 100\,\text{Hz}$).
- [ ] Chá»n dáº¡ng sÃ³ng: Xung vuÃ´ng 2 pha Ä‘á»‘i xá»©ng (Biphasic Square Wave) nháº±m triá»‡t tiÃªu thÃ nh pháº§n DC, trÃ¡nh Äƒn mÃ²n Ä‘iá»‡n phÃ¢n hoáº·c kÃ­ch á»©ng da.
- [ ] Chá»n váº­t liá»‡u Ä‘iá»‡n cá»±c tiáº¿p xÃºc (ThÃ©p khÃ´ng gá»‰ 316L, Silicone dáº«n Ä‘iá»‡n hoáº·c Máº¡ vÃ ng y táº¿).

### Giai Ä‘oáº¡n 2: Thiáº¿t káº¿ máº¡ch táº¡o dÃ²ng (Proof-of-Concept Hardware)
- [ ] Thiáº¿t káº¿ máº¡ch nguá»“n dÃ²ng khÃ´ng Ä‘á»•i (Constant Current Source) Ä‘iá»u khiá»ƒn báº±ng DAC/PWM (vÃ­ dá»¥ máº¡ch Howland Current Pump hoáº·c máº¡ch Op-Amp + BJT).
- [ ] TÃ­ch há»£p báº£o vá»‡ pháº§n cá»©ng: Giá»›i háº¡n dÃ²ng Ä‘iá»‡n tá»‘i Ä‘a tuyá»‡t Ä‘á»‘i (Hardware Current Limiter) á»Ÿ má»©c an toÃ n tá»‘i Ä‘a $< 1\,\text{mA}$.
- [ ] Äo kiá»ƒm dáº¡ng sÃ³ng trÃªn táº£i trá»Ÿ tÆ°Æ¡ng Ä‘Æ°Æ¡ng trá»Ÿ khÃ¡ng da ngÆ°á»i ($500\,\Omega - 10\,\text{k}\Omega$).

### Giai Ä‘oáº¡n 3: TÃ­ch há»£p cÆ¡ khÃ­ & Thiáº¿t káº¿ vá» chuá»™t
- [ ] Chá»n phom dÃ¡ng chuá»™t cÃ´ng thÃ¡i há»c (chuá»™t Ä‘á»©ng Vertical hoáº·c chuá»™t Ergonomic Ã´m lÃ²ng bÃ n tay).
- [ ] Bá»‘ trÃ­ 2 cá»±c tiáº¿p xÃºc (Anode / Cathode): Má»™t cá»±c á»Ÿ lÃ²ng bÃ n tay, má»™t cá»±c á»Ÿ cáº¡nh ngÃ³n cÃ¡i hoáº·c vá»‹ trÃ­ tiáº¿p xÃºc tá»± nhiÃªn.
- [ ] In thá»­ nghiá»‡m máº«u 3D prototype Ä‘áº§u tiÃªn.

### Giai Ä‘oáº¡n 4: Firmware & TÃ­nh nÄƒng thÃ´ng minh
- [ ] PhÃ¡t hiá»‡n cÃ³ ngÆ°á»i cáº§m chuá»™t (Capacitive Touch hoáº·c trá»Ÿ khÃ¡ng tiáº¿p xÃºc) má»›i kÃ­ch hoáº¡t xung Ä‘iá»‡n.
- [ ] Cháº¿ Ä‘á»™ tá»± ngáº¯t: KÃ­ch thÃ­ch theo chu ká»³ (vÃ­ dá»¥: 15-20 phÃºt hoáº¡t Ä‘á»™ng, nghá»‰ 40 phÃºt).
- [ ] Káº¿t ná»‘i chuá»™t: Chuá»™t quang HID chuáº©n qua USB/Bluetooth song song vá»›i máº¡ch vi dÃ²ng.
