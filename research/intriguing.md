> Szegedy, C., Zaremba, W., Sutskever, I., Bruna, J., Erhan, D., Goodfellow, I., & Fergus, R. (2013). Intriguing properties of neural networks. https://arxiv.org/abs/1312.6199

*observations*

deep neural nets have "intrinsic blind spots" (adversarial vulnerabilities), whose structure is connected to the data distribution in a non-obvious way. → adversarial examples are somewhat universal and not just the results of overfitting to a particular model or to the specific selection of the training set.

- i. at higher levels in a neural net we can't distinguish nodes from random linear combinations
	- this means that the space contains the semantic information, not the units
	- the relations between representations is the semantic encoding and they're stable to spacial rotation - but vector embeddings themselves are unlikely to contain any semantic information
- ii. neural nets are brittle and discontinuous
	- results can be manipulated through perturbations not perceptible to humans
- iii. these perturbations are transferable among different networks
	- cross model generalization:
		- a relatively large fraction of examples will be misclassified by networks trained from scratch with different hyper-parameters (number of layers, regularization or initial weights).
	- cross training-set generalization
		- a relatively large fraction of examples will be misclassified by networks trained from scratch on a disjoint training set.

we can formalize and verify the observations (i), (ii) but we still don't know why (iii) these examples generalize across different hyperparameters or training sets. they appear to be in contradiction with the network’s ability to achieve high generalization performance.

*reasoning*

- local generalizations
- effectiveness / expressiveness of neural nets is the reason they learn uninterpertable solutions with counter-intuitive properties.
- adversarial examples represent low-probability (high-dimensional) "pockets" in the manifold, which are hard to efficiently find by simply randomly sampling the input around a given example
- the smoothness assumption that underlies many kernel methods does not hold

# footnotes

use cases:

- "Intriguing Properties of Adversarial ML Attacks in the Problem Space"
	- https://arxiv.org/pdf/1911.02142
	- https://s2lab.cs.ucl.ac.uk/projects/intriguing/
	- https://www.youtube.com/watch?v=lLrnHwrvYiQ
	- https://www.youtube.com/watch?v=tsMcxDZLt4o
	- examples: android malware, windows malware, pdf malware, network malware
- "Why do adversarial attacks transfer? explaining transferability of evasion and poisoning attacks"
	- note: this paper doesn't explain transferability, it's just a survey style paper
	- https://arxiv.org/pdf/1809.02861
	- https://www.usenix.org/sites/default/files/conference/protected-files/sec19_slides_demontis.pdf (slides)
	- https://www.youtube.com/watch?v=WxgVJAY21kI (paper presentation - has 8/14 downvotes)
	- https://www.usenix.org/conference/usenixsecurity19/presentation/demontis
