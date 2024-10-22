> Huh, M., Cheung, B., Wang, T., & Isola, P. (2024). The platonic representation hypothesis. arXiv preprint arXiv:2405.07987: https://arxiv.org/pdf/2405.07987

hypothesis: [very general] neural nets (indifferent to their objectives, data, modalities) are all converging to a shared internal representation (statistical models of reality).

*assumption*

- the level of similarity is increasing over performance and scale
- we assume that all models are converging to a singular representation of the world
	- aka. "all strong visual representations are alike" / "anna karenina scenario" (bansal et al. 2021)
- this isn't because of objectives, data, modalities but reality – data is an intermediary to the world.

examples:

- "rosetta neurons", shared among many different architectures
	- ie. hat detection among stylegan2, resnet50, clip-rn, duno-rn, dino-vit, …
	- ie. image classifiers and colorization networks learn the same neural units
- gabor filters in cats (hubel and wiesel) and alexnet

*definitions*

- representation as kernels:
	- $f: \mathcal X \times \mathcal X \mapsto \mathbb R$
	- $K(x_i, x_j) = \langle f(x_i), f(x_j)\rangle$
	- allows us to measure distances
- kernel-alignment metric:
	- $m: \mathcal K \times \mathcal K \mapsto \mathbb R$
	- distance between kernels

*observations*

- we measure kernel alignment between different models and modals with increasing scale
- there is a language-vision alignment: representations in both vision and language models start aligning with scale

*theory*

- a contrastive learner (spacial distribution of embeddings matters) with NCE objectives will always converge to the pointwise mutual information (pmi)
- therefore: contrastive learning boils down to finding an embedding which similarly equals normalized cooccurrence rates

# footnotes

this is a really far fetched hypothesis. it is simply an interesting thought-provoking impulse but nothing more.

paper presentation:

- https://www.youtube.com/watch?v=1_xH2mUFpZw  🔥
- https://www.youtube.com/watch?v=y9_QFUma8Fo

related:

- https://arxiv.org/pdf/2310.13018 (getting aligned on representational alignment)
- http://lxmls.it.pt/2021/wp-content/uploads/2021/07/Is-scale-all-we-need.pdf (scale is all we need)
- https://arxiv.org/pdf/2104.01489 (the contravariance principle)
	- "The harder the task is, the stronger the constraint, and the more likely any given high-performing solution (e.g. a deep neural network) is similar to any other (e.g. an actual brain). […] Whether that species-relativized constraint landscape is actually sufficiently strong that it determines the architecture of solution fairly closely is an empirical-computational neuroscience question."
	- the more tasks we have to solve, the fewer functions satisfy them all

contrastive learning:

- https://lilianweng.github.io/posts/2021-05-31-contrastive/ 🔥
