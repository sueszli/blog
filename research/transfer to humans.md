> Elsayed, G., Shankar, S., Cheung, B., Papernot, N., Kurakin, A., Goodfellow, I., & Sohl-Dickstein, J. (2018). Adversarial examples that fool both computer vision and time-limited humans. Advances in neural information processing systems, 31: https://papers.nips.cc/paper/2018/file/8562ae5e286544710b2e7ebe9858833b-Paper.pdf

we want to know whether adversarial examples transfer to humans (under a time constraint).

*definition of adversarial examples*

- 1) are designed to cause a mistake (in classification)
- 2) are not defined to be imperceptible

*experiment*

- humans (500-1000 ms) vs. ImageNet
- 3 classes (pets, hazards/danger, vegetables)
- input:
	- `image` = imagenet training set
	- `adv` = adversarial perturbation added to image that can successfully trick classification models. same $\epsilon$ for all perturbations. perturbations must be class perserving judged by a no-time-limit human.
	- `flip` = perturbation from `adv` but flipped vertically before being added to image → serves as a control condition, very similar results to `adv` also on classification models
	- `false` = condition in which subjects are forced to make a mistake (accuracy must be 0) → serves as a control condition, to prove that adversarial examples don't just degrade image quality

*results*

- adversarial examples transfer to humans
- adversarial examples increase human error rate

in depth:

- humans perform significantly worse on adversarial images
- inverse correlation between attack success and response time
- "adversarial perturbations generated using CNNs biased human perception towards the targeted class"
- "effect was stronger for the the hazard, then pets, then vegetables group"

*open questions*

- have we actually fooled human observers or did we change the true class?
	- fooling humans with no time-limit will need to tackle the difficult problem of obtaining a better ground truth signal than visual labeling by humans.
- how do the adversarial examples work?
	- this wasn't discussed in this paper.

# questions

- shouldn't the baseline be a non-time-limited human?
	- it seems like two "types of humans" were introduced in this paper that were treated differently. the time-constrained humans and the non-time-constrained ones.
	- the non-time-constrained ones provided the ground truth.
	- the time-constrained ones were tried to be fooled.
- does this support the "platonic representaiton hypothesis"? are models learning the same representations that humans have learned?
	- see: Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The platonic representation hypothesis. arXiv preprint arXiv:2405.07987: https://arxiv.org/pdf/2405.07987

# footnote

related:

- https://www.nature.com/articles/s41467-023-40499-0

paper presentation:

- https://www.youtube.com/watch?v=UgsmV2cCO44

human perception:

- basics: https://en.wikipedia.org/wiki/Perception
- v1 stage: https://en.wikipedia.org/wiki/Visual_cortex
