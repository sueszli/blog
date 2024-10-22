> Fort, S., & Lakshminarayanan, B. (2024). Ensemble everything everywhere: Multi-scale aggregation for adversarial robustness. arXiv preprint [arXiv:2408.05446](https://arxiv.org/pdf/2408.05446)
> 
> results (no code): https://paperswithcode.com/paper/ensemble-everything-everywhere-multi-scale/review/

*motivation*

- advx are bad for robustness, reliability and alignment of deep neural networks.
- we want to align machine perception (learned cv classification function) with human perception (inaccessible, implicit human classification function). we want cv models to agree with human judgment.
- while these two functions largely agree, the implicit human and learned machine functions are not exactly the same because there are adversarial attacks that affect machine models but do not transfer to (non-time-constrained) humans.
	- this means that their mismatch can be actively exploited by a motivated, active attacker, purposefully looking for such points where the disagreement is large.
	- but the mismatch is also an issue under static perturbations, such as noise or dataset shift (→ out of distribution attacks are when we find a case where the model didn't learn to generalize)
- adversarial robustness is just a primary case study, the broader implications of this alignment extend to aspects such as interpretability, image generation and the security of closed-source models and even other domains such as llms and reinforcement learning.

*definition*

- adversarial examples in the domain of image classification are small (typically human-imperceptible) perturbations $P$ to an image $X$ that cause a classifier, $f: X \mapsto y$, to misclassify the perturbed image $X+P$ as a target class $t$ chosen by the attacker, rather than its correct, ground truth class. This is despite the perturbed image $X+P$ still looking clearly like the ground truth class to a human.
- first described: https://arxiv.org/abs/1312.6199
- attacks transfer between models and architectures to a surprising degree: https://arxiv.org/abs/1412.6572

---

this paper improves adversarial robustness through (1) multi-resolution input representations and (2) self-ensembling of intermediate layer predictions.

benefits:

- can improve model backbones cheaply
- model learns higher-quality, more natural representations because the learned features are human interpretable (in opposite to much-harder-to-find instances of noise-like superstimuli)
	- hypothesis 1: (interpretability robustness hypothesis) a model whose adversarial attacks typically look human-interpretable will also be adversarially robust
	- hypothesis 2: the harder the dataset, the more useful our approach compared to brute force adversarial training

*multi-resolution input representations*

- serves both as a robustness prior and an active defense
- each input downsamples and stacked in the channel dimension: $H \times W \times (3N)$
- classifier makes a decision about all $N$ versions at once
	- this is common throughout multiple epochs but not on a single decision
- mimicking nature: 1) random noise, 2) a random jitter in both axes, 3) a small, random change in contrast and 4) a small, random color-grayscale shift.
	- microsaccades: even the smallest microsaccade motion moves the image projected on the retina by at least one pixel in amplitude
	- cone cells: loss in clarity and color on the borders
	- learning from all angles, distances, under various blurs, rotations, illuminations, contrasts while semantic content is preserved. classification decision is not performed on a single frame but rather on a long stream of such frames based on the motion of the eyes and changing properties of the retina (resolution, color sensitivity) at a place where the object is projected.
	- also reduces input space available to the attacker

*self-ensembling*

- de-correlation as an active defense
- self assembling of intermediate layer predictions
	- we can use (1) independent brittle models (2) predictions of intermediate layers of the same model (3) predictions from several checkpoints of the same model (4) predictions from several self-ensemble models.
- adversarial layer de-correlation = attacks designed to confuse specific layers of a network do not confuse others
	- it is shown via feature visualization that neural networks build up their understanding of an image hierarchically starting from edges, moving to textures, simple patterns, all the way to parts of objects and full objects themselves
	- we can use this to warn the model provider that the input has been tempered with
- crossmax = consensus algorithm for ensemble based on vickery auction and normalizing per predictor and class (by subtracting the max values)
	- robust accuracy is 17-fold larger than standard ensembling in L8/255
	- mean / median in ensembles aren't robust to outliers that can be exploited by fooling a single model
	- vickery is designed to incentivize truthful bidding
	- we choose the k-th highest prediction per class

*results*

- RobustBench AutoAttack with adv accuracy at $L_\infty$ = 8/255 suite using finetuned ImageNet-pretrained ResNet152 without any extra data
- without adversarial training:
	- 0% gain on CIFAR-10
	- +5% gain on CIFAR-100
- with adversarial training:
	- +5% gain on CIFAR-10
	- +9% gain on CIFAR-100

# footnotes

> goodheart: "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes"
> 
> Charles Goodhart. Problems of monetary management: The u.k. experience. In Anthony S. Courakis, editor, Inflation, Depression, and Economic Policy in the West, page 116. Barnes and Noble Books, Totowa, New Jersey, 1981. ISBN 0-389-20144-8.

multi-resolution input representations:

- https://arxiv.org/abs/2401.04727
- https://arxiv.org/abs/2312.02149
- https://arxiv.org/abs/2308.14418
- https://arxiv.org/abs/2312.02780
- https://www.sciencedirect.com/science/article/abs/pii/B9780080515816500659

self ensembling:

- https://arxiv.org/abs/2401.04727
- https://arxiv.org/pdf/2208.02851 (self ensembling vit)

adversarial decorrelation:

- https://staging.distill.pub/2019/activation-atlas/
- https://distill.pub/2017/feature-visualization/

related:

- https://arxiv.org/pdf/2404.09349 (robustness limits)
- https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10634483
- https://arxiv.org/abs/1810.00069 (advx survey)
