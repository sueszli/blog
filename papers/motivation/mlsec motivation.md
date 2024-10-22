# motivation

*why a security focus?*

- https://www.youtube.com/watch?v=ajGX7odA87k&t=241s (james micken's talk)
- https://80000hours.org/career-reviews/
- https://80000hours.org/career-reviews/information-security/#aisystems
- https://80000hours.org/2023/04/why-were-adding-information-security-to-our-list-of-priority-career-paths/
- high impact field of research

*cybersecurity applications of ml*

- https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence
- https://www.securityhq.com/blog/debunking-the-myths-how-machine-learning-ml-benefits-cyber-security/
- https://www.youtube.com/watch?v=TtSRv5q_hlY
- = attacks/defenses **using** machine learning models
- **defenses/blue teaming**:
	- network protection: better intrusion detection
	- endpoint protection: reverse engineering binaries and understanding their behaviour
	- security orchestration, automation and response (SOAR)
	- extended endpoint detection and Response (XDR)
	- indicators of compromise (IOCs)
	- suspect user behavior: identify fraud, credit fraud etc. in real time
- **attacks/red teaming**:
	- llms for social engineering, phishing
	- using sophisticated model vulnerabilities to bypass detection systems

*adversarial ml*

- https://en.wikipedia.org/wiki/Outline_of_machine_learning
- https://en.wikipedia.org/wiki/Applications_of_artificial_intelligence
- https://en.wikipedia.org/wiki/Machine_learning#Applications
- https://en.wikipedia.org/wiki/Machine_learning#Other_limitations_and_vulnerabilities
- https://en.wikipedia.org/wiki/Adversarial_machine_learning
- https://cltc.berkeley.edu/aml/
- https://en.wikipedia.org/wiki/AI_safety
- https://en.wikipedia.org/wiki/AI_safety#Cyber_defense
- = attacks/defenses **on** machine learning models
- the overarching goal is to improve model security/robustness and user privacy
- **defenses/blue teaming**: defensive strategies to protect models, users, providers
	- threat / fraud detection
	- adversarial robustness, explainability, determinism of models
	- large overlap with ai safety
	- can be split up in:
		- **i) reliability**: untrustworthy data
			- = when the model’s training data cannot be trusted (ie. due to data poisoning)
		- **ii) privacy**: untrustworthy models
			- = when the model is trained on private data (ie. confidential data shared on accident)
			- you can reverse engineer the dataset and check how much personally identfiable information was leaked
		- **ii) safety**: untrustworthy users
			- = when the users cannot be trusted (ie. due to deepfake generation)
			- fingerprinting, watermarking
- **attacks/red teaming**: attack vectors, exposing vulnerabilities
	- there 3 dimensions of each attack vector:
		- i) classifier influence: disrupt classification phase if there are no data manipulation constraints.
		- ii) security violation: supply malicious data that gets classified as legitimate. malicious data supplied during training can cause legitimate data to be rejected after training.
		- iii) specificity: targeted attack for intrusion/disruption or indiscriminate attack to cause general chaos.

*mlsec in the industry*

- https://www.robustintelligence.com/ai-application-security
- https://huggingface.co/blog/hugging-face-wiz-security-blog
- https://learn.microsoft.com/en-us/security/ai-red-team/
	- https://www.microsoft.com/en-us/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/
	- https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning
- https://services.google.com/fh/files/blogs/google_ai_red_team_digital_final.pdf
- https://owaspai.org/docs/ai_security_overview/

*cve database*

- there is no proper cve system yet (see: https://arxiv.org/pdf/2101.10865)
- https://avidml.org/database/
- https://atlas.mitre.org/techniques
- https://airisk.io/
- https://protectai.com/threat-research/january-vulnerability-report
- https://owasp.org/www-project-machine-learning-security-top-10/
- https://docs.avidml.org/taxonomy/effect-sep-view/security
- https://learn.microsoft.com/en-us/security/engineering/bug-bar-aiml
- https://www.enisa.europa.eu/publications/securing-machine-learning-algorithms
- https://www.energy.gov/ai/doe-ai-risk-management-playbook-airmp
- https://ethical.institute/security.html

*cve papers*

- https://github.com/stratosphereips/awesome-ml-privacy-attacks?tab=readme-ov-file
- https://github.com/DeepSpaceHarbor/Awesome-AI-Security?tab=readme-ov-file
- https://github.com/trailofbits/awesome-ml-security?tab=readme-ov-file

*challenges*

- flip: https://www.idena.io/flip-challenge
- lab42: https://lab42.global/arc/

*inspiring researchers*

- gautam kamath: https://scholar.google.com/citations?user=MK6zHkYAAAAJ&hl=en
- nils lukas: https://scholar.google.com/citations?user=fmlEab4AAAAJ&hl=en

# papers to read

*paper collections*

- https://nicholas.carlini.com/writing/2019/all-adversarial-example-papers.html
- https://github.com/xiaosen-wang/Adversarial-Examples-Paper
- https://ai.hdm-stuttgart.de/news/2020/selected-topics-1-adversarial-attacks/ (threat models explained)
