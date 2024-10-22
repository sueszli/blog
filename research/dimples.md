
> Shamir, A., Melamed, O., & BenShmuel, O. (2021). The dimpled manifold model of adversarial examples in machine learning. https://arxiv.org/pdf/2106.10151

*adversarial examples*

- in 2013 we found out that neural nets are sensitive to small perturbations, but didn't know why
- adversarial examples have many counter intuitive properties
- all natural images can be compressed losslessly onto a $k$ dimensional manifold using an autoencoder assuming that images have $n$ dimensions, where $k \ll n$
	- manifold = a collection of points forming a certain kind of set, such as those of a topologically closed surface or an analogue of this in three or more dimensions
- a decision boundary has $n\text{–}1$ dimensions

*dmm - dimpled manifold model*

- a mental model that should explain adversarial examples - not in contrast, but in addition to what we know already (a geometric approach to ilyas explaination of robust vs. non-robust features)
- multi-class classifiers have multiple decision boundaries
- phase 1: clinging process
	- fast
	- random decision boundary gets very close to $k$ dimensional image manifold
- phase 2: dimpling phase
	- slow
	- decision boundary gets shallow bulges, to move it to the correct side of the training examples
	- adversarial examples deepen the dimples in decision boundary - but they don't shift the plane
	- networks try to use the large perpendicular subspace (on which they are not judged) to make it easier for them to place the decision boundary within the image manifold correctly
	- they develop large gradients that are roughly perpendicular to the image manifold on the training examples

*dmm explaining counterintuitive properties*

- what are adversarial examples?
	- all natural images can be losslessly compressed to a low-dimensional manifold
	- the redundant dimensions can be used to construct pseudo-images that won't occur in reality but still get classified by the neural net
	- adversarial examples are pseudo-images
- why are adversarial examples so close to the original images?
	- neural nets prefer to perpendicular derivatives, so a short distance is sufficient to cause a strong change in the confidence levels
- why don’t the adversarial perturbations resemble the target class?
	- most adversarial perturbations look like a featureless small-magnitude random noise because we want to move perpendicularly between target classes by exploiting redundant dimensions
- why do robustness and accuracy trade-off?
	- ease of training and the existence of nearby adversarial examples are two sides of the same coin
	- large perpendicular derivatives make the training easier, but they also make the model more fragile
	- any attempt to robustify a network by limiting all its directional derivatives will make it harder to train and thus less accurate

*dmm explaining adversarial training*

- adversarial training = making model more robust by using adversarial examples in the training data
- adversarial examples during training just affect the dimpling phase, not the clinging phase
- they deepen the dimples which makes it harder to move vertically and trick the model, but also reduce accuracy
- illya's experiment:
	- i. train neural net $N_1$ with $s_i$ examples of cats and guacamoles
	- ii. use $N_1$ to generate adversarial examples $t_i$ for each $s_i$ (with the visually wrong target class)
	- iii. train fresh neural net $N_2$ using only $t_i$, classified with the visually wrong target class
	- evaluation: $N_2$ is more performant and robust than $N_1$
- reason: we overshoot and set a reversed-label decision-boundary, so the non-adversarial examples are still classified correctly

*dmm experiments*

- using mnist, cifar10, imagenet datasets
- $M$ = approximation of a natural-image manifold using a high compression-rate autoencoder
- $x$ = local linearization around test-set images (dimensionality $k$ could probably still be lower, but it still works)
- $d$ = perturbations made using multi-step PGD attacks
- $x + d$ = adversarial example
- $x + \text{Proj}_M(d)$ = projected on-manifold example
	- makes the perturbation more interpretable
	- this means manifold dimensions identified the autoencoder (which might be a subset or a superset of the local dimensions of the real image manifold) are more closely associated with human-recognizable features of the image
- $x + (d - \text{Proj}_M(d))$ = projected off-manifold example
	- can follow a different strategy than the on-manifold example to perturb the image

# questions

*redundancy and vulnereability*

> reddit: The central claim is that adversarial examples come from the fact that we fit high-dimensional decision boundaries to low-dimensional images. This leaves a lot of space for the adversarial examples to exist perpendicularly from the true location of the low-dimensional object (the natural image).

> yannic kilcher: in every example the mental model of this paper is giving itself an unfair advantage compared to previous models, by using an additional dimension for the decision boundary (through the assumption that all realistic images can be compressed into a lower dimension). but in practice we know from SVMs how much easier seperation of data becomes this way. so this isn't anything new.

- is the essence of this paper that redundant dimensionality makes models more vulnerable?
	- the decision boundary has $n-1$ dimensions
	- the manifold has $k$ dimensions
	- $k \ll n-1 < n$
	- see: https://youtu.be/HpP35wA8RUc?si=SeEPubLfwuZ3bPxq&t=986 at 16:15
- could we use compression algorithms to reduce dimensionality and increase robustness + detect outliers if that's the case?

*robustness vs. accuracy trade-off*

> yannic kilcher: as you train with adversarial examples, you shift further away from realistic examples and therefore reduce the generalizability of your model.

# footnotes

visualizations:

- https://github.com/odeliamel/Dimpled-Manifold-Model?tab=readme-ov-file

paper explaination by yannic kilcher:

- https://www.youtube.com/watch?v=k_hUdZJNzkU 🔥

talks:

- https://www.youtube.com/watch?v=HpP35wA8RUc 🔥
- https://www.youtube.com/watch?v=e8ZGcbZJDYU

reddit discussion:

- https://www.reddit.com/r/MachineLearning/comments/o6u34b/r_the_dimpled_manifold_model_of_adversarial/ 🔥
- https://www.reddit.com/r/MachineLearning/comments/o8vyt1/d_a_critical_take_on_the_dimpled_manifold_model/

reproduction:

- https://gist.github.com/yk/de8d987c4eb6a39b6d9c08f0744b1f64 🔥
- https://github.com/LukasKarner/dimpled-manifolds 🔥

related papers:

- https://aisecure-workshop.github.io/amlcvpr2021/cr/27.pdf (counter example) 🔥
- https://arxiv.org/pdf/1903.03905 (semantics preserving training)
- https://arxiv.org/pdf/2403.04493 (quantifying realism)
- https://arxiv.org/pdf/1703.00810 (information theory)
