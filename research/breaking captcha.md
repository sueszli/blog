> Plesner, A., Vontobel, T., & Wattenhofer, R. (2024). Breaking reCAPTCHAv2. In 48th IEEE International Conference on Computers, Software, and Applications (COMPSAC 2024). IEEE https://tik-db.ee.ethz.ch/file/7243c3cde307162630a448e809054d25/

*captchas*

- captcha = Completely Automated Public Turing Tests to Tell Computers and Humans Apart
- mostly based on cookie and browser history data
- a good captcha marks the exact boundary between the most intelligent machine and the least intelligent human
- captcha v3 doesn't need image labeling anymore, but falls back on captcha v2 in some edge cases
- captcha v2 has classification and segmentation tasks

*better captchas*

- osadchy et al. used adversarial examples that machines get wrong, but humans get right
- abstract reasoning challenge ARC has challenges that are easier for humans but harder for machines

*solving captchas*

- pretrained yolov8 because it uses less compute, can run on mobile
- vpns, bezier curves for mouse movements, synthetic cookies and history → fewer tests, easier tests
- can solve 100% of captchas (previously 68-71%)
